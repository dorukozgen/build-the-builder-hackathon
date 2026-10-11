"""A practice mock of Freya Bank's application-intake tools (briefs/brief-f.md), in the shape of the organisers' collections mock.

    python tools/mock_bank_f.py [--port 8765]

    POST /v1/practice/sessions   {"case": "PUB-08", "backend": {...}}   header x-team-key required; returns the call variables
    GET  /v1/practice/ledger/<customer_id>                               what the scorer reads
    POST /v1/<tool>                                                      the seven tools of tools/openapi-f.json, no key

Freya's servers must reach it: expose the port with a tunnel (`ngrok http 8765`) and benchmark with
`--host <public url> --openapi tools/openapi-f.json`. The practice customers are the 13 of public-test-set.json (names and
identity answers); a case's `backend` adds existing applications and faults. PUB-10's first create_application is slow:
it goes through, but only after the agent's tool timeout, so the agent must check before it submits again.
"""
import argparse, datetime, json, pathlib, re, secrets, sys, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIXTURES = {c["id"]: c for c in json.load(open(ROOT / "public-test-set.json", encoding="utf-8"))}
TYPES = ("card_replacement", "address_change", "limit_increase")
QUEUES = ("applications", "security", "general")
OUTCOMES = ("application_created", "status_given", "transferred", "not_verified", "no_action")
NO_REASON = ("application_created", "status_given")
STATUSES = ("received", "in_review", "more_info_needed", "approved", "rejected")
TOOLS = ("verify_identity", "get_requirements", "find_applications", "create_application", "get_application", "transfer_to_agent", "close_call")
REQUIREMENTS = {
    "card_replacement": [
        {"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": True},
        {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "required": False},
        {"name": "delivery", "question": "Should the new card go to your home address or to a branch?", "format": "choice", "options": ["home", "branch"], "required": False}],
    "address_change": [
        {"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": True},
        {"name": "city", "question": "Which city?", "format": "text", "required": True},
        {"name": "postcode", "question": "What is the postcode? Five digits.", "format": "postcode", "required": True},
        {"name": "move_date", "question": "From which date does the new address apply?", "format": "date", "required": False}],
    "limit_increase": [
        {"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": True},
        {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "required": False},
        {"name": "monthly_income", "question": "What is your monthly net income?", "format": "amount", "required": False}],
}
DEFAULT_FAULTS = {"PUB-10": {"create_application": {"delay_first": 1}}}
TIMEOUT_DELAY = 16.0            # seconds: longer than the agent's 12 s tool timeout, so the call "times out" at Freya but goes through here

LOCK = threading.Lock()
SESSIONS = {}


def new_id(prefix): return prefix + "".join(secrets.choice("0123456789") for _ in range(6))


def parse_words(s):
    s = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", s.strip().replace(",", "").replace(" of ", " "))
    for f in ("%d %B %Y", "%d %b %Y", "%B %d %Y", "%b %d %Y", "%d/%m/%Y", "%d.%m.%Y", "%d-%m-%Y"):
        try: return datetime.datetime.strptime(s, f).date()
        except ValueError: pass
    return None


def valid(field, value):
    """True when `value` fits the field's format."""
    f, v = field["format"], value
    if f == "amount":
        try: return not isinstance(v, bool) and float(v) > 0 and round(float(v), 2) == float(v)
        except (TypeError, ValueError): return False
    if f == "digits": return bool(re.fullmatch(r"\d+", str(v)))
    if f == "postcode": return bool(re.fullmatch(r"\d{5}", str(v)))
    if f == "date":
        try: datetime.date.fromisoformat(str(v)); return True
        except ValueError: return False
    if f == "choice": return v in field.get("options", [])
    return isinstance(v, str) and bool(v.strip())


