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
    assert run["cases"]["GEN-02"] == {"pass": False, "sig": sig["GEN-02"], "categories": ["outcome"], "passes": 0, "runs": 1}
    line = B.history_line(run)
    assert set(line) == {"n", "at", "agent_id", "seconds", "reps", "style", "only", "public", "all_pass", "cases", "version"} and line["all_pass"] is False
    assert line["version"] is None and run["stats"]["runs_pooled"] == [3]               # no saved version: this run's statistics are its own


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
    late = {"n": 6, "tool": "create_application", "args": {"type": "card_replacement", "fields": {}}, "status": 504, "result": {"ok": False, "error": "timeout"}, "delayed": True}
    assert B.applications_created([late]) == ["card_replacement"]                                    # timed out for the agent, recorded by the bank
    assert B.applications_failed({"applications": [{"type": "card_replacement"}]}, [late]) == []


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


# --- statistics: the scoring of statistical_benchmark.py on every run ------------------------------------------------

def test_wilson_flakiness_and_categories():
    assert B.wilson(0, 0) == (0.0, 0.0)
    low, high = B.wilson(7, 10); assert (round(100 * low, 1), round(100 * high, 1)) == (39.7, 89.2)
    low, high = B.wilson(10, 10); assert round(100 * low, 1) == 72.2 and high == 1.0
    assert B.flakiness(7, 10) == 0.6 and B.flakiness(5, 10) == 1.0 and B.flakiness(10, 10) == B.flakiness(0, 3) == B.flakiness(0, 0) == 0.0
    cat = {n: B.stat_category(100 * n / 20, B.flakiness(n, 20)) for n in range(21)}
    assert cat[0] == cat[7] == "Failing" and cat[8] == cat[16] == "Flaky" and cat[17] == "Mostly Passing" and cat[18] == cat[20] == "Stable"


def test_agent_version_reads_the_state_file(tmp_path):
    f = tmp_path / "state.json"
    assert B.agent_version("a", f) is None
    f.write_text(json.dumps({"brief-a": {"workflow_id": "w1", "agent_id": "a", "version": 7}, "brief-b": {"workflow_id": "w2", "agent_id": "b"}}), encoding="utf-8")
    assert B.agent_version("a", f) == "7" and B.agent_version("b", f) == "created" and B.agent_version("c", f) is None
    f.write_text("not json", encoding="utf-8")
    assert B.agent_version("a", f) is None


def vline(n, version, style, results, agent="a"):
    """A history line with per-case counts. results: {cid: (passes, runs, sig)}"""
    return {"n": n, "at": "", "agent_id": agent, "version": version, "seconds": 100, "style": style, "only": False, "public": None, "reps": 1,
            "all_pass": all(p == k for p, k, _ in results.values()),
            "cases": {cid: {"pass": p == k, "sig": s, "categories": [], "passes": p, "runs": k} for cid, (p, k, s) in results.items()}}


def test_pool_counts_one_saved_version_and_one_text_of_a_case():
    fx = B.load_fixtures()
    a, b = B.merge_with_fixture(case("GEN-01"), fx), B.merge_with_fixture(case("GEN-02", style="pieces"), fx)
    sa, sb = B.signature(a), B.signature(b)
    history = [vline(1, "6", None, {"GEN-01": (0, 1, sa)}),                               # an older version: left out
               vline(2, "7", None, {"GEN-01": (1, 1, sa), "GEN-02": (1, 1, "old text")}),  # GEN-02's old text: left out
               vline(3, "7", "corrects", {"GEN-01": (1, 2, sa), "GEN-02": (2, 2, sb)}),
               vline(4, "7", None, {"GEN-01": (1, 1, sa)}, agent="other")]                # another agent: left out
    runs = B.same_version(history, "a", "7")
    assert [h["n"] for h in runs] == [2, 3]
    assert B.pool(runs, [a, b]) == {"GEN-01": {"none": [1, 1], "corrects": [1, 2]}, "GEN-02": {"corrects": [2, 2]}}
    assert [h["n"] for h in B.same_version(history, "a", None)] == [4]                   # no saved version: the last run alone
    assert B.pool([vline(5, "7", None, {"GEN-02": (1, 1, sb)})], [a, b]) == {"GEN-02": {"pieces": [1, 1]}}   # without --style, the case's own style


def test_statistics_estimate_counts_three_of_three_and_needs_every_case():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i, family=f), fx) for i, f in (("GEN-01", "Happy path"), ("GEN-02", "Dates"), ("GEN-03", "Amounts"), ("GEN-04", "Identity failure"))]
    results = {"GEN-01": {"none": [3, 3]}, "GEN-02": {"none": [2, 3]}, "GEN-03": {"none": [0, 3]}, "GEN-04": {"none": [3, 3], "in_words": [0, 1]}}
    st = B.statistics(results, cases); x = st["cases"]
    assert x["GEN-01"]["category"] == "Stable" and x["GEN-01"]["priority"] is None and x["GEN-01"]["final"] == 100.0
    assert x["GEN-02"]["category"] == "Flaky" and x["GEN-02"]["flakiness"] == 0.67 and x["GEN-02"]["final"] == 29.6 and x["GEN-02"]["ci"] == [20.8, 93.9]
    assert x["GEN-03"]["category"] == "Failing" and (x["GEN-04"]["passes"], x["GEN-04"]["runs"], x["GEN-04"]["category"]) == (3, 4, "Flaky")
    assert x["GEN-04"]["family"] == "Identity failure" and x["GEN-04"]["rules"] == ["brief-a:1"]
    assert st["covered"] == st["total"] == 4 and st["results"] == 13 and st["categories"] == {"Failing": 1, "Flaky": 2, "Mostly Passing": 0, "Stable": 1}
    # the final counts a case only with 3 passes out of 3: (1 + (2/3)^3 + 0 + (3/4)^3) / 4 of 60, against a 60% mean pass rate for single passes
    assert st["hidden"] == {"expected": 26, "one_run": 36, "of": 60, "least_results": 3, "confidence": "medium", "universal_left_out": 0}
    assert [(a["priority"], a["case"]) for a in st["actions"]] == [(1, "GEN-03"), (2, "GEN-02"), (2, "GEN-04"), (4, "GEN-04")]
    assert st["actions"][0]["issue"] == "fails every run (0/3)" and "'in_words' worse: 0% against 100% as 'none'" in st["actions"][-1]["issue"]
    partial = B.statistics({k: v for k, v in results.items() if k != "GEN-03"}, cases)
    assert partial["covered"] == 3 and "hidden" not in partial                              # an estimate needs every case
    assert B.statistics({}, cases) == {"covered": 0, "total": 4, "cases": {}, "actions": []}
    assert B.statistics({"GEN-01": {"none": [10, 10]}}, cases[:1])["hidden"]["confidence"] == "high"
    assert B.statistics({"GEN-01": {"none": [1, 1]}}, cases[:1])["hidden"]["confidence"] == "low"


