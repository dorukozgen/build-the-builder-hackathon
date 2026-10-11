# Retrospective · brief-a · practice run 2026-10-10 (digest: reports/20261010-234303.digest.md)

## Scores, in order
| run | scope | result |
|---|---|---|
| 01 | full + public A (baseline of the existing workflow, re-created) | 28/32 (gen 18/22, pub 10/10) |
| 02 | --only 6 cases | 5/6 |
| 03 | full + public A | 29/32 (gen 20/22, pub 9/10) |
| 04 | --only 7 | 6/7 |
| 05 | --only 4, reps 2 | 4/8 |
| 06 | --only 3, reps 2 | 3/6 |
| 07 | --only 2 (PUB-10, GEN-14), reps 2 | 4/4 |

Last full run: 29/32. Build time 35 min (5 over budget). No full run after the last four fix rounds.

## What cost time or turns
- step 19: `python3` is not on PATH on this machine (a Store alias); one failed call.
- steps 30–38: the agent in `.freya-agents.json` no longer existed (404 Agent/Workflow not found). I tried a benchmark, then an update, before re-creating. Cost ~30 s, but it is a trap: 404 is not transient.
- step 44: two generated cases were wrong. GEN-21: the persona refused an earlier offer before stating the decisive date, so the expected attempt was already spent. GEN-14: a post-write question the persona never got a turn to ask, because the call ends right after the write. Each cost a fix plus a re-run.
- step 70: a heredoc edit hit a failed `assert`, but save + full benchmark still ran (newline-separated, not `&&`). That 8-minute full run tested nothing new.
- steps 62–69: the date-matching bug (a day number mapped to the wrong month) showed that `create_promise` has no code check before the write. I spent ~1 min designing a blocking pre-hook, then dropped it for time. It stays unsettled.
- steps 75/90: judge strictness on a word ("recorded"). It first flagged the mandated opening line, then my new fixed sentence contained the forbidden word. That cost one extra re-run (step 93).
- steps 84–93: three `--only --reps 2` rounds of 1.5–3 min each, which pushed past the 30-minute budget.

## Lessons for any brief
- Check the interpreter name once at the start (`python` vs `python3`).
- A 404 "not found" for the stored workflow/agent is not transient: back up the state entry, drop it, re-create from the workflow file.
- Edit workflow JSON with a script that exits non-zero on failure, and chain save and benchmark with `&&` on one line.
- In case scripts, have the persona state the decisive fact in its first relevant answer, so an earlier refusal cannot consume the branch being tested.
- Rules about what happens after a write can't be tested if the call ends right after the write. Test them at the read-back.
- Fixed sentences the agent must say must not contain words a check forbids before success; check wording must not catch mandated lines.
- Plan the pre-write validation hook (and its failure route) in the first build, not as a late fix.
- After a fix, re-run the failed cases plus one or two neighbours from the same family with `--reps 2`. Leave time for one final full run.

## Lessons for this brief only (not for the skill)
- The early deadline is 2026-11-02, the late one 2026-10-23, attempt 1 is Fri 2026-10-16; the calendar list only reached deadline + 10 days.
- Attempt 1 uses the floor once "too much" was said. A refused deadline is a flat refusal that still triggers an unused attempt.
- The PUB-10 retry must be announced without the word "recorded".

## Lesson lines added to SKILL.md (verbatim)
- Check the interpreter name (`python` vs `python3`) at step 1 and use it everywhere.
- A 404 "not found" for the stored workflow or agent is not transient: back up `.freya-agents.json`, drop that slot's entry, and save again to re-create it.
- Edit workflow JSON with a script that exits non-zero on a failed match, and chain edit, save and benchmark with `&&`, so a failed edit never starts a run.
- In case scripts, have the persona give the decisive fact in its first relevant answer; an earlier refusal can use up the branch the case is meant to test.
- A rule about what happens after a write cannot be reached if the call ends at the write; test it at the read-back instead.
- Fixed sentences the agent says must not contain a word that a check forbids, and checks must not forbid words the brief makes the agent say.
- Build the pre-write validation hook and its failure route in the first version; it is too risky to add in the last minutes.
- After a fix, re-run the failed cases plus a neighbour from the same family with `--reps 2`, and keep about 8 minutes for a final full run.