def open_session(case, backend):
    fx = FIXTURES.get(case)
    if not fx: return None
    s = {"customer_id": "f_" + secrets.token_hex(6), "case": case, "identity": dict(fx["identity"]), "variables": dict(fx["variables"]),
         "verified": {k: False for k in fx["identity"]}, "wrong_left": 3, "applications": [], "created": [], "transfers": [], "calls": [],
         "counts": {}, "closed": False, "outcome": None, "reason": None, "faults": dict(DEFAULT_FAULTS.get(case, {}))}
    backend = backend if isinstance(backend, dict) else {}
    today = s["variables"]["now"][:10]
    for a in backend.get("applications") or []:
        if isinstance(a, dict) and a.get("type") in TYPES:
            s["applications"].append({"application_id": a.get("application_id") or new_id("APP-"), "type": a["type"], "status": a.get("status") if a.get("status") in STATUSES else "received",
                                      "created_on": a.get("created_on") or (datetime.date.fromisoformat(today) - datetime.timedelta(days=5)).isoformat(), "note": a.get("note") or ""})
    if isinstance(backend.get("faults"), dict): s["faults"] = backend["faults"]
    with LOCK: SESSIONS[s["customer_id"]] = s
    return s


def verify_identity(s, body):
    field, answer = body.get("field"), str(body.get("answer", "")).strip()
    if field not in s["identity"]: return {"ok": False, "error": "field must be date_of_birth or phone_last4"}
    real = s["identity"][field]
    def reply(verified, hint=None):
        if verified: s["verified"][field] = True
        r = {"ok": True, "verified": bool(verified), "wrong_answers_left": s["wrong_left"], "all_verified": all(s["verified"].values())}
        if hint: r["hint"] = hint
        return r
    if s["wrong_left"] == 0: return reply(False)
    if field == "phone_last4":
        if not re.fullmatch(r"\d{4}", answer): return {"ok": False, "error": "answer must be four digits"}
        if answer == real: return reply(True)
    else:
        m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", answer)
        if m:
            y, a, b = (int(x) for x in m.groups())
            ry, rm, rd = (int(x) for x in real.split("-"))
            if (y, a, b) == (ry, rm, rd): return reply(True)
            if (y, b, a) == (ry, rm, rd): return reply(False, "day_month_swapped")
        else:
            d = parse_words(answer)
            if d is None: return {"ok": False, "error": "answer is not a date. Send it as YYYY-MM-DD."}
            if d.isoformat() == real: return reply(True)
    s["wrong_left"] -= 1
    return reply(False)


def create_application(s, body):
    t, fields = body.get("type"), body.get("fields")
    if t not in TYPES: return {"ok": False, "error": "unknown type"}, False
    if isinstance(fields, str):
        try: fields = json.loads(fields)
        except ValueError: fields = None
    if not isinstance(fields, dict): return {"ok": False, "error": "fields must be an object"}, False
    for f in REQUIREMENTS[t]:
        if f["required"] and f["name"] not in fields: return {"ok": False, "error": f"missing field {f['name']}"}, False
        if f["name"] in fields and not valid(f, fields[f["name"]]): return {"ok": False, "error": f"invalid field {f['name']}: expected {f['format']}"}, False
    n = s["counts"]["create_application"] = s["counts"].get("create_application", 0) + 1
    delayed = n <= int((s["faults"].get("create_application") or {}).get("delay_first") or 0)
    if delayed: time.sleep(TIMEOUT_DELAY)
    app = {"application_id": new_id("APP-"), "type": t, "status": "received", "created_on": s["variables"]["now"][:10], "note": "", "fields": fields}
    s["applications"].append(app); s["created"].append(app)
    return {"ok": True, "application_id": app["application_id"], "status": "received"}, delayed


def tool_call(s, tool, body):
    """Runs one tool against a session. Returns (result, delayed)."""
    if s["closed"]: return {"ok": False, "error": "call closed"}, False
    if tool == "verify_identity": return verify_identity(s, body), False
    if tool == "get_requirements":
        t = body.get("type")
        return ({"ok": True, "fields": REQUIREMENTS[t]} if t in TYPES else {"ok": False, "error": "unknown type"}), False
    if tool == "transfer_to_agent":
        q = body.get("queue")
        if q not in QUEUES: return {"ok": False, "error": "queue must be one of " + ", ".join(QUEUES)}, False
        s["transfers"].append({"queue": q}); return {"ok": True}, False
    if tool == "close_call":
        o, r = body.get("outcome"), body.get("reason")
        if o not in OUTCOMES: return {"ok": False, "error": "outcome must be one of " + ", ".join(OUTCOMES)}, False
        if o not in NO_REASON and not r: return {"ok": False, "error": "reason is required for outcome " + o}, False
        s["closed"], s["outcome"], s["reason"] = True, o, (None if o in NO_REASON else str(r)); return {"ok": True}, False
    if not all(s["verified"].values()): return {"ok": False, "error": "identity not verified"}, False
    if tool == "find_applications":
        t = body.get("type")
        if t not in TYPES: return {"ok": False, "error": "unknown type"}, False
        return {"ok": True, "applications": [{k: a[k] for k in ("application_id", "type", "status", "created_on", "note")} for a in s["applications"] if a["type"] == t]}, False
    if tool == "create_application": return create_application(s, body)
    if tool == "get_application":
        a = next((a for a in s["applications"] if a["application_id"] == body.get("application_id")), None)
        if not a: return {"ok": False, "error": "unknown application_id"}, False
        return {"ok": True, **{k: a[k] for k in ("application_id", "type", "status", "created_on", "note")}}, False
    return {"ok": False, "error": "unknown tool"}, False


