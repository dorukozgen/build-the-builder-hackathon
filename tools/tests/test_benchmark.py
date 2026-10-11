import copy, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import benchmark as B

GOOD = {"id": "GEN-01", "fixture": "PUB-06", "title": "Accepts the floor", "family": "Amounts", "level": "hard", "rules": ["brief-a:26"],
        "script": "Verified. Says the full amount is too much. Accepts the minimum payment today and confirms.",
        "expected": {"outcome": "promise", "reason": None, "promises": [{"product_id": "p1", "amount": 637.5, "date": "2026-10-14"}],
                     "notes": [], "callbacks": [], "transfers": []},
        "checks": ["the floor is offered once"]}


def test_fixtures_and_product_ids():
    fx = B.load_fixtures()
    assert len(fx) == 13 and B.product_ids(fx["PUB-13"]) == ["p1", "p2"] and B.product_ids(fx["PUB-01"]) == ["p1"]


def test_enums_and_tool_names():
    api = B.load_openapi()
    assert B.tool_names(api) == ["verify_identity", "get_account", "create_promise", "add_note", "schedule_callback", "transfer_to_agent", "close_call"]
    assert "promise" in B.enums(api)["close_call"]["outcome"] and "refused" in B.enums(api)["add_note"]["reason"]


def test_extract_rules(tmp_path):
    a = B.extract_rules(ROOT / "briefs" / "brief-a.md")
    assert len(a) == 47 and a[0] == "brief-a:1" and a[-1] == "brief-a:47"
    assert len(B.extract_rules(ROOT / "briefs" / "brief-b.md")) == 11
    f = tmp_path / "memo.md"; f.write_text("no numbers here\n1. one\n2. two\n1. one again\n", encoding="utf-8")
    assert B.extract_rules(f) == ["memo:1", "memo:2"]
    g = tmp_path / "empty.md"; g.write_text("# nothing\n", encoding="utf-8")
    assert B.extract_rules(g) == []


def test_check_good_case_passes():
    errors, warnings, cov = B.check_cases([GOOD], B.load_fixtures(), B.load_openapi())
    assert errors == [] and warnings == []
    assert cov["cases"] == 1 and cov["by_fixture"] == {"PUB-06": 1} and cov["by_outcome"] == {"promise": 1} and cov["styles"] == []


def test_check_reports_each_error():
    bad = [dict(GOOD, id="GEN-01", fixture="PUB-99"),
           dict(GOOD, id="GEN-01", products=[], level="hot", style="shouty", rules=[], forbidden_tools=["pay"],
                expected={"outcome": "wrong", "reason": None,
                          "promises": [{"product_id": "p9", "amount": "x", "date": "14/10/2026"}],
                          "notes": [{"product_id": "p1", "reason": "bored"}],
                          "callbacks": [{"date": "2026-10-15", "time": "11"}], "transfers": [{"queue": "vip"}]}),
           "not an object"]
    errors, _, _ = B.check_cases(bad, B.load_fixtures(), B.load_openapi())
    text = "\n".join(errors)
    for needle in ["unknown fixture 'PUB-99'", "duplicate id", "`products` is bank data", "level must be", "unknown style 'shouty'",
                   "rules must be", "names a tool the API does not have: pay", "expected.outcome 'wrong'", "product_id 'p9'",
                   "amount must be a number", "must be YYYY-MM-DD", "note reason 'bored'", "must be HH:MM", "transfer queue 'vip'",
                   "every case must be a JSON object"]:
        assert needle in text, needle


def test_check_not_a_list():
    assert B.check_cases({"id": "x"}, {}, B.load_openapi())[0] == ["the cases file must be a JSON list"]


def test_check_warns_on_missing_reason():
    c = dict(GOOD, expected=dict(GOOD["expected"], outcome="no_promise", reason=None, promises=[]))
    errors, warnings, _ = B.check_cases([c], B.load_fixtures(), B.load_openapi())
    assert errors == [] and any("reason is empty" in w for w in warnings)


