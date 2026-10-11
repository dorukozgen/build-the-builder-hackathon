import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import benchmark as B
import statistical_benchmark as S

CASE = {"id": "GEN-01", "fixture": "PUB-06", "title": "Accepts the floor", "family": "Happy path", "level": "easy", "rules": ["brief-a:26"], "script": "Verified.",
        "expected": {"outcome": "promise", "reason": None, "promises": [{"product_id": "p1", "amount": 637.5, "date": "2026-10-14"}], "notes": [], "callbacks": [], "transfers": []},
        "checks": ["the floor is offered once"]}


def rows(cases, passing, tools=()):
    return [{"id": c["id"], "pass": c["id"] in passing, "failed": [], "tools": list(tools), "calls": [], "call_id": None} for c in cases]


def test_play_scores_like_benchmark(monkeypatch):
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(CASE, fx), B.merge_with_fixture(dict(CASE, id="GEN-02", forbidden_tools=["transfer_to_agent"], style="pieces"), fx)]
    monkeypatch.setattr(S.run_cases, "ensure_personas", lambda cases, style=None: {})
    monkeypatch.setattr(S.run_cases, "run_once", lambda agent, cases, ids: (rows(cases, {"GEN-01", "GEN-02"}, ["transfer_to_agent"]), "s", "i", "completed", 5.0, 1.0))
    results = {}
    assert S.play("a", cases, results) == (1, 5.0)                     # GEN-02 called a tool it forbids: a fail, as in benchmark.py
    S.play("a", cases, results, "corrects")
    assert results == {"GEN-01": {"none": [1, 1], "corrects": [1, 1]}, "GEN-02": {"pieces": [0, 1], "corrects": [0, 1]}}


def test_report_is_text_with_every_section():
    st = B.statistics({"GEN-01": {"none": [7, 10]}}, [B.merge_with_fixture(CASE, B.load_fixtures())])
    meta = {"agent_id": "a", "version": None, "at": "now", "seconds": 120, "simulations": 10, "planned": 10, "reps": 10, "style_sweep": False, "critical_only": False, "stopped": None}
    text = S.report("brief-x", st, meta)
    assert isinstance(text, str)
    for needle in ["# Statistical benchmark brief-x", "version unknown", "10 of 10 simulations", "## Statistics", "10 simulations · 1 of 1 cases have results, 10 results in all",
                   "| GEN-01 | Happy path | 7/10 (70%) | 40–89% | 0.60 | 34% | Flaky P2 |", "hidden-brief estimate: 21 of 60", "## Next steps"]:
        assert needle in text, needle


def test_main_saves_after_every_simulation_and_keeps_a_stopped_run(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "ROOT", tmp_path)
    p = tmp_path / "brief-x.cases.json"; p.write_text(json.dumps([CASE]), encoding="utf-8")
    calls = {"n": 0}
    def run_once(agent, cases, ids):
        calls["n"] += 1
        if calls["n"] == 3: raise KeyboardInterrupt
        return rows(cases, {"GEN-01"} if calls["n"] == 1 else set()), "s", "i", "completed", 1.0, 1.0
    monkeypatch.setattr(S.run_cases, "ensure_personas", lambda cases, style=None: {})
    monkeypatch.setattr(S.run_cases, "run_once", run_once)
    monkeypatch.setattr(sys, "argv", ["statistical_benchmark.py", "agent-x", "--cases", str(p), "--reps", "5", "--openapi", str(ROOT / "tools" / "openapi.json")])
    assert S.main() == 1
    out = tmp_path / "results" / "bench" / "brief-x"
    data = json.loads(next(out.glob("statistical-data-*.json")).read_text(encoding="utf-8"))
    assert data["meta"]["simulations"] == 2 and data["meta"]["stopped"] == "interrupted" and data["results"] == {"GEN-01": {"none": [1, 2]}}
    latest = (out / "statistical-latest.md").read_text(encoding="utf-8")
    assert "Stopped early: interrupted" in latest and "2 of 5 simulations" in latest and "| GEN-01 | Happy path | 1/2 (50%)" in latest


def test_style_sweep_without_critical_cases_is_skipped(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(S, "ROOT", tmp_path)
    p = tmp_path / "brief-x.cases.json"; p.write_text(json.dumps([dict(CASE, family="Out of scope")]), encoding="utf-8")
    played = []
    def run_once(agent, cases, ids):
        played.append(len(cases)); return rows(cases, {"GEN-01"}), "s", "i", "completed", 1.0, 1.0
    monkeypatch.setattr(S.run_cases, "ensure_personas", lambda cases, style=None: {})
    monkeypatch.setattr(S.run_cases, "run_once", run_once)
    openapi = ["--openapi", str(ROOT / "tools" / "openapi.json")]
    monkeypatch.setattr(sys, "argv", ["statistical_benchmark.py", "agent-x", "--cases", str(p), "--reps", "2", "--style-sweep"] + openapi)
    assert S.main() == 0 and played == [1, 1] and "The style sweep is skipped" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["statistical_benchmark.py", "agent-x", "--cases", str(p), "--critical-only"] + openapi)
    assert S.main() == 2 and played == [1, 1]                          # nothing critical to play
