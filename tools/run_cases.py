"""Run cases against an agent and score them from the bank's ledger and the judge's reading of the conversation.

    python tools/run_cases.py <agent_id> [--brief A|B] [--cases public-test-set.json] [--out results/run.json] [--reps 3] [--style talkative]

Needs FREYA_API_KEY (your workspace) and FREYA_BANK_TEAM_KEY (any secret of 16+ characters your team picks, the same one every time).
"""
import argparse, hashlib, json, os, pathlib, sys, time
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import freya
from score import http, score_ledger

PERSONA = """OUTPUT RULE: Write only the words you say on the phone. No stage directions, no brackets. One or two short sentences per turn, then wait for the other side.

WHO YOU ARE: {who}

WHAT HAPPENS IN THIS CALL: {script}

RULES:
- Answer what you are asked. Do not volunteer information nobody asked for.
- When you give a number or a date, say all of it in one turn. Never stop halfway through.
- Do not invent dates, amounts or facts that are not written above. If asked something that is not covered, give a short neutral answer.
- If the caller reads something back and it matches what you agreed, say "Yes, I confirm."
- When the caller says goodbye, say "Thank you, goodbye." and say nothing more."""

# How a customer talks. The facts of the case stay the same, only the way of saying them changes.
STYLES = {
    "pieces": "HOW YOU TALK: you give long numbers and dates in two parts. Say the first half, stop, and give the rest in your next turn or when asked. This replaces the rule about saying all of it in one turn.",
    "corrects": "HOW YOU TALK: the first time you say a day or an amount, you say a slightly different one first and correct yourself in the same sentence, like 'the 21st, sorry, I mean the 20th'. The corrected value is the one written above. Do this once or twice in the call, not more. Never do it with a security answer: those you say right the first time unless the text above says otherwise.",
    # The answer comes first: with the chatter first, the simulated customer's turns came out cut off mid-word ("before my cousin'")
    # and the asked-for digits never arrived, so the agent asked fifteen times and the case tested the simulator, not the agent.
    "talkative": "HOW YOU TALK: you talk a lot. You give the answer you were asked for first, then add one sentence about your day, the traffic or how busy work is. Once in the call you mention that your cousin's wedding is on the 30th. It has nothing to do with any payment or application, and you never offer it as a date for one.",
    "asks_back": "HOW YOU TALK: twice in the call, before you answer, you ask a short question back, like 'why do you need that?' or 'which account is this about?'. Whatever the caller replies, you then give your answer.",
    "in_words": "HOW YOU TALK: you say every amount and every date in words and never in digits, like 'four hundred and fifty-five' and 'the twenty-second of October'. Postcodes, years and other codes you say digit by digit.",
}

LANGUAGES = {"tr": "Turkish", "en": "English", "de": "German", "fr": "French", "es": "Spanish", "ar": "Arabic"}


def persona_for(case, ident, style=None):
    v, i = case["variables"], ident.get("identity") or {}
    lang = case.get("language") or ident.get("language")
    if ident.get("persona"):                                          # a brief's own test customer: who they are, in the fixture's words
        who = ident["persona"]
    elif case["family"] == "Third party" or case.get("third_party"):
        me = f"{v['first_name']} {v['last_name']}"
        who = f"You are NOT {me}. You answered this phone. You do not know {me}'s security answers and you would not give them. The text below says who you are."
    else:
        me = f"{v['first_name']} {v['last_name']}"
        say = {"date_of_birth": "Your date of birth is {} (say it in words, like '14 March 1988').", "phone_last4": "The last four digits of your phone number on file are {}.",
               "postcode": "The postcode of your registered address is {}.", "birth_year": "Your year of birth is {}.",
               "company_number": "Your company number is {}.", "founded_year": "The company was founded in {}."}
        who = f"You are {me}. " + " ".join(say.get(k, "Your " + k.replace("_", " ") + " is {}.").format(x) for k, x in i.items()) + " Give these only when asked, and give the wrong ones where the text below says so."
    style = style or case.get("style")
    text = PERSONA.format(who=who, script=case["script"]) + ("\n\n" + STYLES[style] if style else "")
    if lang: text = f"LANGUAGE: You speak only {LANGUAGES.get(lang, lang)}, as a native speaker, in every turn. Never switch language.\n\n" + text
    return {"name": case["id"] + " " + case["title"] + (f" [{style}]" if style else ""), "prompt": text, "successCriteria": "All of these are true:\n- " + "\n- ".join(case["checks"]), "tags": ["hackathon", "brief-" + case["brief"]]}

