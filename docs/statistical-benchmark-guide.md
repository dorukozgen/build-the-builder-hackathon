# Statistical Benchmark Guide

## Overview

The statistical benchmark scores a phone agent on many results per case instead of one: pass rates with confidence intervals, flakiness, a category and a fix priority for every case, a speaking-style analysis and an estimate of the hidden-brief score. The scoring lives in `tools/benchmark.py` and shows up in two places:

- **Every `tools/benchmark.py` run.** Its report (`results/bench/<slot>/latest.md`) has the section "Statistics on this version": every result of the cases on the saved version of the agent you just tested, pooled across runs. This is the one to use in a build.
- **`tools/statistical_benchmark.py`** plays every case 10 times and, with `--style-sweep`, the critical cases in every speaking style. That takes hours, not minutes: use it outside a build.

Both score a result the way the final does: the bank's records, the judge's reading of the conversation, forbidden tools, applications.

## Why use it?

### The problem with one run
```
Run 1: GEN-05 PASS ✓
Run 2: GEN-05 FAIL ✗
Run 3: GEN-05 PASS ✓

Question: is this a bug or just inconsistent LLM behaviour?
```

### What the statistics say
```
GEN-05: 7/10 passed (70%, 95% CI 40–89%, flakiness 0.60) → Flaky, P2
3 of 3: 34% → the final plays every customer three times and counts it only when all three pass:
              this case would count about one time in three
```

## In a build (30 minutes)

A build has 30 minutes, tests included, and a benchmark command is cut off after 15.

- **Do not run `tools/statistical_benchmark.py` in a build.** Ten repetitions are ten simulations, one at a time: 30 to 110 minutes. The command would be cut off after its first few repetitions.
- **Use `tools/benchmark.py`.** Its statistics pool every result of the same saved version of the agent: a full run, an `--only` re-run, a `--reps 2` run and a `--style` run on that version all add up. Saving the workflow makes a new version, and the results before the save stop counting for it.
- **Read "Statistics on this version" first**, then the failed cases and their transcripts.
- **Fix in the fix order**: a regression first (a case that passed before the last save and fails after it), then P1, P2, P3, P4.
- **Aim for three results per case on the last saved version** when the clock allows: a full run plus a `--reps 2` run, or two full runs, without saving in between. Below that the estimate's confidence is low: one pass is a hint, not proof.
- The report's "What this run suggests" repeats the fix order and the estimate, and says whether another full run fits the time left.

## The metrics

### Pass rate and Wilson confidence interval
A case's pass rate is its passes over its results. Its 95% Wilson interval is the range its true pass rate most likely lies in; unlike the plain formula, it holds for small counts. Two passes out of two give 34–100%: two passes prove little. Ten out of ten give 72–100%.

The overall line also gives an interval for all results taken together. It treats every result as a toss of one coin, but the cases differ, so the true range is wider: read it as a rough guide.

### Flakiness
`1 - |2p - 1|`, where p is the pass rate: 0.0 when every result agrees (all pass or all fail), 1.0 at 50%.
- **0.0–0.2:** deterministic (good or bad, but consistent)
- **0.3–0.5:** flaky (needs fixing)
- **0.6–1.0:** highly unstable (critical issue)

Flakiness follows from the pass rate. It says how mixed a case's results are, not why.

### Categories and the fix order

| Category | Pass rate | Priority | What to do |
|---|---|---|---|
| Failing | under 40% | P1 | A deterministic bug ("fails every run" at 0%, else "mostly fails"): its transcript shows the step, route or check that goes wrong. |
| Flaky | 40% to 85% | P2 | A rule held only by a prompt, an ambiguous route or a weak condition: compare a passing and a failing transcript, then move the rule into a route or code. |
| Mostly Passing | 85% to 90% | P3 | The final counts a case only when it passes 3 runs out of 3: read a failing transcript. |
| Stable | 90% and up | – | Nothing. |
| *style weakness* | one style 30+ points below the case's best | P4 | The step that hears the answer must understand a customer who talks that way. |

From 70% to 90% a case is Flaky when its flakiness is above 0.3 and Mostly Passing otherwise; as flakiness follows from the pass rate, that is the 85% line. A case that fails in every style, the plain way included, is no style weakness: it is P1 or P2.

### 3 of 3
The final plays every unseen customer three times and counts it only when all three runs pass. A case's "3 of 3" is p³: 90% per run is 73% in the final, 80% is 51%, 70% is 34%. A flaky case costs more than its pass rate suggests.

### Hidden-brief estimate
The expected passes on 60 hidden cases, if they resemble this set: 60 × the average "3 of 3" of the cases. The report also gives the number one passing run would earn (60 × the mean pass rate); the gap is what flakiness costs.
- It needs results for every case on the version. After an `--only` run on a new version it waits for a full run.
- It leaves the universal cases out: the final scores every case on the bank's records, and universal cases are not scored on records.
- **Confidence:** high with at least 10 results per case, medium with at least 3, low below that.
- It assumes the hidden cases resemble yours and that your expectations are right. It says nothing about rules no case tests.

### Stability and robustness
Stability is `(1 - average flakiness) × 100`. Robustness is `0.7 × mean pass rate + 0.3 × stability`, 0 to 100; the target is above 90. Stability counts a case that always fails as stable, so read robustness next to the pass rate, never alone.

### Style robustness
When a case has results in more than one speaking style on the version (from `--style` runs, from its own `style` field, or from a style sweep), the report adds a table: the case's pass rate in each style and the spread between its best and worst. A spread above 30 points makes a P4 style weakness. The style `none` is the case played as its script is written.

