import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import trace_review as TR


def synthetic(tmp_path):
    cmd = "python3 tools/benchmark.py agent --cases tests/x.cases.json\n"
    lines = [{"start": "2026-10-10T21:39:02+0300", "briefs": ["briefs/brief-a.md"], "model": "m", "self_improve": True},
             {"type": "SystemMessage", "subtype": "thinking_tokens", "data": {"estimated_tokens_delta": 120}},
             {"type": "AssistantMessage", "t": 3.0, "content": [{"thinking": "I should read the brief first.", "signature": "s"}, {"text": "Reading the brief."},
                                                                 {"id": "tu1", "name": "Bash", "input": {"command": cmd}}]},
             {"type": "UserMessage", "t": 60.0, "content": [{"tool_use_id": "tu1", "content": "PASS GEN-01\nFAIL GEN-02\n1 / 2 passed", "is_error": False}]},
             {"type": "AssistantMessage", "t": 61.0, "content": [{"id": "tu2", "name": "Edit", "input": {"file_path": "out/x.workflow.json", "new_string": "abc"}}]},
             {"type": "UserMessage", "t": 62.0, "content": [{"tool_use_id": "tu2", "content": "Exit code 1\nTraceback", "is_error": True}]},
             {"type": "AssistantMessage", "t": 63.0, "content": [{"id": "tu3", "name": "Bash", "input": {"command": "python3 -c \"import freya; freya.save_workflow('x', {})\""}}]},
             {"type": "UserMessage", "t": 64.0, "content": [{"tool_use_id": "tu3", "content": '{"workflow_id": "w", "agent_id": "a"}', "is_error": False}]},
             {"type": "AssistantMessage", "t": 65.0, "content": [{"id": "tu4", "name": "Bash", "input": {"command": cmd}}]},
             {"type": "UserMessation" if False else "UserMessage", "t": 1300.0, "content": [{"tool_use_id": "tu4", "content": "check: ok\nanother simulation is running in this workspace (…), waiting\nCommand timed out after 20m 0s", "is_error": True}]}]
    p = tmp_path / "t.jsonl"
    p.write_text("\n".join(json.dumps(l) for l in lines) + '\n{"type": "AssistantMessage", "content": [{"te', encoding="utf-8")   # partial last line
    return p


def test_short_digest_keeps_what_mattered_and_drops_the_timeline(tmp_path):
    header, messages = TR.load_trace(synthetic(tmp_path))
    assert header["self_improve"] is True and len(messages) == 9                       # the partial last line is skipped
    d = TR.digest(header, messages)
    for needle in ["assistant turns 4", "elapsed 21m40s", "thinking tokens ≈120", "test runs 2", "workflow saves 1", "tool errors 2", "files written: out/x.workflow.json",
                   "## What mattered", "- step 1 [+0m03s] test, 0m57s: Bash: python3 tools/benchmark.py agent", "→ 1 / 2 passed",
                   "- step 2 [+1m01s] error, 0m01s: Edit: out/x.workflow.json", "✖ Exit code 1 Traceback", "- step 3 [+1m03s] save, 0m01s",
                   "- step 4 [+1m05s] test, 20m35s", "timed out after 20m 0s", "command run 2 times",
                   "about 20m35s spent in test runs that waited for the workspace or were cut off"]:
        assert needle in d, needle
    assert "## Timeline" not in d and "thinking: I should read the brief first." not in d   # the short digest has no step-by-step timeline
    assert "untested changes" not in d                                                      # the last test run came after the edit
    full = TR.digest(header, messages, full=True)
    assert "## Timeline" in full and "thinking: I should read the brief first." in full and "said: Reading the brief." in full and "### step 1 [+0m03s]" in full
    assert full.index("## What mattered") < full.index("## Timeline")


def test_flags_untested_edit_and_no_test_run():
    header = {"start": "x"}
    messages = [{"type": "AssistantMessage", "t": 1.0, "content": [{"id": "a", "name": "Bash", "input": {"command": "python3 tools/run_cases.py agent"}}]},
                {"type": "AssistantMessage", "t": 2.0, "content": [{"id": "b", "name": "Write", "input": {"file_path": "out/x.workflow.json", "content": "{}"}}]}]
    d = TR.digest(header, messages)
    assert "edits after the last test run (step 2): untested changes" in d and "no test run at all" not in d
    assert "no test run at all" in TR.digest(header, messages[1:])


def test_digest_on_real_old_trace():
    header, messages = TR.load_trace(ROOT / "traces" / "20261010-213902.jsonl")
    d = TR.digest(header, messages)
    assert "assistant turns 64" in d and "elapsed n/a" in d and len(d) <= TR.DIGEST_MAX + 100
    assert len(d) < len(TR.digest(header, messages, full=True))
