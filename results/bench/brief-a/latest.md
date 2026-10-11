# Benchmark brief-a · run 7

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-11 00:18:03 · 343 s · reps 2 · style none · `--only`

## Score

- generated 1/1 · public 1/1 · total 2/2
- promised on passed cases: 730.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-14, PUB-10
- regressed: none
- still failing: none

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | |
|---|---|---|---|---|---|---|---|---|
| GEN-14 | ✗ | ✓ | ✓ | – | – | ✗ | ✓ | flaky |
| PUB-10 | ✓ | – | ✗ | ✓ | ✗ | ✗ | ✓ |  |
| GEN-01 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-02 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-03 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | – | – | – | – | not in this run |
| GEN-05 | ✓ | ✓ | ✓ | – | – | – | – | not in this run |
| GEN-06 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-07 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | – | – | – | – | not in this run |
| GEN-09 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-10 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-11 | ✓ | – | ✓ | – | ✗ | ✓ | – | not in this run |
| GEN-12 | ✓ | – | ✓ | ✓ | – | – | – | not in this run |
| GEN-13 | ✓ | – | ✓ | ✓ | – | – | – | not in this run |
| GEN-15 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-16 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-17 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-18 | ✓ | ✓ | ✓ | – | – | – | – | not in this run |
| GEN-19 | ✓ | – | ✗ | ✗ | ✓ | – | – | not in this run |
| GEN-20 | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-21 | ✗ | ✗ | ✗ | ✓ | – | – | – | not in this run |
| GEN-22 | ✓ | – | ✓ | – | – | – | – | not in this run |
| PUB-01 | ✓ | – | ✓ | – | – | – | – | not in this run |
| PUB-02 | ✓ | – | ✓ | – | – | – | – | not in this run |
| PUB-03 | ✓ | – | ✓ | – | – | – | – | not in this run |
| PUB-04 | ✓ | – | ✓ | ✓ | – | – | – | not in this run |
| PUB-05 | ✓ | – | ✓ | – | – | – | – | not in this run |
| PUB-06 | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| PUB-07 | ✓ | – | ✓ | ✓ | – | – | – | not in this run |
| PUB-08 | ✓ | – | ✓ | – | – | – | – | not in this run |
| PUB-09 | ✓ | – | ✓ | – | – | – | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

none
flags: slow 1

## Failed cases

none

## Passed cases

- GEN-14 Next Friday, asks about changing it later, service fails once · 13 turns · verify_identity > verify_identity > get_account > create_promise > create_promise > close_call · slowest 1.2 s · `results/bench/brief-a/run-07/GEN-14.md`
- PUB-10 The promise service fails on the first call · 12 turns · verify_identity > verify_identity > get_account > create_promise > create_promise > close_call · slowest 10.1 s · `results/bench/brief-a/run-07/PUB-10.md`

## Timing

median slowest agent turn 10 s · worst 10 s · failed calls where the customer hung up: 0 · **the agent was slow in this run; a re-run may score higher**

## What this run suggests

- Flaky: GEN-14 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-14`.
- The agent was slow in this run (median slowest turn 10 s). A call that ended in a hang-up may pass when re-run; re-run those before changing the workflow.
- The re-run cases pass. Run the full set once before you finish: a fix can break another case.
- Styles not run yet: asks_back, corrects, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 35 of 30 min used; a full run takes ~8 min and does not fit with a 3-minute margin. `--only` on a few cases may; otherwise finish.