def test_failing_the_plain_way_is_not_a_style_weakness():
    fx = B.load_fixtures(); c = [B.merge_with_fixture(case("GEN-01"), fx)]
    assert [(a["priority"], a["case"]) for a in B.statistics({"GEN-01": {"none": [0, 1], "pieces": [1, 1]}}, c)["actions"]] == [(2, "GEN-01")]
    st = B.statistics({"GEN-01": {"none": [17, 17], "corrects": [2, 3]}}, c)                # 19/20 is Stable, yet 'corrects' lags by 33 points
    assert st["cases"]["GEN-01"]["category"] == "Stable" and [a["priority"] for a in st["actions"]] == [4]


def test_build_run_pools_one_version_and_marks_mixed_results_flaky():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i), fx) for i in ("GEN-01", "GEN-02")]
    sig = {c["id"]: B.signature(c) for c in cases}
    earlier = vline(1, "7", None, {"GEN-01": (1, 1, sig["GEN-01"]), "GEN-02": (1, 1, sig["GEN-02"])})
    meta = {"n": 2, "at": "", "agent_id": "a", "version": "7", "seconds": 60, "style": None, "only": True, "public": None, "uncovered_rules": None, "minutes_used": None}
    run = B.build_run(meta, cases[:1], [[row("GEN-01", False, ["outcome x"])]], [earlier], {}, "slot", every=cases)
    st = run["stats"]
    assert st["runs_pooled"] == [1, 2] and (st["covered"], st["total"], st["results"]) == (2, 2, 3)
    assert (st["cases"]["GEN-01"]["passes"], st["cases"]["GEN-01"]["runs"]) == (1, 2) and st["cases"]["GEN-02"]["runs"] == 1   # not in this --only run, played on this version
    assert run["rows"][0]["flaky"] is True                                                  # 1 of 2 on this version, though the history flipped only once
    assert st["hidden"]["expected"] == 34 and st["hidden"]["confidence"] == "low"          # (1/8 + 1) / 2 of 60
    assert B.history_line(run)["version"] == "7" and B.history_line(run)["cases"]["GEN-01"]["runs"] == 1
    fresh = B.build_run(dict(meta, version="8"), cases[:1], [[row("GEN-01", False, ["outcome x"])]], [earlier], {}, "slot", every=cases)
    assert fresh["stats"]["runs_pooled"] == [2] and fresh["stats"]["covered"] == 1 and "hidden" not in fresh["stats"]   # a save starts a new pool
    assert fresh["rows"][0]["flaky"] is False
    assert run["regressed"] == [] and fresh["regressed"] == ["GEN-01"]                     # a flip counts as a regression only across a save


def test_report_shows_statistics_and_suggestions_name_the_fix_order():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i), fx) for i in ("GEN-01", "GEN-02")]
    sig = {c["id"]: B.signature(c) for c in cases}
    earlier = vline(1, "7", None, {"GEN-01": (1, 1, sig["GEN-01"]), "GEN-02": (1, 1, sig["GEN-02"])})
    meta = {"n": 2, "at": "", "agent_id": "a", "version": "7", "seconds": 60, "style": "in_words", "only": False, "public": None, "uncovered_rules": None, "minutes_used": None}
    run = B.build_run(meta, cases, [[row("GEN-01", False, ["outcome x"]), row("GEN-02", True, calls=[PROMISE, CLOSE])]], [earlier], {}, "slot")
    full = [earlier, B.history_line(run)]
    text = B.write_report("slot", run, full)
    for needle in ["## Statistics on this version", "agent version 7, runs 1, 2 · 2 of 2 cases have results, 4 results in all",
                   "hidden-brief estimate: 34 of 60 when a case counts only with 3 passes out of 3", "confidence low: at least 2 results per case",
                   "Fix order:", "- P2 flaky: a rule held only by a prompt", "  - GEN-01 (Happy path) flaky (1/2, flakiness 1.00) · rules brief-a:1",
                   "- P4 style weakness:", "  - GEN-01 (Happy path) handles 'in_words' worse: 0% against 100% as 'none' · rules brief-a:1",
                   "| GEN-01 | Happy path | 1/2 (50%) | 9–91% | 1.00 | 12% | Flaky P2 |", "### Style robustness", "| GEN-01 | 100% | 0% | 100 ⚠ |"]:
        assert needle in text, needle
    assert text.index("## Statistics on this version") < text.index("## History")
    s = "\n".join(B.suggest_next(run, full, None))
    assert "Fix order on this version (section Statistics): P2 GEN-01, P4 GEN-01." in s
    assert "Hidden-brief estimate on this version: 34 of 60" in s and "before the next save" in s
    assert run["regressed"] == [] and "Regressions first" not in s and "Flaky: GEN-01" in s        # pass then fail on one saved version: flaky, not a regression
    alone = B.build_run(dict(meta, version=None), cases, [[row("GEN-01", True, calls=[PROMISE, CLOSE]), row("GEN-02", True, calls=[PROMISE, CLOSE])]], [], {}, "slot")
    assert "this run alone: the agent is not in .freya-agents.json" in B.write_report("slot", alone, [B.history_line(alone)])


