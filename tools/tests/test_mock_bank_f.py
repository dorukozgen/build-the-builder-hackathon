import json, pathlib, sys, threading, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import pytest
import mock_bank_f as M


@pytest.fixture(scope="module")
def base():
    srv = M.make_server("127.0.0.1", 0)
    t = threading.Thread(target=srv.serve_forever, daemon=True); t.start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()


def call(base, path, body=None, key="team-secret"):
    h = {"content-type": "application/json"}
    if key: h["x-team-key"] = key
    req = urllib.request.Request(base + path, data=json.dumps(body).encode() if body is not None else None, headers=h, method="POST" if body is not None else "GET")
    try:
        with urllib.request.urlopen(req, timeout=10) as r: return r.status, json.load(r)
    except urllib.error.HTTPError as e: return e.code, json.load(e)


def session(base, case, backend=None):
    body = {"case": case}
    if backend: body["backend"] = backend
    st, r = call(base, "/v1/practice/sessions", body)
    assert st == 200 and r["ok"], r
    return r["variables"]


def verify(base, cid, dob, phone):
    assert call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": dob})[1]["verified"]
    assert call(base, "/v1/verify_identity", {"customer_id": cid, "field": "phone_last4", "answer": phone})[1]["all_verified"]


def test_session_identity_and_gating(base):
    v = session(base, "PUB-01")
    assert v["customer_id"].startswith("f_") and v["first_name"] == "Daniel" and v["title"] == "Mr" and v["now"] == "2026-10-14T11:00"
    cid = v["customer_id"]
    assert call(base, "/v1/find_applications", {"customer_id": cid, "type": "limit_increase"})[1] == {"ok": False, "error": "identity not verified"}
    assert call(base, "/v1/get_requirements", {"customer_id": cid, "type": "limit_increase"})[1]["ok"]          # no identity needed
    r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": "1998-08-12"})[1]
    assert r == {"ok": True, "verified": False, "wrong_answers_left": 2, "all_verified": False}
    r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": "1988-14-03"})[1]
    assert r["hint"] == "day_month_swapped" and r["wrong_answers_left"] == 2
    r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": "abc"})[1]
    assert r["ok"] is False and "YYYY-MM-DD" in r["error"]
    r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": "14 March 1988"})[1]
    assert r["verified"] is True and r["all_verified"] is False
    r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "phone_last4", "answer": "4471"})[1]
    assert r["verified"] is True and r["all_verified"] is True
    assert call(base, "/v1/verify_identity", {"customer_id": "c_test", "field": "phone_last4", "answer": "4471"})[0] == 404
    assert call(base, "/v1/practice/sessions", {"case": "PUB-01"}, key=None)[0] == 401
    assert call(base, "/v1/practice/sessions", {"case": "NOPE"})[1]["error"] == "unknown practice case"


def test_three_wrong_answers_end_the_check(base):
    cid = session(base, "PUB-03")["customer_id"]
    for left in (2, 1, 0):
        r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": "2000-01-01"})[1]
        assert r["wrong_answers_left"] == left and r["verified"] is False
    r = call(base, "/v1/verify_identity", {"customer_id": cid, "field": "date_of_birth", "answer": "1992-07-21"})[1]   # the right answer, too late
    assert r["verified"] is False and r["wrong_answers_left"] == 0


