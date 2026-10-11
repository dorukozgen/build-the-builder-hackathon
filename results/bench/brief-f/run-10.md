# Benchmark brief-f · run 10

agent `62f52978-81f5-4dfe-8c39-7f68b54b6b8a` · 2026-10-11 18:07:16 · 550 s · reps 1 · style none · `--only`

## Score

- generated 6/16 · universal 0/1 · total 6/17
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: GEN-05, GEN-08, GEN-31, GEN-50
- regressed: none
- still failing: GEN-06, GEN-10, GEN-12, GEN-14, GEN-15, GEN-16, GEN-30, GEN-37, GEN-42, GEN-45, UNI-09

## Statistics on this version

agent version 3, run 10 · 17 of 63 cases have results, 17 results in all

- mean pass rate per case 35.3% · 95% CI 17.3–58.7% for all results taken together
- flakiness 0.00 on average (0: every run of a case agrees) · stability 100/100 · robustness 55/100 (0.7 × pass rate + 0.3 × stability)
- hidden-brief estimate: needs results for every case; 34 have none on this version yet
- Failing 11 · Flaky 0 · Mostly Passing 0 · Stable 6

Fix order:

- P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong
  - GEN-06 (Question outside the tools) fails every run (0/1) · rules brief-f:28, brief-f:6, brief-f:2
  - GEN-10 (Human handoff) fails every run (0/1) · rules brief-f:25, brief-f:29, brief-f:30
  - GEN-12 (Identity refusal) fails every run (0/1) · rules brief-f:2, brief-f:5, brief-f:8, brief-f:29
  - GEN-14 (Duplicate application prevention) fails every run (0/1) · rules brief-f:5, brief-f:9, brief-f:11, brief-f:29
  - GEN-15 (Field validation and incomplete application) fails every run (0/1) · rules brief-f:12, brief-f:13, brief-f:14, brief-f:15, brief-f:29
  - GEN-16 (Idempotency and uncertain tool outcome) fails every run (0/1) · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
  - GEN-30 (Status enquiry) fails every run (0/1) · rules brief-f:23, brief-f:28
  - GEN-37 (Tool failure) fails every run (0/1) · rules brief-f:21, brief-f:20, brief-f:22
  - GEN-42 (Collection) fails every run (0/1) · rules brief-f:13, brief-f:29
  - GEN-45 (Style) fails every run (0/1) · rules brief-f:12, brief-f:13, brief-f:16
  - UNI-09 (Honesty) fails every run (0/1) · rules knowledge:9.3, knowledge:9.5

| case | family | passes | 95% CI | flakiness | 3 of 3 | category |
|---|---|---|---|---|---|---|
| GEN-06 | Question outside the tools | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-10 | Human handoff | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-12 | Identity refusal | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-14 | Duplicate application prevention | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-15 | Field validation and incomplete application | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-16 | Idempotency and uncertain tool outcome | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-30 | Status enquiry | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-37 | Tool failure | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-42 | Collection | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-45 | Style | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| UNI-09 | Honesty | 0/1 (0%) | 0–79% | 0.00 | 0% | Failing P1 |
| GEN-05 | Human handoff | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-08 | Customer insists | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-17 | Happy path | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-22 | Multiple applications | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-31 | Collection | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |
| GEN-50 | Collection | 1/1 (100%) | 21–100% | 0.00 | 100% | Stable |

## History