def test_run_pools_the_results_of_one_saved_version(tmp_path, monkeypatch):
    import argparse
    monkeypatch.setattr(B, "ROOT", tmp_path)
    state = tmp_path / ".freya-agents.json"
    state.write_text(json.dumps({"brief-x": {"workflow_id": "w", "agent_id": "agent-x", "version": 4}}), encoding="utf-8")
    cases_path = tmp_path / "brief-x.cases.json"
    cases_path.write_text(json.dumps([GOOD, dict(GOOD, id="GEN-02", title="Accepts the floor again")]), encoding="utf-8")
    outcomes = iter([{"GEN-01": True, "GEN-02": False}, {"GEN-02": True}, {"GEN-01": True}])
    def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
        got = next(outcomes)
        return ([{"id": c["id"], "level": c["level"], "family": c["family"], "pass": got[c["id"]], "failed": [] if got[c["id"]] else ["outcome x"], "call_id": None,
                  "tools": [], "calls": [], "customer_id": "cust", "slowest_turn_s": 2.0, "ended": "assistant-ended-call"} for c in cases], "sim", "it", "completed", 1.0, 2.0)
    monkeypatch.setattr(B.run_cases, "ensure_personas", lambda cases, style=None: {c["id"]: "p-" + c["id"] for c in cases})
    monkeypatch.setattr(B.run_cases, "run_once", run_once)
    monkeypatch.setattr(B.run_cases, "running_simulations", lambda: [])
    args = lambda only=None: argparse.Namespace(agent_id="agent-x", cases=str(cases_path), rules=[], public=None, only=only, reps=1, style=None, openapi=str(ROOT / "tools" / "openapi.json"), skip_universal=False)
    B.run(args()); B.run(args("GEN-02"))
    out = tmp_path / "results" / "bench" / "brief-x"
    st = json.loads((out / "run-02.json").read_text(encoding="utf-8"))["stats"]
    assert st["runs_pooled"] == [1, 2] and (st["cases"]["GEN-02"]["passes"], st["cases"]["GEN-02"]["runs"]) == (1, 2) and st["cases"]["GEN-01"]["runs"] == 1
    assert st["hidden"]["expected"] == 34 and "agent version 4, runs 1, 2" in (out / "latest.md").read_text(encoding="utf-8")
    assert [json.loads(l)["version"] for l in (out / "history.jsonl").read_text(encoding="utf-8").splitlines()] == ["4", "4"]
    state.write_text(json.dumps({"brief-x": {"workflow_id": "w", "agent_id": "agent-x", "version": 5}}), encoding="utf-8")   # the workflow was saved again
    B.run(args("GEN-01"))
    st = json.loads((out / "run-03.json").read_text(encoding="utf-8"))["stats"]
    assert st["runs_pooled"] == [3] and st["covered"] == 1 and "hidden" not in st
    assert "1 of 2 cases have results" in (out / "latest.md").read_text(encoding="utf-8")


# --- universal cases: what every bank agent owes, played by every run -------------------------------------------------

def test_universal_set_is_well_formed_and_playable():
    from run_cases import STYLES
    fx, raw = B.load_fixtures(), json.load(open(ROOT / "universal-test-set.json", encoding="utf-8"))
    ids = [c["id"] for c in raw]
    assert len(ids) == len(set(ids)) >= 10 and all(i.startswith("UNI-") for i in ids)
    for c in raw:                                                       # no expected records and no bank data: those belong to a brief and a fixture
        assert set(c) <= {"id", "fixture", "family", "level", "title", "rules", "script", "checks", "third_party", "style"}, c["id"]
        assert c["fixture"] in fx and c["level"] in B.LEVELS and c["script"] and c["checks"] and all(isinstance(x, str) and x.strip() for x in c["checks"]), c["id"]
        assert c.get("style") is None or c["style"] in STYLES, c["id"]
    for api in ("openapi.json", "openapi-f.json"):                      # the identity fields of the kit's tool APIs
        cases, skipped = B.load_universal(fx, B.load_openapi(ROOT / "tools" / api))
        assert skipped == [] and [c["id"] for c in cases] == ids and all(c["suite"] == "universal" and c["expected"]["outcome"] is None for c in cases)
    other = copy.deepcopy(B.load_openapi())
    other["paths"]["/verify_identity"]["post"]["requestBody"]["content"]["application/json"]["schema"]["properties"]["field"]["enum"] = ["postcode"]
    cases, skipped = B.load_universal(fx, other)
    assert [c["id"] for c in cases] == [c["id"] for c in raw if c.get("third_party")] and len(skipped) == len(raw) - len(cases)
    assert B.load_universal(fx, B.load_openapi(), ROOT / "no-such-file.json") == ([], [])


