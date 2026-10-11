import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import trace_review as TR


def test_digest_on_synthetic_trace(tmp_path):
    cmd = "python3 tools/benchmark.py agent --cases tests/x.cases.json\n"
    lines = [{"start": "2026-10-10T21:39:02+0300", "briefs": ["briefs/brief-a.md"], "model": "m", "self_improve": True},
             {"type": "SystemMessage", "subtype": "thinking_tokens", "data": {"estimated_tokens_delta": 120}},
             {"type": "AssistantMessage", "t": 3.0, "content": [{"thinking": "I should read the brief first.", "signature": "s"}, {"text": "Reading the brief."},
                                                                 {"id": "tu1", "name": "Bash", "input": {"command": cmd}}]},
             {"type": "UserMessage", "t": 60.0, "content": [{"tool_use_id": "tu1", "content": "PASS GEN-01\nFAIL GEN-02\n1 / 2 passed", "is_error": False}]},
             {"type": "AssistantMessage", "t": 61.0, "content": [{"id": "tu2", "name": "Edit", "input": {"file_path": "out/x.workflow.json", "new_string": "abc"}}]},
             {"type": "UserMessage", "t": 62.0, "content": [{"tool_use_id": "tu2", "content": "Exit code 1\nTraceback", "is_error": True}]},
             {"type": "AssistantMessage", "t": 63.0, "content": [{"id": "tu3", "name": "Bash", "input": {"command": cmd}}]}]
    p = tmp_path / "t.jsonl"
    p.write_text("\n".join(json.dumps(l) for l in lines) + '\n{"type": "AssistantMessage", "content": [{"te', encoding="utf-8")   # partial last line
    header, messages = TR.load_trace(p)
    assert header["self_improve"] is True and len(messages) == 6
    d = TR.digest(header, messages)
    for needle in ["assistant turns 3", "elapsed 1m03s", "thinking tokens ≈120", "test runs 2", "tool errors 1", "files written: out/x.workflow.json",
                   "thinking: I should read the brief first.", "said: Reading the brief.", "PASS GEN-01 | FAIL GEN-02 | 1 / 2 passed",
                   "✖ Exit code 1 Traceback", "command run 2 times", "### step 1 [+0m03s]", "- Bash: python3 tools/benchmark.py agent"]:
        assert needle in d, needle
    assert "untested changes" not in d                       # the last test run came after the edit


def test_untested_edit_flag():
    header = {"start": "x"}
    messages = [{"type": "AssistantMessage", "t": 1.0, "content": [{"id": "a", "name": "Bash", "input": {"command": "python3 tools/run_cases.py agent"}}]},
                {"type": "AssistantMessage", "t": 2.0, "content": [{"id": "b", "name": "Write", "input": {"file_path": "out/x.workflow.json", "content": "{}"}}]}]
    assert "edits after the last test run (step 2): untested changes" in TR.digest(header, messages)


def test_digest_on_real_old_trace():
    header, messages = TR.load_trace(ROOT / "traces" / "20261010-213902.jsonl")
    d = TR.digest(header, messages)
    assert "assistant turns 64" in d and "elapsed n/a" in d and len(d) <= TR.DIGEST_MAX + 100