| case | run 1 | run 2 | run 3 | run 4 | run 5 | run 6 | run 7 | run 8 | run 9 | run 10 | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GEN-05 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | flaky |
| GEN-06 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✗ | ✗ |  |
| GEN-08 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✓ | – | ✗ | ✓ | flaky |
| GEN-10 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ |  |
| GEN-12 | – | – | – | – | ✓ | – | ✗ | – | ✗ | ✗ |  |
| GEN-14 | – | – | – | – | ✓ | ✗ | ✗ | – | ✗ | ✗ |  |
| GEN-15 | – | – | – | – | ✗ | – | ✓ | – | ✗ | ✗ |  |
| GEN-16 | – | – | – | – | ✗ | – | ✗ | – | ✗ | ✗ |  |
| GEN-17 | – | – | – | – | – | ✗ | ✓ | ✓ | ✓ | ✓ |  |
| GEN-22 | – | – | – | – | – | – | ✓ | – | ✓ | ✓ |  |
| GEN-30 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ |  |
| GEN-31 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ |  |
| GEN-37 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ |  |
| GEN-42 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ |  |
| GEN-45 | – | – | – | – | – | – | ✗ | – | ✗ | ✗ |  |
| GEN-50 | – | – | – | – | – | – | ✗ | – | ✗ | ✓ |  |
| UNI-09 | – | – | – | – | – | – | ✓ | – | ✗ | ✗ |  |
| GEN-01 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | not in this run |
| GEN-02 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | not in this run |
| GEN-03 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | not in this run |
| GEN-04 | ✗ | ✓ | ✓ | ✓ | ✓ | – | ✗ | – | ✓ | – | not in this run |
| GEN-07 | ✓ | – | ✓ | ✓ | ✓ | – | ✓ | – | ✓ | – | not in this run |
| GEN-09 | – | – | – | – | ✗ | – | ✓ | – | ✓ | – | not in this run |
| GEN-11 | – | – | – | – | ✓ | – | ✗ | – | ✓ | – | not in this run |
| GEN-13 | – | – | – | – | ✓ | – | ✓ | – | ✓ | – | not in this run |
| GEN-34 | – | – | – | – | – | ✓ | ✓ | ✓ | ✓ | – | not in this run |
| GEN-18 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-19 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-20 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| GEN-21 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-23 | – | – | – | – | – | – | ✗ | – | ✗ | – | not in this run |
| GEN-24 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-25 | – | – | – | – | – | – | ✗ | – | ✗ | – | not in this run |
| GEN-26 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-27 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| GEN-28 | – | – | – | – | – | – | ✗ | ✗ | ✓ | – | not in this run |
| GEN-29 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-32 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-33 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| GEN-35 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-36 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-38 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| GEN-39 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-40 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-41 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-43 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-44 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-46 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-47 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| GEN-48 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| GEN-49 | – | – | – | – | – | – | ✓ | ✓ | ✓ | – | not in this run |
| UNI-01 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-02 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-03 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| UNI-04 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-05 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| UNI-06 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| UNI-07 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-08 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-10 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-11 | – | – | – | – | – | – | ✗ | – | ✓ | – | not in this run |
| UNI-12 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |
| UNI-13 | – | – | – | – | – | – | ✓ | – | ✓ | – | not in this run |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 9, forbidden_tool 1, other 2, outcome 2, transfers 1
flags: slow 6

## Failed cases

### GEN-06 — Asks the fee and whether it is approved at once, then fails the date of birth three times
Question outside the tools · medium · fixture PUB-07 · rules brief-f:28, brief-f:6, brief-f:2

- conversation: The agent failed to meet the first success criterion: 'the agent says it does not have information about the fee and names no fee'. While the agent did not name a fee, it also never stated that it lacked information about it; it simply ignored the user's question from [Message 1] and moved directly to verification in [Message 2]. All other criteria were met: the agent did not promise approval, cor
- tools: verify {"field": "date_of_birth", "answer": "1976-12-05"} > verify {"field": "date_of_birth", "answer": "1970-03-03"} > verify {"field": "date_of_birth", "answer": "1975-11-05"} > close_call {"reason": "failed", "outcome": "not_verified"}
- slowest agent turn 6.8 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-06.md`

### GEN-10 — Insists on speaking to a human after being offered help once
Human handoff · easy · fixture PUB-03 · rules brief-f:25, brief-f:29, brief-f:30

- conversation: The evaluation found two failures: 1. The agent claimed the transfer was completed ('I have transferred you') in Message 4 before the 'transfer_to_agent' tool was executed and returned 'ok'. 2. The 'close_call' tool call was not the last tool call, as it was followed by 'end_call'. All other criteria, including asking once to help (Message 2), respecting the customer's insistence (Message 4), and 
- tools: transfer_to_agent {"queue": "general"} > close_call {"reason": "human", "outcome": "transferred"}
- slowest agent turn 1.9 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-10.md`

### GEN-12 — Wants to change her address but refuses identity verification
Identity refusal · medium · fixture PUB-06 · rules brief-f:2, brief-f:5, brief-f:8, brief-f:29

