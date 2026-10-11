"""Statistical benchmark for phone agents with multi-repetition analysis, flakiness detection, and style robustness testing.

    python3 tools/statistical_benchmark.py <agent_id> --cases tests/<slot>.cases.json [--reps 10] [--style-sweep] [--critical-only]

This enhanced benchmark runs each test case multiple times to provide statistical confidence metrics:
- Pass rate with Wilson confidence intervals
- Flakiness scoring (0.0 = deterministic, 1.0 = random)
- Style robustness analysis (all 5 styles on critical cases)
- Actionable fix recommendations prioritized by impact

Output: Detailed statistical report with per-case metrics and iterative improvement guidance for Doruk.
"""
import argparse, collections, json, math, pathlib, sys, time
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import freya
import run_cases
from run_cases import STYLES
import benchmark

# Critical families that should be tested with all styles
CRITICAL_FAMILIES = {"Happy path", "Identity failure", "Date edges", "Amount edges", "Hardship", "Multi-product"}

def wilson_confidence_interval(successes, trials, confidence=0.95):
    """Calculate Wilson score confidence interval for binomial proportion.
    
    Returns (lower_bound, upper_bound, center) as percentages (0-100).
    This is more accurate than normal approximation for small sample sizes.
    """
    if trials == 0:
        return 0.0, 0.0, 0.0
    
    p = successes / trials
    
    # Z-score for confidence level (1.96 for 95%)
    z = 1.96 if confidence == 0.95 else 2.576  # 99% confidence
    
    denominator = 1 + z**2 / trials
    center = (p + z**2 / (2 * trials)) / denominator
    margin = z * math.sqrt((p * (1 - p) / trials + z**2 / (4 * trials**2))) / denominator
    
    lower = max(0, center - margin)
    upper = min(1, center + margin)
    
    return lower * 100, upper * 100, center * 100


def calculate_flakiness(pass_sequence):
    """Calculate flakiness score from a sequence of pass/fail results.
    
    Args:
        pass_sequence: List of booleans (True = pass, False = fail)
    
    Returns:
        float: Flakiness score from 0.0 (deterministic) to 1.0 (maximum randomness)
        
    Algorithm:
        - All pass or all fail: 0.0 (deterministic)
        - Mixed results: Based on variance from expected (0.5 = maximum flakiness)
    """
    if not pass_sequence:
        return 0.0
    
    pass_rate = sum(pass_sequence) / len(pass_sequence)
    
    # If all pass or all fail, it's deterministic
    if pass_rate == 0.0 or pass_rate == 1.0:
        return 0.0
    
    # Maximum flakiness is at 50% pass rate
    # Scale so that 50% = 1.0, moving toward 0% or 100% reduces flakiness
    flakiness = 1.0 - abs(2 * pass_rate - 1.0)
    
    return round(flakiness, 2)


def categorize_case(pass_rate, flakiness):
    """Categorize a test case based on pass rate and flakiness.
    
    Returns: (category, priority, emoji)
    """
    if pass_rate >= 90:
        return "Stable", 4, "✅"
    elif pass_rate >= 70:
        if flakiness > 0.3:
            return "Flaky", 2, "⚠️"
        else:
            return "Mostly Passing", 3, "🟡"
    elif pass_rate >= 40:
        return "Flaky", 2, "⚠️"
    else:
        return "Failing", 1, "🚨"


def analyze_style_robustness(case_results_by_style):
    """Analyze pass rates across different speaking styles.
    
    Args:
        case_results_by_style: Dict[style_name, List[bool]] - results per style
    
    Returns:
        Dict with per-style pass rates and weakest style identification
    """
    style_stats = {}
    for style, results in case_results_by_style.items():
        if results:
            pass_rate = sum(results) / len(results) * 100
            style_stats[style] = {
                "pass_rate": round(pass_rate, 1),
                "passes": sum(results),
                "total": len(results)
            }
    
    if not style_stats:
        return {}
    
    weakest_style = min(style_stats.items(), key=lambda x: x[1]["pass_rate"])
    strongest_style = max(style_stats.items(), key=lambda x: x[1]["pass_rate"])
    
    return {
        "by_style": style_stats,
        "weakest": {"style": weakest_style[0], "pass_rate": weakest_style[1]["pass_rate"]},
        "strongest": {"style": strongest_style[0], "pass_rate": strongest_style[1]["pass_rate"]},
        "variance": strongest_style[1]["pass_rate"] - weakest_style[1]["pass_rate"]
    }


