# Review of run-18 to run-21 (Brief F, agent 1956bd9e, versions 1 to 4)

## run-18 (v1, full, 20 at a time): 40 / 63
- 19 failures had tool calls with no result, and the mock log had no matching request (mock traffic dropped at 19:17). The tunnel lost them under load, not the agent. They were re-run in run-19.
- UNI-02: the agent offered the security questions to a third party (the system prompt told it to). Fixed in v2.
- GEN-50: "Shall I submit this application?" without reading the value back; a second create_application of the same type after one was received. Fixed in v2 (prompt).
- GEN-41: the first verify_identity call was lost in the tunnel; the agent's retry was right. Passed in run-19.

## run-19 (v2, --only 23): 16 / 23
- GEN-16, 22, 26, 31, 37: tool calls after 19:23:49 never reached the mock (same tunnel fault). The agent's behaviour up to that point was correct.
- GEN-39: the third party was not told that the questions protect the account (rule 8). Fixed in v3 with a fixed sentence.
- GEN-48: the talkative persona loops and never gives the phone digits; the identity step's turn cap closes the call as no_action/out_of_scope.

## run-20 (v3, full, 12 at a time): 61 / 63, universal 13 / 13
- GEN-45: the postcode was given in pieces and counted as failed answers, ending in a transfer. Fixed in v4 (join the pieces, say "Go on").
- GEN-48: persona loop, as above.

## run-21 (v4, --only GEN-45, GEN-47, GEN-48): 2 / 3
- GEN-45 and GEN-47 pass. GEN-48 still fails on the persona loop.

## Decision
I stopped at 23 of 30 minutes: a full run on v4 (~10 min) does not fit. Still open:
- v4 has no full run behind it.
- GEN-48: the case script and the turn-cap fallback reason.
- Rule 13's failed-answer count lives in the prompt, not in code.
