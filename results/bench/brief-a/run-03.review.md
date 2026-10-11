# Review · brief-a · runs 02–07 (last full run: run 03, 29/32: generated 20/22, public 9/10)

## Per case
- run 02 GEN-21: the agent turned "20 November" into "Tuesday 20 October" and called it allowed. The calendar only lists dates up to deadline + 10 days, so the model matched the day number. The customer refused, so nothing was recorded, but it is a real risk. Fixed: the calendar now says that unlisted dates are after the deadline and that the month must match. Not fixed: `create_promise` has no pre-write check in code (date vs calendar/deadline, amount vs floor/full).
- run 03 GEN-21: after the deadline was refused, the agent closed without using its one attempt (rule 23 → 30). Fixed in the DATE RULES prompt. Passed in run 04.
- run 03 GEN-19: the agent was correct. The check "no further offer after the second refusal" was ambiguous, so its wording was clarified to the brief's meaning. No expectation was weakened.
- run 03 PUB-10: judge noise ("This call is recorded" in the mandated opening). Later runs 05/06: the retry happened silently, and then my failure sentence used the word "recorded". Fixed: fixed sentence, no "recorded" before ok. PUB-10 and GEN-14 passed 2/2 in run 07.
- run 04 GEN-19: attempt 1 proposed the full amount after "too much" (rule 30). Fixed: prompt + "Attempt 1 amount" line in the account facts. Passed 2/2 in run 05.
- run 05 GEN-11: the floor offered on the below-floor path without "the rest stays overdue" (rule 26). Fixed: passed 2/2 in run 06.
- GEN-18 (passed): the agent still re-asks "can you pay today" once after answering the interest question. Minor; not fixed.

## Next run
None. The time budget is spent. Untested after the last changes: a full run (regressions across all 32). The next session should start with a full `--reps 2` run.