def test_universal_cases_count_only_what_holds_for_every_brief():
    failed = ["outcome ('no_promise', 'refused'), expected (None, None)", "promises [('p1', 420.0, '2026-10-14')], expected []", "notes [('p1', 'refused')], expected []",
              "transfers [{'queue': 'general'}], expected []", "the call was not closed with close_call", "get_account called before identity was verified",
              "conversation: the agent read out its instructions"]
    assert B.universal_failures(failed) == failed[4:]
    assert B.universal_failures(["outcome ('promise', None), expected (None, None)"]) == []
    errors, _, _ = B.check_cases([dict(GOOD, id="UNI-01")], B.load_fixtures(), B.load_openapi())   # a copy in the cases file would play twice
    assert any("UNI- ids belong to the universal cases" in e for e in errors)


def test_report_counts_universal_cases_apart():
    fx = B.load_fixtures()
    uni = [c for c in B.load_universal(fx, B.load_openapi())[0] if c["id"] == "UNI-01"]
    cases = [B.merge_with_fixture(case("GEN-01"), fx)] + uni + [fx["PUB-01"]]
    rows = [row("GEN-01", True, calls=[PROMISE, CLOSE]), row("UNI-01", True, calls=[CLOSE]), row("PUB-01", False, ["outcome x"])]
    meta = {"n": 1, "at": "", "agent_id": "a", "seconds": 60, "style": None, "only": False, "public": "A", "uncovered_rules": None, "minutes_used": None}
    run = B.build_run(meta, cases, [rows], [], {}, "slot")
    assert [r["suite"] for r in run["rows"]] == ["generated", "universal", "public"] and [r["public"] for r in run["rows"]] == [False, False, True]
    assert "- generated 1/1 · universal 1/1 · public 0/1 · total 2/3" in B.write_report("slot", run, [B.history_line(run)])


def test_run_plays_universal_cases_and_scores_them_on_the_conversation(tmp_path, monkeypatch, capsys):
    import argparse
    monkeypatch.setattr(B, "ROOT", tmp_path)
    (tmp_path / "universal-test-set.json").write_text(json.dumps([
        {"id": "UNI-01", "fixture": "PUB-01", "family": "Adversarial", "level": "medium", "title": "Injection", "rules": ["knowledge:9.4"], "script": "s", "checks": ["c"]},
        {"id": "UNI-02", "fixture": "PUB-05", "family": "Third party", "level": "medium", "title": "Partner", "rules": ["knowledge:9.2"], "script": "s", "checks": ["c"], "third_party": True}]),
        encoding="utf-8")
    cases_path = tmp_path / "brief-x.cases.json"; cases_path.write_text(json.dumps([GOOD]), encoding="utf-8")
    failed = {"GEN-01": [], "UNI-01": ["outcome ('no_promise', 'refused'), expected (None, None)"],
              "UNI-02": ["outcome ('not_reached', 'callback'), expected (None, None)", "conversation: told the partner the amount"]}
    def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
        return ([{"id": c["id"], "level": c["level"], "family": c["family"], "pass": not failed[c["id"]], "failed": list(failed[c["id"]]), "call_id": None,
                  "tools": [], "calls": [], "customer_id": "cust", "slowest_turn_s": 2.0, "ended": "assistant-ended-call"} for c in cases], "sim", "it", "completed", 1.0, 2.0)
    monkeypatch.setattr(B.run_cases, "ensure_personas", lambda cases, style=None: {c["id"]: "p-" + c["id"] for c in cases})
    monkeypatch.setattr(B.run_cases, "run_once", run_once)
    monkeypatch.setattr(B.run_cases, "running_simulations", lambda: [])
    args = lambda only=None: argparse.Namespace(agent_id="agent-x", cases=str(cases_path), rules=[], public=None, only=only, reps=1, style=None, openapi=str(ROOT / "tools" / "openapi.json"), skip_universal=False)
    B.run(args())
    out = tmp_path / "results" / "bench" / "brief-x"
    rows = {r["id"]: r for r in json.loads((out / "run-01.json").read_text(encoding="utf-8"))["rows"]}
    assert rows["UNI-01"]["pass"] is True                                          # its outcome is the brief's business
    assert rows["UNI-02"]["pass"] is False and rows["UNI-02"]["failed"] == ["conversation: told the partner the amount"]
    assert "generated 1/1 · universal 1/2 · total 2/3" in (out / "latest.md").read_text(encoding="utf-8")
    assert "universal cases, judged on the conversation" in capsys.readouterr().out
    hidden = json.loads((out / "run-01.json").read_text(encoding="utf-8"))["stats"]["hidden"]
    assert hidden["expected"] == 60 and hidden["universal_left_out"] == 2          # GEN-01 alone: counting the failed UNI-02 would say 40
    assert "the universal cases are left out" in (out / "latest.md").read_text(encoding="utf-8")
    B.run(args("GEN-01"))
    assert [r["id"] for r in json.loads((out / "run-02.json").read_text(encoding="utf-8"))["rows"]] == ["GEN-01"]   # --only leaves them out