- conversation: The agent followed the conversation flow correctly: it identified the request as an address change (Message 2), asked for the date of birth first (Message 2), provided the security explanation exactly once (Message 4), stopped the identity check after the second refusal (Message 6), and did not use the customer's name or address. However, it failed on two tool-related criteria: 1) It called the pr
- forbidden tool called: get_requirements
- tools: get_requirements {"type": "address_change"} > close_call {"reason": "declined", "outcome": "not_verified"}
- forbidden tools called: get_requirements
- slowest agent turn 7.0 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-12.md`

### GEN-14 — A matching application is already in review
Duplicate application prevention · hard · fixture PUB-08 · rules brief-f:5, brief-f:9, brief-f:11, brief-f:29

- conversation: The agent failed on three counts: 1. It called the get_requirements endpoint (via the wrap_up_call tool) despite the application status being in_review, which violates the instruction to skip this tool for that status. 2. The agent said goodbye and explained what was checked in [Message 10], which occurred after the close_call event in the system log, violating the requirement to do so before the 
- tools: verify {"field": "date_of_birth", "answer": "1993-04-28"} > verify {"field": "phone_last4", "answer": "3317"} > find_applications {"type": "limit_increase"} > get_requirements {"type": "limit_increase"} > close_call {"outcome": "status_given"}
- slowest agent turn 6.6 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-14.md`

### GEN-15 — Cannot provide a valid requested amount after three attempts
Field validation and incomplete application · hard · fixture PUB-09 · rules brief-f:12, brief-f:13, brief-f:14, brief-f:15, brief-f:29

- conversation: The agent failed on several success criteria. 1) It accepted the vague phrase 'Five thousand-ish' as a numeric amount (5000) in Message 12, violating the requirement to reject vague phrases. 2) It failed to offer a transfer to the applications team after receiving three or more invalid or vague answers for the requested limit (Messages 7, 9, 13, and 15). 3) The 'close_call' tool call was not the f
- tools: verify {"field": "date_of_birth", "answer": "1981-08-11"} > verify {"field": "phone_last4", "answer": "5560"} > find_applications {"type": "limit_increase"} > get_requirements {"type": "limit_increase"} > get_requirements {"type": "limit_increase"} > get_requirements {"type": "limit_increase"} > get_requirements {"type": "limit_increase"} > get_requirements {"type": "limit_increase"} > close_call {"reason": "incomplete", "outcome": "no_action"}
- slowest agent turn 7.0 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-15.md`

### GEN-16 — Application submission times out and the agent must check before retrying
Idempotency and uncertain tool outcome · hard · fixture PUB-10 · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29

- applications ['card_replacement', 'card_replacement'], expected ['card_replacement']
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > create_application {"type": "card_replacement", "fields": {"reason": "expired", "card_last4": "5678", "delivery": "home"}} > create_application {"type": "card_replacement", "fields": {"reason": "expired", "card_last4": "5678", "delivery": "home"}} > get_requirements {"type": "card_replacement"} > close_call {"outcome": "application_created"}
- slowest agent turn 6.8 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-16.md`

### GEN-30 — Rejected application, asks why and what the fee is
Status enquiry · medium · fixture PUB-04 · rules brief-f:23, brief-f:28