## How results pool
- The version comes from `.freya-agents.json`, which `freya.save_workflow` updates on every save (`created` before the first update). An agent that is not in that file pools nothing: each run's statistics are its own.
- A result counts only for the same text of its case: editing a case's script, expectation, checks, fixture, forbidden tools or third-party flag starts its count again.
- A pass and then a fail on one saved version is flakiness, not a regression: the report calls a case fixed or regressed only across a save.
- An `--only` run adds results for its cases; the other cases keep theirs.
- The universal cases (`universal-test-set.json`), which every run plays, pool and count like any other case.

## `statistical_benchmark.py` (outside a build)

### Usage
```bash
# 10 repetitions of every case
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json

# fewer repetitions
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json --reps 5

# then the critical cases in each of the 5 speaking styles, --reps times each
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json --style-sweep

# only the critical cases
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-a.cases.json --critical-only

# another tool API and a self-hosted mock, as with benchmark.py
python3 tools/statistical_benchmark.py <agent_id> --cases tests/brief-f.cases.json --openapi tools/openapi-f.json --host https://<tunnel>
```

The critical families are Happy path, Identity failure, Date edges, Amount edges, Hardship and Multi-product, the names `docs/test-case-template-comprehensive.md` uses. A cases file without them has no critical cases, and the tool says so.

### Output
```
results/bench/<slot>/
├── statistical-data-20261011-143022.json    # what was played, every result, the statistics; rewritten after every simulation
├── statistical-report-20261011-143022.md    # the report
└── statistical-latest.md                    # a copy of the latest report
```

A run stopped by Ctrl-C or by a Freya error keeps what it played: the data file holds every finished simulation, and the report says it stopped early. The tool keeps no transcripts (read a case's with `benchmark.py --only <case>`), and its results do not go into the benchmark's history.

### Time
Each repetition is one simulation, and a workspace runs one simulation at a time. A simulation of your set takes as long as one benchmark run of it, 3 to 11 minutes for ten customers and more for a larger set.
- `--reps 10`: 30 to 110 minutes.
- `--style-sweep`: another 5 × reps simulations of the critical cases.
- `--critical-only` and `--reps 5` cut both.

### Report sections
1. What was played: agent, saved version, simulations, and whether it stopped early.
2. Statistics: the overall lines, the fix order, the per-case table and, with styles, the style table. It is the same section as in the benchmark's report.
3. Next steps.

## Iterative improvement workflow

### Step 1: Run
```bash
python3 tools/benchmark.py <agent_id> --cases tests/brief-a.cases.json --rules briefs/brief-a.md --public A
```
Outside a build, `statistical_benchmark.py` gives many results at once.

### Step 2: Read the statistics
Open `results/bench/brief-a/latest.md` and look at "Statistics on this version" and its fix order.

### Step 3: Fix the highest priority
Example from a report:
```
- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-12 (Identity failure) fails every run (0/3) · rules brief-a:11, brief-a:12
```
Read GEN-12's transcript, then fix the workflow: the `verify_identity` routes, the retry logic, the error handling.

### Step 4: Save and run again
```bash
python3 -c "import freya,json,sys; print(json.dumps(freya.save_workflow(sys.argv[1], json.load(open(sys.argv[2])))))" brief-a out/brief-a.workflow.json
python3 tools/benchmark.py <agent_id> --cases tests/brief-a.cases.json --rules briefs/brief-a.md --only GEN-12
```

### Step 5: Verify
- Did GEN-12 move up a category?
- Did any other case move down? A full run on the same version answers that and firms up the estimate.

### Step 6: Repeat
Target metrics:
- every case Stable
- average flakiness under 0.1
- a hidden-brief estimate with medium confidence in a build, high outside it

## Comparison

| | `benchmark.py` | `statistical_benchmark.py` |
|---|---|---|
| Purpose | every run of a build | long checks outside a build |
| Results per case | pooled over the runs of one saved version | `--reps` (10) in one go, plus an optional style sweep |
| Statistics: intervals, flakiness, categories, fix order, estimate | yes | yes, the same scoring |
| Style analysis | from `--style` runs and the cases' own styles | automatic sweep of the critical cases |
| Transcripts, history, fixed and regressed cases | yes | no |
| Fits a 30-minute build | yes | no |

## Troubleshooting

### The estimate says it needs results for every case
The last save made a new version, and only `--only` runs followed it. Run the full set once.

### Confidence stays low
A case needs 3 results on one version for medium confidence and 10 for high. Another full run or `--reps 2` adds them, as long as you do not save in between.

### Every case looks flaky
Check whether the model was slow: the report's Timing section warns when the median slowest turn is above 10 seconds, which makes customers hang up. Re-run before you change the workflow. If it persists, look for rules that live only in prompts.

### The style sweep is skipped
No case belongs to a critical family. Name the families as the test template does, or run `benchmark.py --style <style>`.

### Results from before a save are gone from the statistics
They belong to the earlier version. That is on purpose: a fix changes what the agent does.

## Contributing

The scoring is in `tools/benchmark.py`: `wilson`, `flakiness`, `stat_category`, `case_stats`, `pool`, `statistics`, `actions` and `stats_md`, which renders the report section. `tools/statistical_benchmark.py` only plays the cases and calls them, so a metric changed there changes in both tools. `tools/tests/test_benchmark.py` and `tools/tests/test_statistical_benchmark.py` cover them.

---

**Pro tip:** one green run is a hint, not proof. The 3-of-3 estimate on the last saved version predicts the final better than a single run's pass count.
