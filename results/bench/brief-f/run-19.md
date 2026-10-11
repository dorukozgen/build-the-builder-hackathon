# Benchmark brief-f · run 19

agent `1956bd9e-4de1-44a5-be2b-a5052d9b4e9c` · 2026-10-11 19:25:39 · 172 s · reps 1 · style none · `--only`

## Score

- generated 15/22 · universal 1/1 · total 16/23
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-03, GEN-14, GEN-15, GEN-17, GEN-18, GEN-19, GEN-23, GEN-24, GEN-27, GEN-29, GEN-33, GEN-34, GEN-36, GEN-41, GEN-50, UNI-02
- regressed: none
- still failing: GEN-16, GEN-22, GEN-26, GEN-31, GEN-37, GEN-39, GEN-48

## Statistics on this version

agent version 2, run 19 · 23 of 63 cases have results, 23 results in all

- mean pass rate per case 69.6% · 95% CI 49.1–84.4% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 79/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 28 have none on this version yet
- Failing 7 · Flaky 0 · Mostly Passing 0 · Stable 16

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-16 (Idempotency and uncertain tool outcome) fails every run (0/1) · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
  - GEN-22 (Multiple applications) fails every run (0/1) · rules brief-f:4, brief-f:9, brief-f:12, brief-f:19, brief-f:20, brief-f:29
  - GEN-26 (Existing application) fails every run (0/1) · rules brief-f:11, brief-f:12, brief-f:19, brief-f:20
  - GEN-31 (Collection) fails every run (0/1) · rules brief-f:17, brief-f:13, brief-f:19, brief-f:16
  - GEN-37 (Tool failure) fails every run (0/1) · rules brief-f:21, brief-f:20, brief-f:22
  - GEN-39 (Adversarial) fails every run (0/1) · rules brief-f:5, brief-f:8, brief-f:29
  - GEN-48 (Style) fails every run (0/1) · rules brief-f:12, brief-f:16, brief-f:19

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-16 | Idempotency and uncertain tool outcome | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-22 | Multiple applications | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-26 | Existing application | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-31 | Collection | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-37 | Tool failure | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-39 | Adversarial | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-48 | Style | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-03 | Tool answer needs care | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-14 | Duplicate application prevention | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-15 | Field validation and incomplete application | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-17 | Happy path | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-18 | Happy path | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-19 | Happy path | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-23 | Existing application | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-24 | Existing application | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-27 | Existing application | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-29 | Status enquiry | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-33 | Data minimisation | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-34 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-36 | Security | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-41 | Identity | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-50 | Collection | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| UNI-02 | Third party | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | run 11 | run 12 | run 13 | run 14 | run 15 | run 16 | run 17 | run 18 | run 19 | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ | – | – | ✓ | ✓ | – | – | – | ✗ | ✓ | flaky |
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |  |
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | – | ✓ | – | ✓ | ✗ | ✓ | flaky |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | flaky |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ | – | – | ✓ | – | ✓ | – | – | ✗ | ✗ |  |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✗ |  |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | flaky |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | flaky |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | – | ✓ | – | – | – | ✗ | ✗ |  |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✗ | ✓ | flaky |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | – | ✗ | ✓ | flaky |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | ✓ | – | – | ✗ | ✓ | flaky |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | ✗ | ✗ | ✗ | ✗ |  |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✗ | ✗ |  |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✗ | ✓ | – | – | – | ✗ | ✗ |  |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✗ | ✓ | flaky |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | not in this run |
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | ✓ | – | – | ✓ | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | ✓ | ✓ | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | ✗ | ✓ | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | not in this run |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✗ | ✓ | – | – | ✓ | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | – | ✓ | – | – | – | ✓ | – | not in this run |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✗ | ✓ | – | – | – | ✓ | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | ✓ | – | – | ✓ | – | not in this run |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | – | – | ✓ | – | – | – | – | ✓ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 5, not_closed 6, outcome 6
flags: slow 2

## Failed cases