def test_requirements_create_find_get_close_and_ledger(base):
    cid = session(base, "PUB-09")["customer_id"]; verify(base, cid, "1981-08-11", "5560")
    req = call(base, "/v1/get_requirements", {"customer_id": cid, "type": "limit_increase"})[1]
    names = [f["name"] for f in req["fields"]]
    assert "requested_limit" in names and next(f for f in req["fields"] if f["name"] == "requested_limit")["format"] == "amount"
    assert all({"name", "question", "format", "required"} <= set(f) for f in req["fields"])
    assert call(base, "/v1/get_requirements", {"customer_id": cid, "type": "mortgage"})[1]["ok"] is False
    assert call(base, "/v1/find_applications", {"customer_id": cid, "type": "limit_increase"})[1]["applications"] == []
    bad = call(base, "/v1/create_application", {"customer_id": cid, "type": "limit_increase", "fields": {"requested_limit": "lots"}})[1]
    assert bad["ok"] is False and "requested_limit" in bad["error"]
    r = call(base, "/v1/create_application", {"customer_id": cid, "type": "limit_increase", "fields": json.dumps({"requested_limit": 5000})})[1]   # a JSON string is accepted too
    assert r["ok"] and r["application_id"].startswith("APP-") and r["status"] == "received"
    found = call(base, "/v1/find_applications", {"customer_id": cid, "type": "limit_increase"})[1]["applications"]
    assert [a["application_id"] for a in found] == [r["application_id"]] and found[0]["status"] == "received" and found[0]["created_on"] == "2026-10-14"
    g = call(base, "/v1/get_application", {"customer_id": cid, "application_id": r["application_id"]})[1]
    assert g["ok"] and g["status"] == "received" and g["type"] == "limit_increase" and g["note"] == ""
    assert call(base, "/v1/get_application", {"customer_id": cid, "application_id": "APP-000000"})[1]["ok"] is False
    assert call(base, "/v1/close_call", {"customer_id": cid, "outcome": "no_action"})[1]["ok"] is False          # reason required
    assert call(base, "/v1/close_call", {"customer_id": cid, "outcome": "done"})[1]["ok"] is False
    assert call(base, "/v1/close_call", {"customer_id": cid, "outcome": "application_created"})[1]["ok"] is True
    assert call(base, "/v1/transfer_to_agent", {"customer_id": cid, "queue": "general"})[1] == {"ok": False, "error": "call closed"}
    st, led = call(base, "/v1/practice/ledger/" + cid)
    assert st == 200 and led["outcome"] == "application_created" and led["reason"] is None
    assert [a["type"] for a in led["applications"]] == ["limit_increase"] and led["transfers"] == [] and led["promises"] == [] and led["notes"] == [] and led["callbacks"] == []
    assert led["calls"][-1]["tool"] == "transfer_to_agent" and led["calls"][-1]["result"]["error"] == "call closed"
    assert led["calls"][0]["tool"] == "verify_identity" and led["calls"][0]["n"] == 1 and "customer_id" not in led["calls"][0]["args"]


def test_backend_state_transfer_and_timeout_fault(base, monkeypatch):
    v = session(base, "PUB-08", backend={"applications": [{"type": "limit_increase", "status": "in_review", "created_on": "2026-10-09"}]})
    cid = v["customer_id"]; verify(base, cid, "1993-04-28", "3317")
    found = call(base, "/v1/find_applications", {"customer_id": cid, "type": "limit_increase"})[1]["applications"]
    assert len(found) == 1 and found[0]["status"] == "in_review" and found[0]["application_id"].startswith("APP-") and found[0]["note"] == ""
    assert call(base, "/v1/find_applications", {"customer_id": cid, "type": "address_change"})[1]["applications"] == []
    assert call(base, "/v1/transfer_to_agent", {"customer_id": cid, "queue": "sales"})[1]["ok"] is False
    assert call(base, "/v1/transfer_to_agent", {"customer_id": cid, "queue": "applications"})[1]["ok"] is True
    assert call(base, "/v1/close_call", {"customer_id": cid, "outcome": "transferred", "reason": "applications"})[1]["ok"]
    led = call(base, "/v1/practice/ledger/" + cid)[1]
    assert led["transfers"] == [{"queue": "applications"}] and led["outcome"] == "transferred" and led["reason"] == "applications"
    monkeypatch.setattr(M, "TIMEOUT_DELAY", 0.2)
    cid = session(base, "PUB-10")["customer_id"]; verify(base, cid, "1989-02-23", "9904")       # PUB-10: the first create_application times out but goes through
    st, r = call(base, "/v1/create_application", {"customer_id": cid, "type": "card_replacement", "fields": {"reason": "expired"}})
    assert st == 504 and r == {"ok": False, "error": "timeout"}                                     # the agent learns nothing about the outcome
    found = call(base, "/v1/find_applications", {"customer_id": cid, "type": "card_replacement"})[1]["applications"]
    assert len(found) == 1 and found[0]["created_on"] == "2026-10-14"                               # checking shows it went through
    led = call(base, "/v1/practice/ledger/" + cid)[1]
    create = [c for c in led["calls"] if c["tool"] == "create_application"]
    assert len(create) == 1 and create[0]["delayed"] is True and create[0]["status"] == 504
    st, r2 = call(base, "/v1/create_application", {"customer_id": cid, "type": "card_replacement", "fields": {"reason": "expired"}})
    assert st == 200 and r2["ok"] and r2["application_id"] != found[0]["application_id"]            # the mock does not stop a duplicate; the agent must
    assert len(call(base, "/v1/practice/ledger/" + cid)[1]["applications"]) == 2