def test_rule_coverage():
    rules = ["brief-a:1", "brief-a:2", "brief-a:26"]
    errors, _, cov = B.check_cases([GOOD], B.load_fixtures(), B.load_openapi(), rules)
    assert errors == [] and cov["uncovered_rules"] == ["brief-a:1", "brief-a:2"]
    errors, _, _ = B.check_cases([dict(GOOD, rules=["brief-a:99"])], B.load_fixtures(), B.load_openapi(), rules)
    assert any("brief-a:99 is cited but exists in no --rules file" in e for e in errors)


def test_identity_fields_must_match_tool_api():
    api = copy.deepcopy(B.load_openapi())
    api["paths"]["/verify_identity"]["post"]["requestBody"]["content"]["application/json"]["schema"]["properties"]["field"]["enum"] = ["postcode", "birth_year"]
    errors, _, _ = B.check_cases([GOOD], B.load_fixtures(), api)
    assert any("cannot be played on the mock" in e for e in errors)


def case(cid, fixture="PUB-01", **kw):
    c = {"id": cid, "fixture": fixture, "title": "t " + cid, "family": "Happy path", "level": "easy", "rules": ["brief-a:1"], "script": "s",
         "expected": {"outcome": "promise", "reason": None, "promises": [{"product_id": "p1", "amount": 420.0, "date": "2026-10-14"}],
                      "notes": [], "callbacks": [], "transfers": []}, "checks": ["c"]}
    c.update(kw); return c


PROMISE = {"n": 1, "tool": "create_promise", "args": {"product_id": "p1", "amount": 420.0, "date": "2026-10-14"}, "status": 200, "result": {"ok": True}}
FAILED_PROMISE = {"n": 1, "tool": "create_promise", "args": {"product_id": "p1", "amount": 420.0, "date": "2026-10-14"}, "status": 503, "result": {"ok": False, "error": "service unavailable"}}
CLOSE = {"n": 2, "tool": "close_call", "args": {"outcome": "promise"}, "status": 200, "result": {"ok": True}}


def row(cid, ok, failed=(), calls=(), ended="assistant-ended-call", slow=5.0, call_id="call-1"):
    return {"id": cid, "pass": ok, "failed": list(failed), "tools": [c["tool"] for c in calls], "calls": list(calls),
            "call_id": call_id, "slowest_turn_s": slow, "ended": ended}


def hist(n, results):
    """One history line. results: {cid: (pass, sig)}"""
    return {"n": n, "at": "", "agent_id": "a", "seconds": 100, "style": None, "only": False, "public": None,
            "all_pass": all(p for p, _ in results.values()), "cases": {cid: {"pass": p, "sig": s, "categories": []} for cid, (p, s) in results.items()}}


def test_classify():
    assert B.classify(["outcome ('no_promise', 'x'), expected ('promise', None)"]) == ["outcome"]
    assert B.classify(["get_account called before identity was verified", "conversation: said collections"]) == ["before_identity", "conversation"]
    assert B.classify(["the call was not closed with close_call", "forbidden tool called: transfer_to_agent"]) == ["forbidden_tool", "not_closed"]
    assert B.classify(["something new"]) == ["other"] and B.classify([]) == []


def test_merge_with_fixture_and_promised():
    fx = B.load_fixtures()
    m = B.merge_with_fixture(case("GEN-01", fixture="PUB-13"), fx)
    assert m["identity"] == fx["PUB-13"]["identity"] and m["products"] == fx["PUB-13"]["products"] and m["brief"] == "B" and m["id"] == "GEN-01"
    assert B.promised([PROMISE, FAILED_PROMISE, CLOSE]) == 420.0