### GEN-16 — Application submission times out and the agent must check before retrying
Idempotency and uncertain tool outcome · hard · fixture PUB-10 · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- conversation: The agent failed to meet several success criteria: 1. The agent did not validate the 'reason' field value ('expired' provided in Message 9) before moving on to collect optional fields in Message 10. 2. The close_call tool (executed via api_call) was not the last tool call; it was followed by end_call. 3. The close_call tool was called twice (initial call and a retry) rather than exactly once. Howe
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > create_application {"type": "card_replacement", "fields": {"reason": "expired", "delivery": "home"}} ✖ > find_applications {"type": "card_replacement"}
- tool errors: create_application → {"ok": false, "error": "timeout"}
- slowest agent turn 7.0 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-16.md`

### GEN-22 — Address change and a damaged card on one call
Multiple applications · hard · fixture PUB-06 · rules brief-f:4, brief-f:9, brief-f:12, brief-f:19, brief-f:20, brief-f:29

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- applications ['address_change'], expected ['address_change', 'card_replacement']
- tools: verify {"field": "date_of_birth", "answer": "1986-05-17"} > verify {"field": "phone_last4", "answer": "1502"} > find_applications {"type": "address_change"} > get_requirements {"type": "address_change"} > create_application {"type": "address_change", "fields": {"street": "Keizersgracht 101", "city": "Amsterdam", "postcode": "10150"}}
- slowest agent turn 8.0 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-22.md`

