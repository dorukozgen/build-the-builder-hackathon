# Benchmark brief-f · run 27

agent `a0918965-0e6c-467f-910f-bf66efc8766f` · 2026-10-11 20:11:33 · 98 s · reps 1 · style none · `--only`

## Score

- generated 4/5 · total 4/5
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: none
- regressed: none
- still failing: GEN-10

## Statistics on this version

agent version created, run 27 · 5 of 63 cases have results, 5 results in all

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
| GEN-02 | Identity failure | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-17 | Happy path | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-21 | Unsupported | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-28 | Status enquiry | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | run 11 | run 12 | run 13 | run 14 | run 15 | run 16 | run 17 | run 18 | run 19 | run 20 | run 21 | run 22 | run 23 | run 24 | run 25 | run 26 | run 27 | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✗ | ✗ | ✗ |  |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | ✓ |  |
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | – | ✓ | – | ✓ | ✗ | ✓ | ✓ | – | ✓ | ✓ | – | ✓ | – | ✓ |  |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | ✓ |  |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | ✗ | ✓ | ✓ | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | – | ✓ | – | ✓ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | ✓ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ | – | – | ✓ | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | – | ✗ | ✓ | ✓ | – | ✓ | ✓ | – | ✓ | ✓ | – | not in this run |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | ✗ | ✗ | ✓ | – | – | ✓ | ✓ | – | – | – | not in this run |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | – | ✓ | – | – | – | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✗ | ✓ | – | not in this run |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | ✓ | – | not in this run |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | ✗ | ✗ | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✗ | ✗ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✗ | ✓ | – | ✓ | – | – | – | – | not in this run |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | ✓ | – | – | – | – | not in this run |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✗ | ✓ | – | – | – | ✗ | ✗ | ✗ | ✗ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | – | ✓ | – | – | not in this run |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 1

## Failed cases

### GEN-10 — Insists on speaking to a human after being offered help once
Human handoff · easy · fixture PUB-03 · rules brief-f:25, brief-f:29, brief-f:30

- conversation: While several criteria were met, the call failed on two specific points: 1. The agent claimed to be passing the call and said "Goodbye" in [Message 4] before the transfer_to_agent tool was even initiated or confirmed successful, which constitutes claiming success before the tool returns ok. 2. The close_call tool (api_call) was not the last tool call, as it was followed by the end_call function. O
- tools: transfer_to_agent {"queue": "general"} > close_call {"reason": "human", "outcome": "transferred"}
- slowest agent turn 3.3 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-27/GEN-10.md`

## Passed cases

- GEN-02 Limit increase, wrong date of birth twice, then a wrong phone number · 12 turns · verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 1.7 s · `results/bench/brief-f/run-27/GEN-02.md`
- GEN-17 Damaged card replacement, no optional fields · 16 turns · verify_identity > verify_identity > find_applications > find_applications > get_requirements > create_application > close_call · slowest 8.2 s · `results/bench/brief-f/run-27/GEN-17.md`
- GEN-21 Wants a personal loan application, declines the transfer · 5 turns · close_call · slowest 2.0 s · `results/bench/brief-f/run-27/GEN-21.md`
- GEN-28 Status enquiry on an application in review · 14 turns · verify_identity > verify_identity > get_application > close_call · slowest 4.7 s · `results/bench/brief-f/run-27/GEN-28.md`

## Timing

median slowest agent turn 3 s · worst 8 s · failed calls where the customer hung up: 0 · replies over 10 s: 0% · customers who hung up waiting: 0
calls at a time: 12 in this run; next run 12 (only 5 of 12 slots were in use: kept)

## What this run suggests

- Failing: GEN-10. Read their transcripts, fix, re-run `--only GEN-10`, then a full run for regressions.
- Fix order on this version (section Statistics): P1 GEN-10.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 3 of 30 min used; a full run (~8 min; `--reps 2` ~16 min) still fits with a 3-minute margin.
