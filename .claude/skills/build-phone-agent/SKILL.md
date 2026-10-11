---
name: build-phone-agent
description: Build a Freya phone agent from a bank's brief - read the brief and its tool API, research the banking concepts it relies on, write the workflow with its hard limits in routes and code, and save it on Freya. Use whenever asked to build, create or rebuild a phone agent from a brief, even when the request does not name this skill. Once the agent is saved, test and improve it with the test-phone-agent skill.
---

# Build a phone agent from a brief

Work from the kit folder. Use only what the brief and the tool API file say. Do not copy rules from another brief.

This skill builds the agent and saves it on Freya. Testing it and fixing what fails is the test-phone-agent skill's part: a saved agent is the first version, not the finished one.

## Steps

1. Note the time: `date`. A build may take 30 minutes at most, tests included: the test-phone-agent skill's runs come out of the same 30 minutes.
2. Read every brief file you were given in full, top to bottom. Do not search in it: a rule can sit in any paragraph. Then read `tools/openapi.json`. When a brief is raw material (a mail, a policy extract, a memo, a code list) instead of a numbered list of rules, write `tests/<slot>.facts.md` first: one numbered atomic fact per line with its file and date; a later record governs an earlier one (format in `docs/test-case-template-comprehensive.md`). `<slot>` is the brief's file name without `.md`.
3. Read `docs/workflow-format.md`, `docs/tools-and-code.md` and `docs/banking-customer-service-knowledge.md`.
4. List the banking concepts in the brief: products, processes, terms, regulations. For each one that the knowledge file does not cover, research it with WebSearch and WebFetch before you write anything. Learn what it means, how banks usually handle it, and what an agent must never say or do about it. Keep it short: a few searches per concept. Then say in a line or two per concept what you found and where, and build the agent with it.
5. Read `examples/base-agent.json`. It is a small working agent with two steps. Use it as the pattern for the JSON, not as the answer.
6. If `.freya-agents.json` already has an agent for this slot, or the brief builds on another brief whose agent is there, do not start from scratch: benchmark that agent first with the test-phone-agent skill and its `agent_id`, before changing anything. What passes stays; rewrite only what fails, with steps 7 and 8.
7. Write the workflow to `out/<slot>.workflow.json`.
   - One step per stage of the call. Identity comes first.
   - Move to the next step on a tool result, not on what the customer says.
   - Take every tool field and allowed value from `tools/openapi.json`.
   - Validate every write in code before the tool call: the date against the calendar and the deadline, the amount against the floor and the full amount, the product id against what `get_account` returned. The model's own arithmetic never reaches the bank.
   - Leave `agent_config` out.
8. Save it: `python3 -c "import freya,json,sys; print(json.dumps(freya.save_workflow(sys.argv[1], json.load(open(sys.argv[2])))))" <slot> out/<slot>.workflow.json`
   It prints `workflow_id` and `agent_id`. The same slot updates the same workflow.
9. Test the agent and improve it with the test-phone-agent skill. The build ends with that skill's final line, not here.

## Banking knowledge

`docs/banking-customer-service-knowledge.md` holds general banking principles. Follow them in every agent you build.

- It gives principles, not values. Every rule, number, date, limit, identity question and outcome comes from the brief and `tools/openapi.json`. When the brief and that file disagree, the brief wins.
- When the brief says nothing about an action, do not invent a rule for it. Leave the action out, or hand the call off the way the brief allows.
- What you research (step 4) explains a concept. It never sets a rule or a value for this bank and never overrides the brief or `tools/openapi.json`. Research is not verification.
- What that file calls the "Guard MD" is the workflow's `system_prompt` and step prompts. Write it there, not in a separate file.
- Its process (section 14) is the steps above for phases 1 to 7, and the test-phone-agent skill for testing and fixing (phases 8 and 9). Do not write role files or guard files. Test scenarios go in `tests/<slot>.cases.json` and nowhere else.
- Put its hard limits in routes, code and tool conditions, not only in prompts: no account data before identity passes, no success message before the tool result confirms it, no repeat of a write that timed out without checking first.
- Before each save, check the workflow against the "Final Design Principles" section of that file.

## Rules

- Never edit the agent on the platform by hand. Change the file and save it.
- When a tool call fails, the agent must say so. It must never tell the customer something is recorded when it is not.
- A customer that passes once can fail the next time. Prefer rules in routes and code over rules in prompts.
- An HTTP 5xx or a timeout from Freya or the bank is not a bug: it is transient. Wait a minute and run the same command again.

## Lessons

(none yet)
