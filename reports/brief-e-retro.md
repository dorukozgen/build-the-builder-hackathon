# Retrospective: brief-e (practice run, 2026-10-11, 15:59 to 16:30)

Agent: workflow `dce30bea-5f67-4fa4-8e9a-8d2e0ef36cea`, agent `008c4b8d-3e4a-4253-9926-d0d79d46c85f` (version 1, saved at +4m).
The previous run's brief-e artifacts were kept in `out/_prev_brief-e/` and `tests/_prev_brief-e/`, and were not read.

## Benchmark runs

| # | Command | Result |
|---|---|---|
| 1 | full run (33 generated + 13 universal) | **No score.** The command hit the 20-minute limit. It played no case: the workspace was busy with another session's simulation (brief-f), and the runner kept waiting. No `results/bench/brief-e/` files were written. |
| 2 | `--only GEN-29`, 240 s cap | **No score.** It printed "another simulation is running in this workspace, waiting 30 s" eight times and then hit the cap. |

Hidden-brief estimate: **none**. No case result exists for any version, so confidence is nil. The agent's quality rests only on the build: hook unit tests run locally and a `validate_workflow` dry run that passed.

Even with a free workspace, the organisers' mock only serves the collections tools. `list_campaigns` and the other campaign tools answer `{"ok":false,"error":"not found"}`. So on the practice simulator only identity, transfer and close would have behaved as they will in the real run.

## What cost time or turns

- **Step 60 (about 20 of the 30 minutes):** I started the full benchmark piped through `| tail -40`, with a 20-minute command timeout. The runner's "another simulation is running … waiting" lines were buffered by `tail`, so nothing showed until the timeout. A 1-minute single-case probe first, run unbuffered, would have shown the busy workspace right away.
- **Step 66 (4 minutes):** the diagnostic probe. It found the cause, but too late to act on it.
- **Step 44:** `python3` does not exist on this Windows machine, which cost one repeated save command.
- **Step 52:** I found late, while planning tests, that the hosted mock has none of the brief's campaign tools. A probe of every brief tool at build time would have shaped the case plan earlier.
- Build itself: brief to saved agent took 4m20s. Research took 2 searches. Hooks were exec-tested locally before the save, and the dry-run validation passed first time.

## Lessons that hold for any brief

- Probe the bank host once per tool the brief names before writing cases. A tool that answers "not found" cannot be exercised on the practice mock, so plan cases, and the final line, around that.
- Run the benchmark unbuffered (`python -u`, no `| tail`) so waiting and progress lines show live.
- Before the first full run, make a short single-case `--only` probe with a timeout. It shows a busy shared workspace or a broken host within a minute, instead of losing a full-run slot.
- Exec every pre/post hook and code snippet locally with sample `vars`/`config` before the first save. It is cheap and catches syntax and logic errors that the platform would swallow.
- If `python3` is not on PATH, use `python`.

## Lessons for this brief only (not for skills)

- The brief's tool table differs from `tools/openapi.json`, which is the collections API. `tools/openapi-e.json` (a transcription of section 3) was passed to `--check` with `--openapi`.
- Rules 15, 17 and 24 (ineligible reasons, no offer after ineligible, application retry and failure) cannot be reached by any organisers' fixture.
- Points I could not settle:
  - When campaign info was given and the customer then declines a complaint or sales transfer, should the call close as `informed` (the priority list) or `no_action/out_of_scope` (rules 25 and 26)? I chose the priority list.
  - For a failed application after info was given, I chose `no_action/service_error` (rule 24) over `informed`.

## Lesson lines added to the skills (verbatim)

`.claude/skills/build-phone-agent/SKILL.md`, `## Lessons`:
- Before writing the workflow, POST once to the bank host for every tool the brief names; a "not found" means the practice mock cannot play that tool — record it and plan the tests around it.
- Exec every pre/post hook and code snippet locally with sample `vars` and `config` before the first save; the platform swallows hook errors silently.
- If `python3` is not found, run the same command with `python`.

`.claude/skills/test-phone-agent/SKILL.md`, `## Lessons`:
- Run the benchmark unbuffered (`python -u`, never piped through `tail` or `head`) so waiting and progress lines show live.
- Before the first full run, probe with one `--only` case under a short timeout: a shared workspace busy with another simulation, or a host missing the brief's tools, then costs one minute instead of the whole budget.
- If the workspace is busy with another session's simulation, say so at once and decide with the clock; never start a full run into the queue.