def test_signature_changes_with_expectation():
    a, b = case("GEN-01"), case("GEN-01")
    b["expected"]["promises"][0]["amount"] = 1.0
    assert B.signature(a) != B.signature(b) and B.signature(a) == B.signature(case("GEN-01", title="other title"))


def test_flaky():
    assert B.flaky([True, False, True]) and B.flaky([False, True, False])
    assert not B.flaky([False, True]) and not B.flaky([True, False]) and not B.flaky([False, True, True]) and not B.flaky([True, True, True])
    assert B.flaky([True], passes=1, runs=2) and not B.flaky([True], passes=2, runs=2)


def test_build_run_fixed_regressed_flaky_changed():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i), fx) for i in ("GEN-01", "GEN-02", "GEN-03", "GEN-04")]
    sig = {c["id"]: B.signature(c) for c in cases}
    history = [hist(1, {"GEN-01": (False, sig["GEN-01"]), "GEN-02": (True, "oldsig"), "GEN-03": (True, sig["GEN-03"]), "GEN-04": (True, sig["GEN-04"])}),
               hist(2, {"GEN-01": (False, sig["GEN-01"]), "GEN-02": (True, "oldsig"), "GEN-03": (True, sig["GEN-03"]), "GEN-04": (False, sig["GEN-04"])})]
    rows = [row("GEN-01", True, calls=[PROMISE, CLOSE]),
            row("GEN-02", False, ["outcome x"], ended="customer-ended-call", slow=12.0),
            row("GEN-03", False, ["promises y"]),
            row("GEN-04", True, calls=[PROMISE, CLOSE])]
    meta = {"n": 3, "at": "now", "agent_id": "a", "seconds": 200, "style": None, "only": False, "public": None, "uncovered_rules": ["brief-a:2"], "minutes_used": 12.0}
    run = B.build_run(meta, cases, [rows], history, {"GEN-01": 8}, "slot")
    assert run["fixed"] == ["GEN-01", "GEN-04"] and run["regressed"] == ["GEN-02", "GEN-03"] and run["still_failing"] == []
    r = {x["id"]: x for x in run["rows"]}
    assert r["GEN-02"]["changed"] is True and r["GEN-03"]["changed"] is False
    assert r["GEN-04"]["flaky"] is True and r["GEN-01"]["flaky"] is False and r["GEN-02"]["flaky"] is False
    assert r["GEN-02"]["flags"] == ["hung_up", "slow"] and r["GEN-01"]["flags"] == []
    assert run["promised_passed"] == 840.0 and r["GEN-01"]["turns"] == 8 and r["GEN-02"]["turns"] is None
    assert r["GEN-01"]["transcript"] == "results/bench/slot/run-03/GEN-01.md"
    assert run["median_slowest_s"] == 5.0 and run["worst_slowest_s"] == 12.0 and run["slow"] is False and run["hung_up"] == 1
    assert run["cases"]["GEN-02"] == {"pass": False, "sig": sig["GEN-02"], "categories": ["outcome"]}
    line = B.history_line(run)
    assert set(line) == {"n", "at", "agent_id", "seconds", "reps", "style", "only", "public", "all_pass", "cases"} and line["all_pass"] is False


def test_build_run_reps_disagree():
    fx = B.load_fixtures(); cases = [B.merge_with_fixture(case("GEN-01"), fx)]
    good, bad = row("GEN-01", True, calls=[PROMISE, CLOSE], call_id="call-good"), row("GEN-01", False, ["outcome z"], call_id="call-bad")
    run = B.build_run({"n": 1, "at": "", "agent_id": "a", "seconds": 1, "style": None, "only": False, "public": None, "uncovered_rules": None, "minutes_used": None},
                      cases, [[bad], [good]], [], {}, "slot")
    r = run["rows"][0]
    assert r["pass"] is False and r["passes"] == 1 and r["runs"] == 2 and r["flaky"] is True and r["failed"] == ["outcome z"]
    assert r["call_id"] == "call-bad" and r["calls"] == []          # the failing rep is the one the report shows


