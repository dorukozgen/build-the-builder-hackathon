---
name: build-phone-agent
description: Build a Freya phone agent from a bank's brief, write its test scenarios, benchmark it on the practice simulator and fix what fails. Use when asked to build or improve a phone agent from a brief.
---

# Build a phone agent from a brief

Work from the kit folder. Use only what the brief and the tool API file say. Do not copy rules from another brief.

## Steps

1. Note the time: `date`. A build may take 30 minutes at most, tests included.
2. Read every brief file you were given in full, top to bottom. Do not search in it: a rule can sit in any paragraph. Then read `tools/openapi.json`. When a brief is raw material (a mail, a policy extract, a memo, a code list) instead of a numbered list of rules, write `tests/<slot>.facts.md` first: one numbered atomic fact per line with its file and date; a later record governs an earlier one (format in `docs/test-case-template.md`). `<slot>` is the brief's file name without `.md`.
3. Read `docs/workflow-format.md`, `docs/tools-and-code.md`, `docs/banking-customer-service-knowledge.md` and `docs/test-case-template.md`.
4. List the banking concepts in the brief: products, processes, terms, regulations. For each one that the knowledge file does not cover, research it with WebSearch and WebFetch before you write anything. Learn what it means, how banks usually handle it, and what an agent must never say or do about it. Keep it short: a few searches per concept. Then say in a line or two per concept what you found and where, and build the agent with it.
5. Read `examples/base-agent.json`. It is a small working agent with two steps. Use it as the pattern for the JSON, not as the answer.
6. Write the test cases before the workflow. `python3 tools/benchmark.py --fixtures` shows the practice customers whose bank data a case can borrow. Write `tests/<slot>.cases.json` from the brief, following `docs/test-case-template.md`. Check it: `python3 tools/benchmark.py --check --cases tests/<slot>.cases.json --rules <each brief file> [--rules tests/<slot>.facts.md]`. Fix every error. A passing check also writes `tests/<slot>.test-set.json`, the same cases with the fixture data merged in; it is derived, so never edit it, edit the cases file and check again. For each rule it lists as cited by no case, add a case, or note why no fixture can reach it. If it says the fixtures' identity fields are not in the tool API, the practice simulator cannot play identity for this brief: keep the third-party and callback cases (they still run), take the others out of the file, build the rest from the brief alone, and say so in your final line. Do not change `public-test-set.json`, `tools/openapi.json` or the tools, and do not bend the agent's identity step to fit the practice mock.
7. If `.freya-agents.json` already has an agent for this slot, or the brief builds on another brief whose agent is there, benchmark that agent first with step 10's command and its `agent_id`, before changing anything. What passes stays; rewrite only what fails.
8. Write the workflow to `out/<slot>.workflow.json`.
   - One step per stage of the call. Identity comes first.
   - Move to the next step on a tool result, not on what the customer says.
   - Take every tool field and allowed value from `tools/openapi.json`.
   - Validate every write in code before the tool call: the date against the calendar and the deadline, the amount against the floor and the full amount, the product id against what `get_account` returned. The model's own arithmetic never reaches the bank.
   - Leave `agent_config` out.
9. Save it: `python3 -c "import freya,json,sys; print(json.dumps(freya.save_workflow(sys.argv[1], json.load(open(sys.argv[2])))))" <slot> out/<slot>.workflow.json`
   It prints `workflow_id` and `agent_id`. The same slot updates the same workflow.
10. Benchmark it: `python3 tools/benchmark.py <agent_id> --cases tests/<slot>.cases.json --rules <the same files as in step 6>`. Add `--public A` when the brief is `briefs/brief-a.md` and `--public B` when it is `briefs/brief-b.md`, nothing otherwise: the public customers' expected records follow those two briefs and no other. A run takes 3 to 11 minutes. Run it in the foreground and wait for it to finish. Never start it in the background and never end your turn while a run is going: the builder stops when you stop.
11. Read `results/bench/<slot>/latest.md`, then `results/bench/<slot>/run-NN.transcripts.md`. Write `results/bench/<slot>/run-NN.review.md` (sections "Reading a benchmark report" and "Transcript review"). Fix the workflow file, save it again, benchmark again.
12. After every run, decide whether to run again (section "How many runs").
13. Finish with one line: the `workflow_id`, the `agent_id`, the score of the last full run (generated and public), how many runs you made, the rules no case reaches, and the brief points you could not settle.
14. Retrospective, only when the request says it is a practice run (section "Retrospective").