def ledger(s):
    return {"customer_id": s["customer_id"], "case": s["case"], "outcome": s["outcome"], "reason": s["reason"], "promises": [], "notes": [], "callbacks": [],
            "transfers": list(s["transfers"]), "applications": [dict(a) for a in s["created"]], "calls": list(s["calls"])}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args): pass

    def send(self, status, obj):
        data = json.dumps(obj).encode()
        self.send_response(status); self.send_header("content-type", "application/json"); self.send_header("content-length", str(len(data))); self.end_headers()
        self.wfile.write(data)

    def body(self):
        n = int(self.headers.get("content-length") or 0)
        try: b = json.loads(self.rfile.read(n) or b"{}")
        except ValueError: return None
        return b if isinstance(b, dict) else None

    def do_GET(self):
        m = re.fullmatch(r"/v1/practice/ledger/([^/]+)", self.path)
        if not m: return self.send(404, {"ok": False, "error": "not found"})
        if not self.headers.get("x-team-key"): return self.send(401, {"ok": False, "error": "x-team-key header required"})
        with LOCK: s = SESSIONS.get(m.group(1))
        if not s: return self.send(404, {"ok": False, "error": "unknown customer_id"})
        with LOCK: self.send(200, ledger(s))

    def do_POST(self):
        b = self.body()
        if b is None: return self.send(400, {"ok": False, "error": "body must be a JSON object"})
        if self.path == "/v1/practice/sessions":
            if not self.headers.get("x-team-key"): return self.send(401, {"ok": False, "error": "x-team-key header required"})
            s = open_session(b.get("case"), b.get("backend"))
            if not s: return self.send(404, {"ok": False, "error": "unknown practice case"})
            log(f"session {s['customer_id']} case {s['case']} apps {len(s['applications'])} faults {s['faults'] or '-'}")
            return self.send(200, {"ok": True, "variables": {"customer_id": s["customer_id"], **s["variables"]}})
        m = re.fullmatch(r"/v1/(\w+)", self.path)
        if not m or m.group(1) not in TOOLS: return self.send(404, {"ok": False, "error": "not found"})
        tool = m.group(1)
        with LOCK: s = SESSIONS.get(str(b.get("customer_id")))
        if not s: return self.send(404, {"ok": False, "error": "unknown customer_id"})
        result, delayed = tool_call(s, tool, b)                        # a delayed call sleeps outside the lock
        with LOCK:
            rec = {"n": len(s["calls"]) + 1, "tool": tool, "args": {k: v for k, v in b.items() if k != "customer_id"}, "status": 200, "result": result}
            if delayed: rec["delayed"] = True
            s["calls"].append(rec)
        log(f"{s['customer_id']} {tool} {json.dumps(rec['args'])[:120]} -> {json.dumps(result)[:160]}{' (delayed)' if delayed else ''}")
        self.send(200, result)


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def make_server(host="127.0.0.1", port=8765):
    srv = ThreadingHTTPServer((host, port), Handler); srv.daemon_threads = True
    return srv


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8765); ap.add_argument("--host", default="127.0.0.1")
    a = ap.parse_args()
    srv = make_server(a.host, a.port)
    log(f"brief-f mock listening on http://{a.host}:{srv.server_address[1]}  (fixtures: {', '.join(FIXTURES)})")
    try: srv.serve_forever()
    except KeyboardInterrupt: pass