def test_build_run_without_call_id():
    fx = B.load_fixtures(); cases = [B.merge_with_fixture(case("GEN-01"), fx)]
    run = B.build_run({"n": 1, "at": "", "agent_id": "a", "seconds": 1, "style": None, "only": False, "public": None, "uncovered_rules": None, "minutes_used": None},
                      cases, [[row("GEN-01", False, ["conversation: no verdict"], call_id=None, slow=None)]], [], {}, "slot")
    r = run["rows"][0]
    assert r["call_id"] is None and r["flags"] == [] and run["median_slowest_s"] == 0


def test_transcript_md_and_without_call():
    c = case("GEN-01"); r = row("GEN-01", False, ["outcome x"], calls=[PROMISE], slow=4.2)
    call = {"messages": [
        {"role": "assistant", "message": "Hello, this is Freya Bank."},
        {"role": "system", "message": json.dumps({"event": "node_enter", "node": "identity", "from_node": "start", "reason": "first"})},
        {"role": "user", "message": "Yes, speaking."},
        {"role": "system", "message": json.dumps({"event": "function_call_start", "function": "create_promise", "args": {"body": {"amount": 420}}})},
        {"role": "system", "message": json.dumps({"event": "function_call_complete", "function": "create_promise", "result": {"ok": True}})},
        {"role": "system", "message": json.dumps({"event": "route_evaluated", "matched": True, "from_node": "promise", "target": "close", "reason": "tool ok"})},
        {"role": "system", "message": json.dumps({"event": "route_evaluated", "matched": False, "from_node": "promise", "target": "retry", "reason": "no"})},
        {"role": "system", "message": "not json"}]}
    md = B.transcript_md(c, r, call)
    assert md.startswith("## GEN-01 — t GEN-01\nresult: FAIL: outcome x\n")
    assert "**agent:** Hello, this is Freya Bank." in md and "**customer:** Yes, speaking." in md
    assert "→ node identity" not in md and '⚙ create_promise {"amount": 420}' in md and '⚙ create_promise → {"ok": true}' in md
    assert "↪ promise → close: tool ok" in md and "retry" not in md and "turns 2" in md
    assert "(no transcript)" in B.transcript_md(c, r, {})


def test_write_report_and_suggestions():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i), fx) for i in ("GEN-01", "GEN-02")]
    sig = {c["id"]: B.signature(c) for c in cases}
    history = [hist(1, {"GEN-01": (True, sig["GEN-01"]), "GEN-02": (True, sig["GEN-02"])}), hist(2, {"GEN-01": (True, sig["GEN-01"]), "GEN-02": (False, sig["GEN-02"])})]
    rows = [row("GEN-01", True, calls=[PROMISE, CLOSE]), row("GEN-02", True, calls=[PROMISE, CLOSE])]
    meta = {"n": 3, "at": "now", "agent_id": "agent-x", "seconds": 300, "style": None, "only": False, "public": None, "uncovered_rules": ["brief-a:7"], "minutes_used": 20.0}
    run = B.build_run(meta, cases, [rows], history, {}, "slot")
    full = history + [B.history_line(run)]
    text = B.write_report("slot", run, full)
    for needle in ["# Benchmark slot · run 3", "generated 2/2 · total 2/2", "promised on passed cases: 840.00", "fixed since the previous run: GEN-02",
                   "| GEN-02 | ✓ | ✗ | ✓ | flaky |", "rules cited by no case: brief-a:7", "## Passed cases", "- GEN-01 t GEN-01", "## What this run suggests"]:
        assert needle in text, needle
    s = "\n".join(B.suggest_next(run, full, 20.0))
    assert "Flaky: GEN-02" in s and "Everything passed once" in s and "(~5 min" in s and "still fits" in s
    # two full passes in a row, little time left
    full2 = [hist(1, {"GEN-01": (True, sig["GEN-01"]), "GEN-02": (True, sig["GEN-02"])}), B.history_line(run)]
    s2 = "\n".join(B.suggest_next(run, full2, 27.0))
    assert "2 full runs in a row" in s2 and "does not fit" in s2
    # failures and regressions
    rows3 = [row("GEN-01", False, ["outcome q"]), row("GEN-02", True, calls=[PROMISE, CLOSE])]
    run3 = B.build_run(dict(meta, n=4), cases, [rows3], full, {}, "slot")
    s3 = "\n".join(B.suggest_next(run3, full + [B.history_line(run3)], None))
    assert "Regressions first: GEN-01" in s3 and "--only GEN-01" in s3 and "Time:" not in s3
    text3 = B.write_report("slot", run3, full + [B.history_line(run3)])
    assert "### GEN-01 — t GEN-01" in text3 and "regressed: GEN-01" in text3


