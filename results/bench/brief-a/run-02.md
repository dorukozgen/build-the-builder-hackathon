# Benchmark brief-a · run 2

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-10 23:54:16 · 138 s · reps 1 · style none · `--only`

## Score

- generated 5/6 · total 5/6
- promised on passed cases: 365.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-04, GEN-08, GEN-14
- regressed: none
- still failing: GEN-21

## History

| case | run 1 | run 2 | |
|---|---|---|---|
| GEN-04 | ✗ | ✓ |  |
| GEN-05 | ✓ | ✓ |  |
| GEN-08 | ✗ | ✓ |  |
| GEN-14 | ✗ | ✓ | changed |
| GEN-18 | ✓ | ✓ |  |
| GEN-21 | ✗ | ✗ | changed |
| GEN-01 | ✓ | – | not in this run |
| GEN-02 | ✓ | – | not in this run |
| GEN-03 | ✓ | – | not in this run |
| GEN-06 | ✓ | – | not in this run |
| GEN-07 | ✓ | – | not in this run |
| GEN-09 | ✓ | – | not in this run |
| GEN-10 | ✓ | – | not in this run |
| GEN-11 | ✓ | – | not in this run |
| GEN-12 | ✓ | – | not in this run |
| GEN-13 | ✓ | – | not in this run |
| GEN-15 | ✓ | – | not in this run |
| GEN-16 | ✓ | – | not in this run |
| GEN-17 | ✓ | – | not in this run |
| GEN-19 | ✓ | – | not in this run |
| GEN-20 | ✓ | – | not in this run |
| GEN-22 | ✓ | – | not in this run |
| PUB-01 | ✓ | – | not in this run |
| PUB-02 | ✓ | – | not in this run |
| PUB-03 | ✓ | – | not in this run |
| PUB-04 | ✓ | – | not in this run |
| PUB-05 | ✓ | – | not in this run |
| PUB-06 | ✓ | – | not in this run |
| PUB-07 | ✓ | – | not in this run |
| PUB-08 | ✓ | – | not in this run |
| PUB-09 | ✓ | – | not in this run |
| PUB-10 | ✓ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 1

## Failed cases

### GEN-21 — Wants 20 November, refuses the deadline and the Friday offer
Dates · hard · fixture PUB-01 · rules brief-a:23, brief-a:30, brief-a:31

- conversation: The agent failed to meet one of the required success criteria. Specifically, it did not propose Friday 16 October after the user refused the November 2nd date. While the agent correctly stated the latest date it could record was Monday 2 November [Message 10] and did not read back a promise for 20 November (it read back October 20 instead in [Message 8]), it ended the call [Message 12] immediately
- tools: verify {"field": "date_of_birth", "answer": "1988-03-14"} > verify {"field": "phone_last4", "answer": "4471"} > get_account > close_call {"reason": "refused", "outcome": "no_promise"}
- slowest agent turn 1.4 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-02/GEN-21.md`

## Passed cases

- GEN-04 Wrong number · 3 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-02/GEN-04.md`
- GEN-05 Mother says the customer has died · 3 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-02/GEN-05.md`
- GEN-08 Never confirms who he is · 5 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-02/GEN-08.md`
- GEN-14 Next Friday, asks about changing it later, service fails once · 13 turns · verify_identity > verify_identity > get_account > create_promise > create_promise > close_call · slowest 2.0 s · `results/bench/brief-a/run-02/GEN-14.md`
- GEN-18 Asks about interest, then twice does not want to talk · 15 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.9 s · `results/bench/brief-a/run-02/GEN-18.md`

## Timing

median slowest agent turn 1 s · worst 2 s · failed calls where the customer hung up: 0

## What this run suggests

- Failing: GEN-21. Read their transcripts, fix, re-run `--only GEN-21`, then a full run for regressions.
- Changed since the previous run: GEN-14, GEN-21. If a change weakened a check or an expectation, undo it unless the brief says the old version was wrong.
- Styles not run yet: asks_back, corrects, in_words, pieces. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 11 of 30 min used; a full run (~5 min; `--reps 2` ~10 min) still fits with a 3-minute margin.
