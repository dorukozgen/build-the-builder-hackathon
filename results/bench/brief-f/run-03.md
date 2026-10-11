# Benchmark brief-f · run 3

agent `9b1b1617-e7e7-48bd-bc0d-7c61b1a79678` · 2026-10-11 02:30:55 · 245 s · reps 2 · style none

## Score

- generated 8/8 · total 8/8
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: none
- regressed: none
- still failing: none

## History

| case | run 1 | run 2 | run 3 | |
|---|---|---|---|---|
| GEN-01 | ✓ | – | ✓ |  |
| GEN-02 | ✓ | – | ✓ |  |
| GEN-03 | ✓ | – | ✓ |  |
| GEN-04 | ✗ | ✓ | ✓ |  |
| GEN-05 | ✓ | – | ✓ |  |
| GEN-06 | ✗ | ✓ | ✓ |  |
| GEN-07 | ✓ | – | ✓ |  |
| GEN-08 | ✗ | ✓ | ✓ |  |

## Rule coverage

rules cited by no case: brief-f:3, brief-f:4, brief-f:9, brief-f:10, brief-f:11, brief-f:12, brief-f:13, brief-f:14, brief-f:17, brief-f:18, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:23, brief-f:24, brief-f:27

## Failure categories

none

## Failed cases

none

## Passed cases

- GEN-01 Wants an address change, refuses the security questions twice · 7 turns · close_call · slowest 0.4 s · `results/bench/brief-f/run-03/GEN-01.md`
- GEN-02 Limit increase, wrong date of birth twice, then a wrong phone number · 11 turns · verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 4.2 s · `results/bench/brief-f/run-03/GEN-02.md`
- GEN-03 Damaged card, date of birth with month and day swapped, then wrong phone digits · 13 turns · verify_identity > verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 7.6 s · `results/bench/brief-f/run-03/GEN-03.md`
- GEN-04 Asks for his balance, accepts the transfer · 5 turns · transfer_to_agent > close_call · slowest 4.3 s · `results/bench/brief-f/run-03/GEN-04.md`
- GEN-05 Wants a person, insists · 5 turns · transfer_to_agent > close_call · slowest 1.1 s · `results/bench/brief-f/run-03/GEN-05.md`
- GEN-06 Asks the fee and whether it is approved at once, then fails the date of birth three times · 9 turns · verify_identity > verify_identity > verify_identity > close_call · slowest 5.6 s · `results/bench/brief-f/run-03/GEN-06.md`
- GEN-07 Address change, gives the date of birth, refuses the phone digits · 9 turns · verify_identity > close_call · slowest 4.6 s · `results/bench/brief-f/run-03/GEN-07.md`
- GEN-08 Limit increase, asks his current limit and the decision, then insists on a person · 9 turns · transfer_to_agent > close_call · slowest 5.2 s · `results/bench/brief-f/run-03/GEN-08.md`

## Timing

median slowest agent turn 5 s · worst 8 s · failed calls where the customer hung up: 0

## What this run suggests

- Everything passed once. One pass is a hint, not proof: run again (`--reps 2`, or a `--style` run) if the clock allows.
- Styles not run yet: corrects, pieces. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 17 of 30 min used; a full run (~2 min; `--reps 2` ~4 min) still fits with a 3-minute margin.