def ensure_personas(cases, style=None, store=ROOT / ".personas.json"):
    """One persona per case, created on first use and cached in `store`. Returns {case_id: persona_id}.
    A persona is recreated whenever its text changes, so an edited case never runs with a stale customer."""
    ident = {c["id"]: {"identity": c.get("identity") or {}, "persona": c.get("persona"), "language": c.get("language")} for c in cases}
    store = pathlib.Path(store); ids = json.load(open(store)) if store.exists() else {}
    spec = {c["id"]: persona_for(c, ident[c["id"]], style) for c in cases}
    key = {i: i + ":" + hashlib.sha1(json.dumps(p, sort_keys=True).encode()).hexdigest()[:10] for i, p in spec.items()}
    new = [c for c in cases if key[c["id"]] not in ids]
    if new:
        made = freya.create_personas([spec[c["id"]] for c in new])["personas"]
        ids.update({key[c["id"]]: p["id"] for c, p in zip(new, made)}); json.dump(ids, open(store, "w"), indent=1)
    return {c["id"]: ids[key[c["id"]]] for c in cases}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("agent_id"); ap.add_argument("--brief"); ap.add_argument("--cases", default=str(ROOT / "public-test-set.json")); ap.add_argument("--out"); ap.add_argument("--only"); ap.add_argument("--reps", type=int, default=1); ap.add_argument("--style", choices=sorted(STYLES)); ap.add_argument("--rerun-if-slow", type=int, default=0)
    a = ap.parse_args()
    cases = [c for c in json.load(open(a.cases)) if (not a.brief or c["brief"] == a.brief) and (not a.only or c["id"] in a.only.split(","))]
    ids = ensure_personas(cases, a.style)
    (ROOT / "results").mkdir(exist_ok=True)
    reps, total_s = [], 0
    for rep in range(a.reps):
        for attempt in range(1 + a.rerun_if_slow):                   # organisers: a run made while the model was slow is thrown away and repeated
            rows, sim_id, it_id, status, took, med = run_once(a.agent_id, cases, ids, a.style)
            if med <= 10 or attempt == a.rerun_if_slow: break
            print(f"-- run discarded: median slowest turn {med:.0f} s. Waiting 5 minutes, then repeating it.\n", flush=True); time.sleep(300)
        reps.append(rows); total_s += took
        if a.reps > 1: print(f"-- run {rep + 1} of {a.reps}: {sum(r['pass'] for r in rows)} / {len(rows)} passed, {took:.0f} s\n")
    need = a.reps                                                # a customer counts only when every run passes
    final = [{"id": c["id"], "family": c["family"], "passes": sum(r[k]["pass"] for r in reps), "runs": a.reps, "pass": sum(r[k]["pass"] for r in reps) >= need} for k, c in enumerate(cases)]
    n = sum(f["pass"] for f in final)
    if a.reps > 1:
        for f in final: print(("PASS" if f["pass"] else "FAIL"), f["id"], f"{f['passes']}/{f['runs']}")
    print(f"\n{n} / {len(final)} passed (bank records and conversation checks){'' if a.reps == 1 else f', a customer counts with {need} of {a.reps} runs'}. Last simulation {sim_id}, status {status}, {total_s:.0f} s.")
    with open(ROOT / "results" / "log.jsonl", "a") as f:      # one line per run, the record of how the score moved over time
        f.write(json.dumps({"at": time.strftime("%Y-%m-%d %H:%M:%S"), "agent_id": a.agent_id, "brief": a.brief, "runs": a.reps, "passed": n, "total": len(final), "seconds": round(total_s), "failed": [f["id"] for f in final if not f["pass"]]}) + "\n")
    if a.out:
        pathlib.Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        json.dump({"agent_id": a.agent_id, "simulation_id": sim_id, "iteration_id": it_id, "seconds": round(total_s), "passed": n, "total": len(final), "runs": a.reps, "final": final, "rows": reps[-1], "all_rows": reps}, open(a.out, "w"), indent=1)

