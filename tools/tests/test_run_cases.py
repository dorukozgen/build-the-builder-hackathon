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
    monkeypatch.setattr(run_cases.freya, "run_simulation", lambda *a, **k: ("sim", "it", "completed"))
    monkeypatch.setattr(run_cases.freya, "get_iteration", lambda sim, it: {"runs": [{"personaId": "p-UNI-01", "outcome": "pass", "callId": None}, {"personaId": "p-GEN-01", "outcome": "pass", "callId": None}]})
    rows, *_ = run_cases.run_once("agent", [uni, gen], {"UNI-01": "p-UNI-01", "GEN-01": "p-GEN-01"})
    by = {r["id"]: r for r in rows}
    assert by["UNI-01"]["pass"] is True and by["UNI-01"]["failed"] == []                 # records differ from the placeholder: not its business
    assert by["GEN-01"]["pass"] is False and any("outcome" in f for f in by["GEN-01"]["failed"])
