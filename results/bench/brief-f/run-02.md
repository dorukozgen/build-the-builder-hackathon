# Benchmark brief-f · run 2

agent `9b1b1617-e7e7-48bd-bc0d-7c61b1a79678` · 2026-10-11 02:26:42 · 52 s · reps 1 · style none · `--only`

## Score

- generated 3/3 · total 3/3
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-04, GEN-06, GEN-08
- regressed: none
- still failing: none

## History

| case | run 1 | run 2 | |
|---|---|---|---|
| GEN-04 | ✗ | ✓ | changed |
| GEN-06 | ✗ | ✓ | changed |
| GEN-08 | ✗ | ✓ | changed |
| GEN-01 | ✓ | – | not in this run |
| GEN-02 | ✓ | – | not in this run |
| GEN-03 | ✓ | – | not in this run |
| GEN-05 | ✓ | – | not in this run |
| GEN-07 | ✓ | – | not in this run |

## Rule coverage

rules cited by no case: brief-f:3, brief-f:4, brief-f:9, brief-f:10, brief-f:11, brief-f:12, brief-f:13, brief-f:14, brief-f:17, brief-f:18, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:23, brief-f:24, brief-f:27

## Failure categories

none

## Failed cases

none

## Passed cases

- GEN-04 Asks for his balance, accepts the transfer · 5 turns · transfer_to_agent > close_call · slowest 1.4 s · `results/bench/brief-f/run-02/GEN-04.md`
- GEN-06 Asks the fee and whether it is approved at once, then fails the date of birth three times · 9 turns · verify_identity > verify_identity > verify_identity > close_call · slowest 2.1 s · `results/bench/brief-f/run-02/GEN-06.md`
- GEN-08 Limit increase, asks his current limit and the decision, then insists on a person · 7 turns · transfer_to_agent > close_call · slowest 1.3 s · `results/bench/brief-f/run-02/GEN-08.md`

## Timing

median slowest agent turn 1 s · worst 2 s · failed calls where the customer hung up: 0

## What this run suggests

- Changed since the previous run: GEN-04, GEN-06, GEN-08. If a change weakened a check or an expectation, undo it unless the brief says the old version was wrong.
- The re-run cases pass. Run the full set once before you finish: a fix can break another case.
- Styles not run yet: corrects, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 13 of 30 min used; a full run (~3 min; `--reps 2` ~6 min) still fits with a 3-minute margin.
