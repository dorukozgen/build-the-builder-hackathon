# Benchmark brief-a · run 3

agent `33fde166-3bfc-4ae6-96b2-3ffeeb22dee2` · 2026-10-11 00:03:02 · 477 s · reps 1 · style none

## Score

- generated 20/22 · public 9/10 · total 29/32
- promised on passed cases: 5190.00 (the organisers' first tie-breaker)
- fixed since the previous run: none
- regressed: GEN-19, PUB-10
- still failing: GEN-21

## History

| case | run 1 | run 2 | run 3 | |
|---|---|---|---|---|
| GEN-01 | ✓ | – | ✓ |  |
| GEN-02 | ✓ | – | ✓ |  |
| GEN-03 | ✓ | – | ✓ |  |
| GEN-04 | ✗ | ✓ | ✓ |  |
| GEN-05 | ✓ | ✓ | ✓ |  |
| GEN-06 | ✓ | – | ✓ |  |
| GEN-07 | ✓ | – | ✓ |  |
| GEN-08 | ✗ | ✓ | ✓ |  |
| GEN-09 | ✓ | – | ✓ |  |
| GEN-10 | ✓ | – | ✓ |  |
| GEN-11 | ✓ | – | ✓ |  |
| GEN-12 | ✓ | – | ✓ |  |
| GEN-13 | ✓ | – | ✓ |  |
| GEN-14 | ✗ | ✓ | ✓ |  |
| GEN-15 | ✓ | – | ✓ |  |
| GEN-16 | ✓ | – | ✓ |  |
| GEN-17 | ✓ | – | ✓ |  |
| GEN-18 | ✓ | ✓ | ✓ |  |
| GEN-19 | ✓ | – | ✗ |  |
| GEN-20 | ✓ | – | ✓ |  |
| GEN-21 | ✗ | ✗ | ✗ |  |
| GEN-22 | ✓ | – | ✓ |  |
| PUB-01 | ✓ | – | ✓ |  |
| PUB-02 | ✓ | – | ✓ |  |
| PUB-03 | ✓ | – | ✓ |  |
| PUB-04 | ✓ | – | ✓ |  |
| PUB-05 | ✓ | – | ✓ |  |
| PUB-06 | ✓ | – | ✓ |  |
| PUB-07 | ✓ | – | ✓ |  |
| PUB-08 | ✓ | – | ✓ |  |
| PUB-09 | ✓ | – | ✓ |  |
| PUB-10 | ✓ | – | ✗ |  |

## Rule coverage

every rule is cited by at least one case

## Failure categories

conversation 3

## Failed cases

### GEN-19 — One wrong birth year, then too much and refuses the floor
Amounts · hard · fixture PUB-03 · rules brief-a:12, brief-a:26, brief-a:30, brief-a:31

- conversation: - The agent correctly asked for the date of birth again after the first response was incorrect. - The agent's single persuasion attempt offered 28.50 on Friday, October 16th, and noted the rest would remain overdue. - However, the agent failed the requirement of 'no further offer after the second refusal'. The first refusal occurred at [Message 9] regarding payment today, and the second at [Messag
- tools: verify {"field": "date_of_birth", "answer": "1993-07-21"} > verify {"field": "date_of_birth", "answer": "1992-07-21"} > verify {"field": "phone_last4", "answer": "6630"} > get_account > close_call {"reason": "refused", "outcome": "no_promise"}
- slowest agent turn 2.8 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-03/GEN-19.md`

### GEN-21 — Wants 20 November, refuses the deadline and the Friday offer
Dates · hard · fixture PUB-01 · rules brief-a:23, brief-a:30, brief-a:31

- conversation: The agent correctly identified Monday 2 November as the latest recordable date in Message 8. However, it failed to meet the requirement of proposing Friday 16 October after that refusal, as the agent instead moved to close the call in Message 10 following the user's rejection of the November 2nd date. No promise for 20 November was read back.
- tools: verify {"field": "date_of_birth", "answer": "1988-03-14"} > verify {"field": "phone_last4", "answer": "4471"} > get_account > close_call {"reason": "refused", "outcome": "no_promise"}
- slowest agent turn 0.9 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-03/GEN-21.md`

### PUB-10 — The promise service fails on the first call
Tool failure · hard · fixture PUB-10 · rules –

- conversation: The agent met the first criterion by successfully recording exactly one promise (pr1) after retrying the create_promise tool following a technical error. However, the second criterion was not met because the agent said the word 'recorded' in Message 0 ('This call is recorded'), which occurred before any successful tool calls (such as identity verification or the promise creation). The call ended p
- tools: verify {"field": "date_of_birth", "answer": "1989-02-23"} > verify {"field": "phone_last4", "answer": "9904"} > get_account > promise {"date": "2026-10-16", "amount": 365, "product_id": "p1"} ✖ > promise {"date": "2026-10-16", "amount": 365, "product_id": "p1"} > close_call {"outcome": "promise"}
- tool errors: create_promise → {"ok": false, "error": "service unavailable, nothing was recorded"}
- slowest agent turn 2.6 s · ended assistant-ended-call · transcript `results/bench/brief-a/run-03/PUB-10.md`

## Passed cases

- GEN-01 Asks robot and scam questions, then pays in full this Friday · 13 turns · verify_identity > verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.6 s · `results/bench/brief-a/run-03/GEN-01.md`
- GEN-02 Husband answers, offers to pay, she is back tomorrow at eleven · 5 turns · schedule_callback > close_call · slowest 2.6 s · `results/bench/brief-a/run-03/GEN-02.md`
- GEN-03 Sister offers Saturday, then nine in the evening · 7 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-03/GEN-03.md`
- GEN-04 Wrong number · 5 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-03/GEN-04.md`
- GEN-05 Mother says the customer has died · 3 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-03/GEN-05.md`
- GEN-06 Gives the birth date as numbers, month first, then in words; pays today · 13 turns · verify_identity > verify_identity > verify_identity > get_account > create_promise > close_call · slowest 4.2 s · `results/bench/brief-a/run-03/GEN-06.md`
- GEN-07 Refuses the security questions twice · 7 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-03/GEN-07.md`
- GEN-08 Never confirms who he is · 5 turns · close_call · slowest 0.0 s · `results/bench/brief-a/run-03/GEN-08.md`
- GEN-09 Late band, refuses both persuasion attempts · 13 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.1 s · `results/bench/brief-a/run-03/GEN-09.md`
- GEN-10 Early band, one flat refusal ends it · 13 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.6 s · `results/bench/brief-a/run-03/GEN-10.md`
- GEN-11 Offers 50, accepts the floor next Monday · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.5 s · `results/bench/brief-a/run-03/GEN-11.md`
- GEN-12 Partial amount on a Saturday, then changes the date at read-back · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.4 s · `results/bench/brief-a/run-03/GEN-12.md`
- GEN-13 Vague end of month twice, accepts the deadline · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.3 s · `results/bench/brief-a/run-03/GEN-13.md`
- GEN-14 Next Friday, asks about changing it later, service fails once · 13 turns · verify_identity > verify_identity > get_account > create_promise > create_promise > close_call · slowest 1.0 s · `results/bench/brief-a/run-03/GEN-14.md`
- GEN-15 Says the loan was paid off and closed years ago · 9 turns · verify_identity > verify_identity > get_account > close_call · slowest 0.9 s · `results/bench/brief-a/run-03/GEN-15.md`
- GEN-16 Insists on a human · 11 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 1.2 s · `results/bench/brief-a/run-03/GEN-16.md`
- GEN-17 In hospital, accepts the support team · 11 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 1.4 s · `results/bench/brief-a/run-03/GEN-17.md`
- GEN-18 Asks about interest, then twice does not want to talk · 15 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.2 s · `results/bench/brief-a/run-03/GEN-18.md`
- GEN-20 Wrong answers across both questions · 11 turns · verify_identity > verify_identity > verify_identity > verify_identity > close_call · slowest 1.3 s · `results/bench/brief-a/run-03/GEN-20.md`
- GEN-22 Asks for lower instalments · 10 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 2.6 s · `results/bench/brief-a/run-03/GEN-22.md`
- PUB-01 Confirms identity and pays the full amount today · 11 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.0 s · `results/bench/brief-a/run-03/PUB-01.md`
- PUB-02 A relative answers · 6 turns · schedule_callback > close_call · slowest 0.2 s · `results/bench/brief-a/run-03/PUB-02.md`
- PUB-03 Three wrong answers · 9 turns · verify_identity > verify_identity > verify_identity > close_call · slowest 1.6 s · `results/bench/brief-a/run-03/PUB-03.md`
- PUB-04 Wants a date after the deadline · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 7.0 s · `results/bench/brief-a/run-03/PUB-04.md`
- PUB-05 Lost his job, declines the support team · 11 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.7 s · `results/bench/brief-a/run-03/PUB-05.md`
- PUB-06 Full amount is too much, accepts the floor · 13 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 2.0 s · `results/bench/brief-a/run-03/PUB-06.md`
- PUB-07 A vague period, then a holiday · 15 turns · verify_identity > verify_identity > get_account > create_promise > close_call · slowest 1.2 s · `results/bench/brief-a/run-03/PUB-07.md`
- PUB-08 Says she already paid · 9 turns · verify_identity > verify_identity > get_account > close_call · slowest 1.2 s · `results/bench/brief-a/run-03/PUB-08.md`
- PUB-09 Asks for a new payment plan · 10 turns · verify_identity > verify_identity > get_account > transfer_to_agent > close_call · slowest 2.1 s · `results/bench/brief-a/run-03/PUB-09.md`

## Timing

median slowest agent turn 1 s · worst 7 s · failed calls where the customer hung up: 0

## What this run suggests

- Regressions first: GEN-19, PUB-10 passed before and fail now. Fix, then `--only GEN-19,PUB-10`.
- Failing: GEN-21. Read their transcripts, fix, re-run `--only GEN-21`, then a full run for regressions.
- Styles not run yet: asks_back, pieces. Final customers talk like people; a `--style` run shows whether the agent copes.
- Time: 20 of 30 min used; a full run takes ~8 min and does not fit with a 3-minute margin. `--only` on a few cases may; otherwise finish.