def session_body(case):
    """What the practice-session endpoint gets: the fixture to play and, for a self-hosted mock that takes it, the case's backend state."""
    body = {"case": case.get("fixture", case["id"])}
    if case.get("backend"): body["backend"] = case["backend"]
    return body

# Calls played at the same time in one simulation (the API allows 1 to 1000). A simulation of N customers takes about N / concurrency
# waves of a minute or so: at 5, 63 customers took 16 minutes, more than half a build. The agent's model is shared by every team and
# its own load moved its speed more than ours did: at 5 and at 8 calls a sixth of the replies took over 10 s, and 4 calls at 5 once
# saw half of them do so. tools/benchmark.py adapts the number per slot from the share of slow replies, between CONCURRENCY_MIN and
# CONCURRENCY_MAX; this is the starting point. freya.py is the kit's client and stays as the kit ships it, so the simulation helpers live here.
CONCURRENCY = int(os.environ.get("FREYA_SIM_CONCURRENCY", "16"))
CONCURRENCY_MIN, CONCURRENCY_MAX = 5, 40
SLOW_TURN_S = 10.0                                                     # a reply slower than this is a slow one; benchmark.py counts them per run


def running_simulations():
    """The simulations of the workspace that are still running, newest first: {id, name, status, createdAt}. [] when the listing fails."""
    try:
        r = freya.api("GET", "/api/v2/simulations", workspaceId=freya.workspace_id()); items = r.get("simulations") or r.get("items") or r
        return sorted([s for s in items if isinstance(s, dict) and s.get("status") in ("running", "pending", "queued")], key=lambda s: s.get("createdAt") or "", reverse=True)
    except Exception: return []


FINISHED = ("pass", "fail", "inconclusive", "error")                   # a run's outcome once its call ended and the judge read it


def set_simulation_status(sim_id, status):
    """Best effort: pause a simulation (no new call starts) or mark it completed (the workspace is free for the next one)."""
    for params in ({}, {"workspaceId": freya.workspace_id()}):
        try: freya.api("PUT", f"/api/v2/simulations/{sim_id}", {"status": status}, **params); return True
        except Exception as e: err = e
    print(f"could not set simulation {sim_id} to {status}: {str(err)[:160]}", flush=True); return False


# When the agent's model does not answer, the customer says its first sentence, waits a minute in silence and hangs up. Such a call
# tests nothing in the workflow: it is not scored, and a run whose calls all go that way is stopped instead of waiting 15 minutes.
NO_REPLY_S = 30                                                        # seconds of silence after the customer's words before a hang-up counts
NO_REPLY_FIRST, NO_REPLY_STREAK = 3, 5                                 # the first 3 calls that ended, or the last 5, all without a reply


def silence(call):
    """(answered, waited): whether the phone agent replied to anything the customer said, and how many seconds the customer's last
    words had waited for a reply when the call ended (0 when they got one)."""
    answered, since = False, None
    for m in call.get("messages") or []:
        t = m.get("secondsFromStart")
        if t is None or m.get("role") not in ("user", "assistant"): continue
        if m["role"] == "user": since = t if since is None else since
        elif since is not None: answered, since = True, None
    return answered, (round(max(0.0, (call.get("duration") or 0) - since), 1) if since is not None else 0.0)


