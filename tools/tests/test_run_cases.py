import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import run_cases

CASE = {"id": "T-01", "title": "t", "brief": "A", "family": "Happy path", "level": "easy", "script": "s", "checks": ["c"],
        "variables": {"first_name": "A", "last_name": "B", "title": "Mr", "now": "2026-10-14T11:00"},
        "identity": {"date_of_birth": "1990-01-01", "phone_last4": "1234"}}


def test_ensure_personas_creates_once_then_caches(tmp_path, monkeypatch):
    calls = []
    def fake_create(personas):
        calls.append(personas)
        return {"personas": [{"id": f"pid-{len(calls)}-{i}"} for i, _ in enumerate(personas)]}
    monkeypatch.setattr(run_cases.freya, "create_personas", fake_create)
    store = tmp_path / "personas.json"
    assert run_cases.ensure_personas([CASE], None, store) == {"T-01": "pid-1-0"}
    assert run_cases.ensure_personas([CASE], None, store) == {"T-01": "pid-1-0"}      # same text: cached, not created again
    assert len(calls) == 1
    assert run_cases.ensure_personas([CASE], "pieces", store) == {"T-01": "pid-2-0"}  # a style changes the text: new persona
    assert len(calls) == 2
    assert len(json.load(open(store))) == 2


def test_session_body_carries_backend_state_only_when_present():
    assert run_cases.session_body({"id": "PUB-01"}) == {"case": "PUB-01"}
    assert run_cases.session_body({"id": "GEN-01", "fixture": "PUB-08"}) == {"case": "PUB-08"}
    assert run_cases.session_body({"id": "GEN-01", "fixture": "PUB-08", "backend": {"applications": []}}) == {"case": "PUB-08", "backend": {"applications": []}}