def generate_fix_recommendations(case_stats, style_analysis=None):
    """Generate actionable fix recommendations prioritized by impact.
    
    Returns: List of (priority, case_id, recommendation) tuples
    """
    recommendations = []
    
    # Priority 1: Deterministic failures (0% pass rate)
    for case_id, stats in case_stats.items():
        if stats["pass_rate"] == 0.0 and stats["flakiness"] < 0.2:
            recommendations.append((
                1,
                case_id,
                f"**{case_id}** ({stats['family']}) - Always fails (0/{stats['total']})",
                f"Issue: Agent NEVER passes this scenario\n"
                f"Rules: {', '.join(stats['rules'])}\n"
                f"Action: Check workflow logic for {stats['family']} family"
            ))
    
    # Priority 2: Flaky cases (inconsistent results)
    for case_id, stats in case_stats.items():
        if stats["flakiness"] >= 0.4:
            recommendations.append((
                2,
                case_id,
                f"**{case_id}** ({stats['family']}) - Flaky ({stats['passes']}/{stats['total']}, flakiness: {stats['flakiness']})",
                f"Issue: Inconsistent behavior (sometimes pass, sometimes fail)\n"
                f"Rules: {', '.join(stats['rules'])}\n"
                f"Action: Race condition, ambiguous route, or weak validation - strengthen conditions"
            ))
    
    # Priority 3: Consistent failures (but not 0%)
    for case_id, stats in case_stats.items():
        if 0 < stats["pass_rate"] < 40 and stats["flakiness"] < 0.4:
            recommendations.append((
                3,
                case_id,
                f"**{case_id}** ({stats['family']}) - Mostly failing ({stats['passes']}/{stats['total']}, {stats['pass_rate']:.0f}%)",
                f"Issue: Usually fails with some rare passes\n"
                f"Rules: {', '.join(stats['rules'])}\n"
                f"Action: Core logic issue - review {stats['family']} handling"
            ))
    
    # Priority 4: Style-specific weaknesses
    if style_analysis:
        for case_id, analysis in style_analysis.items():
            if analysis.get("variance", 0) > 30:  # >30% difference between best and worst style
                weak = analysis["weakest"]
                recommendations.append((
                    4,
                    case_id,
                    f"**{case_id}** - Style weakness in '{weak['style']}' ({weak['pass_rate']:.0f}%)",
                    f"Issue: Agent struggles with '{weak['style']}' speaking style\n"
                    f"Action: Improve parsing/handling for {weak['style']} input patterns"
                ))
    
    # Sort by priority (lower number = higher priority)
    recommendations.sort(key=lambda x: (x[0], x[1]))
    
    return recommendations