def no_reply(call):
    """True when the agent replied to nothing the customer said and the customer hung up after NO_REPLY_S seconds or more of silence:
    the agent's model did not answer, so the call tested nothing in the workflow."""
    answered, waited = silence(call)
    return not answered and call.get("endedReason") == "customer-ended-call" and waited >= NO_REPLY_S


UNREACHABLE = ("Cannot connect to host", "Server disconnected", "Connection reset", "ClientConnectorError")


def unreachable(call):
    """How many tool calls in this call never reached the bank's host: a connection error, not an answer from the bank. A free tunnel
    refuses connections for the rest of a minute once about 120 arrived; such a call tested the outage, not the agent."""
    return sum(m.get("role") == "system" and "function_call_error" in (m.get("message") or "") and any(k in m["message"] for k in UNREACHABLE)
               for m in call.get("messages") or [])


def no_reply_watch(sim_id):
    """A watch for wait_simulation: "silent" once the agent's model has stopped answering, i.e. none of the first NO_REPLY_FIRST calls
    that ended got a reply, or none of the last NO_REPLY_STREAK. Reads each ended call once."""
    answered, it = {}, []                                              # call id -> whether the agent answered, in the order the calls were read
    def check():
        try:
            if not it:
                its = freya.api("GET", f"/api/v2/simulations/{sim_id}/iterations"); its = its.get("iterations") or its.get("items") or its
                if not its: return None
                it.append(its[0]["id"])
            runs = freya.get_iteration(sim_id, it[0]).get("runs") or []
        except Exception: return None
        for r in sorted(runs, key=lambda r: r.get("startedAt") or ""):
            if not r.get("callId") or r["callId"] in answered or r.get("outcome") in ("queued", "running"): continue
            try: call = freya.get_call(r["callId"])
            except Exception: continue
            if call.get("endedReason"): answered[r["callId"]] = not no_reply(call)
        got = list(answered.values())
        if (len(got) >= NO_REPLY_FIRST and not any(got)) or (len(got) >= NO_REPLY_STREAK and not any(got[-NO_REPLY_STREAK:])): return "silent"
        return None
    return check


CUT_GRACE_S = 90                                                       # after a cut, how long the calls already playing may take to end and be judged


def in_flight(sim_id):
    """How many calls of the simulation are still playing or being judged; 0 when that cannot be read."""
    try:
        its = freya.api("GET", f"/api/v2/simulations/{sim_id}/iterations"); its = its.get("iterations") or its.get("items") or its
        return sum(r.get("outcome") in ("running", "analyzing") for r in freya.get_iteration(sim_id, its[0]["id"]).get("runs") or []) if its else 0
    except Exception: return 0


def finish_in_flight(sim_id, grace_s=CUT_GRACE_S, poll_s=10):
    """A paused simulation starts no new call, but the calls already playing go on and are judged. Wait up to `grace_s` for them, so
    the caller scores them instead of reporting them as not played."""
    end = time.time() + grace_s
    while time.time() < end:
        n = in_flight(sim_id)
        if not n: return
        print(f"waiting up to {end - time.time():.0f} s for the {n} call{'s' if n != 1 else ''} still playing or being judged", flush=True)
        time.sleep(poll_s)