## Reading a benchmark report

- For each failed case, read the rules it cites again and decide: is the agent wrong, or the case? Public cases are never wrong. Change a generated case only when the brief shows its expectation is wrong, and say so in the review file. Never weaken a check or an expectation to make a run pass, and never test against anything but the real simulation.
- Find the cause in the transcript: the `↪` route lines, the `⚙` tool arguments and results, what the agent said just before.
- Fix the regressions first. Make the smallest fix; prefer routes, code and tool conditions over prompts.
- A flaky case counts as failing: the final runs every customer three times and counts only three passes.

## Transcript review

- After every full run, read `run-NN.transcripts.md`, passed cases too, against the whole brief, not only against the case's checks.
- For each case note: rules broken that no check named; anything the agent claimed without a tool result behind it (recorded, scheduled, transferred); turns a customer would find unclear; the turn before each hang-up; places where the customer's phrasing confused the agent.
- Write `results/bench/<slot>/run-NN.review.md`: one block per case with the findings, then the fixes you decided on, then the cases you will add for rules the run showed untested, then your decision about the next run and its reason.
- A finding from a passed case is fixed with the same priority as a failure: the final customers' checks are not yours.

## How many runs

- After every run you decide whether to run again, what to run, and when to stop. Decide from three things: the report's "What this run suggests" section, your transcript-review findings, and the clock. Write the decision and its reason at the end of the review file.
- A run takes 3 to 11 minutes. After a fix, re-run the failed cases with `--only`, then one full run before finishing to catch regressions.
- A benchmark command is cut off after 15 minutes. `--reps 2` on the full set fits only when the last full run took under 7 minutes; otherwise use `--reps 2` with `--only` on the flaky cases.
- One pass is a hint, not proof. When everything passes and time remains, run again (`--reps 2`, or a `--style` run) rather than stopping.
- Do not stop with time left while a case fails, is flaky, is untested after a change, or a review finding is unfixed.
- Stop when time is nearly out, when two consecutive full runs pass everything with no review findings, or when a fix round changed nothing.

## Banking knowledge

`docs/banking-customer-service-knowledge.md` holds general banking principles. Follow them in every agent you build.

- It gives principles, not values. Every rule, number, date, limit, identity question and outcome comes from the brief and `tools/openapi.json`. When the brief and that file disagree, the brief wins.
- When the brief says nothing about an action, do not invent a rule for it. Leave the action out, or hand the call off the way the brief allows.
- What you research (step 4) explains a concept. It never sets a rule or a value for this bank and never overrides the brief or `tools/openapi.json`. Research is not verification.
- What that file calls the "Guard MD" is the workflow's `system_prompt` and step prompts. Write it there, not in a separate file.
- Its process (section 14) is the steps above. Do not write role files or guard files. Test scenarios go in `tests/<slot>.cases.json` and nowhere else.
- Put its hard limits in routes, code and tool conditions, not only in prompts: no account data before identity passes, no success message before the tool result confirms it, no repeat of a write that timed out without checking first.
- Before each save, check the workflow against the "Final Design Principles" section of that file.

## Rules

- Never edit the agent on the platform by hand. Change the file and save it.
- When a tool call fails, the agent must say so. It must never tell the customer something is recorded when it is not.
- A customer that passes once can fail the next time. Prefer rules in routes and code over rules in prompts.
- An HTTP 5xx or a timeout from Freya or the bank is not a bug: it is transient. Wait a minute and run the same command again. Any other crash in `tools/benchmark.py` or `tools/trace_review.py` is a bug: say so in your final line. Do not edit the tools and do not test another way.

## Retrospective

Only when the request says it is a practice run.

1. `python3 tools/trace_review.py` writes `reports/<trace>.digest.md`, a digest of your own run so far: what you thought at each step (summarised), what you ran, what failed, how long each stretch took, commands you repeated, edits you never tested. Read it.
2. Write `reports/<slot>-retro.md` with: the score of every benchmark run of this build, in order; what cost time or turns, each with the digest's step number (a rule misread, a guess a test later contradicted, a repeated command, a tool error, a run started before `--check`); lessons that hold for any brief; lessons for this brief only, which never go into the skill; and, verbatim, the lesson lines you add to, change in or remove from this file.
3. Update the `## Lessons` section at the end of this file and nothing else in it: one line per lesson; general only — no rule, number, date, name, product, queue, outcome value or holiday from any brief; at most 12 lines; merge, replace or drop old lines rather than growing the list.

## Lessons

(none yet)
