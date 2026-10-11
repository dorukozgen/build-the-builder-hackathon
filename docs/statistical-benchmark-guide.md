# Statistical Benchmark Guide

## Overview

The statistical benchmark provides enhanced testing with multi-repetition analysis, flakiness detection, and style robustness testing. It's designed for iterative agent improvement through actionable insights.

## Why Use Statistical Benchmark?

### Problem with Single-Run Testing
```
Run 1: GEN-05 PASS ✓
Run 2: GEN-05 FAIL ✗
Run 3: GEN-05 PASS ✓

Question: Is this a bug or just inconsistent LLM behavior?
```

### Statistical Benchmark Solution
```
GEN-05: 7/10 pass (70%, CI: 55-85%, flakiness: 0.42)
→ FLAKY! Needs workflow fix for consistency
```

## Key Features

### 1. Multi-Repetition Testing
- Runs each test case 10 times (configurable)
- Provides pass rate with statistical confidence
- Identifies deterministic vs. flaky failures

### 2. Flakiness Detection
- **Flakiness Score:** 0.0 (deterministic) to 1.0 (random)
- Distinguishes between:
  - Broken logic (always fails)
  - Race conditions (sometimes fails)
  - Working cases (always passes)

### 3. Style Robustness Analysis
- Tests critical cases with all 5 speaking styles:
  - `pieces` - gives info in parts
  - `corrects` - self-corrects
  - `talkative` - adds chitchat
  - `asks_back` - asks questions
  - `in_words` - says numbers as words
- Identifies style-specific weaknesses

### 4. Actionable Recommendations
- Prioritized fix list (P1-P4)
- Specific issue diagnosis
- Estimated iterations to perfection

## Usage

### Basic Usage
```bash
# Run 10 repetitions per case
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json

# Custom repetition count
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json --reps 5
```

### Style Sweep Mode
```bash
# Test all 5 styles on critical cases (Happy path, Identity, Dates, Amounts, etc.)
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json --style-sweep
```

### Critical Cases Only
```bash
# Focus on most important test families
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json --critical-only
```

## Output

### Report Files
```
results/bench/<slot>/
├── statistical-report-20261011-143022.md  # Detailed analysis
├── statistical-latest.md                   # Symlink to latest report
└── statistical-data-20261011-143022.json  # Raw data for automation
```

### Report Sections

1. **Aggregate Metrics**
   - Weighted pass rate
   - 95% confidence interval
   - Average flakiness
   - Robustness score (0-100)

2. **Action Required (Prioritized)**
   - P1: Critical failures (0% pass rate)
   - P2: Flaky cases (inconsistent)
   - P3: Consistent failures
   - P4: Style weaknesses

3. **Per-Case Statistics**
   - Pass rate with confidence interval
   - Flakiness score
   - Category (Failing/Flaky/Mostly Passing/Stable)

4. **Style Robustness Analysis** (if --style-sweep)
   - Pass rates per style
   - Weakest style identification
   - Variance across styles

5. **Hidden Brief Prediction**
   - Estimated score on 60 hidden cases
   - Confidence level

## Iterative Improvement Workflow

### Step 1: Run Benchmark
```bash
python3 tools/statistical_benchmark.py ag_abc123 --cases tests/brief-a.cases.json
```

### Step 2: Read Report
```bash
cat results/bench/brief-a/statistical-latest.md
```

Look for **Action Required** section with prioritized fixes.

### Step 3: Fix Highest Priority Issue
Example from report:
```
Priority 1: CRITICAL FAILURES

1. GEN-12 (Identity failure) - Always fails (0/10)
   Issue: Agent NEVER passes this scenario
   Rules: brief-a:11, brief-a:12
   Action: Check workflow logic for Identity failure family
```

Fix the workflow JSON:
- Check `verify_identity` route conditions
- Ensure retry logic works
- Validate error handling

### Step 4: Save and Re-Run
```bash
python3 -c "import freya,json,sys; print(json.dumps(freya.save_workflow(sys.argv[1], json.load(open(sys.argv[2])))))" brief-a out/brief-a.workflow.json

python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json
```

### Step 5: Verify Improvement
Check if:
- GEN-12 moved from "Failing" to "Stable"
- Pass rate increased
- Flakiness decreased

### Step 6: Repeat Until Perfect
Target metrics:
- Pass rate: >95%
- Average flakiness: <0.1
- All cases in "Stable" category

## Metrics Explained

### Wilson Confidence Interval
Statistical confidence range for true pass rate.

Example: `65%-85% CI` means:
- We're 95% confident the true pass rate is between 65% and 85%
- Wider interval = more uncertainty (need more reps)
- Narrow interval = high confidence

### Flakiness Score
Measures consistency of results:
- **0.0-0.2:** Deterministic (good or bad, but consistent)
- **0.3-0.5:** Flaky (needs fixing)
- **0.6-1.0:** Highly unstable (critical issue)

