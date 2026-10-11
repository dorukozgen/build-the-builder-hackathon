"""A practice mock of Freya Bank's campaign tools (briefs/brief-e.md), in the shape of tools/mock_bank_f.py.

    py -3 tools/mock_bank_e.py [--port 8766]

    POST /v1/practice/sessions   {"case": "PUB-01", "backend": {...}}   header x-team-key required; returns the call variables
    GET  /v1/practice/ledger/<customer_id>                               what the scorer reads
    POST /v1/<tool>                                                      the eight tools of tools/openapi-e.json, no key

Expose it with a tunnel and benchmark with `--host <public url> --openapi tools/openapi-e.json`.
A case's `backend` may set: "marketing" (bool, default false), "eligibility" ({campaign_id: true | reason}, default true),
"campaigns" (replaces the catalogue), "faults" ({"start_application": {"fail_first": N}, "check_eligibility": {"fail_first": N}}).
"""
import argparse, datetime, json, pathlib, re, secrets, threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIXTURES = {c["id"]: c for c in json.load(open(ROOT / "public-test-set.json", encoding="utf-8"))}
QUEUES = ("sales", "security", "general")
OUTCOMES = ("informed", "not_eligible", "applied", "transferred", "not_verified", "no_action")
NO_REASON = ("informed", "not_eligible", "applied")
REASONS = ("existing_product", "already_enrolled", "age", "income_not_on_file", "account_status", "not_checked")
TOOLS = ("verify_identity", "list_campaigns", "get_campaign", "get_consent", "check_eligibility", "start_application", "transfer_to_agent", "close_call")

CATALOGUE = [
    {"campaign_id": "cmp_cc_cashback", "name": "Autumn Cashback Card", "product": "credit_card", "valid_from": "2026-09-01", "valid_to": "2026-11-30",
     "summary": "2% cashback on groceries for the first six months.",
     "conditions": ["Cashback is 2% on grocery purchases for the first six months after the card is opened.", "Cashback is capped at 50 euros per month.",
                    "The card must be used for at least five purchases in each calendar month to earn cashback that month."],
     "exclusions": ["Cash withdrawals and balance transfers earn no cashback.", "Customers who held a Freya Bank credit card in the last 12 months are excluded."],
     "fees": "Annual fee 0 euros in the first year, 45 euros from the second year.", "how_to_apply": "Apply by phone, in the mobile app or at a branch."},
    {"campaign_id": "cmp_cc_travel", "name": "Travel Miles Card", "product": "credit_card", "valid_from": "2026-10-01", "valid_to": "2026-12-31",
     "summary": "Earn 3 miles per euro on travel, no foreign transaction fee.",
     "conditions": ["Earn 2 miles per euro spent on flights and hotels booked with the card.", "Miles expire 24 months after they are earned."],
     "exclusions": ["Purchases refunded or disputed earn no miles."],
     "fees": "Annual fee 90 euros. Foreign transaction fee 1.5%.", "how_to_apply": "Apply by phone or in the mobile app."},
    {"campaign_id": "cmp_sav_bonus", "name": "Saver Bonus 2026", "product": "savings_account", "valid_from": "2026-10-01", "valid_to": "2026-10-31",
     "summary": "A bonus rate on new savings.",
     "conditions": ["A bonus rate of 3.1% a year applies to new money deposited between 1 October and 31 October 2026.", "The bonus rate applies for six months from the deposit date.",
                    "The minimum deposit is 1,000 euros."],
     "exclusions": ["Money transferred from another Freya Bank account does not count as new money."],
     "fees": "No account fee.", "how_to_apply": "Open the account by phone, in the app or at a branch."},
    {"campaign_id": "cmp_sav_summer", "name": "Summer Saver", "product": "savings_account", "valid_from": "2026-06-01", "valid_to": "2026-09-30",
     "summary": "Summer bonus rate on savings.", "conditions": ["A bonus rate of 2.8% a year on new deposits made in the summer."],
     "exclusions": ["Business customers are excluded."], "fees": "No account fee.", "how_to_apply": "No longer available."},
    {"campaign_id": "cmp_loan_green", "name": "Green Home Loan Offer", "product": "personal_loan", "valid_from": "2026-11-01", "valid_to": "2027-01-31",
     "summary": "Reduced rate for energy-saving home improvements.", "conditions": ["The loan must be used for energy-saving home improvements, shown by an invoice."],
     "exclusions": ["Loans above 30,000 euros are excluded."], "fees": "Arrangement fee 1% of the loan amount.", "how_to_apply": "Apply at a branch."},
    {"campaign_id": "cmp_loan_quick", "name": "Quick Cash Loan Discount", "product": "personal_loan", "valid_from": "2026-10-01", "valid_to": "2026-12-15",
     "summary": "Half the arrangement fee on personal loans.", "conditions": ["The arrangement fee is reduced by half for loans taken out during the campaign.", "The loan amount must be between 2,000 and 20,000 euros."],
     "exclusions": ["Refinancing of an existing Freya Bank loan is excluded."], "fees": "Arrangement fee normally 2% of the loan amount; 1% during the campaign.",
     "how_to_apply": "Apply by phone or in the app."},
]

LOCK = threading.Lock()
SESSIONS = {}


def new_id(prefix): return prefix + "".join(secrets.choice("0123456789") for _ in range(6))


