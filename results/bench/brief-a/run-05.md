# Benchmark brief-a · run 5

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-11 00:08:53 · 182 s · reps 2 · style none · `--only`

## Score

- generated 1/2 · public 1/2 · total 2/4
- promised on passed cases: 637.50 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-19
- regressed: GEN-11, PUB-10
- still failing: none

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | |
|---|---|---|---|---|---|---|
| GEN-11 | ✓ | – | ✓ | – | ✗ |  |
| GEN-19 | ✓ | – | ✗ | ✗ | ✓ |  |
| PUB-06 | ✓ | – | ✓ | – | ✓ |  |
| PUB-10 | ✓ | – | ✗ | ✓ | ✗ | flaky |
| GEN-01 | ✓ | – | ✓ | – | – | not in this run |
| GEN-02 | ✓ | – | ✓ | – | – | not in this run |
| GEN-03 | ✓ | – | ✓ | – | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | – | – | not in this run |
| GEN-05 | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-06 | ✓ | – | ✓ | – | – | not in this run |
| GEN-07 | ✓ | – | ✓ | – | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | – | – | not in this run |
| GEN-09 | ✓ | – | ✓ | – | – | not in this run |
| GEN-10 | ✓ | – | ✓ | – | – | not in this run |
| GEN-12 | ✓ | – | ✓ | ✓ | – | not in this run |
| GEN-13 | ✓ | – | ✓ | ✓ | – | not in this run |
| GEN-14 | ✗ | ✓ | ✓ | – | – | not in this run |
| GEN-15 | ✓ | – | ✓ | – | – | not in this run |
| GEN-16 | ✓ | – | ✓ | – | – | not in this run |
| GEN-17 | ✓ | – | ✓ | – | – | not in this run |
| GEN-18 | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-20 | ✓ | – | ✓ | – | – | not in this run |
| GEN-21 | ✗ | ✗ | ✗ | ✓ | – | not in this run |
| GEN-22 | ✓ | – | ✓ | – | – | not in this run |
| PUB-01 | ✓ | – | ✓ | – | – | not in this run |
| PUB-02 | ✓ | – | ✓ | – | – | not in this run |
| PUB-03 | ✓ | – | ✓ | – | – | not in this run |
| PUB-04 | ✓ | – | ✓ | ✓ | – | not in this run |
| PUB-05 | ✓ | – | ✓ | – | – | not in this run |
| PUB-07 | ✓ | – | ✓ | ✓ | – | not in this run |
| PUB-08 | ✓ | – | ✓ | – | – | not in this run |
| PUB-09 | ✓ | – | ✓ | – | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 2

## Failed cases

### GEN-11 — Offers 50, accepts the floor next Monday
Amounts · hard · fixture PUB-06 · rules brief-a:24, brief-a:25, brief-a:26, brief-a:27, brief-a:22 · 0/2 reps passed

- conversation: The agent failed to satisfy the criterion: 'the agent says the rest stays overdue'. While the agent correctly requested the full amount of 2125.10 initially ([Message 6]), rejected the user's offer of 50 ([Message 8]), and provided a correct read-back of 637.50 for Monday 19 October ([Message 10]), it never informed the customer that the remaining balance would remain overdue after the partial pay
- tools: verify {"field": "date_of_birth", "answer": "1986-05-17"} > verify {"field": "phone_last4", "answer": "1502"} > get_account > promise {"date": "2026-10-19", "amount": 637.5, "product_id": "p1"} > close_call {"outcome": "promise"}
- slowest agent turn 1.5 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-05/GEN-11.md`

### PUB-10 — The promise service fails on the first call
Tool failure · hard · fixture PUB-10 · rules – · 0/2 reps passed

- conversation: The evaluation shows mixed results for the success criteria. 1. Exactly one promise in the ledger: This criterion was met. System Event 11 shows the first 'create_promise' attempt failed with a message that nothing was recorded, while System Event 13 shows the second attempt (the retry) was successful, resulting in exactly one promise. 2. Agent does not say 'recorded' before a successful call: Thi
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > get_account > promise {"date": "2026-10-16", "amount": 365, "product_id": "p1"} ✖ > promise {"date": "2026-10-16", "amount": 365, "product_id": "p1"} > close_call {"outcome": "promise"}
- tool errors: create_promise → {"ok": false, "error": "service unavailable, nothing was recorded"}
- slowest agent turn 2.6 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-05/PUB-10.md`

## Passed cases

- GEN-19 One wrong birth year, then too much and refuses the floor · 15 turns · verify_identity > verify_identity > verify_identity > get_account > close_call · slowest 1.0 s · `results/bench/brief-a/run-05/GEN-19.md`
- PUB-06 Full amount is too much, accepts the floor · 13 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.3 s · `results/bench/brief-a/run-05/PUB-06.md`

## Timing

median slowest agent turn 2 s · worst 3 s · failed calls where the customer hung up: 0

## What this run suggests

- Regressions first: GEN-11, PUB-10 passed before and fail now. Fix, then `--only GEN-11,PUB-10`.
- Flaky: PUB-10 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only PUB-10`.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 26 of 30 min used; a full run takes ~8 min and does not fit with a 3-minute margin. `--only` on a few cases may; otherwise finish.
