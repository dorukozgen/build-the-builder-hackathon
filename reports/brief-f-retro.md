# Retrospective: Brief F build (practice run, 2026-10-11, 19:40)

Agent: workflow `b245f135-c3f7-4a3a-bcf6-06f7b5ac903b`, agent `af6616bb-9524-4fa2-a462-08a04b0ac5d0`, version 3.
Digest: `reports/20261011-194016.digest.md` (26m33s, 5 test runs, 4 saves, 1 tool error).

## Scores, in order

| Run | Version | What | Result |
|---|---|---|---|
| run-22 | 1 | `--only` smoke, one case per exit | 4 / 4 |
| run-23 | 1 | full, 16 calls at a time | 61 / 63 (universal 13 / 13) |
| run-24 | 2 | `--only` the 2 failures and 4 neighbours | 6 / 6 |
| run-25 | 2 | full | 38 / 40 scored, 23 not played (tunnel), universal 13 / 13 |
| run-26 | 3 | `--only` the security cases and GEN-10 | 4 / 5 |

Hidden-brief estimate: on v1, 58 of 60, confidence low. None on v3, which has no full run.

## What cost time or turns

- **Steps 50–51: a failed Edit was chained into a full run.** The prompt fix for the duplicate find_applications call failed with "string not found". The same step went on to regenerate, save (a no-op, still version 2) and start an 8-minute full run, so that run did not test the change I thought it tested.
- **Step 51: the tunnel refused connections at 16 calls at a time.** 23 of 63 cases went unplayed. With no time left for a re-run, v3 has no full run.
- **Step 29: the first full run took 9m32s.** That left one fix round and one more full run, as the lessons predicted.
- **The start went well.** The leftover generator was reused, the mock and tunnel were started by hand, the smoke run began at minute 1 and the first full run at minute 3.

## Lessons for any brief

- When the model skips a mandatory lookup at the start of a step, run the lookup engine-side, fed by an enum extracted earlier. Name that variable differently from every model-filled tool field.
- Word a global interrupt's intent narrowly and give it not-examples.
- Never chain an edit with save and benchmark until you have seen the edit apply.
- The free tunnel drops connections at 16 calls at a time too. Plan a re-run of the not-played cases.

## Lessons for this brief only (not in the lessons file)

- GEN-24: the agent asked its own "which address" question without get_requirements. Fixed with the engine-run `first_find` node.
- GEN-33: a customer reading out a PIN set off the security transfer. Fixed by narrowing the intent (rule 27 is about a code given to another person).
- GEN-50: the check's wording was ambiguous ("after the first no"). It now states what rules 17 and 19 require.
- Still open:
  - GEN-10: the judge reads the fixed transfer line spoken after the tool, and the engine's end_call, as violations. A short "I will transfer you now" before the transfer call might settle it.
  - After `first_find`, the model calls find_applications a second time.
  - Rule 13's counter is still enforced in the prompt only.
- `out/brief-f.workflow.json` was regenerated with the placeholder base URL `https://SUBMISSION-BASE-URL/v1`.

## Lesson lines changed in docs/builder-lessons.md (verbatim)

Removed from "Building the agent":
- `If python3 is not found, run the same command with python.` (the skill already says it)

Added to "Building the agent":
- `When the model skips a mandatory lookup at the start of a step, run it engine-side in a passthrough node fed by an enum extracted earlier; give that variable a name no model-filled tool field uses, or its value gets baked into those tools for later requests.`

Changed in "Building the agent" (appended to the global-interrupt line):
- `Word that node's intent narrowly (who received what, from whom), with not-examples: a broad one fired on a customer merely reading their own data to the agent.`

Changed in "Testing and fixing" (the tunnel-drop line now ends):
- `(it happened at 16 and 20 calls at a time, a third of a full run): budget a re-run of the not-played cases, and do not fix the agent for them.`

Added to "Testing and fixing":
- `Never chain an Edit with save and benchmark in one step without seeing the edit applied: a failed Edit then tests and saves the old version as if fixed.`
