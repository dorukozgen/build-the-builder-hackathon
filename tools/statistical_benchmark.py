"""Statistical benchmark: every case played many times, for pass rates you can trust. Scored exactly like tools/benchmark.py, whose
reports carry the same statistics on every run (section "Statistics on this version"). Guide: docs/statistical-benchmark-guide.md.

    python3 tools/statistical_benchmark.py <agent_id> --cases tests/<slot>.cases.json [--reps 10] [--style-sweep] [--critical-only] [--openapi FILE] [--host URL]

Each repetition is one simulation, and a workspace runs one simulation at a time: 10 reps last as long as ten benchmark runs, 30 to
110 minutes, and a style sweep adds 5 x reps simulations of the critical cases. That fits neither a 30-minute build nor its 15-minute
command limit. Inside a build use benchmark.py, whose statistics pool every --reps, --only and --style run of the same saved agent
version; use this tool outside a build. It keeps no transcripts: read a case's with `benchmark.py <agent_id> --cases ... --only <case>`.
Writes results/bench/<slot>/statistical-data-<time>.json after every simulation, so a stopped run keeps what it played, then
statistical-report-<time>.md and its copy statistical-latest.md.
"""
import argparse, json, pathlib, shutil, sys, time, urllib.error
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import benchmark as B
import run_cases
from run_cases import STYLES

# The families docs/test-case-template-comprehensive.md asks for first. --critical-only plays only their cases; the style sweep plays them in every style.
CRITICAL_FAMILIES = {"Happy path", "Identity failure", "Date edges", "Amount edges", "Hardship", "Multi-product"}


def play(agent_id, cases, results, style=None):
    """One simulation of `cases`, scored as benchmark.py scores them (ledger, judge, forbidden tools, applications). Adds each case's result
    to results[case][style], the style being `style`, else the case's own, else "none", as in benchmark.pool. Returns (passed, seconds)."""
    rows, _, _, _, took, _ = run_cases.run_once(agent_id, cases, run_cases.ensure_personas(cases, style))
    passed = 0
    for r, c in zip(rows, cases):
        ok = bool(r["pass"]) and not set(r["tools"]) & set(c.get("forbidden_tools") or []) and not B.applications_failed(c.get("expected") or {}, r.get("calls") or [])
        acc = results.setdefault(c["id"], {}).setdefault(style or c.get("style") or "none", [0, 0])
        acc[0] += ok; acc[1] += 1; passed += ok
    return passed, took