def wait_simulation(sim_id, poll_s=10, deadline=None, watch=None):
    """Wait for a simulation to reach a final status and return it. A 5xx or a timeout while polling does not stop the simulation on
    Freya, so the poll goes on (after a pause) instead of raising: raising made the caller start a second run that queued behind the first.
    At `deadline` (epoch seconds) the simulation is paused, the calls already playing get CUT_GRACE_S to end, and it is returned with
    status "cut": the caller scores the calls that finished. `watch`, asked every third poll, can stop it at once: the status it returns
    ("silent", see no_reply_watch) replaces "cut"."""
    import urllib.error
    slips = polls = 0
    while True:
        time.sleep(poll_s); polls += 1
        try:
            s = freya.api("GET", f"/api/v2/simulations/{sim_id}"); s = s.get("simulation") or s; slips = 0
        except (RuntimeError, urllib.error.URLError, TimeoutError, OSError) as e:
            slips += 1
            if slips > 20: raise RuntimeError(f"polling simulation {sim_id} failed 20 times in a row: {e}") from None
            print(f"polling simulation {sim_id}: {str(e)[:120]} — it keeps running on Freya, polling again in 30 s", flush=True); time.sleep(30); continue
        if s.get("status") in ("completed", "failed", "paused"): return s
        if deadline and time.time() >= deadline:
            print(f"the run reached its time limit: pausing simulation {sim_id} and scoring the calls that finished", flush=True)
            set_simulation_status(sim_id, "paused"); finish_in_flight(sim_id)
            return {**s, "status": "cut"}
        why = watch() if watch and polls % 3 == 0 else None
        if why:
            print(f"the phone agent's model stopped answering: the calls that ended got no reply to the customer's words. Pausing simulation {sim_id}", flush=True)
            set_simulation_status(sim_id, "paused")
            return {**s, "status": why}


def start_simulation(agent_id, name, variables_by_persona, concurrency=None, max_seconds=420, deadline=None):
    """Start a text simulation with the kit's request (freya.run_simulation's body), wait for it, return (simulation_id, iteration_id, status).
    Names the simulation the workspace is busy with and how long this run has waited for it. With a `deadline` (epoch seconds) the
    status is "cut" when the simulation had to be paused before it ended; it is "silent" when it was paused because the agent's model
    stopped answering (no_reply_watch)."""
    body = {"agentId": agent_id, "name": name, "mode": "chat", "selectedPersonaIds": list(variables_by_persona),
            "customerVariablesMap": variables_by_persona, "maxConcurrentCalls": concurrency or CONCURRENCY, "runsPerPersona": 1, "maxCallDurationSeconds": max_seconds,
            "assistantLlmOverride": freya.AGENT_LLM, "routingLlmOverride": freya.AGENT_LLM, "extractionLlmOverride": freya.AGENT_LLM,
            "personaLlmOverride": freya.SIM_LLM, "analysisLlmOverride": freya.SIM_LLM}
    waited = 0
    while True:                      # a workspace runs one simulation at a time: wait for the running one instead of failing
        try: sim = freya.api("POST", "/api/v2/simulations", body); break
        except RuntimeError as e:
            if "concurrent simulations" not in str(e): raise
            if deadline and time.time() >= deadline: raise RuntimeError(f"the workspace stayed busy with another simulation until this run's time limit ({waited // 60} min of waiting)") from None
            if waited == 0:
                busy = running_simulations(); who = ", ".join(f"{s.get('name')!r} since {s.get('createdAt')}" for s in busy[:3]) or "unknown"
                print(f"another simulation is running in this workspace ({who}); this run waits for it. "
                      "If it is yours from a run that was cut off, it ends on its own; another builder's needs its builder to finish.", flush=True)
            else: print(f"still waiting for the workspace, {waited // 60} min so far", flush=True)
            time.sleep(30); waited += 30
    sim_id = (sim.get("simulation") or sim)["id"]
    print(f"simulation {sim_id} started, {len(variables_by_persona)} customers, {body['maxConcurrentCalls']} at a time"
          + (f", time limit {time.strftime('%H:%M:%S', time.localtime(deadline))}" if deadline else ""), flush=True)
    s = wait_simulation(sim_id, deadline=deadline, watch=no_reply_watch(sim_id))
    its = freya.api("GET", f"/api/v2/simulations/{sim_id}/iterations"); its = its.get("iterations") or its.get("items") or its
    return sim_id, its[0]["id"], s.get("status")


