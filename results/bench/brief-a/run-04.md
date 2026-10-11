# Benchmark brief-a · run 4

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-11 00:05:36 · 108 s · reps 1 · style none · `--only`

## Score

- generated 3/4 · public 3/3 · total 6/7
- promised on passed cases: 2535.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-21, PUB-10
- regressed: none
- still failing: GEN-19

## History

| case | run 1 | run 2 | run 3 | run 4 | |
|---|---|---|---|---|---|
| GEN-12 | ✓ | – | ✓ | ✓ |  |
| GEN-13 | ✓ | – | ✓ | ✓ |  |
| GEN-19 | ✓ | – | ✗ | ✗ | changed |
| GEN-21 | ✗ | ✗ | ✗ | ✓ |  |
| PUB-04 | ✓ | – | ✓ | ✓ |  |
| PUB-07 | ✓ | – | ✓ | ✓ |  |
| PUB-10 | ✓ | – | ✗ | ✓ | flaky |
| GEN-01 | ✓ | – | ✓ | – | not in this run |
| GEN-02 | ✓ | – | ✓ | – | not in this run |
| GEN-03 | ✓ | – | ✓ | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | – | not in this run |
| GEN-05 | ✓ | ✓ | ✓ | – | not in this run |
| GEN-06 | ✓ | – | ✓ | – | not in this run |
| GEN-07 | ✓ | – | ✓ | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | – | not in this run |
| GEN-09 | ✓ | – | ✓ | – | not in this run |
| GEN-10 | ✓ | – | ✓ | – | not in this run |
| GEN-11 | ✓ | – | ✓ | – | not in this run |
| GEN-14 | ✗ | ✓ | ✓ | – | not in this run |
| GEN-15 | ✓ | – | ✓ | – | not in this run |
| GEN-16 | ✓ | – | ✓ | – | not in this run |
| GEN-17 | ✓ | – | ✓ | – | not in this run |
| GEN-18 | ✓ | ✓ | ✓ | – | not in this run |
| GEN-20 | ✓ | – | ✓ | – | not in this run |
| GEN-22 | ✓ | – | ✓ | – | not in this run |
| PUB-01 | ✓ | – | ✓ | – | not in this run |
| PUB-02 | ✓ | – | ✓ | – | not in this run |
| PUB-03 | ✓ | – | ✓ | – | not in this run |
| PUB-05 | ✓ | – | ✓ | – | not in this run |
| PUB-06 | ✓ | – | ✓ | – | not in this run |
| PUB-08 | ✓ | – | ✓ | – | not in this run |
| PUB-09 | ✓ | – | ✓ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 1

## Failed cases

### GEN-19 — One wrong birth year, then too much and refuses the floor
Amounts · hard · fixture PUB-03 · rules brief-a:12, brief-a:26, brief-a:30, brief-a:31

- conversation: - The agent successfully asked for the date of birth again after an incorrect answer in [Message 4]. - The agent offered the minimum payment of 28.50 once in [Message 10]. - The persuasion attempt in [Message 12] proposed 95.00 instead of 28.50, violating the specific amount requirement. - The agent made a further offer in [Message 12] after the customer refused the minimum payment in [Message 11]
- tools: verify {"field": "date_of_birth", "answer": "1993-07-21"} > verify {"field": "date_of_birth", "answer": "1992-07-21"} > verify {"field": "phone_last4", "answer": "6630"} > get_account > close_call {"reason": "refused", "outcome": "no_promise"}
- slowest agent turn 3.7 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-04/GEN-19.md`

## Passed cases

- GEN-12 Partial amount on a Saturday, then changes the date at read-back · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.0 s · `results/bench/brief-a/run-04/GEN-12.md`
- GEN-13 Vague end of month twice, accepts the deadline · 17 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.2 s · `results/bench/brief-a/run-04/GEN-13.md`
- GEN-21 Wants 20 November, refuses the deadline and the Friday offer · 13 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.4 s · `results/bench/brief-a/run-04/GEN-21.md`
- PUB-04 Wants a date after the deadline · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.4 s · `results/bench/brief-a/run-04/PUB-04.md`
- PUB-07 A vague period, then a holiday · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.8 s · `results/bench/brief-a/run-04/PUB-07.md`
- PUB-10 The promise service fails on the first call · 12 turns · verify_identity > verify_identity > get_account > create_promise > create_promise > close_call · slowest 5.9 s · `results/bench/brief-a/run-04/PUB-10.md`

## Timing

median slowest agent turn 2 s · worst 6 s · failed calls where the customer hung up: 0

## What this run suggests

- Failing: GEN-19. Read their transcripts, fix, re-run `--only GEN-19`, then a full run for regressions.
- Flaky: PUB-10 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only PUB-10`.
- Changed since the previous run: GEN-19. If a change weakened a check or an expectation, undo it unless the brief says the old version was wrong.
- Styles not run yet: asks_back, corrects, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 23 of 30 min used; a full run takes ~8 min and does not fit with a 3-minute margin. `--only` on a few cases may; otherwise finish.