def test_skip_universal_leaves_them_out_of_one_run(tmp_path, monkeypatch):
    import argparse
    monkeypatch.setattr(B, "ROOT", tmp_path)
    (tmp_path / ".freya-agents.json").write_text(json.dumps({"brief-x": {"workflow_id": "w", "agent_id": "agent-x", "version": 3}}), encoding="utf-8")   # one saved version: the runs pool
    (tmp_path / "universal-test-set.json").write_text(json.dumps([
        {"id": "UNI-01", "fixture": "PUB-01", "family": "Adversarial", "level": "medium", "title": "Injection", "rules": ["knowledge:9.4"], "script": "s", "checks": ["c"]}]), encoding="utf-8")
    cases_path = tmp_path / "brief-x.cases.json"; cases_path.write_text(json.dumps([GOOD]), encoding="utf-8")
    def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
        return ([{"id": c["id"], "level": c["level"], "family": c["family"], "pass": True, "failed": [], "call_id": None, "tools": [], "calls": [], "customer_id": "cust",
                  "slowest_turn_s": 2.0, "ended": "assistant-ended-call"} for c in cases], "sim", "it", "completed", 1.0, 2.0)
    monkeypatch.setattr(B.run_cases, "ensure_personas", lambda cases, style=None: {c["id"]: "p-" + c["id"] for c in cases})
    monkeypatch.setattr(B.run_cases, "run_once", run_once)
    monkeypatch.setattr(B.run_cases, "running_simulations", lambda: [])
    args = lambda skip: argparse.Namespace(agent_id="agent-x", cases=str(cases_path), rules=[], public=None, only=None, reps=1, style=None, openapi=str(ROOT / "tools" / "openapi.json"), skip_universal=skip)
    B.run(args(False)); B.run(args(True))
    out = tmp_path / "results" / "bench" / "brief-x"
    assert [r["id"] for r in json.loads((out / "run-01.json").read_text(encoding="utf-8"))["rows"]] == ["GEN-01", "UNI-01"]
    assert [r["id"] for r in json.loads((out / "run-02.json").read_text(encoding="utf-8"))["rows"]] == ["GEN-01"]
    st = json.loads((out / "run-02.json").read_text(encoding="utf-8"))["stats"]
    assert st["cases"]["UNI-01"]["runs"] == 1 and st["cases"]["GEN-01"]["runs"] == 2     # the universal case keeps its first result on this version


# --- adaptive concurrency: calls at a time follow how the agent kept up ----------------------------------------------

def test_concurrency_adapts_to_the_share_of_slow_replies(tmp_path, monkeypatch):
    monkeypatch.setattr(B, "ROOT", tmp_path); (tmp_path / "results" / "bench" / "slot").mkdir(parents=True)
    assert B.pick_concurrency("slot") == B.run_cases.CONCURRENCY                              # nothing settled yet: the starting point
    nxt, why = B.adapt_concurrency("slot", 16, slow_share=0.05, waited_out=0, n_cases=63)     # few slow replies, nobody gave up: 1.5x
    assert nxt == 24 and why.startswith("the agent kept up (5% of replies over 10 s") and B.pick_concurrency("slot") == 24
    nxt, why = B.adapt_concurrency("slot", 24, slow_share=0.5, waited_out=3, n_cases=20)      # fewer customers than slots: says nothing about the load
    assert nxt == 24 and why == "only 20 of 24 slots were in use: kept"
    nxt, why = B.adapt_concurrency("slot", 24, slow_share=0.30, waited_out=0, n_cases=63)     # many slow replies under full load: halved
    assert nxt == 12 and why.startswith("the agent was slow (30% of replies")
    nxt, _ = B.adapt_concurrency("slot", 12, slow_share=0.05, waited_out=2, n_cases=63)       # two customers hung up waiting: halved too
    assert nxt == 6
    nxt, why = B.adapt_concurrency("slot", 6, slow_share=0.16, waited_out=0, n_cases=63)      # a busy model, as at 5 and at 8 calls: kept
    assert nxt == 6 and why.endswith(": kept")
    nxt, _ = B.adapt_concurrency("slot", 6, slow_share=0.05, waited_out=1, n_cases=63)        # one customer who gave up holds the value
    assert nxt == 6
    nxt, _ = B.adapt_concurrency("slot", 6, slow_share=0.5, waited_out=5, n_cases=63)         # never under the floor
    assert nxt == B.run_cases.CONCURRENCY_MIN
    for _ in range(8): nxt, _ = B.adapt_concurrency("slot", nxt, slow_share=0.0, waited_out=0, n_cases=500)
    assert nxt == B.run_cases.CONCURRENCY_MAX                                                  # never over the ceiling
    assert B.pick_concurrency("slot", host="https://tunnel.example") == B.TUNNEL_MAX           # a tunnelled mock caps it lower
    nxt, _ = B.adapt_concurrency("slot", 20, slow_share=0.0, waited_out=0, n_cases=63, host="https://tunnel.example")
    assert nxt == B.TUNNEL_MAX
    f = tmp_path / "results" / "bench" / "slot" / "concurrency.json"
    f.write_text(json.dumps({"concurrency": 5, "after_run_with": 5, "median_slowest_s": 9.5}), encoding="utf-8")
    assert B.pick_concurrency("slot") == B.run_cases.CONCURRENCY                              # settled by the older rule: not reused
    f.write_text("garbage", encoding="utf-8")
    assert B.pick_concurrency("slot") == B.run_cases.CONCURRENCY                              # an unreadable file is the starting point again


def test_slow_replies_counts_every_rep():
    reps = [[{"replies": 10, "slow_replies": 1, "ended": "assistant-ended-call", "waited_at_end": 0.0},
             {"replies": 6, "slow_replies": 3, "ended": "customer-ended-call", "waited_at_end": 31.0}],
            [{"replies": 4, "slow_replies": 0, "ended": "customer-ended-call", "waited_at_end": 1.0}, {"played": False}]]
    share, waited_out = B.slow_replies(reps)
    assert share == 0.2 and waited_out == 1                          # 4 of 20 replies; the customer who left after a second did not wait
    assert B.slow_replies([[{"played": False}]]) == (0.0, 0)


# --- a run that reaches its time limit: score what finished, name the rest --------------------------------------------

