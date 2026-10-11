# Benchmark brief-f · run 6

agent `30fd33bc-25d5-48c1-8960-95c961aff499` · 2026-10-11 17:02:06 · 101 s · reps 1 · style none · `--only`

## Score

- generated 1/3 · total 1/3
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: none
- regressed: GEN-14
- still failing: none

## Statistics on this version

agent version 2, run 6 · 3 of 63 cases have results, 3 results in all

- mean pass rate per case 33.3% · 95% CI 6.1–79.2% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 53/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 47 have none on this version yet
- Failing 2 · Flaky 0 · Mostly Passing 0 · Stable 1

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-14 (Duplicate application prevention) fails every run (0/1) · rules brief-f:5, brief-f:9, brief-f:11, brief-f:29
  - GEN-17 (Happy path) fails every run (0/1) · rules brief-f:1, brief-f:2, brief-f:5, brief-f:9, brief-f:12, brief-f:19, brief-f:20, brief-f:29, brief-f:30

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-14 | Duplicate application prevention | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-17 | Happy path | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-34 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | |
|---|---|---|---|---|---|---|---|
| GEN-14 | – | – | – | – | ✓ | ✗ |  |
| GEN-17 | – | – | – | – | – | ✗ |  |
| GEN-34 | – | – | – | – | – | ✓ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | not in this run |
| GEN-09 | – | – | – | – | ✗ | – | not in this run |
| GEN-10 | – | – | – | – | ✓ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | not in this run |
| GEN-12 | – | – | – | – | ✓ | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | not in this run |
| GEN-15 | – | – | – | – | ✗ | – | not in this run |
| GEN-16 | – | – | – | – | ✗ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 2
flags: slow 1

## Failed cases

### GEN-14 — A matching application is already in review
Duplicate application prevention · hard · fixture PUB-08 · rules brief-f:5, brief-f:9, brief-f:11, brief-f:29

- conversation: The agent failed to meet several success criteria related to the call's conclusion. Specifically: 1) The agent did not thank the customer and say goodbye before calling the `close_call` tool; the conversation ended abruptly after the user's final message. 2) The `close_call` tool was not the last tool call, as it was followed by the `end_call` tool. The agent correctly performed identity verificat
- tools: verify {"field": "date_of_birth", "answer": "1993-04-28"} > verify {"field": "phone_last4", "answer": "3317"} > find_applications {"type": "limit_increase"} > find_applications {"type": "limit_increase"} > close_call {"outcome": "status_given"}
- slowest agent turn 13.2 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-06/GEN-14.md`

### GEN-17 — Damaged card replacement, no optional fields
Happy path · easy · fixture PUB-04 · rules brief-f:1, brief-f:2, brief-f:5, brief-f:9, brief-f:12, brief-f:19, brief-f:20, brief-f:29, brief-f:30

- conversation: The agent failed to meet the closing criteria. Specifically, the agent did not provide a single-sentence summary of what was done and what the customer can expect, and failed to thank the customer or say goodbye before the call was terminated. The transcript shows the agent stopped talking after the user's final response in Message 20, leading directly to the close_call and end_call events without
- tools: verify {"field": "date_of_birth", "answer": "1984-01-30"} > verify {"field": "phone_last4", "answer": "2219"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > create_application {"type": "card_replacement", "fields": {"reason": "damaged", "delivery": "home"}} > close_call {"outcome": "application_created"}
- slowest agent turn 6.5 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-06/GEN-17.md`

## Passed cases

- GEN-34 Lost card at the start of the call · 4 turns · transfer_to_agent > close_call · slowest 0.6 s · `results/bench/brief-f/run-06/GEN-34.md`

## Timing

median slowest agent turn 6 s · worst 13 s · failed calls where the customer hung up: 0

## What this run suggests

- Regressions first: GEN-14 passed before and fail now. Fix, then `--only GEN-14`.
- Failing: GEN-17. Read their transcripts, fix, re-run `--only GEN-17`, then a full run for regressions.
- Fix order on this version (section Statistics): P1 GEN-14, P1 GEN-17.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 9 of 30 min used; a full run (~5 min; `--reps 2` ~9 min) still fits with a 3-minute margin.