### Robustness Score
Overall agent quality (0-100):
- Weighted average of pass rate (70%) and stability (30%)
- Higher = better
- Target: >90 for production readiness

## Time Estimates

### Standard Run (10 reps, 40 cases)
- Sequential: ~20-30 minutes
- With Freya concurrency: ~5-10 minutes

### Style Sweep (10 reps, 40 cases, 5 styles)
- Critical cases only: ~15-20 minutes
- All cases: ~40-60 minutes

### Full Iteration Cycle
1. Run benchmark: 5-10 min
2. Read report: 2-3 min
3. Fix workflow: 5-10 min
4. Save + re-run: 5-10 min

**Total per iteration:** 15-25 minutes

**Target:** 3-5 iterations to perfection

## Comparison: Standard vs Statistical Benchmark

| Feature | Standard benchmark.py | Statistical benchmark.py |
|---------|----------------------|-------------------------|
| Purpose | Pass/fail scoring | Iterative improvement |
| Runs per case | 1-3 | 10+ |
| Flakiness detection | Manual observation | Automated scoring |
| Style testing | Manual --style flag | Automated sweep |
| Confidence intervals | No | Yes (Wilson CI) |
| Fix recommendations | No | Yes (prioritized) |
| Hidden brief prediction | No | Yes |
| Best for | Final scoring | Development & debugging |

## Best Practices

### When to Use Statistical Benchmark
- ✅ During agent development (iterative improvement)
- ✅ After comprehensive test generation
- ✅ Before hidden brief phase (validation)
- ✅ When cases fail inconsistently

### When to Use Standard Benchmark
- ✅ Quick validation after small changes
- ✅ Final scoring runs
- ✅ Public test set evaluation
- ✅ When time is limited

### Optimization Tips

1. **Start with --critical-only** to focus on important cases
2. **Use --reps 5** for faster iterations, increase to 10 for final validation
3. **Run --style-sweep** only after achieving 90%+ base pass rate
4. **Fix P1 issues first** - highest impact, lowest effort
5. **Re-run after each fix** to track progress

## Example Session

```bash
# Initial benchmark
$ python3 tools/statistical_benchmark.py ag_abc123 --cases tests/brief-a.cases.json
✓ Loaded 42 test cases
🔄 Running 10 repetitions per case...
Rep 1/10... → 28/42 passed, 187s
Rep 2/10... → 30/42 passed, 192s
...
✅ Statistical benchmark complete!
   Duration: 31.2 minutes
   Total test runs: 420

🎯 Quick Summary:
   🚨 Failing: 8 cases
   ⚠️ Flaky: 6 cases
   🟡 Mostly Passing: 4 cases
   ✅ Stable: 24 cases

💡 Next: Review results/bench/brief-a/statistical-latest.md

# Read report and fix P1 issues
$ cat results/bench/brief-a/statistical-latest.md | head -n 100

# Fix workflow, save, re-run
$ vim out/brief-a.workflow.json
$ python3 -c "import freya,json,sys; ..." brief-a out/brief-a.workflow.json
$ python3 tools/statistical_benchmark.py ag_abc123 --cases tests/brief-a.cases.json

# After 3-4 iterations
🎯 Quick Summary:
   ✅ Stable: 40 cases
   🟡 Mostly Passing: 2 cases

Overall Robustness Score: 94.2/100
Predicted hidden brief score: 54-58 cases (90-97%)
```

## Troubleshooting

### Benchmark Takes Too Long
- Use `--critical-only` flag
- Reduce `--reps` to 5
- Skip `--style-sweep` until later

### All Cases Showing Flaky
- Check if model is under load (slow responses)
- Verify workflow has proper validation
- Check for race conditions in tool calls

### Low Confidence Intervals
- Increase `--reps` to 15-20
- More repetitions = narrower confidence interval

### Style Sweep Issues
- Ensure comprehensive tests include style variants
- Check persona generation in run_cases.py
- Verify STYLES dictionary is complete

## Integration with Existing Workflow

Statistical benchmark complements the standard benchmark:

```bash
# Development cycle
1. Generate comprehensive tests (40+ cases)
2. Initial standard benchmark (quick validation)
3. Statistical benchmark (find flaky cases)
4. Iterative fixes using statistical insights
5. Final standard benchmark with --reps 3
6. Hidden brief phase with confidence
```

## Contributing

To extend statistical benchmark:
- Add new metrics in `calculate_*` functions
- Enhance recommendations in `generate_fix_recommendations`
- Improve report formatting in `build_statistical_report`

---

**Pro Tip:** Run statistical benchmark at least once before hidden brief phase. The confidence interval and flakiness scores predict hidden brief performance better than single-run pass rates.
