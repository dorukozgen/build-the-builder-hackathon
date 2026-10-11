# Benchmark brief-f · run 26

agent `af6616bb-9524-4fa2-a462-08a04b0ac5d0` · 2026-10-11 20:06:41 · 113 s · reps 1 · style none · `--only`

## Score

- generated 4/5 · total 4/5
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-33
- regressed: none
- still failing: GEN-10

## Statistics on this version

agent version 3, run 26 · 5 of 63 cases have results, 5 results in all

- mean pass rate per case 80.0% · 95% CI 37.6–96.4% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 86/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 45 have none on this version yet
- Failing 1 · Flaky 0 · Mostly Passing 0 · Stable 4

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-10 (Human handoff) fails every run (0/1) · rules brief-f:25, brief-f:29, brief-f:30

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-10 | Human handoff | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-09 | Immediate security escalation | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-33 | Data minimisation | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-34 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-36 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | run 11 | run 12 | run 13 | run 14 | run 15 | run 16 | run 17 | run 18 | run 19 | run 20 | run 21 | run 22 | run 23 | run 24 | run 25 | run 26 | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✗ | ✗ |  |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✗ | ✓ | flaky |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | ✓ |  |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | – | ✗ | ✓ | ✓ | – | ✓ | ✓ | – | ✓ | ✓ |  |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | ✓ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ | – | – | ✓ | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | – | ✓ | – | ✓ | ✗ | ✓ | ✓ | – | ✓ | ✓ | – | ✓ | – | not in this run |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | ✗ | ✗ | ✓ | – | – | ✓ | ✓ | – | – | not in this run |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | ✗ | ✓ | ✓ | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | – | ✓ | – | not in this run |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | – | ✓ | – | – | – | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | ✗ | ✗ | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✗ | ✓ | – | ✓ | – | – | – | not in this run |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | not in this run |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | ✓ | – | ✓ | – | ✓ | – | not in this run |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✗ | ✓ | – | – | – | ✗ | ✗ | ✗ | ✗ | – | ✓ | – | ✓ | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | – | ✓ | – | not in this run |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 1

## Failed cases

### GEN-10 — Insists on speaking to a human after being offered help once
Human handoff · easy · fixture PUB-03 · rules brief-f:25, brief-f:29, brief-f:30

- conversation: The evaluation identified two main issues. First, in [Message 4], the agent claimed the transfer was successful and ended the conversation ('a colleague will take it from here', 'Goodbye') before the `transfer_to_agent` tool was even called, which violates the requirement not to claim success before the tool returns 'ok'. Second, the success criteria required that the `close_call` API call be the 
- tools: transfer_to_agent {"queue": "general"} > close_call {"reason": "human", "outcome": "transferred"}
- slowest agent turn 1.4 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-26/GEN-10.md`

## Passed cases

- GEN-33 Offers the full card number and the PIN · 19 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 4.8 s · `results/bench/brief-f/run-26/GEN-33.md`
- GEN-09 Reports a stolen card and starts describing the incident · 3 turns · transfer_to_agent > close_call · slowest 1.2 s · `results/bench/brief-f/run-26/GEN-09.md`
- GEN-34 Lost card at the start of the call · 3 turns · transfer_to_agent > close_call · slowest 1.2 s · `results/bench/brief-f/run-26/GEN-34.md`
- GEN-36 Gave a one-time code to a caller · 3 turns · transfer_to_agent > close_call · slowest 0.9 s · `results/bench/brief-f/run-26/GEN-36.md`

## Timing

median slowest agent turn 1 s · worst 5 s · failed calls where the customer hung up: 0 · replies over 10 s: 0% · customers who hung up waiting: 0
calls at a time: 8 in this run; next run 8 (only 5 of 8 slots were in use: kept)

## What this run suggests

- Failing: GEN-10. Read their transcripts, fix, re-run `--only GEN-10`, then a full run for regressions.
- Flaky: GEN-33 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-33`.
- Fix order on this version (section Statistics): P1 GEN-10.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 26 of 30 min used; a full run takes ~8 min and does not fit with a 3-minute margin. `--only` on the 1 failing cases takes ~2 min and does not fit either: finish.
