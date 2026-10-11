"""Digest of a builder trace for the builder's own review: what it thought (summarised), did, got wrong, and how long it took.

    python3 tools/trace_review.py [traces/<file>.jsonl] [--out reports/<file>.digest.md]

Without a path it takes the newest trace, which is the running builder's own. The trace may still be growing: a partial
last line is skipped. Old traces without timestamps or thinking text are digested with what they have.
"""
import argparse, collections, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the console and the builder read UTF-8
THINK_MAX, TEXT_MAX, ERR_MAX, DIGEST_MAX = 400, 300, 300, 120_000
TEST_LINE = re.compile(r"^(PASS|FAIL) |passed|check: |^- ")


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
    return "run_cases.py" in cmd or ("benchmark.py" in cmd and "--check" not in cmd and "--fixtures" not in cmd)


def digest(header, messages):
    tools, commands, writes = collections.Counter(), collections.Counter(), []
    errors = thinking_tokens = test_runs = saves = n = 0
    steps, pending, t_last, last_test, last_edit = [], {}, None, None, None
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
                    tools[b["name"]] += 1; step["calls"].append(tool_call_line(b)); pending[b.get("id")] = step
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
                step = pending.get(b["tool_use_id"]); content = b.get("content")
                text = "\n".join(c.get("text", "") for c in content if isinstance(c, dict)) if isinstance(content, list) else str(content or "")
                if b.get("is_error"):
                    errors += 1
                    if step: step["results"].append("✖ " + short(text, ERR_MAX))
                elif step:
                    hits = [l for l in text.splitlines() if TEST_LINE.search(l)]
                    step["results"].append(f"{len(text)} chars" + ((": " + " | ".join(short(h, 120) for h in hits[:40])) if hits else ""))
    L = ["# Trace digest", "",
         f"start {header.get('start')} · model {header.get('model')} · briefs {header.get('briefs')} · self_improve {header.get('self_improve', False)}",
         f"assistant turns {n} · elapsed {mmss(t_last) if t_last is not None else 'n/a'} · tool calls {dict(tools)} · tool errors {errors} · test runs {test_runs} · workflow saves {saves} · thinking tokens ≈{thinking_tokens}",
         "files written: " + (", ".join(sorted({w for w in writes if w})) or "none"), ""]
    flags = [f"command run {k} times: `{short(cmd.splitlines()[0], 120)}`" for cmd, k in commands.items() if k > 1 and cmd]
    if last_edit and (last_test is None or last_edit > last_test): flags.append(f"edits after the last test run (step {last_edit}): untested changes")
    if errors: flags.append(f"{errors} tool errors; see the ✖ lines")
    L += ["## Flags", ""] + ([f"- {f}" for f in flags] or ["- none"]) + ["", "## Timeline", ""]
    for s in steps:
        L.append(f"### step {s['n']}" + (f" [+{mmss(s['t'])}]" if s["t"] is not None else ""))
        if s["think"]: L.append(f"thinking: {s['think']}")
        if s["text"]: L.append(f"said: {s['text']}")
        L += [f"- {c}" for c in s["calls"]] + [f"  → {r}" for r in s["results"]] + [""]
    out = "\n".join(L)
    return out if len(out) <= DIGEST_MAX else out[:DIGEST_MAX] + "\n\n[digest cut at 120 KB; later steps omitted]\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("trace", nargs="?"); ap.add_argument("--out"); a = ap.parse_args()
    path = pathlib.Path(a.trace) if a.trace else max((ROOT / "traces").glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    text = digest(*load_trace(path))
    out = pathlib.Path(a.out) if a.out else ROOT / "reports" / (path.stem + ".digest.md")
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text, encoding="utf-8")
    print(text.split("## Timeline")[0]); print(f"digest written to {out}")


if __name__ == "__main__": main()