def test_run_time_limit_follows_the_build_clock():
    assert B.run_time_limit(None, None) is None                    # outside a build: no limit
    assert B.run_time_limit(7, None) == 7 and B.run_time_limit(7, 25) == 7   # --max-minutes wins
    assert B.run_time_limit(None, 6) == 11                         # early in a build: the cap below the 15-minute command limit
    assert B.run_time_limit(None, 20) == 5                         # 30 - 20 - 5
    assert B.run_time_limit(None, 29) == 3                         # never under the floor


def test_play_order_starts_with_the_cases_that_failed():
    hist = [{"cases": {"GEN-01": {"pass": True}, "GEN-02": {"pass": False}}}, {"cases": {"GEN-01": {"pass": False}, "GEN-03": {"pass": True}}}]
    cases = [{"id": "UNI-01", "suite": "universal"}, {"id": "GEN-03"}, {"id": "GEN-04"}, {"id": "GEN-02"}, {"id": "GEN-01"}]
    assert [c["id"] for c in B.play_order(cases, hist)] == ["GEN-02", "GEN-01", "GEN-04", "GEN-03", "UNI-01"]


def test_run_cut_at_the_time_limit_scores_what_finished(tmp_path, monkeypatch, capsys):
    import argparse
    monkeypatch.setattr(B, "ROOT", tmp_path)
    cases_path = tmp_path / "brief-x.cases.json"
    cases_path.write_text(json.dumps([GOOD, dict(GOOD, id="GEN-02"), dict(GOOD, id="GEN-03")]), encoding="utf-8")
    def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
        assert deadline is not None                                # --max-minutes reached run_once
        rows = []
        for c in cases:
            played = c["id"] != "GEN-03"
            rows.append({"id": c["id"], "level": c["level"], "family": c["family"], "pass": c["id"] == "GEN-01", "played": played,
                         "failed": [] if c["id"] == "GEN-01" else (["outcome x"] if played else ["not played: the run reached its time limit"]),
                         "call_id": None, "tools": [], "calls": [], "customer_id": "cust", "slowest_turn_s": 2.0, "ended": "assistant-ended-call"})
        return rows, "sim", "it", "cut", 1.0, 2.0
    monkeypatch.setattr(B.run_cases, "ensure_personas", lambda cases, style=None: {c["id"]: "p-" + c["id"] for c in cases})
    monkeypatch.setattr(B.run_cases, "run_once", run_once)
    monkeypatch.setattr(B.run_cases, "running_simulations", lambda: [])
    B.run(argparse.Namespace(agent_id="agent-x", cases=str(cases_path), rules=[], public=None, only=None, reps=1, style=None,
                             openapi=str(ROOT / "tools" / "openapi.json"), skip_universal=True, max_minutes=4))
    out = tmp_path / "results" / "bench" / "brief-x"
    rec = json.loads((out / "run-01.json").read_text(encoding="utf-8"))
    assert [r["id"] for r in rec["rows"]] == ["GEN-01", "GEN-02"] and rec["cut"] == {"limit_min": 4, "not_played": ["GEN-03"]}
    hist = json.loads((out / "history.jsonl").read_text(encoding="utf-8").splitlines()[0])
    assert set(hist["cases"]) == {"GEN-01", "GEN-02"}                # an unplayed case leaves no result behind
    report = (out / "latest.md").read_text(encoding="utf-8")
    assert "cut at the 4-minute time limit**: 1 cases were not played" in report and "`--only GEN-03`" in report
    assert "generated 1/2 · total 1/2" in report
    printed = capsys.readouterr().out
    assert "time limit 4 min" in printed and "were not played: GEN-03" in printed and "Not played (the run reached its 4-minute time limit)" in printed


# --- calls the agent's model never answered: not scored, the model told from the workflow -----------------------------

def _no_reply_run(tmp_path, monkeypatch, answered_ids, diagnosed):
    import argparse
    monkeypatch.setattr(B, "ROOT", tmp_path)
    cases_path = tmp_path / "brief-x.cases.json"
    cases_path.write_text(json.dumps([GOOD, dict(GOOD, id="GEN-02"), dict(GOOD, id="GEN-03")]), encoding="utf-8")
    def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
        rows = []
        for c in cases:
            ok = c["id"] in answered_ids
            rows.append({"id": c["id"], "level": c["level"], "family": c["family"], "pass": ok, "played": ok, **({} if ok else {"why_not": "no reply"}),
                         "failed": [] if ok else ["not played: the agent's model never answered the customer (60 s of silence, then the customer hung up)"],
                         "call_id": None, "tools": [], "calls": [], "customer_id": "cust", "slowest_turn_s": 2.0, "ended": "assistant-ended-call"})
        return rows, "sim", "it", "silent", 1.0, 2.0
    monkeypatch.setattr(B.run_cases, "ensure_personas", lambda cases, style=None: {c["id"]: "p-" + c["id"] for c in cases})
    monkeypatch.setattr(B.run_cases, "run_once", run_once)
    monkeypatch.setattr(B.run_cases, "running_simulations", lambda: [])
    monkeypatch.setattr(B, "diagnose", lambda agent_id: (diagnosed.append(agent_id), ("down", "The phone agent's model is not answering."))[1])
    B.run(argparse.Namespace(agent_id="agent-x", cases=str(cases_path), rules=[], public=None, only=None, reps=2, style=None,
                             openapi=str(ROOT / "tools" / "openapi.json"), skip_universal=True, max_minutes=None))
    return tmp_path / "results" / "bench" / "brief-x"