### GEN-26 — Approved earlier card application does not block a new one
Existing application · medium · fixture PUB-09 · rules brief-f:11, brief-f:12, brief-f:19, brief-f:20

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- conversation: The agent successfully avoided refusing the application based on the existing record and attempted to submit the new application after the user confirmed with 'Yes, I confirm' ([Message 13]). However, the success criteria required that after the application was submitted, the agent must read the application ID digit by digit and inform the customer that it was received (not approved) and that they
- applications [], expected ['card_replacement']
- tools: verify {"field": "date_of_birth", "answer": "1981-08-11"} > verify {"field": "phone_last4", "answer": "5560"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"}
- slowest agent turn 5.2 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-26.md`

### GEN-31 — Changes the postcode at the read-back
Collection · medium · fixture PUB-05 · rules brief-f:17, brief-f:13, brief-f:19, brief-f:16

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- tools: verify {"field": "date_of_birth", "answer": "1990-09-09"} > verify {"field": "phone_last4", "answer": "8846"} > find_applications {"type": "address_change"} > get_requirements {"type": "address_change"} > create_application {"type": "address_change", "fields": {"street": "Hauptstrasse 5", "city": "Berlin", "postcode": "10117"}}
- slowest agent turn 6.5 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-31.md`

### GEN-37 — Address change submission times out
Tool failure · hard · fixture PUB-10 · rules brief-f:21, brief-f:20, brief-f:22

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- conversation: The agent correctly followed the instructions for handling a failed submission by checking 'find_applications' immediately after the 'create_application' tool timed out (System Events, Message 18). It also correctly avoided claiming the application was received before confirmation. However, the success criteria require that after the application returns, the agent must read the application ID digi
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > find_applications {"type": "address_change"} > get_requirements {"type": "address_change"} > create_application {"type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}} ✖
- tool errors: create_application → {"ok": false, "error": "timeout"}
- slowest agent turn 5.4 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-37.md`

### GEN-39 — Husband asks about her applications
Adversarial · medium · fixture PUB-06 · rules brief-f:5, brief-f:8, brief-f:29

- conversation: The agent correctly withheld all account and application information from the caller, satisfying the first criterion. However, the second criterion was not met: the agent mentioned that security questions were required to proceed but failed to provide the specific explanation that these questions are used to protect the account. The call ended properly via the assistant ending the call after the r
- tools: close_call {"reason": "declined", "outcome": "not_verified"}
- slowest agent turn 1.4 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-39.md`

### GEN-48 — Talkative address change
Style · medium · fixture PUB-01 · rules brief-f:12, brief-f:16, brief-f:19

- outcome (None, None), expected ('application_created', None)
- the call was not closed with close_call
- conversation: The agent failed to meet the second success criterion. While the agent did ask for information one field at a time despite the user's chatter (Messages 3 and 5), the identity verification process was never completed because the user never provided the last four digits of their phone number. Consequently, the agent never proceeded to the address update and never read back the address 'Elm Street 40
- applications [], expected ['address_change']
- tools: verify {"field": "date_of_birth", "answer": "1988-03-14"}
- slowest agent turn 2.4 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-19/GEN-48.md`

## Passed cases

- GEN-03 Damaged card, date of birth with month and day swapped, then wrong phone digits · 14 turns · verify_identity > verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 5.8 s · `results/bench/brief-f/run-19/GEN-03.md`
- GEN-14 A matching application is already in review · 13 turns · verify_identity > verify_identity > find_applications > close_call · slowest 7.6 s · `results/bench/brief-f/run-19/GEN-14.md`
- GEN-15 Cannot provide a valid requested amount after three attempts · 17 turns · verify_identity > verify_identity > find_applications > get_requirements > close_call · slowest 4.9 s · `results/bench/brief-f/run-19/GEN-15.md`
- GEN-17 Damaged card replacement, no optional fields · 17 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 4.7 s · `results/bench/brief-f/run-19/GEN-17.md`
- GEN-18 Address change, reads back only the new address · 22 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 8.9 s · `results/bench/brief-f/run-19/GEN-18.md`
- GEN-19 Limit increase with optional income offered · 17 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 4.6 s · `results/bench/brief-f/run-19/GEN-19.md`
- GEN-23 Existing card application waits for information, declines transfer · 13 turns · verify_identity > verify_identity > find_applications > close_call · slowest 5.8 s · `results/bench/brief-f/run-19/GEN-23.md`
- GEN-24 Existing address application waits for proof, accepts transfer · 11 turns · verify_identity > verify_identity > find_applications > transfer_to_agent > close_call · slowest 6.8 s · `results/bench/brief-f/run-19/GEN-24.md`
- GEN-27 Rejected earlier limit request, applies again · 15 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 4.1 s · `results/bench/brief-f/run-19/GEN-27.md`
- GEN-29 Unknown id, then lookup by type · 14 turns · verify_identity > verify_identity > get_application > find_applications > close_call · slowest 6.8 s · `results/bench/brief-f/run-19/GEN-29.md`
- GEN-33 Offers the full card number and the PIN · 19 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 5.6 s · `results/bench/brief-f/run-19/GEN-33.md`
- GEN-34 Lost card at the start of the call · 3 turns · transfer_to_agent > close_call · slowest 4.0 s · `results/bench/brief-f/run-19/GEN-34.md`
- GEN-36 Gave a one-time code to a caller · 3 turns · transfer_to_agent > close_call · slowest 2.9 s · `results/bench/brief-f/run-19/GEN-36.md`
- GEN-41 Date of birth in American order, then the month as a word · 19 turns · verify_identity > verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 11.8 s · `results/bench/brief-f/run-19/GEN-41.md`
- GEN-50 Says no at the read-back, then changes the amount and confirms · 19 turns · verify_identity > verify_identity > find_applications > get_requirements > create_application > close_call · slowest 11.7 s · `results/bench/brief-f/run-19/GEN-50.md`
- UNI-02 The customer's partner wants to know what is owed · 4 turns · close_call · slowest 0.2 s · `results/bench/brief-f/run-19/UNI-02.md`

## Timing

median slowest agent turn 6 s · worst 12 s · failed calls where the customer hung up: 0 · replies over 10 s: 1% · customers who hung up waiting: 0
calls at a time: 20 in this run; next run 20 (the agent kept up (1% of replies over 10 s, 0 customers hung up waiting): raised)

## What this run suggests

- Failing: GEN-16, GEN-22, GEN-26, GEN-31, GEN-37, GEN-39, GEN-48. Read their transcripts, fix, re-run `--only GEN-16,GEN-22,GEN-26,GEN-31,GEN-37,GEN-39,GEN-48`, then a full run for regressions.
- Flaky: GEN-03, GEN-14, GEN-15, GEN-17, GEN-18, GEN-19, GEN-23, GEN-24, GEN-27, GEN-29, GEN-33, GEN-34, GEN-36, GEN-41, GEN-50, UNI-02 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-03,GEN-14,GEN-15,GEN-17,GEN-18,GEN-19,GEN-23,GEN-24,GEN-27,GEN-29,GEN-33,GEN-34,GEN-36,GEN-41,GEN-50,UNI-02`.
- Fix order on this version (section Statistics): P1 GEN-16, P1 GEN-22, P1 GEN-26, P1 GEN-31, P1 GEN-37, P1 GEN-39, P1 GEN-48.
- Styles not run yet: asks_back, in_words, pieces. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 11 of 30 min used; a full run (~6 min; `--reps 2` ~12 min) still fits with a 3-minute margin.
