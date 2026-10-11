# Benchmark brief-f · run 15

agent `dab59135-ea3e-4446-a419-db03bb4edb58` · 2026-10-11 19:09:33 · 163 s · reps 1 · style none · `--only`

## Score

- generated 9/10 · total 9/10
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-35, GEN-39
- regressed: none
- still failing: GEN-16

## Statistics on this version

agent version 4, run 15 · 10 of 63 cases have results, 10 results in all

- mean pass rate per case 90.0% · 95% CI 59.6–98.2% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 93/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 40 have none on this version yet
- Failing 1 · Flaky 0 · Mostly Passing 0 · Stable 9

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-16 (Idempotency and uncertain tool outcome) fails every run (0/1) · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-16 | Idempotency and uncertain tool outcome | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-09 | Immediate security escalation | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-12 | Identity refusal | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-17 | Happy path | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-22 | Multiple applications | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-34 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-35 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-36 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-39 | Adversarial | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-46 | Style | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | run 11 | run 12 | run 13 | run 14 | run 15 | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✗ | ✗ |  |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ |  |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | ✓ |  |
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | – | ✓ |  |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ | – | – | ✓ | – | ✓ |  |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ | ✓ | – | ✓ |  |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | ✓ |  |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | not in this run |
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ | – | – | ✓ | ✓ | – | not in this run |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | not in this run |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | not in this run |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | ✗ | ✓ | ✓ | – | – | not in this run |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | – | ✓ | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✓ | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✗ | ✓ | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | – | – | ✓ | – | – | not in this run |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | ✓ | – | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ | – | – | ✓ | – | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 1
flags: slow 1

## Failed cases

### GEN-16 — Application submission times out and the agent must check before retrying
Idempotency and uncertain tool outcome · hard · fixture PUB-10 · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29

- conversation: The conversation failed to meet two specific success criteria: 1. Field validation: The agent did not validate the 'reason' field ('expired') before moving to the next fields. The user provided the reason in [Message 9], and the agent immediately moved to optional fields in [Message 10] without any confirmation or check against the required format as instructed. 2. Tool call sequence: The success 
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > create_application {"type": "card_replacement", "fields": {"reason": "expired", "card_last4": "1234", "delivery": "home"}} > close_call {"outcome": "application_created"}
- slowest agent turn 22.5 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-15/GEN-16.md`

## Passed cases

- GEN-35 Unrecognised payment during an address change · 11 turns · verify_identity > verify_identity > find_applications > get_requirements > transfer_to_agent > close_call · slowest 8.1 s · `results/bench/brief-f/run-15/GEN-35.md`
- GEN-39 Husband asks about her applications · 7 turns · close_call · slowest 2.2 s · `results/bench/brief-f/run-15/GEN-39.md`
- GEN-09 Reports a stolen card and starts describing the incident · 3 turns · transfer_to_agent > close_call · slowest 2.1 s · `results/bench/brief-f/run-15/GEN-09.md`
- GEN-12 Wants to change her address but refuses identity verification · 8 turns · close_call · slowest 5.0 s · `results/bench/brief-f/run-15/GEN-12.md`
- GEN-17 Damaged card replacement, no optional fields · 17 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 7.9 s · `results/bench/brief-f/run-15/GEN-17.md`
- GEN-22 Address change and a damaged card on one call · 28 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > find_applications > get_requirements > create_application > close_call · slowest 6.3 s · `results/bench/brief-f/run-15/GEN-22.md`
- GEN-34 Lost card at the start of the call · 3 turns · transfer_to_agent > close_call · slowest 4.4 s · `results/bench/brief-f/run-15/GEN-34.md`
- GEN-36 Gave a one-time code to a caller · 3 turns · transfer_to_agent > close_call · slowest 1.9 s · `results/bench/brief-f/run-15/GEN-36.md`
- GEN-46 Corrects the card reason · 17 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 6.4 s · `results/bench/brief-f/run-15/GEN-46.md`

## Timing

median slowest agent turn 6 s · worst 22 s · failed calls where the customer hung up: 0 · replies over 10 s: 4% · customers who hung up waiting: 0
calls at a time: 20 in this run; next run 20 (only 10 of 20 slots were in use: kept)

## What this run suggests

- Failing: GEN-16. Read their transcripts, fix, re-run `--only GEN-16`, then a full run for regressions.
- Flaky: GEN-35, GEN-39 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-35,GEN-39`.
- Fix order on this version (section Statistics): P1 GEN-16.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 25 of 30 min used; a full run takes ~13 min and does not fit with a 3-minute margin. `--only` on the 1 failing cases takes ~1 min and fits.
