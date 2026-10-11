# Retrospective · brief-f · practice run 2026-10-11 (digest: reports/20261011-021330.digest.md)

## Scores, in order
| run | scope | result |
|---|---|---|
| 01 | full, 8 generated | 5/8 |
| 02 | --only GEN-04, GEN-06, GEN-08 | 3/3 |
| 03 | full, --reps 2 | 8/8 + 8/8 |
| 04 | full, --style corrects | 8/8 |

Last full run: 8/8 generated (no public set applies to brief F). About 20 minutes to the final run, inside the 30-minute budget.

## What cost time or turns
- Steps 12 and 16: `python3` is a Store alias here; one Bash failure plus one denied PowerShell call before `py -3` (step 17). The brief-A retro had already found this, but the lesson was not in the skill file.
- Steps 18–23: working out that the practice mock lacks `get_requirements`, `find_applications`, `create_application` and `get_application`, and that its enums lack two queues and three outcomes. Probing with curl (step 22) settled it in one call. That shrank the testable scope to identity, refusal and general transfers.
- Step 32: a long design pass (about 2 min of thinking) for paths the mock cannot exercise: the existing-application check, the validation pre-hook, the recheck before retry, and multi-application loops. These were unit-tested locally (step 42) but never run end to end.
- Step 48 to step 51, GEN-06: a guess the test contradicted. My "wrong" date was the fixture's date with day and month swapped. The mock returned the swap hint, which the brief says is not a wrong answer, so the case expectation was wrong, not the agent.
- Step 51, GEN-08: the case let the persona pass identity, so it ran into the mock gap. The case was rewritten so the person request comes before identity.
- Step 51, GEN-04: the agent paraphrased the prescribed wording ("I cannot do that" instead of the digital-assistant wording). The judge also read an ambiguous check ("in one sentence ... thanks ... goodbye") more strictly than the rule.
- Step 46: no check that the global node survived the save. It is never triggered on the mock, so its storage is still unverified.
- No repeated commands. No run was started before `--check`.

## Lessons for any brief
- Fix the interpreter name at step 1.
- Probe every tool path and enum on the mock before writing cases, and scope the cases to what can actually be played.
- Wrong identity answers in cases must not be near-variants of the right one.
- The persona's decisive action must come before anything that moves the call into another branch.
- Prescribed wording goes verbatim into prompts or fixed lines.
- Check wording must mirror the rule's sentence boundaries.
- Do write validation in a pre-hook that reroutes to a harmless read on bad input. Unit-test hooks locally.
- Hook messages must not carry text the model would echo ("Day and month look swapped").

## Lessons for this brief only (not for the skill)
- The practice mock cannot play rules 3, 4, 9–24 and 27 (the tools are missing; the `applications`/`security` queues and the `application_created`/`status_given`/`no_action` outcomes are not in its enums). Every verified case ends in the service-problem branch.
- The brief's tools are taken to live at the same mock base URL (`…/v1/<tool>`). That is unconfirmed.
- The day/month swap hint fires for a numbers-only date read day-first when the real date is month-first. Wrong answers in cases must avoid that pattern.

## Lesson lines for SKILL.md (verbatim; the section is empty). NOT applied: the permission mode denied the edit to `.claude/skills/build-phone-agent/SKILL.md`. They must be pasted in by hand.
- Check the interpreter name at step 1 (`python3` may be a store alias; try `py -3` or `python`) and use it everywhere.
- Before writing cases, POST once to every tool path the brief names and compare its enums with `tools/openapi.json`; plan runnable cases from what the mock really has and list the rest as unreachable from the start.
- A wrong security answer in a case must be unrelated to the fixture's value; a swapped or transposed variant can trigger a hint that the brief does not count as wrong.
- In case scripts, have the persona give the decisive fact or action in its first relevant answer, before anything that could move the call into another branch.
- When the brief prescribes wording for a reply, put that phrase verbatim in the prompt or a fixed line; the judge rejects paraphrases.
- Word each check with the same sentence boundaries as the brief's rule, and never forbid a word the brief makes the agent say.
- Validate every write in a pre-hook that, on bad input, reroutes the request to a side-effect-free read and returns the reason via the post-hook; unit-test every hook and code snippet locally with fake `vars`/`config`/`result` before saving.
- Hook messages the model reads must say what to ask or do, not internal reasons; the model echoes them to the customer.
- Generate the workflow from a script that exits non-zero on a failed edit, and chain generate, save and benchmark with `&&`.
- A 404 "not found" for the stored workflow or agent is not transient: back up `.freya-agents.json`, drop that slot's entry, and save again.
- A rule about what happens after a write cannot be reached if the call ends at the write; test it at the read-back instead.
- After a fix, re-run the failed cases with `--only`, then one full `--reps 2` run, and keep a few minutes for the retrospective.