def build_statistical_report(slot, agent_id, case_stats, style_analysis, recommendations, meta):
    """Build comprehensive statistical analysis report in markdown."""
    
    lines = [
        f"# Statistical Benchmark Report: {slot}",
        "",
        f"**Agent:** `{agent_id}`",
        f"**Date:** {meta['timestamp']}",
        f"**Repetitions per case:** {meta['reps']}",
        f"**Total cases:** {len(case_stats)}",
        f"**Total test runs:** {meta['total_runs']}",
        f"**Duration:** {meta['duration_seconds']:.0f}s ({meta['duration_seconds']/60:.1f} min)",
        "",
        "---",
        "",
        "## 📊 Aggregate Metrics",
        ""
    ]
    
    # Calculate aggregate statistics
    all_pass_rates = [s["pass_rate"] for s in case_stats.values()]
    all_flakiness = [s["flakiness"] for s in case_stats.values()]
    
    weighted_pass_rate = sum(all_pass_rates) / len(all_pass_rates) if all_pass_rates else 0
    avg_flakiness = sum(all_flakiness) / len(all_flakiness) if all_flakiness else 0
    
    # Aggregate Wilson CI (using pooled data)
    total_passes = sum(s["passes"] for s in case_stats.values())
    total_runs = sum(s["total"] for s in case_stats.values())
    ci_lower, ci_upper, ci_center = wilson_confidence_interval(total_passes, total_runs)
    
    # Robustness score: weighted combination of metrics
    stability_score = (1.0 - avg_flakiness) * 100  # Higher is better
    robustness_score = (weighted_pass_rate * 0.7 + stability_score * 0.3)
    
    lines.extend([
        f"- **Weighted Pass Rate:** {weighted_pass_rate:.1f}%",
        f"- **95% Confidence Interval:** {ci_lower:.1f}% - {ci_upper:.1f}%",
        f"- **Average Flakiness:** {avg_flakiness:.2f} (0.0 = deterministic, 1.0 = random)",
        f"- **Stability Score:** {stability_score:.1f}/100",
        f"- **Overall Robustness Score:** {robustness_score:.1f}/100",
        "",
    ])
    
    # Category breakdown
    categories = collections.Counter(s["category"] for s in case_stats.values())
    lines.extend([
        "### Test Case Distribution",
        ""
    ])
    for category in ["Failing", "Flaky", "Mostly Passing", "Stable"]:
        count = categories.get(category, 0)
        if count > 0:
            emoji = {"Failing": "🚨", "Flaky": "⚠️", "Mostly Passing": "🟡", "Stable": "✅"}
            lines.append(f"- {emoji.get(category, '')} **{category}:** {count} cases")
    lines.append("")
    
    # Style analysis summary
    if style_analysis:
        lines.extend([
            "### Style Robustness",
            ""
        ])
        
        # Average pass rate per style across all cases
        style_aggregates = collections.defaultdict(lambda: {"passes": 0, "total": 0})
        for analysis in style_analysis.values():
            for style, stats in analysis.get("by_style", {}).items():
                style_aggregates[style]["passes"] += stats["passes"]
                style_aggregates[style]["total"] += stats["total"]
        
        for style in sorted(STYLES):
            if style in style_aggregates and style_aggregates[style]["total"] > 0:
                agg = style_aggregates[style]
                rate = agg["passes"] / agg["total"] * 100
                lines.append(f"- **{style}:** {rate:.1f}% ({agg['passes']}/{agg['total']})")
        lines.append("")
    
    # Hidden brief prediction
    lines.extend([
        "## 🎯 Hidden Brief Score Prediction",
        "",
        "Based on current robustness metrics, estimated performance on 60 hidden test cases:",
        "",
        f"- **Predicted pass range:** {int(60 * ci_lower / 100)} - {int(60 * ci_upper / 100)} cases ({ci_lower:.0f}% - {ci_upper:.0f}%)",
        f"- **Expected passes:** {int(60 * ci_center / 100)} cases ({ci_center:.0f}%)",
        f"- **Confidence:** {'High' if ci_upper - ci_lower < 20 else 'Medium' if ci_upper - ci_lower < 35 else 'Low'} (CI width: {ci_upper - ci_lower:.0f}%)",
        "",
        "Note: Assumes hidden cases have similar distribution to current test set.",
        "",
        "---",
        "",
    ])
    
    # Action required section
    lines.extend([
        "## 🚨 Action Required (Prioritized)",
        "",
        "Fix recommendations in priority order for iterative improvement:",
        ""
    ])
    
    if not recommendations:
        lines.append("✅ **No critical issues found!** All tests are stable.")
    else:
        current_priority = None
        for priority, case_id, summary, detail in recommendations:
            priority_labels = {1: "CRITICAL FAILURES", 2: "FLAKY CASES", 3: "CONSISTENT FAILURES", 4: "STYLE WEAKNESSES"}
            
            if priority != current_priority:
                lines.extend(["", f"### Priority {priority}: {priority_labels.get(priority, 'Other')}", ""])
                current_priority = priority
            
            lines.extend([
                f"{priority}. {summary}",
                f"   ```",
                f"   {detail}",
                f"   ```",
                ""
            ])
    
    return lines  # Part 1 - continuing in next append


    # Continuing build_statistical_report...
    lines.extend([
        "---",
        "",
        "## 📈 Per-Case Statistics",
        "",
        "| Case ID | Family | Pass Rate | CI (95%) | Flakiness | Category | Priority |",
        "|---------|--------|-----------|----------|-----------|----------|----------|"
    ])
    
    # Sort by category priority (Failing first, Stable last)
    sorted_cases = sorted(
        case_stats.items(),
        key=lambda x: (x[1]["priority"], -x[1]["pass_rate"], x[0])
    )
    
    for case_id, stats in sorted_cases:
        ci_low, ci_high, _ = wilson_confidence_interval(stats["passes"], stats["total"])
        lines.append(
            f"| {case_id} | {stats['family']} | {stats['passes']}/{stats['total']} ({stats['pass_rate']:.0f}%) | "
            f"{ci_low:.0f}%-{ci_high:.0f}% | {stats['flakiness']:.2f} | "
            f"{stats['emoji']} {stats['category']} | P{stats['priority']} |"
        )
    
    lines.append("")
    
    # Style analysis details
    if style_analysis:
        lines.extend([
            "---",
            "",
            "## 🎭 Style Robustness Analysis",
            "",
            "Pass rates for critical cases across all speaking styles:",
            "",
            "| Case ID | pieces | corrects | talkative | asks_back | in_words | Variance |",
            "|---------|--------|----------|-----------|-----------|----------|----------|"
        ])
        
        for case_id in sorted(style_analysis.keys()):
            analysis = style_analysis[case_id]
            by_style = analysis.get("by_style", {})
            
            row = [case_id]
            for style in ["pieces", "corrects", "talkative", "asks_back", "in_words"]:
                if style in by_style:
                    rate = by_style[style]["pass_rate"]
                    row.append(f"{rate:.0f}%")
                else:
                    row.append("-")
            
            variance = analysis.get("variance", 0)
            row.append(f"{variance:.0f}%" + (" ⚠️" if variance > 30 else ""))
            
            lines.append("| " + " | ".join(row) + " |")
        
        lines.append("")
    
    # Footer
    lines.extend([
        "---",
        "",
        "## 📝 Next Steps for Iterative Improvement",
        "",
        "1. **Fix Priority 1 issues first** (deterministic failures - highest impact)",
        "2. **Save updated workflow** and re-run statistical benchmark",
        "3. **Verify fixes** by checking if affected cases move to higher categories",
        "4. **Iterate until** >95% pass rate with <0.1 average flakiness",
        "5. **Target:** All cases in 'Stable' category before hidden brief phase",
        "",
        f"**Estimated iterations needed:** {max(1, len([r for r in recommendations if r[0] <= 2]) // 3)} - {max(2, len([r for r in recommendations if r[0] <= 3]) // 2)}",
        f"**Time per iteration:** ~15-20 minutes (benchmark + fix + test)",
        "",
        "---",
        "",
        f"*Report generated by statistical_benchmark.py at {meta['timestamp']}*"
    ])
    
    return "\n".join(lines)