def ledger_from_call(call):
    """The tool calls of one call, read from its transcript: for a mock that keeps no ledger. A call with a URL is named by the URL's
    last path segment, so a tool run by the engine and the same tool called by the model get one name. No records: `outcome` is None."""
    calls, open_ = [], {}
    for m in (call or {}).get("messages") or []:
        if m.get("role") != "system": continue
        try: ev = json.loads(m.get("message") or "")
        except ValueError: continue
        if not isinstance(ev, dict): continue
        kind, fn = ev.get("event"), ev.get("function")
        if kind == "function_call_start" and fn and fn not in ("code_exec", "end_call"):
            args = ev.get("args") if isinstance(ev.get("args"), dict) else {}
            url = str(args.get("url") or "")
            rec = {"tool": url.rstrip("/").rsplit("/", 1)[-1] if url else fn, "args": args.get("body", args), "result": {}, "status": None}
            calls.append(rec); open_[fn] = rec
        elif kind in ("function_call_complete", "function_call_error") and fn in open_:
            rec, res = open_.pop(fn), ev.get("result")
            if kind == "function_call_error": rec["result"] = {"ok": False, "error": ev.get("error")}
            elif isinstance(res, dict):
                data = res.get("data")
                rec["status"] = res.get("status_code")
                rec["result"] = {"ok": res.get("status") == "success", **(data if isinstance(data, dict) else {"data": data})}
    return {"source": "transcript", "outcome": None, "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": [], "calls": calls}


def customer_key(variables):
    """The session's customer: `customer_id` on the practice mock, else the first variable a brief's own mock returns (its customer number)."""
    return str(variables.get("customer_id") or variables.get("customerNumber") or next(iter(variables.values()), ""))


def forget_personas(store=ROOT / ".personas.json"):
    """Drop the persona cache: its ids belong to another workspace (Freya answers "Persona not found"). The next ensure_personas recreates them."""
    store = pathlib.Path(store)
    if store.exists(): store.replace(store.with_suffix(".stale.json"))


