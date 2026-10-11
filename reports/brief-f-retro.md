# Retrospective: Brief F build (practice run, 2026-10-11)

## Scores, in order

| Run | What | Result |
|---|---|---|
| run-06 | smoke test, `--only GEN-17,GEN-34,GEN-14`, version 2 | 1 / 3 |
| run-07 | full run, version 3 | 38 / 63 (generated 34 / 50, universal 9 / 13 on the conversation) |

Last hidden-brief estimate (version 3): **35 of 60**, confidence **low** (one result per case).

Agent: workflow `f673d421-3637-4599-84bc-53ebcce3a450`, agent `30fd33bc-25d5-48c1-8960-95c961aff499`.

## What cost time or turns (step numbers from the digest)

- **Step 71: the full run took 16m24s** for 63 cases (50 generated + 13 universal), more than half the budget. It started at minute 10 and ended at minute 27, which left no time for a fix round. This was the main loss.
- **Step 38: a shell `sed` patch of a code string silently did not match.** The save went out unchanged and a second save was needed (step 43). The lessons file already warns against shell patches; I broke that rule.
- **Steps 48 to 68: the smoke test showed the model calls `close_call` without the closing sentence.** I redesigned closing as a fixed spoken line built in code, followed by an engine-run `close_call`. That was right, but the transfer path kept a bare goodbye with no sentence naming the team. Four cases failed on that gap, and the smoke test had not included a transfer that needed explaining.
- **The rule-13 failure counter was a guess.** It was enforced in code, but only on answers the model chose to send to the tool. The test showed the model does not send "I don't have it" (GEN-42).
- **Reusing the existing `tests/brief-f.cases.json`.** It was written from this brief in an earlier practice run and passed `--check` on the first try with `--openapi`. That saved writing 50 cases. My first `--check` left out `--openapi` and gave false errors, which cost one extra command.
- **Leftover mocks and tunnels** (one mock, three ngrok processes) had to be killed by hand at the start. The lessons file predicted this, so it cost under a minute.

## Lessons for any brief

- Model-facing close tools are unreliable at speaking before they act. Speak the closing summary from a fixed line computed in code, then run the real close as an engine call. Every branch needs that line, including transfers.
- A counted rule (N failed answers) must count every reply to the question, not only the replies the model forwards to a tool.
- With 60 or more cases, one full run takes about 16 minutes. Plan for exactly one full run, and use the smoke test on one case per exit path (create, transfer, status, close) to catch structural bugs before it.
- A pre-hook can rewrite a model tool's request to a harmless read-only endpoint, with a post-hook that validates the stored arguments. This puts per-answer validation in code, but the extra reads show up in the ledger.

## Lessons for this brief only (not in the lessons file)

- The rule 21 timeout case in the mock records the slow first create *after* the immediate `find_applications`, so a check straight after the timeout cannot see it. A short wait or a second check is needed.
- The universal cases' "no claim without a tool result" check flags the brief's prescribed "this call is recorded" opening line. That conflicts with rule 1, so those cases count as settled.
- The status-path closing must fall back to `status_given`, not `out_of_scope`, when the customer only enquired.

## Lesson lines changed in docs/builder-lessons.md (verbatim)

Added to "Building the agent":
- `Speak the closing summary from a fixed line computed in code and run the close as an engine call after it, on every exit path including transfers: the model often calls a closing tool without its closing sentence.`
- `A rule that counts failed answers must count every reply to the question in code; the model does not forward non-answers ("I don't have it") to a validation tool.`

Changed in "Testing and fixing" (replaces "Smoke-test the plumbing with `--only` on 2–3 short cases before the first full run, and start that run by minute 10."):
- `Smoke-test with --only on one case per exit path (create, transfer, status, close) before the first full run, and start that run by minute 8: a full run of 60+ cases takes about 16 minutes, so it may be the only one.`