def run_statistical_benchmark(args):
    """Main statistical benchmark execution."""
    t0 = time.time()
    
    print(f"Statistical Benchmark starting...")
    print(f"Agent: {args.agent_id}")
    print(f"Repetitions: {args.reps}")
    if args.style_sweep:
        print("Style sweep: ENABLED (testing all 5 styles on critical cases)")
    print()
    
    # Load and validate cases
    fixtures = benchmark.load_fixtures()
    openapi = benchmark.load_openapi(args.openapi)
    gen = json.load(open(args.cases, encoding="utf-8"))
    
    errors, warnings, cov = benchmark.check_cases(gen, fixtures, openapi, None)
    if errors:
        print("ERROR: Cases file has validation errors:")
        for e in errors:
            print(f"  - {e}")
        return 1
    
    print(f"✓ Loaded {len(gen)} test cases")
    
    # Filter to critical cases if requested
    if args.critical_only:
        original_count = len(gen)
        gen = [c for c in gen if c.get("family") in CRITICAL_FAMILIES]
        print(f"✓ Filtered to {len(gen)} critical cases (from {original_count} total)")
    
    # Prepare cases
    cases = [benchmark.merge_with_fixture(c, fixtures) for c in gen]
    slot = benchmark.slot_of(args.cases)
    
    # Storage for results
    case_results = collections.defaultdict(list)  # case_id -> list of pass/fail booleans
    case_metadata = {c["id"]: {"family": c.get("family", "Unknown"), "rules": c.get("rules", [])} for c in cases}
    style_results = collections.defaultdict(lambda: collections.defaultdict(list))  # case_id -> style -> list of results
    
    total_runs = 0
    
    # Run base repetitions (no style override)
    print(f"\n🔄 Running {args.reps} repetitions per case...")
    print(f"   Estimated time: {len(cases) * args.reps * 3 // 60}-{len(cases) * args.reps * 10 // 60} minutes")
    print()
    
    for rep in range(args.reps):
        print(f"Rep {rep + 1}/{args.reps}...", flush=True)
        
        ids = run_cases.ensure_personas(cases, style=None)
        rows, sim_id, it_id, status, took, med = run_cases.run_once(args.agent_id, cases, ids)
        
        for r, c in zip(rows, cases):
            # Apply additional validation (forbidden tools, etc.)
            r["forbidden"] = sorted({t for t in r["tools"] if t in (c.get("forbidden_tools") or [])})
            if r["forbidden"]:
                r["failed"].append("forbidden tool called: " + ", ".join(r["forbidden"]))
                r["pass"] = False
            
            more = benchmark.applications_failed(c.get("expected") or {}, r.get("calls") or [])
            if more:
                r["failed"] += more
                r["pass"] = False
            
            case_results[c["id"]].append(r["pass"])
        
        total_runs += len(cases)
        print(f"   → {sum(r['pass'] for r in rows)}/{len(rows)} passed, {took:.0f}s\n")
    
    # Style sweep if requested
    if args.style_sweep:
        critical_cases = [c for c in cases if c.get("family") in CRITICAL_FAMILIES]
        
        if critical_cases:
            print(f"\n🎭 Running style sweep on {len(critical_cases)} critical cases...")
            print(f"   Testing all {len(STYLES)} styles × {args.reps} reps")
            print()
            
            for style_name in sorted(STYLES):
                print(f"Testing style '{style_name}'...", flush=True)
                
                for rep in range(args.reps):
                    ids = run_cases.ensure_personas(critical_cases, style=style_name)
                    rows, sim_id, it_id, status, took, med = run_cases.run_once(args.agent_id, critical_cases, ids)
                    
                    for r, c in zip(rows, critical_cases):
                        # Apply same validation
                        r["forbidden"] = sorted({t for t in r["tools"] if t in (c.get("forbidden_tools") or [])})
                        if r["forbidden"]:
                            r["pass"] = False
                        
                        more = benchmark.applications_failed(c.get("expected") or {}, r.get("calls") or [])
                        if more:
                            r["pass"] = False
                        
                        style_results[c["id"]][style_name].append(r["pass"])
                    
                    total_runs += len(critical_cases)
                
                passed = sum(any(style_results[c["id"]][style_name]) for c in critical_cases)
                print(f"   → {style_name}: {passed}/{len(critical_cases)} cases passed at least once\n")
    
    # Calculate statistics
    print("\n📊 Calculating statistics...")
    
    case_stats = {}
    for case_id, results in case_results.items():
        passes = sum(results)
        total = len(results)
        pass_rate = (passes / total * 100) if total > 0 else 0.0
        flakiness = calculate_flakiness(results)
        category, priority, emoji = categorize_case(pass_rate, flakiness)
        
        case_stats[case_id] = {
            "passes": passes,
            "total": total,
            "pass_rate": round(pass_rate, 1),
            "flakiness": flakiness,
            "category": category,
            "priority": priority,
            "emoji": emoji,
            "family": case_metadata[case_id]["family"],
            "rules": case_metadata[case_id]["rules"]
        }
    
    # Analyze style robustness
    style_analysis = {}
    if args.style_sweep and style_results:
        for case_id, styles_data in style_results.items():
            style_analysis[case_id] = analyze_style_robustness(styles_data)
    
    # Generate recommendations
    recommendations = generate_fix_recommendations(case_stats, style_analysis if args.style_sweep else None)
    
    # Build report
    meta = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "reps": args.reps,
        "total_runs": total_runs,
        "duration_seconds": time.time() - t0
    }
    
    report = build_statistical_report(slot, args.agent_id, case_stats, style_analysis, recommendations, meta)
    
    # Save report
    out_dir = ROOT / "results" / "bench" / slot
    out_dir.mkdir(parents=True, exist_ok=True)
    
    report_file = out_dir / f"statistical-report-{time.strftime('%Y%m%d-%H%M%S')}.md"
    report_file.write_text(report, encoding="utf-8")
    
    # Also save as latest
    latest_file = out_dir / "statistical-latest.md"
    latest_file.write_text(report, encoding="utf-8")
    
    # Save raw JSON data
    json_data = {
        "meta": meta,
        "agent_id": args.agent_id,
        "case_stats": case_stats,
        "style_analysis": style_analysis if args.style_sweep else None,
        "recommendations": [{"priority": p, "case_id": c, "summary": s, "detail": d} for p, c, s, d in recommendations]
    }
    
    json_file = out_dir / f"statistical-data-{time.strftime('%Y%m%d-%H%M%S')}.json"
    json_file.write_text(json.dumps(json_data, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"\n✅ Statistical benchmark complete!")
    print(f"   Duration: {meta['duration_seconds']/60:.1f} minutes")
    print(f"   Total test runs: {total_runs}")
    print(f"\n📄 Report saved to:")
    print(f"   {report_file}")
    print(f"   {latest_file}")
    print(f"   {json_file}")
    print(f"\n🎯 Quick Summary:")
    
    # Print quick summary
    categories = collections.Counter(s["category"] for s in case_stats.values())
    for category in ["Failing", "Flaky", "Mostly Passing", "Stable"]:
        count = categories.get(category, 0)
        if count > 0:
            emoji = {"Failing": "🚨", "Flaky": "⚠️", "Mostly Passing": "🟡", "Stable": "✅"}
            print(f"   {emoji.get(category, '')} {category}: {count} cases")
    
    print(f"\n💡 Next: Review {latest_file} for detailed fix recommendations")
    
    return 0


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("agent_id", help="Agent ID to benchmark")
    ap.add_argument("--cases", required=True, help="tests/<slot>.cases.json file")
    ap.add_argument("--reps", type=int, default=10, help="Repetitions per test case (default: 10)")
    ap.add_argument("--style-sweep", action="store_true", help="Test all 5 styles on critical cases")
    ap.add_argument("--critical-only", action="store_true", help="Only test critical family cases")
    ap.add_argument("--openapi", default=str(ROOT / "tools" / "openapi.json"), help="Tool API file")
    
    args = ap.parse_args()
    
    try:
        return run_statistical_benchmark(args)
    except KeyboardInterrupt:
        print("\n\nBenchmark interrupted by user")
        return 130
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
