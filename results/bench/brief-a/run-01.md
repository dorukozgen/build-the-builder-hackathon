# Benchmark brief-a · run 1

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-10 23:50:26 · 286 s · reps 1 · style none

## Score

- generated 18/22 · public 10/10 · total 28/32
- promised on passed cases: 5190.00 (the organisers' first tie-breaker)
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
| GEN-06 | ✓ |  |
| GEN-07 | ✓ |  |
| GEN-08 | ✗ |  |
| GEN-09 | ✓ |  |
| GEN-10 | ✓ |  |
| GEN-11 | ✓ |  |
| GEN-12 | ✓ |  |
| GEN-13 | ✓ |  |
| GEN-14 | ✗ |  |
| GEN-15 | ✓ |  |
| GEN-16 | ✓ |  |
| GEN-17 | ✓ |  |
| GEN-18 | ✓ |  |
| GEN-19 | ✓ |  |
| GEN-20 | ✓ |  |
| GEN-21 | ✗ |  |
| GEN-22 | ✓ |  |
| PUB-01 | ✓ |  |
| PUB-02 | ✓ |  |
| PUB-03 | ✓ |  |
| PUB-04 | ✓ |  |
| PUB-05 | ✓ |  |
| PUB-06 | ✓ |  |
| PUB-07 | ✓ |  |
| PUB-08 | ✓ |  |
| PUB-09 | ✓ |  |
| PUB-10 | ✓ |  |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 4
flags: slow 1

## Failed cases

### GEN-04 — Wrong number
Third party · easy · fixture PUB-07 · rules brief-a:8

- conversation: The agent did not meet all success criteria. While the agent correctly avoided stating the reason for the call, it failed to thank the user before ending the conversation, only saying 'Goodbye'.
- tools: close_call {"reason": "wrong_number", "outcome": "not_reached"}
- slowest agent turn 0.0 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-01/GEN-04.md`

### GEN-08 — Never confirms who he is
Identity · medium · fixture PUB-05 · rules brief-a:3

- conversation: The agent asked the same question ('Am I speaking with Mr Novak?') three times, violating the success criterion that the agent must ask at most twice. - Ask 1: Message 0 - Ask 2: Message 2 - Ask 3: Message 4
- tools: close_call {"reason": "unclear", "outcome": "not_reached"}
- slowest agent turn 0.0 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-01/GEN-08.md`

### GEN-14 — Next Friday, service fails once, then asks to change it
Tool failure · hard · fixture PUB-10 · rules brief-a:22, brief-a:37, brief-a:36

- conversation: The agent failed to meet one of the success criteria: it did not mention that the promise can be changed in the mobile app. Other criteria were met: the date was correctly read back as Friday 23 October in [Message 8], the agent did not say 'recorded' until after the retry succeeded in [Message 11], and the create_promise function was called exactly twice according to system events.
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > get_account > promise {"date": "2026-10-23", "amount": 365, "product_id": "p1"} ✖ > promise {"date": "2026-10-23", "amount": 365, "product_id": "p1"} > close_call {"outcome": "promise"}
- tool errors: create_promise → {"ok": false, "error": "service unavailable, nothing was recorded"}
- slowest agent turn 0.9 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-01/GEN-14.md`

### GEN-21 — Wants 20 November, refuses the deadline and the Friday offer
Dates · hard · fixture PUB-01 · rules brief-a:23, brief-a:30, brief-a:31

- conversation: The agent failed to meet the success criteria because it did not propose Friday 16 October after stating the date limit of Monday 2nd November. The agent proposed Friday 16 October earlier in the call at [Message 8], before the user mentioned 20 November. After stating 'The latest date I can record is Monday, November 2nd' in [Message 10], the agent only proposed that specific date and then ended 
- tools: verify {"field": "date_of_birth", "answer": "1988-03-14"} > verify {"field": "phone_last4", "answer": "4471"} > get_account > close_call {"reason": "refused", "outcome": "no_promise"}
- slowest agent turn 1.4 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-01/GEN-21.md`

## Passed cases

- GEN-01 Asks robot and scam questions, then pays in full this Friday · 14 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 0.0 s · `results/bench/brief-a/run-01/GEN-01.md`
- GEN-02 Husband answers, offers to pay, she is back tomorrow at eleven · 7 turns · schedule_callback > close_call · slowest 2.5 s · `results/bench/brief-a/run-01/GEN-02.md`
- GEN-03 Sister offers Saturday, then nine in the evening · 7 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-01/GEN-03.md`
- GEN-05 Mother says the customer has died · 3 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-01/GEN-05.md`
- GEN-06 Gives the birth date as numbers, month first, then in words; pays today · 13 turns · verify_identity > verify_identity > verify_identity > get_account > create_promise > close_call · slowest 0.8 s · `results/bench/brief-a/run-01/GEN-06.md`
- GEN-07 Refuses the security questions twice · 7 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-01/GEN-07.md`
- GEN-09 Late band, refuses both persuasion attempts · 13 turns · verify_identity > verify_identity > get_account > close_call · slowest 2.5 s · `results/bench/brief-a/run-01/GEN-09.md`
- GEN-10 Early band, one flat refusal ends it · 11 turns · verify_identity > verify_identity > get_account > close_call · slowest 3.0 s · `results/bench/brief-a/run-01/GEN-10.md`
- GEN-11 Offers 50, accepts the floor next Monday · 13 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.9 s · `results/bench/brief-a/run-01/GEN-11.md`
- GEN-12 Partial amount on a Saturday, then changes the date at read-back · 17 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 0.9 s · `results/bench/brief-a/run-01/GEN-12.md`
- GEN-13 Vague end of month twice, accepts the deadline · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.0 s · `results/bench/brief-a/run-01/GEN-13.md`
- GEN-15 Says the loan was paid off and closed years ago · 9 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.2 s · `results/bench/brief-a/run-01/GEN-15.md`
- GEN-16 Insists on a human · 11 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 1.2 s · `results/bench/brief-a/run-01/GEN-16.md`
- GEN-17 In hospital, accepts the support team · 11 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 2.8 s · `results/bench/brief-a/run-01/GEN-17.md`
- GEN-18 Asks about interest, then twice does not want to talk · 17 turns · verify_identity > verify_identity > get_account > close_call · slowest 2.1 s · `results/bench/brief-a/run-01/GEN-18.md`
- GEN-19 One wrong birth year, then too much and refuses the floor · 15 turns · verify_identity > verify_identity > verify_identity > get_account > close_call · slowest 1.8 s · `results/bench/brief-a/run-01/GEN-19.md`
- GEN-20 Wrong answers across both questions · 11 turns · verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 2.0 s · `results/bench/brief-a/run-01/GEN-20.md`
- GEN-22 Asks for lower instalments · 10 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 10.9 s · `results/bench/brief-a/run-01/GEN-22.md`
- PUB-01 Confirms identity and pays the full amount today · 11 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.7 s · `results/bench/brief-a/run-01/PUB-01.md`
- PUB-02 A relative answers · 5 turns · schedule_callback > close_call · slowest 1.0 s · `results/bench/brief-a/run-01/PUB-02.md`
- PUB-03 Three wrong answers · 9 turns · verify_identity > verify_identity > verify_identity > close_call · slowest 3.5 s · `results/bench/brief-a/run-01/PUB-03.md`
- PUB-04 Wants a date after the deadline · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 4.3 s · `results/bench/brief-a/run-01/PUB-04.md`
- PUB-05 Lost his job, declines the support team · 11 turns · verify_identity > verify_identity > get_account > close_call · slowest 5.5 s · `results/bench/brief-a/run-01/PUB-05.md`
- PUB-06 Full amount is too much, accepts the floor · 13 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.4 s · `results/bench/brief-a/run-01/PUB-06.md`
- PUB-07 A vague period, then a holiday · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.2 s · `results/bench/brief-a/run-01/PUB-07.md`
- PUB-08 Says she already paid · 9 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.0 s · `results/bench/brief-a/run-01/PUB-08.md`
- PUB-09 Asks for a new payment plan · 10 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 1.3 s · `results/bench/brief-a/run-01/PUB-09.md`
- PUB-10 The promise service fails on the first call · 14 turns · verify_identity > verify_identity > get_account > create_promise > create_promise > close_call · slowest 2.8 s · `results/bench/brief-a/run-01/PUB-10.md`

## Timing

median slowest agent turn 2 s · worst 11 s · failed calls where the customer hung up: 0

## What this run suggests

- Failing: GEN-04, GEN-08, GEN-14, GEN-21. Read their transcripts, fix, re-run `--only GEN-04,GEN-08,GEN-14,GEN-21`, then a full run for regressions.
- Styles not run yet: asks_back, pieces. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 7 of 30 min used; a full run (~5 min; `--reps 2` ~10 min) still fits with a 3-minute margin.
