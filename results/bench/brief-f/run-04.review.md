# Review · brief-f · runs 03 (full, reps 2: 8/8 + 8/8) and 04 (full, style corrects: 8/8)

## Per case (all passed)
- GEN-01 and GEN-07: the decline was explained once; the close line came before `close_call`; no name was used before verification.
- GEN-02, GEN-03, GEN-06: the fixed failure line says "call back or visit a branch". The hint retry no longer mentions swapping. No correct values were revealed.
- GEN-04: the "As a digital assistant, I cannot help with that" wording held, with a transfer offer before the transfer.
- GEN-05 and GEN-08: asked once whether it could help, then queue general.
- Minor (run 03, GEN-06): one turn answered the fee question and named the request back but did not ask for the date of birth in the same message. The next turn asked it, so no rule was broken. Not fixed.
- Nothing was claimed without a tool result. No hang-ups mid-call.

## Untested (mock limitation)
Rules 3, 4, 9–24 and 27: the mock lacks the tools and the queue/outcome values. That covers the collection, submission, retry, existing-application and status paths. Only the code was unit-tested locally.

## Decision
Stop. Two consecutive full runs passed everything with no open review finding, at about 20 of 30 minutes. The remaining risk is in paths the practice mock cannot play, and no further run here can reduce it.
