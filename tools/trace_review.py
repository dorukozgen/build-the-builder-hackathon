"""Digest of a builder trace for the builder's own retrospective: the test runs, the saves, the errors, the long waits, the repeated
commands and the untested edits, with the timing of each. It is short on purpose: a retrospective needs what went wrong and what it
cost, not every step. `--full` adds the step-by-step timeline with the summarised thinking.

    python3 tools/trace_review.py [traces/<file>.jsonl] [--out reports/<file>.digest.md] [--full]

Without a path it takes the newest trace, which is the running builder's own. The trace may still be growing: a partial
last line is skipped. Old traces without timestamps or thinking text are digested with what they have.
"""
import argparse, collections, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the console and the builder read UTF-8
THINK_MAX, TEXT_MAX, ERR_MAX, DIGEST_MAX = 400, 300, 300, 120_000
LONG_STEP_S = 120                                                    # a tool call that took longer than this is worth a line
TEST_LINE = re.compile(r"^(PASS|FAIL) |passed|check: |^- |waiting|timed out|answered with an error|Exit code")
SCORE_LINE = re.compile(r"\d+ / \d+ passed|generated \d+/\d+[^\n]*|hidden-brief estimate[^\n]*|timed out[^\n]*|answered with an error[^\n]{0,100}|waiting for the workspace[^\n]*|another simulation[^\n]{0,80}")


def load_trace(path):
    header, messages = None, []
    for line in pathlib.Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        try: d = json.loads(line)
        except json.JSONDecodeError: continue              # the last line may still be being written
        if header is None: header = d
        else: messages.append(d)
    return header or {}, messages


def mmss(s): return f"{int(s // 60)}m{int(s % 60):02d}s"


def short(s, n):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n] + f" … [{len(s) - n} more]"


def tool_call_line(b):
    name, inp = b.get("name"), b.get("input") or {}
    if name == "Bash": return "Bash: " + short((inp.get("command") or "").strip().splitlines()[0] if (inp.get("command") or "").strip() else "", 160)
    if name in ("Write", "Edit"): return f"{name}: {inp.get('file_path')} ({len(inp.get('content') or inp.get('new_string') or '')} chars)"
    if name == "Read": return f"Read: {inp.get('file_path')}"
    return f"{name}: {short(json.dumps(inp, ensure_ascii=False), 160)}"


def is_test_command(cmd):
    return "run_cases.py" in cmd or ("benchmark.py" in cmd and "--check" not in cmd and "--fixtures" not in cmd and "--help" not in cmd)


def analyse(header, messages):
    """Walk the trace once. Returns the counters, the steps (one per assistant turn) and the events the retrospective is about."""
    tools, commands, writes = collections.Counter(), collections.Counter(), []
    errors = thinking_tokens = test_runs = saves = n = 0
    steps, pending, t_last, last_test, last_edit, events = [], {}, None, None, None, []
    for m in messages:
        if m.get("t") is not None: t_last = m["t"]
        if m.get("type") == "SystemMessage" and m.get("subtype") == "thinking_tokens":
            thinking_tokens += (m.get("data") or {}).get("estimated_tokens_delta") or 0
        elif m.get("type") == "AssistantMessage":
            n += 1; step = {"n": n, "t": m.get("t"), "think": "", "text": "", "calls": [], "results": []}
            for b in m.get("content") or []:
                if not isinstance(b, dict): continue
                if b.get("thinking"): step["think"] = short(b["thinking"], THINK_MAX)
                elif "text" in b: step["text"] = short(b["text"], TEXT_MAX)
                elif "name" in b:
                    tools[b["name"]] += 1; step["calls"].append(tool_call_line(b)); pending[b.get("id")] = (step, b)
                    inp = b.get("input") or {}
                    if b["name"] == "Bash":
                        cmd = (inp.get("command") or "").strip(); commands[cmd] += 1
                        if is_test_command(cmd): test_runs += 1; last_test = n
                        if "save_workflow" in cmd: saves += 1
                    if b["name"] in ("Write", "Edit"): writes.append(inp.get("file_path")); last_edit = n
            steps.append(step)
        elif m.get("type") == "UserMessage" and isinstance(m.get("content"), list):
            for b in m["content"]:
                if not isinstance(b, dict) or "tool_use_id" not in b: continue
                step, call = pending.get(b["tool_use_id"], (None, None)); content = b.get("content")
                text = "\n".join(c.get("text", "") for c in content if isinstance(c, dict)) if isinstance(content, list) else str(content or "")
                if step is None: continue
                took = (m.get("t") or 0) - (step["t"] or 0) if m.get("t") is not None and step["t"] is not None else None
                cmd = (call.get("input") or {}).get("command", "") if call.get("name") == "Bash" else ""
                kind = ("test" if cmd and is_test_command(cmd) else "save" if "save_workflow" in cmd else "error" if b.get("is_error") else
                        "slow" if took is not None and took > LONG_STEP_S else None)
                if b.get("is_error"):
                    errors += 1; step["results"].append("✖ " + short(text, ERR_MAX))
                else:
                    hits = [l for l in text.splitlines() if TEST_LINE.search(l)]
                    step["results"].append(f"{len(text)} chars" + ((": " + " | ".join(short(h, 120) for h in hits[:40])) if hits else ""))
                if kind:
                    gist = "✖ " + short(text, ERR_MAX) if b.get("is_error") else " | ".join(dict.fromkeys(short(x.group(0), 110) for x in SCORE_LINE.finditer(text))) or short(text, 160)
                    events.append({"step": n if step is None else step["n"], "t": step["t"], "took": took, "kind": kind, "call": tool_call_line(call), "gist": gist})
    flags = [f"command run {k} times: `{short(cmd.splitlines()[0], 120)}`" for cmd, k in commands.items() if k > 1 and cmd]
    if last_edit and (last_test is None or last_edit > last_test): flags.append(f"edits after the last test run (step {last_edit}): untested changes")
    if errors: flags.append(f"{errors} tool errors; see the ✖ lines")
    if not test_runs: flags.append("no test run at all")
    waited = sum(e["took"] or 0 for e in events if e["kind"] == "test" and ("waiting" in e["gist"] or "timed out" in e["gist"] or "another simulation" in e["gist"]))
    if waited > LONG_STEP_S: flags.append(f"about {mmss(waited)} spent in test runs that waited for the workspace or were cut off: check for another builder or a simulation left running")
    return {"tools": tools, "errors": errors, "thinking_tokens": thinking_tokens, "test_runs": test_runs, "saves": saves, "n": n, "t_last": t_last,
            "writes": writes, "steps": steps, "events": events, "flags": flags}