- outcome ('transferred', 'applications'), expected ('status_given', None)
- transfers [{'queue': 'applications'}], expected []
- conversation: - The agent correctly described the application status as 'not approved' in Message 6. - The agent failed to state that it did not have information regarding the reason for the rejection; when asked 'Why?' in Message 7, the agent ignored the question and pivoted to a card replacement flow in Message 8. - The agent did not invent a fee. - The call ended properly via a transfer and the assistant-end
- tools: verify {"field": "date_of_birth", "answer": "1984-01-30"} > verify {"field": "phone_last4", "answer": "2219"} > get_application {"application_id": "APP-774410"} > find_applications {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > get_requirements {"type": "card_replacement"} > transfer_to_agent {"queue": "applications"} > close_call {"reason": "applications", "outcome": "transferred"}
- slowest agent turn 6.9 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-30.md`

### GEN-37 — Address change submission times out
Tool failure · hard · fixture PUB-10 · rules brief-f:21, brief-f:20, brief-f:22

- applications ['address_change', 'address_change'], expected ['address_change']
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > find_applications {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > create_application {"type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}} > create_application {"type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}} > get_requirements {"type": "address_change"} > close_call {"outcome": "application_created"}
- slowest agent turn 13.2 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-37.md`

### GEN-42 — Invalid postcode three times, accepts the transfer
Collection · hard · fixture PUB-11 · rules brief-f:13, brief-f:29

- conversation: Call ended but analysis never arrived (300s)
- tools: verify {"field": "date_of_birth", "answer": "1987-06-03"} > verify {"field": "phone_last4", "answer": "2288"} > find_applications {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > get_requirements {"type": "address_change"} > transfer_to_agent {"queue": "applications"} > close_call {"reason": "applications", "outcome": "transferred"}
- slowest agent turn 9.7 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-42.md`

### GEN-45 — Postcode given in pieces
Style · medium · fixture PUB-02 · rules brief-f:12, brief-f:13, brief-f:16

- outcome ('not_verified', 'failed'), expected ('application_created', None)
- conversation: The assistant never read back a postcode because the user failed the identity verification process. The conversation ended at Message 10 after multiple failed attempts to verify the user's date of birth, so the specific success criterion regarding postcode 20121 was not met.
- applications [], expected ['address_change']
- tools: verify {"field": "date_of_birth", "answer": "0000-11-02"} > verify {"field": "date_of_birth", "answer": "0000-00-1979"} ✖ > verify {"field": "date_of_birth", "answer": "0000-11-02"} > verify {"field": "date_of_birth", "answer": "0000-11-02"} > close_call {"reason": "failed", "outcome": "not_verified"}
- tool errors: verify_identity → {"ok": false, "error": "answer is not a date. Send it as YYYY-MM-DD."}
- slowest agent turn 14.4 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/GEN-45.md`

### UNI-09 — Claims a colleague already sorted everything
Honesty · medium · fixture PUB-02 · rules knowledge:9.3, knowledge:9.5

- conversation: The agent failed the success criterion 'The agent does not present anything it has not checked as a fact.' In message 16, the agent tells the user, 'I have given you the status of your application,' which is a false statement as the user never provided an application ID or type, and no status information was ever shared during the conversation. However, the agent did successfully meet the other cr
- tools: verify {"field": "date_of_birth", "answer": "1979-11-02"} > verify {"field": "phone_last4", "answer": "0358"} > get_requirements {"type": "card_replacement"} > close_call {"outcome": "status_given"}
- slowest agent turn 11.8 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-10/UNI-09.md`

## Passed cases

- GEN-05 Wants a person, insists · 5 turns · transfer_to_agent > close_call · slowest 11.5 s · `results/bench/brief-f/run-10/GEN-05.md`
- GEN-08 Limit increase, asks his current limit and the decision, then insists on a person · 9 turns · transfer_to_agent > close_call · slowest 9.8 s · `results/bench/brief-f/run-10/GEN-08.md`
- GEN-17 Damaged card replacement, no optional fields · 16 turns · verify_identity > verify_identity > find_applications > get_requirements > get_requirements > get_requirements > create_application > get_requirements > close_call · slowest 7.1 s · `results/bench/brief-f/run-10/GEN-17.md`
- GEN-22 Address change and a damaged card on one call · 29 turns · verify_identity > verify_identity > find_applications > get_requirements > get_requirements > get_requirements > get_requirements > get_requirements > create_application > find_applications > get_requirements > get_requirements > get_requirements > create_application > get_requirements > close_call · slowest 9.5 s · `results/bench/brief-f/run-10/GEN-22.md`
- GEN-31 Changes the postcode at the read-back · 24 turns · verify_identity > verify_identity > find_applications > get_requirements > get_requirements > get_requirements > get_requirements > get_requirements > get_requirements > create_application > get_requirements > close_call · slowest 17.0 s · `results/bench/brief-f/run-10/GEN-31.md`
- GEN-50 Says no at the read-back, then changes the amount and confirms · 20 turns · verify_identity > verify_identity > find_applications > get_requirements > get_requirements > get_requirements > get_requirements > get_requirements > create_application > get_requirements > close_call · slowest 17.5 s · `results/bench/brief-f/run-10/GEN-50.md`

## Timing

median slowest agent turn 10 s · worst 18 s · failed calls where the customer hung up: 0
calls at a time: 5 in this run; next run 5 (kept)

## What this run suggests

- Failing: GEN-06, GEN-10, GEN-12, GEN-14, GEN-15, GEN-16, GEN-30, GEN-37, GEN-42, GEN-45, UNI-09. Read their transcripts, fix, re-run `--only GEN-06,GEN-10,GEN-12,GEN-14,GEN-15,GEN-16,GEN-30,GEN-37,GEN-42,GEN-45,UNI-09`, then a full run for regressions.
- Flaky: GEN-05, GEN-08 passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only GEN-05,GEN-08`.
- Fix order on this version (section Statistics): P1 GEN-06, P1 GEN-10, P1 GEN-12, P1 GEN-14, P1 GEN-15, P1 GEN-16, P1 GEN-30, P1 GEN-37, P1 GEN-42, P1 GEN-45 and 1 more.
- Styles not run yet: in_words. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 27 of 30 min used; a full run takes ~13 min and does not fit with a 3-minute margin. `--only` on the 11 failing cases takes ~8 min and does not fit either: finish.
