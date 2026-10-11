# Benchmark brief-a · run 6

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-11 00:12:10 · 180 s · reps 2 · style none · `--only`

## Score

- generated 1/2 · public 0/1 · total 1/3
- promised on passed cases: 637.50 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-11
- regressed: GEN-14
- still failing: PUB-10

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | |
|---|---|---|---|---|---|---|---|
| GEN-11 | ✓ | – | ✓ | – | ✗ | ✓ | flaky |
| GEN-14 | ✗ | ✓ | ✓ | – | – | ✗ | flaky |
| PUB-10 | ✓ | – | ✗ | ✓ | ✗ | ✗ |  |
| GEN-01 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-02 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-03 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | – | – | – | not in this run |
| GEN-05 | ✓ | ✓ | ✓ | – | – | – | not in this run |
| GEN-06 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-07 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | – | – | – | not in this run |
| GEN-09 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-10 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-12 | ✓ | – | ✓ | ✓ | – | – | not in this run |
| GEN-13 | ✓ | – | ✓ | ✓ | – | – | not in this run |
| GEN-15 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-16 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-17 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-18 | ✓ | ✓ | ✓ | – | – | – | not in this run |
| GEN-19 | ✓ | – | ✗ | ✗ | ✓ | – | not in this run |
| GEN-20 | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-21 | ✗ | ✗ | ✗ | ✓ | – | – | not in this run |
| GEN-22 | ✓ | – | ✓ | – | – | – | not in this run |
| PUB-01 | ✓ | – | ✓ | – | – | – | not in this run |
| PUB-02 | ✓ | – | ✓ | – | – | – | not in this run |
| PUB-03 | ✓ | – | ✓ | – | – | – | not in this run |
| PUB-04 | ✓ | – | ✓ | ✓ | – | – | not in this run |
| PUB-05 | ✓ | – | ✓ | – | – | – | not in this run |
| PUB-06 | ✓ | – | ✓ | – | ✓ | – | not in this run |
| PUB-07 | ✓ | – | ✓ | ✓ | – | – | not in this run |
| PUB-08 | ✓ | – | ✓ | – | – | – | not in this run |
| PUB-09 | ✓ | – | ✓ | – | – | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 2

## Failed cases

### GEN-14 — Next Friday, asks about changing it later, service fails once
Tool failure · hard · fixture PUB-10 · rules brief-a:22, brief-a:37, brief-a:36 · 1/2 reps passed

- conversation: The evaluation is a failure because the agent used the word 'recorded' before the retry of the promise creation succeeded, which violates the specific negative constraint. This occurred in Message 0 ('This call is recorded') and Message 11 ('the promise is not recorded yet'). All other success criteria were met: the agent read back the date 'Friday 23 October' in Message 8, mentioned the mobile ap
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > get_account > promise {"date": "2026-10-23", "amount": 365, "product_id": "p1"} ✖ > promise {"date": "2026-10-23", "amount": 365, "product_id": "p1"} > close_call {"outcome": "promise"}
- tool errors: create_promise → {"ok": false, "error": "service unavailable, nothing was recorded"}
- slowest agent turn 2.6 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-06/GEN-14.md`

### PUB-10 — The promise service fails on the first call
Tool failure · hard · fixture PUB-10 · rules – · 0/2 reps passed

- conversation: The call successfully recorded exactly one promise after a retry. However, the agent violated the criterion to not say 'recorded' before a successful call. The word 'recorded' was used in Message 0 ('This call is recorded') and Message 12 ('the promise is not recorded yet') prior to the successful completion of the create_promise API call. The conversation ended correctly without a timeout or infi
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > get_account > promise {"date": "2026-10-16", "amount": 365, "product_id": "p1"} ✖ > promise {"date": "2026-10-16", "amount": 365, "product_id": "p1"} > close_call {"outcome": "promise"}
- tool errors: create_promise → {"ok": false, "error": "service unavailable, nothing was recorded"}
- slowest agent turn 4.7 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-06/PUB-10.md`

## Passed cases

- GEN-11 Offers 50, accepts the floor next Monday · 13 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 4.4 s · `results/bench/brief-a/run-06/GEN-11.md`

## Timing

median slowest agent turn 4 s · worst 5 s · failed calls where the customer hung up: 0

## What this run suggests

- Regressions first: GEN-14 passed before and fail now. Fix, then `--only GEN-14`.
- Failing: PUB-10. Read their transcripts, fix, re-run `--only PUB-10`, then a full run for regressions.
- Flaky: GEN-11, GEN-14 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-11,GEN-14`.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 29 of 30 min used; a full run takes ~8 min and does not fit with a 3-minute margin. `--only` on a few cases may; otherwise finish.