def parse_words(s):
    s = re.sub(r"(\d)(st|nd|rd|th)\b", r"\1", s.strip().replace(",", "").replace(" of ", " "))
    for f in ("%d %B %Y", "%d %b %Y", "%B %d %Y", "%b %d %Y", "%d/%m/%Y", "%d.%m.%Y", "%d-%m-%Y"):
        try: return datetime.datetime.strptime(s, f).date()
        except ValueError: pass
    return None


def open_session(case, backend):
    fx = FIXTURES.get(case)
    if not fx: return None
    backend = backend if isinstance(backend, dict) else {}
    s = {"customer_id": "e_" + secrets.token_hex(6), "case": case, "identity": dict(fx["identity"]), "variables": dict(fx["variables"]),
         "verified": {k: False for k in fx["identity"]}, "wrong_left": 3, "transfers": [], "calls": [], "applications": [],
         "counts": {}, "closed": False, "outcome": None, "reason": None,
         "campaigns": backend.get("campaigns") or CATALOGUE, "marketing": bool(backend.get("marketing", False)),
         "eligibility": backend.get("eligibility") or {}, "faults": backend.get("faults") or {}}
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


def fault(s, tool):
    n = s["counts"][tool] = s["counts"].get(tool, 0) + 1
    return n <= int((s["faults"].get(tool) or {}).get("fail_first") or 0)


def campaign(s, cid): return next((c for c in s["campaigns"] if c.get("campaign_id") == cid), None)


def tool_call(s, tool, body):
    """Runs one tool against a session. Returns (http_status, result)."""
    if s["closed"]: return 200, {"ok": False, "error": "call closed"}
    if tool == "verify_identity": return 200, verify_identity(s, body)
    if tool == "list_campaigns":
        return 200, {"ok": True, "campaigns": [{k: c.get(k) for k in ("campaign_id", "name", "product", "valid_from", "valid_to", "summary")} for c in s["campaigns"]]}
    if tool == "get_campaign":
        c = campaign(s, body.get("campaign_id"))
        if not c: return 200, {"ok": False, "error": "unknown campaign_id"}
        return 200, {"ok": True, **{k: c.get(k) for k in ("name", "product", "valid_from", "valid_to", "conditions", "exclusions", "fees", "how_to_apply")}}
    if tool == "transfer_to_agent":
        q = body.get("queue")
        if q not in QUEUES: return 200, {"ok": False, "error": "queue must be one of " + ", ".join(QUEUES)}
        s["transfers"].append({"queue": q}); return 200, {"ok": True}
    if tool == "close_call":
        o, r = body.get("outcome"), body.get("reason")
        if o not in OUTCOMES: return 200, {"ok": False, "error": "outcome must be one of " + ", ".join(OUTCOMES)}
        if o not in NO_REASON and not r: return 200, {"ok": False, "error": "reason is required for outcome " + o}
        s["closed"], s["outcome"], s["reason"] = True, o, (None if o in NO_REASON else str(r)); return 200, {"ok": True}
    if not all(s["verified"].values()): return 200, {"ok": False, "error": "identity not verified"}
    if tool == "get_consent": return 200, {"ok": True, "marketing": s["marketing"]}
    if tool == "check_eligibility":
        if not campaign(s, body.get("campaign_id")): return 200, {"ok": False, "error": "unknown campaign_id"}
        if fault(s, tool): return 500, {"ok": False, "error": "service unavailable"}
        e = s["eligibility"].get(body.get("campaign_id"), True)
        return 200, ({"ok": True, "eligible": True} if e is True else {"ok": True, "eligible": False, "reason": e if e in REASONS else "not_checked"})
    if tool == "start_application":
        if not campaign(s, body.get("campaign_id")): return 200, {"ok": False, "error": "unknown campaign_id"}
        if fault(s, tool): return 500, {"ok": False, "error": "service unavailable"}
        a = {"application_id": new_id("4"), "campaign_id": body.get("campaign_id")}
        s["applications"].append(a); return 200, {"ok": True, "application_id": a["application_id"]}
    return 200, {"ok": False, "error": "unknown tool"}


def ledger(s):
    return {"customer_id": s["customer_id"], "case": s["case"], "outcome": s["outcome"], "reason": s["reason"], "promises": [], "notes": [], "callbacks": [],
            "transfers": list(s["transfers"]), "applications": [dict(a) for a in s["applications"]], "calls": list(s["calls"])}


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
            log(f"session {s['customer_id']} case {s['case']} backend {json.dumps(b.get('backend') or {})[:120]}")
            return self.send(200, {"ok": True, "variables": {"customer_id": s["customer_id"], **s["variables"]}})
        m = re.fullmatch(r"/v1/(\w+)", self.path)
        if not m or m.group(1) not in TOOLS: return self.send(404, {"ok": False, "error": "not found"})
        tool = m.group(1)
        with LOCK:
            s = SESSIONS.get(str(b.get("customer_id")))
            if not s: return self.send(404, {"ok": False, "error": "unknown customer_id"})
            status, result = tool_call(s, tool, b)
            s["calls"].append({"n": len(s["calls"]) + 1, "tool": tool, "args": {k: v for k, v in b.items() if k != "customer_id"}, "status": status, "result": result})
        log(f"{s['customer_id']} {tool} {json.dumps(b)[:120]} -> {status} {json.dumps(result)[:160]}")
        self.send(status, result)


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8766); ap.add_argument("--host", default="127.0.0.1")
    a = ap.parse_args()
    srv = ThreadingHTTPServer((a.host, a.port), Handler); srv.daemon_threads = True
    log(f"brief-e mock listening on http://{a.host}:{srv.server_address[1]}")
    try: srv.serve_forever()
    except KeyboardInterrupt: pass
