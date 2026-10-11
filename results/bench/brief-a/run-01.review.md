# Review · brief-a · run 01 (28/32: generated 18/22, public 10/10)

Note: `.freya-agents.json` pointed at a workflow/agent that no longer exists (404). Backed up to `.freya-agents.stale.json`, re-created from the unchanged `out/brief-a.workflow.json`. Run 01 is the baseline of that existing file.

## Per case
- GEN-04 FAIL (agent): wrong number closed with "I apologize for the mistake. Goodbye." — no thanks (rule 47).
- GEN-05 PASS but finding: "I am sorry for your loss. Goodbye." — no thanks (rule 47).
- GEN-08 FAIL (agent): asked "Am I speaking with Mr Novak?" a third time after "go ahead" (rule 3: close after the second ask).
- GEN-14 FAIL (case): the agent hangs up right after the recorded promise, so the persona never gets to ask about changing it. Rule 36 is now tested at the read-back ("can I change it later?"). The agent did not say "recorded" before the retry succeeded. OK.
- GEN-21 FAIL (case): the persona refused Friday (attempt 1, early band = 1 attempt) before naming 20 November, so closing as refused after the deadline was refused is correct under rules 23/30/31. Script reordered so the date comes first.
- GEN-18 PASS but finding: after the interest question the agent asked "can you pay today?" twice more before attempt 1 (repeated offer; rule 30 says a non-answer uses an attempt). Called the car-loan instalment "the minimum amount" (wording only).
- GEN-02/PUB-02: "I cannot disclose the reason for the call" is borderline on rule 5 but says nothing about the account. Left as is.
- Others: read-backs, dates (16 Oct, 23 Oct, 2 Nov, 19/20 Oct, 27 Oct), floors and outcomes are correct. No claim without a tool result.

## Fixes
1. system_prompt: thank and say goodbye in the same message before every close_call.
2. opening: explicit ASK 1/ASK 2 counting with `{{opening.current_turns}}`; never a third ask.
3. opening: fixed farewells for wrong number and deceased now include thanks.
4. collection: never re-ask "today"; a non-answer goes to the next attempt; the answer to "can I change it later" is the mobile app.

## Cases changed
GEN-14 and GEN-21, as above. The brief shows the earlier expectation was unreachable or wrong. No check was weakened.

## Next run
Re-run `--only GEN-04,GEN-05,GEN-08,GEN-14,GEN-18,GEN-21`, then one full run for regressions (the last full run took 286 s).
