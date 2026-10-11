# Benchmark brief-f · run 21

agent `1956bd9e-4de1-44a5-be2b-a5052d9b4e9c` · 2026-10-11 19:38:11 · 97 s · reps 1 · style none · `--only`

## Score

- generated 2/3 · total 2/3
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-45
- regressed: none
- still failing: GEN-48

## Statistics on this version

agent version 4, run 21 · 3 of 63 cases have results, 3 results in all

- mean pass rate per case 66.7% · 95% CI 20.8–93.9% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 77/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 47 have none on this version yet
- Failing 1 · Flaky 0 · Mostly Passing 0 · Stable 2

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-48 (Style) fails every run (0/1) · rules brief-f:12, brief-f:16, brief-f:19

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-48 | Style | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-45 | Style | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-47 | Style | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | run 11 | run 12 | run 13 | run 14 | run 15 | run 16 | run 17 | run 18 | run 19 | run 20 | run 21 | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✗ | ✓ | flaky |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✗ | ✓ | – | – | – | ✗ | ✗ | ✗ | ✗ |  |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | ✓ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ | – | – | ✓ | ✓ | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | – | not in this run |
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | – | ✓ | – | ✓ | ✗ | ✓ | ✓ | – | not in this run |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | ✗ | ✗ | ✓ | – | not in this run |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✗ | ✓ | – | not in this run |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | ✗ | ✓ | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | – | ✓ | – | – | – | ✗ | ✗ | ✓ | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | ✓ | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | ✗ | ✗ | ✗ | ✗ | ✓ | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✗ | ✗ | ✓ | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✓ | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | ✓ | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | ✓ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 1, outcome 1

## Failed cases

### GEN-48 — Talkative address change
Style · medium · fixture PUB-01 · rules brief-f:12, brief-f:16, brief-f:19

- outcome ('no_action', 'out_of_scope'), expected ('application_created', None)
- conversation: The agent correctly asked for one field at a time, first requesting the date of birth and then the phone number digits. However, the user provided repetitive chatter instead of answering the second security question. Consequently, the conversation reached a 15-turn limit in the identity verification node and the agent terminated the call. Therefore, the requirement to read back the address 'Elm St
- applications [], expected ['address_change']
- tools: verify {"field": "date_of_birth", "answer": "1988-03-14"} > close_call {"reason": "out_of_scope", "outcome": "no_action"}
- slowest agent turn 1.4 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-21/GEN-48.md`

## Passed cases

- GEN-45 Postcode given in pieces · 22 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 7.5 s · `results/bench/brief-f/run-21/GEN-45.md`
- GEN-47 Asks why the birthday is needed · 21 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 1.4 s · `results/bench/brief-f/run-21/GEN-47.md`

## Timing

median slowest agent turn 1 s · worst 8 s · failed calls where the customer hung up: 0 · replies over 10 s: 0% · customers who hung up waiting: 0
calls at a time: 12 in this run; next run 12 (only 3 of 12 slots were in use: kept)

## What this run suggests

- Failing: GEN-48. Read their transcripts, fix, re-run `--only GEN-48`, then a full run for regressions.
- Flaky: GEN-45 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-45`.
- Fix order on this version (section Statistics): P1 GEN-48.
- Styles not run yet: in_words. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 23 of 30 min used; a full run takes ~10 min and does not fit with a 3-minute margin. `--only` on the 1 failing cases takes ~3 min and fits.