import pytest


def test_slot_of():
    assert B.slot_of("tests/brief-a.cases.json") == "brief-a" and B.slot_of("tests\\final-1.cases.json") == "final-1" and B.slot_of("x.json") == "x"


def test_select_only():
    cases = [case("GEN-01"), case("GEN-02")]
    assert [c["id"] for c in B.select_only(cases, "GEN-02")] == ["GEN-02"]
    with pytest.raises(SystemExit) as e: B.select_only(cases, "GEN-02,GEN-09")
    assert "GEN-09" in str(e.value)


def test_rule_ids_from_warns(tmp_path, capsys):
    f = tmp_path / "memo.md"; f.write_text("nothing numbered\n", encoding="utf-8")
    assert B.rule_ids_from([str(ROOT / "briefs" / "brief-b.md"), str(f)]) == [f"brief-b:{i}" for i in range(1, 12)]
    assert "no numbered rules found in" in capsys.readouterr().out
    assert B.rule_ids_from([]) is None


def test_minutes_since_builder_start(tmp_path, monkeypatch):
    monkeypatch.setattr(B, "ROOT", tmp_path)
    assert B.minutes_since_builder_start() is None
    (tmp_path / "traces").mkdir()
    import datetime as dt
    start = (dt.datetime.now().astimezone() - dt.timedelta(minutes=7)).strftime("%Y-%m-%dT%H:%M:%S%z")
    (tmp_path / "traces" / "t.jsonl").write_text(json.dumps({"start": start}) + "\n", encoding="utf-8")
    assert 6.9 < B.minutes_since_builder_start() < 7.5


def test_minutes_since_builder_start_ignores_stale_trace(tmp_path, monkeypatch):
    import datetime as dt, os, time as t
    monkeypatch.setattr(B, "ROOT", tmp_path); (tmp_path / "traces").mkdir()
    start = (dt.datetime.now().astimezone() - dt.timedelta(minutes=90)).strftime("%Y-%m-%dT%H:%M:%S%z")
    p = tmp_path / "traces" / "old.jsonl"; p.write_text(json.dumps({"start": start}) + "\n", encoding="utf-8")
    old = t.time() - 90 * 60; os.utime(p, (old, old))
    assert B.minutes_since_builder_start() is None                   # no builder has written to it for over an hour


def test_reason_exempt_outcomes():
    api = B.load_openapi()
    assert B.reason_exempt_outcomes(api) == {"promise", "paid"}
    api2 = copy.deepcopy(api); props = api2["paths"]["/close_call"]["post"]["requestBody"]["content"]["application/json"]["schema"]["properties"]
    props["outcome"]["enum"] = ["settled", "open"]; props["reason"]["description"] = "Required for every outcome except settled. See the brief."
    assert B.reason_exempt_outcomes(api2) == {"settled"}
    del props["reason"]["description"]
    assert B.reason_exempt_outcomes(api2) == set()
    c = dict(GOOD, expected=dict(GOOD["expected"], outcome="open", reason=None, promises=[]))
    assert B.check_cases([c], B.load_fixtures(), api2)[1] == []     # nothing to go on: no warning