def test_run_once_keeps_only_conversation_failures_for_universal_cases(monkeypatch):
    uni = dict(CASE, id="UNI-01", suite="universal", expected={"outcome": None, "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []})
    gen = dict(CASE, id="GEN-01", expected={"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []})
    ledger = {"outcome": "no_promise", "reason": "refused", "promises": [], "notes": [], "callbacks": [], "transfers": [{"queue": "general"}],
              "calls": [{"tool": "transfer_to_agent", "args": {}, "result": {"ok": True}}, {"tool": "close_call", "args": {}, "result": {"ok": True}}]}
    monkeypatch.setattr(run_cases, "http", lambda path, body=None: {"variables": {"customer_id": "cust"}} if "sessions" in path else ledger)
    monkeypatch.setattr(run_cases, "start_simulation", lambda *a, **k: ("sim", "it", "completed"))
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": [{"personaId": "p-UNI-01", "outcome": "pass", "callId": None}, {"personaId": "p-GEN-01", "outcome": "pass", "callId": None}]})
    rows, *_ = run_cases.run_once("agent", [uni, gen], {"UNI-01": "p-UNI-01", "GEN-01": "p-GEN-01"})
    by = {r["id"]: r for r in rows}
    assert by["UNI-01"]["pass"] is True and by["UNI-01"]["failed"] == []                 # records differ from the placeholder: not its business
    assert by["GEN-01"]["pass"] is False and any("outcome" in f for f in by["GEN-01"]["failed"])


def test_run_once_cut_at_the_deadline_leaves_unfinished_calls_unscored(monkeypatch):
    a = dict(CASE, id="GEN-01", expected={"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []})
    b = dict(CASE, id="GEN-02", expected=a["expected"])
    ledger = {"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": [], "calls": [{"tool": "close_call", "args": {}, "result": {"ok": True}}]}
    asked, statuses = [], []
    monkeypatch.setattr(run_cases, "http", lambda path, body=None: (asked.append(path), {"variables": {"customer_id": "cust-" + str(len(asked))}} if "sessions" in path else ledger)[1])
    monkeypatch.setattr(run_cases, "start_simulation", lambda *a, **k: ("sim", "it", "cut"))
    monkeypatch.setattr(run_cases, "set_simulation_status", lambda sim, st: statuses.append(st) or True)
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": [{"personaId": "p-GEN-01", "outcome": "pass", "callId": None},
                                                                                {"personaId": "p-GEN-02", "outcome": "queued", "callId": None}]})
    rows, *_ = run_cases.run_once("agent", [a, b], {"GEN-01": "p-GEN-01", "GEN-02": "p-GEN-02"}, deadline=1.0)
    by = {r["id"]: r for r in rows}
    assert by["GEN-01"]["played"] is True and by["GEN-01"]["pass"] is True
    assert by["GEN-02"]["played"] is False and by["GEN-02"]["failed"] == ["not played: the run reached its time limit"]
    assert sum("ledger" in p for p in asked) == 1                    # the unfinished call's ledger is not even read
    assert statuses == ["completed"]                                 # the cut simulation is closed so the workspace frees up


# --- calls the agent's model never answered: not scored, and a run of them is stopped ------------------------------------

def _call(*turns, duration=62, ended="customer-ended-call"):
    """A call record: turns are (seconds, role, text); system events in between are what Freya logs around a turn."""
    msgs = [{"role": role, "message": text, "secondsFromStart": t} for t, role, text in turns]
    return {"messages": msgs, "duration": duration, "endedReason": ended}


SILENT = _call((0.2, "assistant", "Thank you for calling."), (1.9, "user", "My card is damaged."), (1.92, "system", "{\"event\":\"route_evaluated\"}"))
ANSWERED = _call((0.2, "assistant", "Thank you for calling."), (1.9, "user", "My card is damaged."), (6.0, "assistant", "I can help."),
                 (8.0, "user", "Bye."), duration=9)


def test_silence_tells_an_unanswered_call_from_an_ordinary_end():
    assert run_cases.silence(SILENT) == (False, 60.1)
    assert run_cases.no_reply(SILENT) is True
    assert run_cases.silence(ANSWERED) == (True, 1.0)                # the customer's goodbye waited a second: an ordinary end
    assert run_cases.no_reply(ANSWERED) is False
    quick = _call((0.2, "assistant", "Hello."), (1.0, "user", "Lost card!"), duration=3, ended="assistant-ended-call")
    assert run_cases.no_reply(quick) is False                        # an agent that transfers without a word ended the call itself
    short = _call((0.2, "assistant", "Hello."), (1.0, "user", "Never mind."), duration=4)
    assert run_cases.no_reply(short) is False                        # the customer left after 3 s: not a silent model


def test_no_reply_watch_stops_a_run_whose_calls_go_unanswered(monkeypatch):
    calls = {}
    monkeypatch.setattr(run_cases.freya, "api", lambda method, path, body=None, **k: {"iterations": [{"id": "it"}]})
    runs = []
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": runs})
    monkeypatch.setattr(run_cases.freya, "get_call", lambda cid: calls[cid])
    def ended(cid, call, at):
        calls[cid] = call; runs.append({"callId": cid, "outcome": "fail", "startedAt": at})
    watch = run_cases.no_reply_watch("sim")
    ended("c1", SILENT, "1"); ended("c2", SILENT, "2")
    runs.append({"callId": "c9", "outcome": "running", "startedAt": "0"})   # a call still going is not read
    assert watch() is None                                           # two unanswered calls are not yet a pattern
    ended("c3", SILENT, "3")
    assert watch() == "silent"                                       # the first three that ended got no reply
    watch, runs[:] = run_cases.no_reply_watch("sim2"), []
    ended("a1", ANSWERED, "1")
    for i in range(4): ended(f"s{i}", SILENT, f"2{i}")
    assert watch() is None                                           # the model answered once, and four in a row is not five
    ended("s4", SILENT, "30")
    assert watch() == "silent"                                       # it stopped answering mid-run: the last five got no reply


def test_wait_simulation_pauses_when_the_watch_says_so(monkeypatch):
    statuses = []
    monkeypatch.setattr(run_cases.freya, "api", lambda method, path, body=None, **k: {"simulation": {"status": "running"}})
    monkeypatch.setattr(run_cases, "set_simulation_status", lambda sim, st: statuses.append(st) or True)
    asked = []
    s = run_cases.wait_simulation("sim", poll_s=0, watch=lambda: asked.append(1) or ("silent" if len(asked) >= 2 else None))
    assert s["status"] == "silent" and statuses == ["paused"] and len(asked) == 2      # asked every third poll, so six polls


def test_run_once_does_not_score_calls_the_model_never_answered(monkeypatch):
    a = dict(CASE, id="GEN-01", expected={"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []})
    b, c = dict(CASE, id="GEN-02", expected=a["expected"]), dict(CASE, id="GEN-03", expected=a["expected"])
    ledger = {"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": [], "calls": [{"tool": "close_call", "args": {}, "result": {"ok": True}}]}
    asked, statuses = [], []
    monkeypatch.setattr(run_cases, "http", lambda path, body=None: (asked.append(path), {"variables": {"customer_id": "cust-" + str(len(asked))}} if "sessions" in path else ledger)[1])
    monkeypatch.setattr(run_cases, "start_simulation", lambda *a, **k: ("sim", "it", "silent"))
    monkeypatch.setattr(run_cases, "set_simulation_status", lambda sim, st: statuses.append(st) or True)
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": [{"personaId": "p-GEN-01", "outcome": "pass", "callId": "c1"},
                                                                                {"personaId": "p-GEN-02", "outcome": "fail", "callId": "c2"},
                                                                                {"personaId": "p-GEN-03", "outcome": "queued", "callId": None}]})
    monkeypatch.setattr(run_cases.freya, "get_call", lambda cid: {"c1": ANSWERED, "c2": SILENT}[cid])
    rows, sim, it, status, took, med = run_cases.run_once("agent", [a, b, c], {"GEN-01": "p-GEN-01", "GEN-02": "p-GEN-02", "GEN-03": "p-GEN-03"})
    by = {r["id"]: r for r in rows}
    assert by["GEN-01"]["played"] is True and by["GEN-01"]["pass"] is True and by["GEN-01"]["slowest_turn_s"] == 4.1
    assert by["GEN-02"]["played"] is False and by["GEN-02"]["why_not"] == "no reply" and "never answered" in by["GEN-02"]["failed"][0]
    assert by["GEN-03"]["played"] is False and by["GEN-03"]["why_not"] == "no reply"          # stopped before it started
    assert sum("ledger" in p for p in asked) == 1 and statuses == ["completed"]
    assert med == 4.1                                                # the unanswered call says nothing about the agent's speed


def test_slowest_turn_counts_the_customers_last_words_that_got_no_reply(monkeypatch):
    a = dict(CASE, id="GEN-01", expected={"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []})
    ledger = {"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": [], "calls": []}
    late = _call((0.2, "assistant", "Hello."), (1.0, "user", "Card."), (5.0, "assistant", "Sure."), (6.0, "user", "Well?"), duration=66)
    monkeypatch.setattr(run_cases, "http", lambda path, body=None: {"variables": {"customer_id": "cust"}} if "sessions" in path else ledger)
    monkeypatch.setattr(run_cases, "start_simulation", lambda *a, **k: ("sim", "it", "completed"))
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": [{"personaId": "p-GEN-01", "outcome": "fail", "callId": "c1"}]})
    monkeypatch.setattr(run_cases.freya, "get_call", lambda cid: late)
    rows, *_ , med = run_cases.run_once("agent", [a], {"GEN-01": "p-GEN-01"})
    assert rows[0]["played"] is True and rows[0]["slowest_turn_s"] == 60.0 and med == 60.0      # answered once, then a minute of silence
    assert (rows[0]["replies"], rows[0]["slow_replies"], rows[0]["waited_at_end"]) == (2, 1, 60.0)    # the unanswered wait is one slow reply


def test_a_cut_lets_the_calls_already_playing_finish(monkeypatch):
    statuses, left = [], [2, 1, 0]                                   # calls still playing or being judged, poll after poll
    monkeypatch.setattr(run_cases.freya, "api", lambda method, path, body=None, **k: {"simulation": {"status": "running"}})
    monkeypatch.setattr(run_cases, "set_simulation_status", lambda sim, st: statuses.append(st) or True)
    monkeypatch.setattr(run_cases, "in_flight", lambda sim: left.pop(0))
    monkeypatch.setattr(run_cases.time, "sleep", lambda s: None)
    s = run_cases.wait_simulation("sim", poll_s=0, deadline=1.0)
    assert s["status"] == "cut" and statuses == ["paused"] and left == []    # paused, then waited until nothing was in flight
    left[:] = [3] * 1000
    clock = iter(range(0, 10_000, 10))
    monkeypatch.setattr(run_cases.time, "time", lambda: next(clock))
    run_cases.finish_in_flight("sim", grace_s=60)                            # calls that never end: the wait stops at the grace
    assert len(left) > 990


# --- calls whose tool calls could not reach the bank's host: not scored ---------------------------------------------------

LOST = {"messages": [{"role": "assistant", "message": "Hello.", "secondsFromStart": 0.2}, {"role": "user", "message": "Card.", "secondsFromStart": 1.0},
                     {"role": "system", "message": '{"event":"function_call_error","function":"find_applications","error":"API request failed: Cannot connect to host x.ngrok-free.app:443 ssl:default [None]"}', "secondsFromStart": 2.0},
                     {"role": "assistant", "message": "I have a technical issue.", "secondsFromStart": 3.0}],
        "duration": 5, "endedReason": "assistant-ended-call"}


def test_unreachable_counts_connection_errors_only():
    assert run_cases.unreachable(LOST) == 1
    answered = {"messages": [{"role": "system", "message": '{"event":"function_call_error","function":"x","error":"HTTP 500: bank error"}'}]}
    assert run_cases.unreachable(answered) == 0                       # the bank answered with an error: that is the agent's to handle
    assert run_cases.unreachable({}) == 0


def test_run_once_does_not_score_calls_that_lost_the_bank(monkeypatch):
    a = dict(CASE, id="GEN-01", expected={"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []})
    b = dict(CASE, id="GEN-02", expected=a["expected"])
    ledger = {"outcome": "promise", "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": [], "calls": [{"tool": "close_call", "args": {}, "result": {"ok": True}}]}
    monkeypatch.setattr(run_cases, "http", lambda path, body=None: {"variables": {"customer_id": "cust"}} if "sessions" in path else ledger)
    monkeypatch.setattr(run_cases, "start_simulation", lambda *a, **k: ("sim", "it", "completed"))
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": [{"personaId": "p-GEN-01", "outcome": "pass", "callId": "c1"},
                                                                                {"personaId": "p-GEN-02", "outcome": "fail", "callId": "c2"}]})
    monkeypatch.setattr(run_cases.freya, "get_call", lambda cid: {"c1": ANSWERED, "c2": LOST}[cid])
    rows, *_ = run_cases.run_once("agent", [a, b], {"GEN-01": "p-GEN-01", "GEN-02": "p-GEN-02"})
    by = {r["id"]: r for r in rows}
    assert by["GEN-01"]["played"] is True and by["GEN-01"]["pass"] is True
    assert by["GEN-02"]["played"] is False and by["GEN-02"]["why_not"] == "host" and "could not reach the bank's host" in by["GEN-02"]["failed"][0]


# --- a brief that brings its own test customers and a mock without a ledger -----------------------------------------------

def test_ledger_from_call_reads_the_tool_calls_of_the_transcript():
    ev = lambda **e: {"role": "system", "message": json.dumps(e)}
    call = {"messages": [
        ev(event="function_call_start", function="code_exec", args={"code": "x"}),
        ev(event="function_call_start", function="api_call", args={"url": "https://m.example/api/v1/list_items", "method": "POST", "body": {"data": {"customerId": "1"}}}),
        ev(event="function_call_complete", function="api_call", result={"status": "success", "status_code": 200, "data": {"data": {"items": []}}}),
        {"role": "assistant", "message": "Hello"},
        ev(event="function_call_start", function="read_item", args={"url": "https://m.example/api/v1/get_item", "body": {"data": {"itemId": "x"}}}),
        ev(event="function_call_error", function="read_item", error="API request failed: 404"),
        ev(event="function_call_start", function="end_call", args={})]}
    led = run_cases.ledger_from_call(call)
    assert led["source"] == "transcript" and led["outcome"] is None
    assert [(c["tool"], c["result"]["ok"]) for c in led["calls"]] == [("list_items", True), ("get_item", False)]
    assert led["calls"][0]["args"] == {"data": {"customerId": "1"}} and led["calls"][0]["status"] == 200


def test_customer_key_and_a_persona_in_the_customers_language():
    assert run_cases.customer_key({"customer_id": "c1", "now": "x"}) == "c1"
    assert run_cases.customer_key({"customerNumber": "10000001", "now": "x"}) == "10000001"
    case = {"id": "GEN-01", "title": "t", "family": "Happy", "script": "Asks for the debt.", "checks": ["c"], "brief": "x",
            "variables": {"customerNumber": "10000001", "now": "2026-01-05T10:00:00+03:00"},
            "persona": "You are Ada Test. You have one card, a Classic card ending 1234.", "language": "tr"}
    p = run_cases.persona_for(case, case)
    assert p["prompt"].startswith("LANGUAGE: You speak only Turkish") and "Ada Test" in p["prompt"]
