# Builder lessons

What the practice runs taught, kept outside `.claude/` so that the builder can write here: Claude Code refuses edits to the skill files in the builder's permission mode, and lessons left in a retrospective never reached the next run.

Both skills read this file at their first step. The retrospective (test-phone-agent, section "Retrospective") updates it: one line per lesson, general only — no rule, number, date, name, product, queue, outcome value or holiday from any brief — at most 12 lines per section; merge, replace or drop old lines rather than growing the list.

## Building the agent

- Check which tool API file matches the brief: `tools/openapi.json` is the collections API of Briefs A and B. When the brief has its own tool table or a per-brief API file, use that, and pass the tool base URL to the generator as a parameter instead of writing it into the workflow by hand.
- Write the workflow from a generator script; compile every hook and exec it locally on sample inputs before the first save. Never patch code strings through shell heredocs: escaped newlines come out as real ones.
- In post-hooks, read request fields that a pre-hook stored in `vars`; do not rely on `<tool>_args` being set yet.
- Before writing the workflow, POST once to the bank host for every tool the brief names; a "not found" means the practice mock cannot play that tool — record it and plan the tests around it.
- A 404 "not found" for the stored workflow or agent is not transient: back up `.freya-agents.json`, drop that slot's entry, and save again to re-create it.
- If `python3` is not found, run the same command with `python`.
- Speak the closing summary from a fixed line computed in code and run the close as an engine call after it, on every exit path including transfers: the model often calls a closing tool without its closing sentence.
- A rule that counts failed answers must count every reply to the question in code; the model does not forward non-answers ("I don't have it") to a validation tool.

## Testing and fixing

- Before the first run, clear leftovers: `python3 tools/benchmark.py` tells you when the workspace is busy with another simulation and recreates a persona cache another workspace left behind; old mocks and tunnels on your port must go by hand (take the URL from your own tunnel's log).
- Never pipe a benchmark through `tail` or `head`: run it with `python -u`, in the foreground, and read its output; "waiting for the workspace" then shows at once instead of after the timeout.
- A 5xx while a simulation is being polled does not stop it on Freya; the runner keeps polling now. If a command was still cut off, the simulation is probably running: wait for it, do not start another.
- Smoke-test with `--only` on one case per exit path (create, transfer, status, close) before the first full run, and start that run by minute 6: a full run of 60+ cases took 16 minutes at 5 calls at a time (now 10), so the budget holds one first full run, one or two `--only` fix rounds and one last full run.
- A wrong security answer in a case must be unrelated to the fixture's value; a swapped or transposed variant can trigger a hint that the brief does not count as wrong.
- In case scripts, have the persona give the decisive fact or action in its first relevant answer, before anything that could move the call into another branch.
- When the brief prescribes wording for a reply, put that phrase verbatim in the prompt or a fixed line; the judge rejects paraphrases. Word each check with the same sentence boundaries as the brief's rule, and never forbid a word the brief makes the agent say.
- A rule about what happens after a write cannot be reached if the call ends at the write; test it at the read-back instead.
- After a fix, re-run the failed cases plus a neighbour from the same family with `--only`, then keep about 8 minutes for a final full run.