def test_identity_mismatch_allows_third_party_cases():
    api = copy.deepcopy(B.load_openapi())
    api["paths"]["/verify_identity"]["post"]["requestBody"]["content"]["application/json"]["schema"]["properties"]["field"]["enum"] = ["postcode"]
    third = dict(GOOD, id="GEN-02", fixture="PUB-02", family="Third party", third_party=True,
                 expected={"outcome": "not_reached", "reason": "callback", "promises": [], "notes": [], "callbacks": [{"date": "2026-10-14", "time": "16:00"}], "transfers": []})
    errors, _, _ = B.check_cases([GOOD, third], B.load_fixtures(), api)
    assert any(e.startswith("GEN-01:") and "cannot be played" in e for e in errors)
    assert not any(e.startswith("GEN-02:") for e in errors)


def test_signature_tracks_forbidden_tools_fixture_and_third_party():
    assert B.signature(case("GEN-01", forbidden_tools=["transfer_to_agent"])) != B.signature(case("GEN-01"))
    assert B.signature(case("GEN-01", fixture="PUB-02")) != B.signature(case("GEN-01"))
    assert B.signature(case("GEN-01", third_party=True)) != B.signature(case("GEN-01"))


def test_transcript_md_is_compact_and_survives_odd_messages():
    c = case("GEN-01"); r = row("GEN-01", True, calls=[PROMISE])
    call = {"messages": [
        {"role": "system", "message": json.dumps({"event": "node_enter", "node": "setup", "from_node": None, "reason": None})},
        {"role": "system", "message": json.dumps({"event": "function_call_start", "function": "code_exec", "args": {"timeout_ms": 1, "code": "import x"}})},
        {"role": "system", "message": json.dumps({"event": "function_call_start", "function": "create_promise", "args": {"url": "u", "method": "POST", "headers": {"a": "b"}, "body": {"amount": 420, "customer_id": "c"}}})},
        {"role": "system", "message": json.dumps({"event": "route_evaluated", "matched": True, "from_node": "setup", "target": "opening", "reason": "always"})},
        {"role": "system", "message": json.dumps({"event": "node_enter", "node": "opening", "from_node": "setup", "reason": "always"})},
        {"role": "system", "message": "null"}, {"role": "system", "message": "[1, 2]"}, {"role": "system", "message": {"event": "error", "message": "boom"}}, {"role": "system", "message": None}]}
    md = B.transcript_md(c, r, call)
    assert "→ node setup" in md and "(from None" not in md
    assert "⚙ code_exec (code)" in md and "import x" not in md
    assert '⚙ create_promise {"amount": 420, "customer_id": "c"}' in md and "headers" not in md
    assert "↪ setup → opening: always" in md and "node opening" not in md and "✖ error: boom" in md


def test_write_report_keeps_cases_absent_from_this_run():
    fx = B.load_fixtures(); cases = [B.merge_with_fixture(case("GEN-01"), fx)]
    history = [hist(1, {"GEN-01": (True, B.signature(cases[0])), "GEN-03": (True, "s3")})]
    meta = {"n": 2, "at": "", "agent_id": "a", "seconds": 60, "style": None, "only": False, "public": None, "uncovered_rules": None, "minutes_used": None}
    run = B.build_run(meta, cases, [[row("GEN-01", True, calls=[PROMISE, CLOSE])]], history, {}, "slot")
    assert "| GEN-03 | ✓ | – | removed |" in B.write_report("slot", run, history + [B.history_line(run)])
    run_only = B.build_run(dict(meta, only=True), cases, [[row("GEN-01", True, calls=[PROMISE, CLOSE])]], history, {}, "slot")
    assert "| GEN-03 | ✓ | – | not in this run |" in B.write_report("slot", run_only, history + [B.history_line(run_only)])