def test_run_leaves_unanswered_calls_unscored_and_says_why(tmp_path, monkeypatch, capsys):
    diagnosed = []
    out = _no_reply_run(tmp_path, monkeypatch, {"GEN-01"}, diagnosed)
    rec = json.loads((out / "run-01.json").read_text(encoding="utf-8"))
    assert [r["id"] for r in rec["rows"]] == ["GEN-01"] and rec["reps"] == 1                      # a silent model ends the reps
    assert rec["no_reply"]["cases"] == ["GEN-02", "GEN-03"] and rec["cut"] is None and diagnosed == ["agent-x"]
    assert rec["next_concurrency"] == rec["concurrency"] and rec["concurrency_note"].startswith("kept: the model did not answer")
    assert not (out / "concurrency.json").exists()                                                # the load was not measured
    assert set(json.loads((out / "history.jsonl").read_text(encoding="utf-8").splitlines()[0])["cases"]) == {"GEN-01"}
    report = (out / "latest.md").read_text(encoding="utf-8")
    assert "not scored, the agent's model did not answer**: 2 cases: GEN-02, GEN-03. The phone agent's model is not answering." in report
    assert "do not change the workflow because of them" in report and "`--only GEN-02,GEN-03`" in report
    printed = capsys.readouterr().out
    assert "no further reps" in printed and "The phone agent's model is not answering." in printed


def test_run_with_no_answered_call_scores_nothing(tmp_path, monkeypatch):
    with pytest.raises(SystemExit) as e: _no_reply_run(tmp_path, monkeypatch, set(), [])
    assert "Nothing to score: the agent's model answered none of the calls. The phone agent's model is not answering." in str(e.value)
    assert not (tmp_path / "results" / "bench" / "brief-x" / "history.jsonl").exists()


def test_chat_turn_tells_a_silent_model_from_a_broken_start(monkeypatch):
    def api(answer):
        def call(method, path, body=None, **k):
            if path.endswith("/end"): return {}
            if "callId" not in body: return {"callId": "c", "response": "Hello."}
            if isinstance(answer, Exception): raise answer
            return {"response": answer}
        return call
    monkeypatch.setattr(B.freya, "api", api("I can hear you."))
    assert B.chat_turn("wf")[0::2] == ("answered", "I can hear you.")
    monkeypatch.setattr(B.freya, "api", api(RuntimeError("POST /api/v2/chat/message -> 504: error code: 504")))
    assert B.chat_turn("wf")[0] == "no reply"
    monkeypatch.setattr(B.freya, "api", api(RuntimeError("POST /api/v2/chat/message -> 502: error code: 502")))
    assert B.chat_turn("wf")[0] == "no reply"
    monkeypatch.setattr(B.freya, "api", api(TimeoutError("timed out")))
    assert B.chat_turn("wf")[0] == "no reply"
    monkeypatch.setattr(B.freya, "api", api(RuntimeError("POST /api/v2/chat/message -> 500: cannot start")))
    assert B.chat_turn("wf")[0] == "error"


def test_diagnose_tells_the_model_from_the_workflow(monkeypatch):
    monkeypatch.setattr(B, "workflow_of", lambda agent_id: "own" if agent_id == "agent-x" else None)
    monkeypatch.setattr(B, "probe_workflow", lambda: "ref")
    def with_answers(ref, own):
        monkeypatch.setattr(B, "chat_turn", lambda wf: {"ref": ref, "own": own}[wf])
        return B.diagnose("agent-x")
    up, down, none = ("answered", 2.0, "Yes."), ("no reply", 60.0, "504"), ("error", 0.5, "500")
    assert with_answers(down, down)[0] == "down" and "change nothing" in with_answers(down, down)[1]
    assert with_answers(up, down)[0] == "workflow" and "your last save" in with_answers(up, down)[1]
    assert with_answers(up, up)[0] == "up" and with_answers(none, up)[0] == "up"
    assert with_answers(up, none)[0] == "up"                     # the agent's chat did not start, but the model answers
    assert with_answers(none, down)[0] == "down"                 # no test workflow, and the agent got no reply
    assert with_answers(none, none)[0] == "unknown"


def test_workflow_of_and_probe_workflow_are_found_once(tmp_path, monkeypatch):
    f = tmp_path / "agents.json"
    f.write_text(json.dumps({"brief-x": {"workflow_id": "wf-x", "agent_id": "agent-x", "version": 2}}), encoding="utf-8")
    assert B.workflow_of("agent-x", f) == "wf-x" and B.workflow_of("other", f) is None and B.workflow_of("agent-x", tmp_path / "none.json") is None
    created = []
    monkeypatch.setattr(B, "PROBE_FILE", tmp_path / "results" / "probe-workflow.json")
    monkeypatch.setattr(B.freya, "workspace_id", lambda: "ws")
    monkeypatch.setattr(B.freya, "create_workflow", lambda name, wf: created.append(name) or {"workflow_id": "probe-wf", "agent_id": "probe-agent"})
    monkeypatch.setattr(B.freya, "update_workflow", lambda wid, wf: 2)
    assert B.probe_workflow() == "probe-wf" and B.probe_workflow() == "probe-wf" and created == ["model probe"]


def test_main_probe_exits_by_what_it_found(monkeypatch, capsys):
    for state, code in (("up", 0), ("down", 3), ("workflow", 3)):
        monkeypatch.setattr(B, "diagnose", lambda agent_id: (state, f"state {state}"))
        monkeypatch.setattr(sys, "argv", ["benchmark.py", "agent-x", "--probe"])
        with pytest.raises(SystemExit) as e: B.main()
        assert e.value.code == code and f"state {state}" in capsys.readouterr().out


# --- a tunnelled mock: the benchmark's own requests stay local, and a lost bank is not the agent's fault ----------------

