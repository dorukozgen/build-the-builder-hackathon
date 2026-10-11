# Benchmark brief-f · run 11

agent `cdfee81f-9cad-47fa-b5a2-297c730c58f1` · 2026-10-11 18:17:12 · 227 s · reps 1 · style none · `--only`

## Score

- generated 2/4 · total 2/4
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: none
- regressed: GEN-17, GEN-28
- still failing: none

## Statistics on this version

agent version created, run 11 · 4 of 63 cases have results, 4 results in all

- mean pass rate per case 50.0% · 95% CI 15.0–85.0% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 65/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 46 have none on this version yet
- Failing 2 · Flaky 0 · Mostly Passing 0 · Stable 2

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-17 (Happy path) fails every run (0/1) · rules brief-f:1, brief-f:2, brief-f:5, brief-f:9, brief-f:12, brief-f:19, brief-f:20, brief-f:29, brief-f:30
  - GEN-28 (Status enquiry) fails every run (0/1) · rules brief-f:5, brief-f:23, brief-f:29

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-17 | Happy path | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-28 | Status enquiry | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-21 | Unsupported | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-34 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | run 11 | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |  |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | ✓ |  |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | ✗ | flaky |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | ✓ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | not in this run |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ | – | not in this run |
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ | – | not in this run |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | not in this run |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | not in this run |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | not in this run |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | – | not in this run |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 2, not_closed 1, outcome 2
flags: hung_up 1, slow 3

## Failed cases

### GEN-17 — Damaged card replacement, no optional fields
Happy path · easy · fixture PUB-04 · rules brief-f:1, brief-f:2, brief-f:5, brief-f:9, brief-f:12, brief-f:19, brief-f:20, brief-f:29, brief-f:30

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- conversation: The agent successfully used the prescribed opening, identified the request as a card replacement before starting security verification, and addressed the customer as Ms Hoffmann only after verification. The agent also correctly read the application ID and status details digit by digit. However, the agent failed the closing criteria: there was no one-sentence summary of the actions and expectations
- tools: verify {"field": "date_of_birth", "answer": "1984-01-30"} > verify {"field": "phone_last4", "answer": "2219"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > create_application {"type": "card_replacement", "fields": {"reason": "damaged"}}
- slowest agent turn 17.4 s · ended customer-ended-call · transcript `results/bench/brief-f/run-11/GEN-17.md`

### GEN-28 — Status enquiry on an application in review
Status enquiry · easy · fixture PUB-01 · rules brief-f:5, brief-f:23, brief-f:29

- outcome ('no_action', 'out_of_scope'), expected ('status_given', None)
- conversation: The conversation failed to meet two of the success criteria: 1) The agent did not state that the application is 'being reviewed' (it was unable to find the application at all). 2) When the user asked 'When will I hear?', the agent responded with 'I do not have that information' instead of the required timeframe of 'within five business days'. Identity verification was correctly performed before ca
- tools: verify {"field": "date_of_birth", "answer": "1988-03-14"} > verify {"field": "phone_last4", "answer": "4471"} > get_application {"application_id": "APP482913"} ✖ > close_call {"reason": "out_of_scope", "outcome": "no_action"}
- tool errors: get_application → {"ok": false, "error": "unknown application_id"}
- slowest agent turn 22.1 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-11/GEN-28.md`

## Passed cases

- GEN-21 Wants a personal loan application, declines the transfer · 5 turns · close_call · slowest 12.6 s · `results/bench/brief-f/run-11/GEN-21.md`
- GEN-34 Lost card at the start of the call · 3 turns · transfer_to_agent > close_call · slowest 5.6 s · `results/bench/brief-f/run-11/GEN-34.md`

## Timing

median slowest agent turn 17 s · worst 22 s · failed calls where the customer hung up: 1 · **the agent was slow in this run; a re-run may score higher**
calls at a time: 5 in this run; next run 5 (the agent was slow (median slowest turn 17 s, 1 hang-up): halved)

## What this run suggests

- Regressions first: GEN-17, GEN-28 passed before and fail now. Fix, then `--only GEN-17,GEN-28`.
- Flaky: GEN-28 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-28`.
- Fix order on this version (section Statistics): P1 GEN-17, P1 GEN-28.
- The agent was slow in this run (median slowest turn 17 s). A call that ended in a hang-up may pass when re-run; re-run those before changing the workflow.
- Styles not run yet: asks_back, in_words, pieces, talkative. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 10 of 30 min used; a full run (~13 min; `--reps 2` ~26 min) still fits with a 3-minute margin.