def test_suggest_next_only_runs_and_time_estimate():
    fx = B.load_fixtures(); cases = [B.merge_with_fixture(case("GEN-01"), fx)]
    full = dict(hist(1, {"GEN-01": (True, B.signature(cases[0]))}), seconds=480, reps=1)
    meta = {"n": 2, "at": "", "agent_id": "a", "seconds": 60, "style": None, "only": True, "public": None, "uncovered_rules": None, "minutes_used": 10.0}
    run = B.build_run(meta, cases, [[row("GEN-01", True, calls=[PROMISE, CLOSE])]], [full], {}, "slot")
    s = "\n".join(B.suggest_next(run, [full, B.history_line(run)], 10.0))
    assert "Run the full set once" in s and "full runs in a row" not in s and "Everything passed once" not in s
    assert "(~8 min" in s and "`--reps 2` ~16" in s and "still fits" in s     # estimated from the last full run, not from this --only run
    run2 = B.build_run(dict(meta, n=3, only=False, seconds=400), cases, [[row("GEN-01", True, calls=[PROMISE, CLOSE])]], [full, B.history_line(run)], {}, "slot")
    s2 = "\n".join(B.suggest_next(run2, [full, B.history_line(run), B.history_line(run2)], 25.0))
    assert "2 full runs in a row" in s2 and "does not fit" in s2            # the --only run in between does not break the streak
    assert B.history_line(run2)["reps"] == 1


def test_main_explains_transient_api_errors(monkeypatch):
    def boom(a): raise RuntimeError("POST /api/v2/personas -> 503: temporarily unavailable")
    monkeypatch.setattr(B, "run", boom)
    monkeypatch.setattr(sys, "argv", ["benchmark.py", "agent-x", "--cases", "tests/none.cases.json"])
    with pytest.raises(SystemExit) as e: B.main()
    assert "transient" in str(e.value) and "503" in str(e.value)


PUBLIC_ORDER = ["id", "brief", "family", "level", "title", "variables", "identity", "products", "script", "expected", "checks"]


def test_write_test_set_is_public_shaped_and_follows_updates(tmp_path):
    fx = B.load_fixtures(); cases_path = tmp_path / "brief-x.cases.json"
    gen = [case("GEN-01", fixture="PUB-10", forbidden_tools=["add_note"]), case("GEN-02", fixture="PUB-13", third_party=True)]
    out = B.write_test_set(cases_path, gen, fx)
    assert out == tmp_path / "brief-x.test-set.json"
    got = json.loads(out.read_text(encoding="utf-8"))
    assert [c["id"] for c in got] == ["GEN-01", "GEN-02"]
    first = got[0]
    assert list(first)[:len(PUBLIC_ORDER) + 1] == PUBLIC_ORDER[:8] + ["faults"] + PUBLIC_ORDER[8:]     # PUB-10 has faults; the public key order, then the generated fields
    assert first["variables"] == fx["PUB-10"]["variables"] and first["identity"] == fx["PUB-10"]["identity"] and first["products"] == fx["PUB-10"]["products"]
    assert first["faults"] == fx["PUB-10"]["faults"] and first["brief"] == "A" and first["fixture"] == "PUB-10" and first["forbidden_tools"] == ["add_note"]
    assert "faults" not in got[1] and got[1]["third_party"] is True and got[1]["brief"] == "B"
    gen[0]["script"] = "changed"; B.write_test_set(cases_path, gen[:1], fx)                         # an edited file replaces the derived one
    got = json.loads(out.read_text(encoding="utf-8"))
    assert [c["id"] for c in got] == ["GEN-01"] and got[0]["script"] == "changed"