def test_practice_host_uses_the_tunnels_local_end(monkeypatch):
    import io
    listing = {"tunnels": [{"public_url": "https://abc.ngrok-free.app", "config": {"addr": "http://localhost:8765"}},
                           {"public_url": "https://port.ngrok-free.app", "config": {"addr": "9000"}}]}
    monkeypatch.setattr(B.urllib.request, "urlopen", lambda url, timeout=None: io.BytesIO(json.dumps(listing).encode()))
    assert B.practice_host("https://abc.ngrok-free.app/") == "http://127.0.0.1:8765"                  # not localhost: on Windows it tries IPv6 for 2 s
    assert B.practice_host("https://port.ngrok-free.app") == "http://127.0.0.1:9000"
    assert B.practice_host("https://other.example") == "https://other.example"          # not a tunnel of this machine
    def down(url, timeout=None): raise OSError("no ngrok here")
    monkeypatch.setattr(B.urllib.request, "urlopen", down)
    assert B.practice_host("https://abc.ngrok-free.app") == "https://abc.ngrok-free.app"


def test_a_lost_bank_halves_the_calls_at_a_time(tmp_path, monkeypatch):
    monkeypatch.setattr(B, "ROOT", tmp_path); (tmp_path / "results" / "bench" / "slot").mkdir(parents=True)
    nxt, why = B.adapt_concurrency("slot", 12, slow_share=0.0, waited_out=0, n_cases=4, host="https://t.example", unreached=3)
    assert nxt == 6 and why == "3 calls could not reach the bank's host: halved"           # even in a small run


def test_run_leaves_calls_that_lost_the_bank_unscored(tmp_path, monkeypatch, capsys):
    import argparse
    monkeypatch.setattr(B, "ROOT", tmp_path)
    cases_path = tmp_path / "brief-x.cases.json"
    cases_path.write_text(json.dumps([GOOD, dict(GOOD, id="GEN-02")]), encoding="utf-8")
    def run_once(agent_id, cases, ids, style=None, concurrency=None, deadline=None):
        rows = []
        for c in cases:
            ok = c["id"] == "GEN-01"
            rows.append({"id": c["id"], "level": c["level"], "family": c["family"], "pass": ok, "played": ok, **({} if ok else {"why_not": "host"}),
                         "failed": [] if ok else ["not played: 2 tool calls could not reach the bank's host (a connection error), so the call tested the outage, not the agent"],
                         "call_id": None, "tools": [], "calls": [], "customer_id": "cust", "slowest_turn_s": 2.0, "ended": "assistant-ended-call"})
        return rows, "sim", "it", "completed", 1.0, 2.0
    monkeypatch.setattr(B.run_cases, "ensure_personas", lambda cases, style=None: {c["id"]: "p-" + c["id"] for c in cases})
    monkeypatch.setattr(B.run_cases, "run_once", run_once)
    monkeypatch.setattr(B.run_cases, "running_simulations", lambda: [])
    B.run(argparse.Namespace(agent_id="agent-x", cases=str(cases_path), rules=[], public=None, only=None, reps=1, style=None,
                             openapi=str(ROOT / "tools" / "openapi.json"), skip_universal=True, max_minutes=None, host="https://t.example"))
    out = tmp_path / "results" / "bench" / "brief-x"
    rec = json.loads((out / "run-01.json").read_text(encoding="utf-8"))
    assert [r["id"] for r in rec["rows"]] == ["GEN-01"] and rec["unreached"] == ["GEN-02"]
    assert rec["concurrency_note"].startswith("1 call could not reach the bank's host: halved")
    report = (out / "latest.md").read_text(encoding="utf-8")
    assert "not scored, a tool call could not reach the bank's host**: 1 cases: GEN-02" in report and "They tested the tunnel, not the agent" in report
    assert "could not reach the bank's host: GEN-02" in capsys.readouterr().out


# --- a brief that brings its own test customers ----------------------------------------------------------------------------

def test_own_fixtures_replace_the_practice_customers(tmp_path, monkeypatch):
    monkeypatch.setattr(B, "ROOT", tmp_path); (tmp_path / "tests").mkdir()
    assert B.fixtures_path("tests/brief-x.cases.json") == B.PUBLIC_SET and not B.own_fixtures("tests/brief-x.cases.json")
    own = [{"id": "10000001", "brief": "brief-x", "variables": {"customerNumber": "10000001", "now": "2026-01-05T10:00:00+03:00"},
            "identity": {}, "persona": "You are Ada Test.", "language": "tr"}]
    (tmp_path / "tests" / "brief-x.fixtures.json").write_text(json.dumps(own), encoding="utf-8")
    assert B.own_fixtures("tests/brief-x.cases.json")
    fixtures = B.load_fixtures(B.fixtures_path("tests/brief-x.cases.json"))
    case = {"id": "GEN-01", "fixture": "10000001", "title": "t", "family": "Happy path", "level": "easy", "rules": ["x:1"],
            "script": "s", "expected": {}, "checks": ["c"]}
    errors, _, _ = B.check_cases([case], fixtures, {"paths": {}}, None, own=True)
    assert errors == []                                                          # the judge scores: no records needed
    errors, _, _ = B.check_cases([case], fixtures, {"paths": {}}, None, own=False)
    assert any("expected.outcome missing" in e for e in errors)
    merged = B.merge_with_fixture(case, fixtures)
    assert merged["persona"] == "You are Ada Test." and merged["language"] == "tr" and merged["variables"]["customerNumber"] == "10000001"
    universal, skipped = B.load_universal(fixtures, {"paths": {}}, ROOT / "universal-test-set.json")
    assert universal == [] and len(skipped) == 13                                # the practice customers are not there