def report(slot, st, meta):
    """The report: what was played, benchmark.py's statistics section, then the next steps."""
    L = [f"# Statistical benchmark {slot}", "",
         f"agent `{meta['agent_id']}` · version {meta['version'] or 'unknown'} · {meta['at']} · {meta['seconds'] / 60:.1f} min · "
         f"{meta['simulations']} of {meta['planned']} simulations · {meta['reps']} reps" + (" · style sweep" if meta["style_sweep"] else "")
         + (" · critical cases only" if meta["critical_only"] else ""), ""]
    if meta.get("stopped"): L += [f"**Stopped early: {meta['stopped']}.** The statistics cover what was played.", ""]
    L += B.stats_md(st, "Statistics", f"{meta['simulations']} simulation{'' if meta['simulations'] == 1 else 's'}")
    L += ["## Next steps", "",
          "1. Fix in the fix order, P1 first. This tool keeps no transcripts: read a case's with `python3 tools/benchmark.py <agent_id> --cases ... --only <case>`.",
          "2. Save the workflow. Its saved version changes, so the results before the save stop counting for it.",
          "3. Run again and check that the fixed cases moved up a category and that no other case moved down.",
          "4. Aim for every case Stable, flakiness under 0.1 on average and a hidden-brief estimate with high confidence.", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("agent_id"); ap.add_argument("--cases", required=True, help="tests/<slot>.cases.json")
    ap.add_argument("--reps", type=int, default=10, help="simulations of the whole set (default 10)")
    ap.add_argument("--style-sweep", action="store_true", help="then play the critical cases in each of the 5 styles, --reps times each")
    ap.add_argument("--critical-only", action="store_true", help="play only the cases of the critical families")
    ap.add_argument("--openapi", default=str(ROOT / "tools" / "openapi.json"), help="the tool API file to validate against; default tools/openapi.json")
    ap.add_argument("--host", help="base URL of a self-hosted bank mock, as in benchmark.py")
    a = ap.parse_args()
    if a.host:
        import score; score.HOST = a.host.rstrip("/")
    fixtures, gen = B.load_fixtures(), json.load(open(a.cases, encoding="utf-8"))
    errors, warnings, _ = B.check_cases(gen, fixtures, B.load_openapi(a.openapi))
    for w in warnings: print("warning", w)
    if errors:
        for e in errors: print("ERROR", e)
        print("check: FAILED"); return 2
    cases = [B.merge_with_fixture(c, fixtures) for c in gen]
    critical = [c for c in cases if c.get("family") in CRITICAL_FAMILIES]
    if (a.critical_only or a.style_sweep) and not critical:
        print("warning: no case of the critical families (" + ", ".join(sorted(CRITICAL_FAMILIES)) + "); this file's families: "
              + ", ".join(sorted({str(c.get("family")) for c in cases})) + (". Nothing to play." if a.critical_only else ". The style sweep is skipped."))
        if a.critical_only: return 2
    if a.critical_only: cases = critical
    plan = [None] * a.reps + ([s for s in sorted(STYLES) for _ in range(a.reps)] if a.style_sweep and critical else [])
    slot = B.slot_of(a.cases); out = ROOT / "results" / "bench" / slot; out.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S"); data = out / f"statistical-data-{stamp}.json"
    meta = {"agent_id": a.agent_id, "version": B.agent_version(a.agent_id), "at": time.strftime("%Y-%m-%d %H:%M:%S"), "reps": a.reps, "style_sweep": a.style_sweep,
            "critical_only": a.critical_only, "planned": len(plan), "simulations": 0, "seconds": 0, "stopped": None}
    print(f"{len(plan)} simulations, each as long as one benchmark run (3 to 11 minutes): {a.reps} of {len(cases)} cases"
          + (f", then {len(plan) - a.reps} of the {len(critical)} critical cases, {a.reps} in each style" if len(plan) > a.reps else ""), flush=True)
    results, t0 = {}, time.time()
    try:
        for i, style in enumerate(plan, 1):
            group = critical if style else cases
            passed, took = play(a.agent_id, group, results, style)
            meta.update(simulations=i, seconds=round(time.time() - t0))
            print(f"simulation {i} of {len(plan)}" + (f", style {style}" if style else "") + f": {passed}/{len(group)} passed, {took:.0f} s", flush=True)
            data.write_text(json.dumps({"meta": meta, "results": results}, indent=1), encoding="utf-8")     # after every simulation: a stopped run keeps what it played
    except KeyboardInterrupt: meta["stopped"] = "interrupted"
    except (RuntimeError, urllib.error.URLError, TimeoutError) as e: meta["stopped"] = f"Freya or the bank answered with an error, usually transient: {e}"
    meta["seconds"] = round(time.time() - t0)
    if not results: print(f"nothing was played: {meta['stopped']}"); return 1
    st = B.statistics(results, cases)
    data.write_text(json.dumps({"meta": meta, "results": results, "statistics": st}, indent=1, ensure_ascii=False), encoding="utf-8")
    md = out / f"statistical-report-{stamp}.md"
    md.write_text(report(slot, st, meta), encoding="utf-8"); shutil.copyfile(md, out / "statistical-latest.md")
    print("\n" + " · ".join(f"{k} {v}" for k, v in st["categories"].items()))
    h = st.get("hidden")
    if h: print(f"hidden-brief estimate: {h['expected']} of {h['of']} counting only 3 passes out of 3 ({h['one_run']} if one pass counted), confidence {h['confidence']}")
    print(f"report: results/bench/{slot}/statistical-latest.md · data: results/bench/{slot}/{data.name}" + (f" · stopped early: {meta['stopped']}" if meta["stopped"] else ""))
    return 1 if meta["stopped"] else 0


if __name__ == "__main__": sys.exit(main())