def test_check_with_another_tool_api_backend_and_applications():
    api_f, fx = B.load_openapi(ROOT / "tools" / "openapi-f.json"), B.load_fixtures()
    c = case("GEN-09", fixture="PUB-08", backend={"applications": [{"type": "limit_increase", "status": "in_review"}]},
             expected={"outcome": "status_given", "promises": [], "notes": [], "callbacks": [], "transfers": [], "applications": []})
    errors, warnings, _ = B.check_cases([c], fx, api_f)
    assert errors == [] and warnings == []                                      # status_given needs no reason in this API
    d = case("GEN-10", fixture="PUB-10", expected={"outcome": "application_created", "promises": [], "notes": [], "callbacks": [], "transfers": [], "applications": [{"type": "mortgage"}]})
    errors, _, _ = B.check_cases([d], fx, api_f)
    assert any("mortgage" in e for e in errors)
    errors, _, _ = B.check_cases([c], fx, B.load_openapi())                      # the collections API has no such outcome
    assert any("status_given" in e for e in errors)
    assert B.signature(c) != B.signature(dict(c, backend=None))


def test_applications_created_and_scored():
    ok = {"n": 3, "tool": "create_application", "args": {"type": "card_replacement", "fields": {"reason": "expired"}}, "status": 200, "result": {"ok": True, "application_id": "APP-1"}}
    dup = {"n": 5, "tool": "create_application", "args": {"type": "card_replacement", "fields": {"reason": "expired"}}, "status": 200, "result": {"ok": True, "application_id": "APP-2"}}
    failed = {"n": 4, "tool": "create_application", "args": {"type": "limit_increase", "fields": {}}, "status": 503, "result": {"ok": False, "error": "x"}}
    assert B.applications_created([ok, failed, dup]) == ["card_replacement", "card_replacement"]
    assert B.applications_failed({"applications": [{"type": "card_replacement"}]}, [ok, failed]) == []
    assert B.applications_failed({"applications": [{"type": "card_replacement"}]}, [ok, dup]) == ["applications ['card_replacement', 'card_replacement'], expected ['card_replacement']"]
    assert B.applications_failed({"outcome": "x"}, [ok, dup]) == []                                  # nothing expected: nothing checked


def test_main_takes_openapi_and_host(tmp_path, monkeypatch):
    import score
    seen = {}
    monkeypatch.setattr(B, "run", lambda a: seen.update(vars(a)))
    monkeypatch.setattr(sys, "argv", ["benchmark.py", "agent-x", "--cases", "tests/none.cases.json", "--openapi", "tools/openapi-f.json", "--host", "https://mock.example"])
    B.main()
    assert seen["openapi"] == "tools/openapi-f.json" and score.HOST == "https://mock.example"
    monkeypatch.setattr(sys, "argv", ["benchmark.py", "--check", "--cases", str(tmp_path / "x.cases.json"), "--openapi", "tools/openapi-f.json"])
    (tmp_path / "x.cases.json").write_text(json.dumps([case("GEN-01", expected={"outcome": "status_given", "promises": [], "notes": [], "callbacks": [], "transfers": []})]), encoding="utf-8")
    with pytest.raises(SystemExit) as e: B.main()
    assert e.value.code == 0


def test_check_writes_test_set_only_when_valid(tmp_path, monkeypatch):
    p = tmp_path / "brief-y.cases.json"; p.write_text(json.dumps([GOOD]), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["benchmark.py", "--check", "--cases", str(p)])
    with pytest.raises(SystemExit) as e: B.main()
    assert e.value.code == 0
    got = json.loads((tmp_path / "brief-y.test-set.json").read_text(encoding="utf-8"))
    assert len(got) == 1 and got[0]["products"] == B.load_fixtures()["PUB-06"]["products"]
    bad = tmp_path / "brief-z.cases.json"; bad.write_text(json.dumps([dict(GOOD, fixture="PUB-99")]), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["benchmark.py", "--check", "--cases", str(bad)])
    with pytest.raises(SystemExit) as e: B.main()
    assert e.value.code == 1 and not (tmp_path / "brief-z.test-set.json").exists()
