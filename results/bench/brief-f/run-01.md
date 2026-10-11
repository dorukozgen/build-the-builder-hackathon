# Benchmark brief-f · run 1

agent `9b1b1617-e7e7-48bd-bc0d-7c61b1a79678` · 2026-10-11 02:25:03 · 166 s · reps 1 · style none

## Score

- generated 5/8 · total 5/8
- promised on passed cases: 0.00 (the organisers' first tie-breaker)
- fixed since the previous run: none
- regressed: none
- still failing: none

## History

| case | run 1 | |
|---|---|---|
| GEN-01 | ✓ |  |
| GEN-02 | ✓ |  |
| GEN-03 | ✓ |  |
| GEN-04 | ✗ |  |
| GEN-05 | ✓ |  |
| GEN-06 | ✗ |  |
| GEN-07 | ✓ |  |
| GEN-08 | ✗ |  |

## Rule coverage

rules cited by no case: brief-f:3, brief-f:4, brief-f:9, brief-f:10, brief-f:11, brief-f:12, brief-f:13, brief-f:14, brief-f:17, brief-f:18, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:23, brief-f:24, brief-f:27

## Failure categories

conversation 2, forbidden_tool 1, outcome 2, transfers 1

## Failed cases

### GEN-04 — Asks for his balance, accepts the transfer
Out of scope · easy · fixture PUB-05 · rules brief-f:26, brief-f:29, brief-f:30

- conversation: The agent failed to meet two specific criteria: 1) The agent did not explicitly state that the 'digital assistant' cannot give a balance, only stating 'I cannot do that' in Message 2, which is a generic refusal. 2) The closing statement in Message 4 ('I am transferring you to a colleague now. Thank you for calling Freya Bank, goodbye.') was delivered in two distinct sentences, failing the requirem
- tools: transfer_to_agent {"queue": "general"} > close_call {"reason": "human", "outcome": "transferred"}
- slowest agent turn 0.8 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-01/GEN-04.md`

### GEN-06 — Asks the fee and whether it is approved at once, then fails the date of birth three times
Question outside the tools · medium · fixture PUB-07 · rules brief-f:28, brief-f:6, brief-f:2

- outcome (None, None), expected ('not_verified', 'failed')
- forbidden tool called: transfer_to_agent
- tools: verify {"field": "date_of_birth", "answer": "1976-12-05"} > verify {"field": "date_of_birth", "answer": "1975-05-12"} > verify {"field": "date_of_birth", "answer": "1975-11-05"} > verify {"field": "date_of_birth", "answer": "1975-12-05"} > verify {"field": "phone_last4", "answer": "7093"} > transfer_to_agent {"queue": "applications"} ✖ > close_call {"reason": "applications", "outcome": "transferred"} ✖
- tool errors: transfer_to_agent → {"ok": false, "error": "unknown queue"}; close_call → {"ok": false, "error": "this outcome needs one of these reasons: restructuring, human, support"}
- forbidden tools called: transfer_to_agent
- slowest agent turn 2.5 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-01/GEN-06.md`

### GEN-08 — Limit increase, asks his current limit and the decision, then insists on a person
Customer insists · hard · fixture PUB-09 · rules brief-f:15, brief-f:28, brief-f:25

- outcome (None, None), expected ('transferred', 'human')
- transfers [], expected [{'queue': 'general'}]
- conversation: The agent failed to meet the requirement of asking only once whether it could help before transferring. While the agent correctly refrained from stating current limits, new limits, likely decisions, or approvals (Message 13), it asked the user if they wanted to be transferred in Message 11 and then repeated the same offer in Message 13. This resulted in the agent asking twice. The call was ended p
- tools: verify {"field": "date_of_birth", "answer": "1981-08-11"} > verify {"field": "phone_last4", "answer": "5560"} > transfer_to_agent {"queue": "applications"} ✖ > close_call {"reason": "applications", "outcome": "transferred"} ✖
- tool errors: transfer_to_agent → {"ok": false, "error": "unknown queue"}; close_call → {"ok": false, "error": "this outcome needs one of these reasons: restructuring, human, support"}
- slowest agent turn 1.9 s · ended assistant-ended-call · transcript `results/bench/brief-f/run-01/GEN-08.md`

## Passed cases

- GEN-01 Wants an address change, refuses the security questions twice · 7 turns · close_call · slowest 0.4 s · `results/bench/brief-f/run-01/GEN-01.md`
- GEN-02 Limit increase, wrong date of birth twice, then a wrong phone number · 11 turns · verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 4.9 s · `results/bench/brief-f/run-01/GEN-02.md`
- GEN-03 Damaged card, date of birth with month and day swapped, then wrong phone digits · 13 turns · verify_identity > verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 4.9 s · `results/bench/brief-f/run-01/GEN-03.md`
- GEN-05 Wants a person, insists · 5 turns · transfer_to_agent > close_call · slowest 1.5 s · `results/bench/brief-f/run-01/GEN-05.md`
- GEN-07 Address change, gives the date of birth, refuses the phone digits · 9 turns · verify_identity > close_call · slowest 1.1 s · `results/bench/brief-f/run-01/GEN-07.md`

## Timing

median slowest agent turn 2 s · worst 5 s · failed calls where the customer hung up: 0

## What this run suggests

- Failing: GEN-04, GEN-06, GEN-08. Read their transcripts, fix, re-run `--only GEN-04,GEN-06,GEN-08`, then a full run for regressions.
- Styles not run yet: corrects, pieces. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 12 of 30 min used; a full run (~3 min; `--reps 2` ~6 min) still fits with a 3-minute margin.
