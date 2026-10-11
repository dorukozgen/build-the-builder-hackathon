# Retrospective · brief-e · practice run · 2026-10-11 15:25 (digest: reports/20261011-152506.digest.md)

Agent `1f999db5-a23c-4bcb-8684-a1a1f902212c`, workflow `a4012cdd-f13a-4d08-a71d-740e88615205` (version 2). Elapsed 31 minutes.

## Scores, in order
| run | digest step | scope | result |
|---|---|---|---|
| 1 | 69 | full, 47 generated | no result: cut off at 16 min. 48 practice sessions were opened at 15:33, but the agent made no tool call on the mock. The simulation never started. |
| 2 | 75 | --only GEN-01, GEN-11 | no result: "another simulation is running in this workspace" for 7 min, then killed by my `timeout 420` |

No benchmark run finished, so there is no score and no hidden-brief estimate (confidence: none). The agent is unverified end to end. Only its hooks were unit-tested locally (out/test_hooks_e.py, 17 checks, all as intended).

## What cost time or turns
- Steps 69 to 78, about 23 of the 31 minutes: the workspace was shared with a second Claude Code session (a brief-F build started at 15:19, digest 20261011-151930). That session had its own mock on port 8765 and its own ngrok tunnel, and its simulations held the workspace's single simulation slot. I could have spotted it at step 24: the brief-F retro already warned about exactly this. At step 51, the `f_` customer id from a foreign tunnel was a second sign. I checked processes only at step 78.
- Step 69: the first run was the whole 47-case set, started with no `timeout` and no single-case smoke run first. The run was blocked from the start, and the cut-off took 16 minutes to show it.
- Steps 50 to 52: I took the first tunnel in ngrok's list. It was the other session's tunnel to the brief-F mock, which cost one save with the wrong base URL and a re-save (steps 51 and 57).
- Steps 12 and 15: `python3` and then `python` failed: on this machine both are Store aliases. `py -3` works. A previous retro had recorded this, but the lesson never reached the skill file.
- Steps 18 to 25: probing showed that the hosted mock lacks every brief-E tool. A self-hosted mock, an API file and a tunnel had to be built (tools/mock_bank_e.py, tools/openapi-e.json). This was needed work, done in about 5 minutes by copying the brief-F mock's shape.
- Not run before `--check`: no run was. No repeated command except the forced benchmark retry. Edits never tested end to end: the whole workflow.

## Lessons for any brief
- Before the first benchmark, check that the workspace is not shared: process list, mocks or tunnels you did not start, recent digests from another session. One simulation runs at a time per workspace.
- Make the first run of a new agent a 2–3 case `--only` smoke run under a shell `timeout` shorter than the cut-off. Size the full set from its seconds per case.
- When a tunnel starts, match its public URL to your local port. Never take the first tunnel in the list.
- Gate each write tool by node: it exists only in the node reached after its precondition tool succeeded, with the id baked from code.
- Decide the close outcome by the brief's priority in a close_call pre-hook, from flags that post-hooks set. The model's choice is only the fallback.

## Lessons for this brief only (not for the skills)
- Brief E's tools are not on the hosted mock. Practice needs `tools/mock_bank_e.py` (port 8766), a tunnel to it, `--openapi tools/openapi-e.json --host <tunnel>`, and `BRIEF_E_BASE=<tunnel> py -3 out/gen_brief_e.py` before saving. A new tunnel URL needs a re-save.
- The mock catalogue has, on 2026-10-14: one expired campaign, one not yet started, one whose summary contradicts its conditions, and no current-account campaign. Each case's `backend` sets consent, eligibility reasons and start_application faults.
- Unsettled brief points: the outcome after a `not_checked` result when the customer declines sales (that case was removed), and whether `informed` beats `no_action` when information was given before a declined transfer (the pre-hook keeps `no_action`).
- 47 cases written (tests/gen_cases_e.py) and every rule is cited, but none has run.

## Lesson lines added to the skill files (verbatim)
build-phone-agent/SKILL.md:
- Check the interpreter at step 1 (`python3` can be a Store alias; try `py -3`) and use the working one in every command.
- Before designing, probe each tool the brief names on the mock; if any is missing, plan a self-hosted mock, its tool API file and a tunnel first, modelled on an existing one in tools/.
- When you start a tunnel, match its public URL to your local port; another session's tunnel can be listed first.
- Gate every write tool by node: it exists only in the node reached after its precondition tool succeeded, and its id is baked from code, not chosen by the model.
- Compute the close outcome by the brief's priority in a close_call pre-hook from flags set in post-hooks; the model's choice is only the fallback.
- Unit-test every hook locally with fake vars and results, and after each save read the stored workflow back to confirm hooks, global nodes and tool-call transitions survived.

test-phone-agent/SKILL.md:
- Before the first benchmark, check the workspace is not shared (process list, mocks or tunnels you did not start, recent digests); one simulation runs at a time per workspace.
- Make the first run of a new agent a 2–3 case `--only` smoke run under a shell `timeout` below the cut-off; size the full set from its seconds per case and split it with `--only` if it would not fit.
- Write cases with a small generator script so identity answers, rule citations and backend state stay consistent across 40+ cases.