def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
    """One simulation: every case once. Returns the scored rows. `style` is the run's --style, needed only to recreate stale personas;
    `concurrency` is how many calls play at once (CONCURRENCY when None). With a `deadline` (epoch seconds) a simulation still running
    then is paused: the calls that finished are scored, the others come back with `played` False and are not scored at all.
    A call the agent's model never answered (no_reply) comes back the same way, `why_not` "no reply" instead of "time limit"; so does
    a call whose tool calls could not reach the bank's host (unreachable), `why_not` "host"."""
    # a generated case borrows a practice customer's bank data through `fixture` (tools/benchmark.py); a public case is its own fixture
    sessions = {c["id"]: http("/v1/practice/sessions", session_body(c))["variables"] for c in cases}
    t0 = time.time()
    try: sim_id, it_id, status = start_simulation(agent_id, f"cases {time.strftime('%H:%M:%S')}", {ids[c["id"]]: sessions[c["id"]] for c in cases}, concurrency, deadline=deadline)
    except RuntimeError as e:
        if "Persona not found" not in str(e): raise
        print("Freya does not know the cached personas (they belong to another workspace): recreating them once", flush=True)
        forget_personas(); ids.update(ensure_personas(cases, style))
        sim_id, it_id, status = start_simulation(agent_id, f"cases {time.strftime('%H:%M:%S')}", {ids[c["id"]]: sessions[c["id"]] for c in cases}, concurrency, deadline=deadline)
    took = time.time() - t0
    judge = {r["personaId"]: r for r in freya.get_iteration(sim_id, it_id)["runs"]}
    if status in ("cut", "silent"): set_simulation_status(sim_id, "completed")       # its unfinished calls are given up: free the workspace
    rows, calls = [], {}
    def unplayed(c, why, reason, call_id=None):
        rows.append({"id": c["id"], "level": c["level"], "family": c["family"], "pass": False, "played": False, "why_not": why, "failed": [f"not played: {reason}"],
                     "call_id": call_id, "tools": [], "calls": [], "customer_id": customer_key(sessions[c["id"]])})
        print("NOT PLAYED", c["id"], f"{c['level']:<6}", f"{c['family']:<14}", "|", reason)
    for c in cases:
        j = judge.get(ids[c["id"]], {})                      # the conversation checks, read from the transcript by the judge model
        if status in ("cut", "silent") and j.get("outcome") not in FINISHED:
            if status == "cut": unplayed(c, "time limit", "the run reached its time limit")
            else: unplayed(c, "no reply", "the run was stopped because the agent's model stopped answering")
            continue
        try: call = freya.get_call(j["callId"]) if j.get("callId") else None
        except Exception: call = None
        if call and no_reply(call):
            unplayed(c, "no reply", f"the agent's model never answered the customer ({silence(call)[1]:.0f} s of silence, then the customer hung up)", j.get("callId")); continue
        lost = unreachable(call) if call else 0
        if lost:
            unplayed(c, "host", f"{lost} tool call{'s' if lost != 1 else ''} could not reach the bank's host (a connection error), so the call tested the outage, not the agent", j.get("callId")); continue
        calls[c["id"]] = call
        try: led = http("/v1/practice/ledger/" + customer_key(sessions[c["id"]]))
        except Exception: led = None
        if not isinstance(led, dict) or "calls" not in led: led = ledger_from_call(call)       # a mock without a ledger
        r = score_ledger(c, led)
        if j.get("outcome") != "pass": r["failed"].append("conversation: " + " ".join(str(j.get("reason") or "no verdict").split())[:400])
        if c.get("suite") == "universal":                    # a universal case has no expected records: only what holds for every brief counts
            keep = ("conversation:", "not closed with close_call", "before identity was verified", "not on the line")
            r["failed"] = [f for f in r["failed"] if any(k in f for k in keep)]
        r["pass"] = not r["failed"]
        rows.append({"id": c["id"], "level": c["level"], "family": c["family"], "pass": r["pass"], "played": True, "failed": r["failed"], "call_id": j.get("callId"), "tools": [x["tool"] for x in led["calls"]], "calls": led["calls"], "customer_id": customer_key(sessions[c["id"]])})
        print(("PASS" if r["pass"] else "FAIL"), c["id"], f"{c['level']:<6}", f"{c['family']:<14}", "|", " > ".join(x["tool"].replace("verify_identity", "verify").replace("create_promise", "promise") for x in led["calls"]) or "(no tool calls)")
        for f in r["failed"]: print("       -", f[:260])
    # How long the phone agent kept the customer waiting. A call whose customer hung up after long silences says
    # something about the speed of the model at that moment, not only about the agent.
    waits = []
    for r in rows:
        call = calls.get(r["id"])
        if not call: continue
        last_user, worst, replies = None, 0.0, []
        for m in call.get("messages", []):
            t = m.get("secondsFromStart")
            if t is None: continue
            if m.get("role") == "user": last_user = t
            elif last_user is not None:
                worst = max(worst, t - last_user)
                if m.get("role") == "assistant": replies.append(t - last_user); last_user = None
        tail = silence(call)[1]                              # the customer's last words that never got a reply count as a turn too
        if tail > SLOW_TURN_S: replies.append(tail)
        worst = max(worst, tail)
        r["slowest_turn_s"] = round(worst, 1); r["ended"] = call.get("endedReason"); r["waited_at_end"] = tail; waits.append(worst)
        r["replies"], r["slow_replies"] = len(replies), sum(x > SLOW_TURN_S for x in replies)
    if waits:
        waits.sort(); med = waits[len(waits) // 2]; hung = sum(r.get("ended") == "customer-ended-call" and not r["pass"] and r.get("played", True) for r in rows)
        print(f"\nslowest agent turn per call: median {med:.0f} s, worst {waits[-1]:.0f} s. Failed calls where the customer hung up: {hung}.")
        if med > 10: print("WARNING: the phone agent was slow in this run. If the same agent is fast in another run, the model was busy and this score is too low.")
    silent = [r["id"] for r in rows if r.get("why_not") == "no reply"]
    if silent: print(f"\nthe agent's model answered none of the customer's words in {len(silent)} call{'s' if len(silent) != 1 else ''}: not scored ({', '.join(silent)}).")
    return rows, sim_id, it_id, status, took, (med if waits else 0)

if __name__ == "__main__": main()
