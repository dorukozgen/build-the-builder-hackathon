# Builder lessons

What the practice runs taught, kept outside `.claude/` so that the builder can write here: Claude Code refuses edits to the skill files in the builder's permission mode, and lessons left in a retrospective never reached the next run.

Both skills read this file at their first step. The retrospective (test-phone-agent, section "Retrospective") updates it: one line per lesson, general only — no rule, number, date, name, product, queue, outcome value or holiday from any brief — at most 12 lines per section; merge, replace or drop old lines rather than growing the list.

## Building the agent

- Check which tool API file matches the brief: `tools/openapi.json` is the collections API of Briefs A and B. When the brief has its own tool table or a per-brief API file, use that (pass it to `--check` too), and pass the tool base URL to the generator as a parameter instead of writing it into the workflow by hand.
- Write the workflow from a generator script; compile every hook and exec it locally on sample inputs before the first save. Never patch code strings through shell heredocs: escaped newlines come out as real ones.
- In post-hooks, read request fields that a pre-hook stored in `vars`; do not rely on `<tool>_args` being set yet.
- Before writing the workflow, POST once to the bank host for every tool the brief names; a "not found" means the practice mock cannot play that tool — record it and plan the tests around it.
- A 404 "not found" for the stored workflow or agent is not transient: back up `.freya-agents.json`, drop that slot's entry, and save again to re-create it.
- A generator left by an earlier session of the same brief is the starting point even when the agent registry is empty: review it against the brief, regenerate with the current base URL and save; that put the first full run at minute 1.
- Speak the closing summary from a fixed line computed in code and run the close as an engine call after it, on every exit path including transfers: the model often calls a closing tool without its closing sentence. A node runs its `pre_actions` before its `on_enter` line, so a node holding both says the line after the close: speak the line in a passthrough node of its own and call the closing tool in the next one. Run a transfer before the sentence that announces it.
- A rule that counts failed answers must count every reply to the question in code; the model does not forward non-answers ("I don't have it") to a validation tool.
- Set any "a write was attempted" flag in the write's pre-hook and clear it in the post-hook on success: a post-hook does not see an error or timeout response, so state written only there is missing exactly when the timed-out-write path needs it.
- A request that must escalate from any point of the call (a security report mid-collection) belongs in a global `matches_intent` node with an engine-run transfer; a system-prompt rule alone lost to the current step's own offer. Word that node's intent narrowly (who received what, from whom), with not-examples: a broad one fired on a customer merely reading their own data to the agent.
- When the model skips a mandatory lookup at the start of a step, run it engine-side in a passthrough node fed by an enum extracted earlier; give that variable a name no model-filled tool field uses, or its value gets baked into those tools for later requests.
- Never point a model-facing helper (a "wrap up", "check field" or "next step" tool) at a real bank endpoint: every call lands in the bank's ledger, trips the cases' forbidden tools and reads to the judge as a needless call. Let the model end a step through an extracted variable and a route instead, and keep tool calls for what the bank must record or answer.

## Testing and fixing

- Before the first run, clear leftovers: `python3 tools/benchmark.py` tells you when the workspace is busy with another simulation and recreates a persona cache another workspace left behind; old mocks and tunnels on your port must go by hand (take the URL from your own tunnel's log).
- Never pipe a benchmark through `tail` or `head`: run it with `python -u`, in the foreground, and read its output; "waiting for the workspace" then shows at once instead of after the timeout.
- A 5xx while a simulation is being polled does not stop it on Freya; the runner keeps polling now. If a command was still cut off, or a full run stopped at its time limit, the simulation may still hold the workspace for minutes: the next run queues behind it.
- Restart a hosted mock whenever its file may have changed, and before judging a fault case, check the mock log that the fault fired; a fault that never fires tests nothing and the judge then fails the agent on side remarks. A tool call with no result and no matching request in the mock log was dropped by the tunnel under load (it happened at 16 and 20 calls at a time, a third of a full run): budget a re-run of the not-played cases, and do not fix the agent for them.
- Smoke-test with `--only` on one case per exit path (create, transfer, status, close) before the first full run, and start that run by minute 6: a full run of 60+ cases took 9 to 10 minutes at 12 to 16 calls at a time (16 at 5; the number adapts to the share of slow replies, and a tunnelled mock caps it at 12), so the budget holds one first full run, one or two `--only` fix rounds and one last full run.
- A wrong security answer in a case must be unrelated to the fixture's value; a swapped or transposed variant can trigger a hint that the brief does not count as wrong.
- In case scripts, have the persona give the decisive fact or action in its first relevant answer, before anything that could move the call into another branch.
- When the brief prescribes wording for a reply, put that phrase verbatim in the prompt or a fixed line; the judge rejects paraphrases. Word each check with the same sentence boundaries as the brief's rule, and never forbid a word the brief makes the agent say. Leave the order of speech and tool calls, and "the last tool call", to the ledger: the judge sees the tools apart from the conversation and counts `end_call` as one, so such checks fail a correct agent.
- A rule about what happens after a write cannot be reached if the call ends at the write; test it at the read-back instead.
- After a fix, re-run the failed cases plus a neighbour from the same family with `--only`, then keep about 8 minutes for a final full run.
- Never chain an Edit with save and benchmark in one step without seeing the edit applied: a failed Edit then tests and saves the old version as if fixed.
- When every customer hangs up after its first sentence and the agent said nothing, the shared model was down (once for 24 minutes), not the agent: the judge still writes "the customer ended the call", which reads like an agent fault. Probe with `--probe`, change nothing until it answers.
