# Review of run 07 (agent version 3): 38 / 63 (generated 34 / 50, universal 9 / 13 on the conversation)

## Findings by cause

- **Transfers not explained** (GEN-04, GEN-10, GEN-11, UNI-11): the model calls `transfer_to_agent` without saying which team takes over. The fixed closing line after a transfer is only "Thank you for calling Freya Bank. Goodbye.", which does not meet rule 30. Fix: compute the transfer sentence in code from the queue and speak it in `close_transferred` ("I am transferring you to the <team> team, who will take it from here.").
- **Transfer closed but no close_call in the ledger** (GEN-20): the route went `close_transferred → end` but the ledger shows only the transfer. In GEN-34 the same node did record the close. Cause not settled: maybe the call ended before the pre-action reached the mock. Needs a re-run with `--only GEN-20 --reps 2`.
- **Rule 13 counter never reached** (GEN-42): when the customer says "I don't have it", the model asks again but does not send the answer to `check_field`, so the three-failures route never fires. The model then closes `no_action / incomplete` without offering the transfer. Fix: tell the model that any answer to a required question (including "I don't have it") goes to `check_field`, and also count non-answers in code.
- **Timeout recovery race** (GEN-16, GEN-37): the first create is slow and lands in the mock *after* `recover` has run `find_applications`. The retry then creates a second application, and the late first create appears after `close_call` in the ledger. The flow follows rule 21 as written. The open question is how long to wait before checking. Possible fix: a short fixed line plus a second `find_applications` before the retry.
- **Calls ending without close_call** (GEN-38, GEN-50): created, then no wrap-up. These transcripts were not read in the time left.
- **Status lookups** (GEN-28, GEN-30): the id was not found (probably the model transcribed it wrongly), and the closing summary defaulted to `out_of_scope`. In GEN-30 the agent transferred after a rejected status, which the brief does not ask for.
- **Wrong closing line**: when no status was given, `WRAP_PRE` falls back to `out_of_scope`. The status path needs its own fallback.
- **Identity with speaking styles** (GEN-45, GEN-48): the pieces-style and talkative customers never completed identity. These transcripts were not read in the time left.
- **Universal cases UNI-03, 05, 06**: the judge counts "this call is recorded" in the opening as a claim with no tool result behind it. Rule 1 prescribes that sentence word for word, so these are settled against the brief and left failing.
- **Read-back** now uses "here is what you have given me"; no "recorded" before submit was seen in the passing cases.

## Decision about the next run

None. The clock is at 27 of 30 minutes and a full run takes about 16 minutes. The fixes above are listed for the next build, in this order: transfer sentence, rule 13 counting, closing fallback for status, then the timeout race.