def digest(header, messages, full=False):
    a = analyse(header, messages)
    L = ["# Trace digest", "",
         f"start {header.get('start')} · model {header.get('model')} · briefs {header.get('briefs')} · self_improve {header.get('self_improve', False)}",
         f"assistant turns {a['n']} · elapsed {mmss(a['t_last']) if a['t_last'] is not None else 'n/a'} · tool calls {dict(a['tools'])} · tool errors {a['errors']} · test runs {a['test_runs']} · workflow saves {a['saves']} · thinking tokens ≈{a['thinking_tokens']}",
         "files written: " + (", ".join(sorted({w for w in a["writes"] if w})) or "none"), ""]
    L += ["## Flags", ""] + ([f"- {f}" for f in a["flags"]] or ["- none"]) + [""]
    L += ["## What mattered", "", "Test runs, saves, errors and tool calls over two minutes, in order. The step number is the assistant turn.", ""]
    labels = {"test": "test", "save": "save", "error": "error", "slow": "slow"}
    for e in a["events"]:
        when = f"[+{mmss(e['t'])}]" if e["t"] is not None else ""
        L.append(f"- step {e['step']} {when} {labels[e['kind']]}" + (f", {mmss(e['took'])}" if e["took"] is not None else "") + f": {e['call']}")
        if e["gist"]: L.append(f"  → {e['gist']}")
    if not a["events"]: L.append("- nothing: no test run, no save, no error")
    L.append("")
    if full:
        L += ["## Timeline", ""]
        for s in a["steps"]:
            L.append(f"### step {s['n']}" + (f" [+{mmss(s['t'])}]" if s["t"] is not None else ""))
            if s["think"]: L.append(f"thinking: {s['think']}")
            if s["text"]: L.append(f"said: {s['text']}")
            L += [f"- {c}" for c in s["calls"]] + [f"  → {r}" for r in s["results"]] + [""]
    out = "\n".join(L)
    return out if len(out) <= DIGEST_MAX else out[:DIGEST_MAX] + "\n\n[digest cut at 120 KB; later steps omitted]\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("trace", nargs="?"); ap.add_argument("--out"); ap.add_argument("--full", action="store_true", help="add the step-by-step timeline with the summarised thinking")
    a = ap.parse_args()
    path = pathlib.Path(a.trace) if a.trace else max((ROOT / "traces").glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    text = digest(*load_trace(path), full=a.full)
    out = pathlib.Path(a.out) if a.out else ROOT / "reports" / (path.stem + ".digest.md")
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text, encoding="utf-8")
    print(text if not a.full else text.split("## Timeline")[0]); print(f"digest written to {out}")


if __name__ == "__main__": main()
