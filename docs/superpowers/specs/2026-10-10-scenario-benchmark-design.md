# Scenario generation, benchmark and self-improvement loop for the builder

**Date:** 2026-10-10
**Status:** Draft for review
**Scope:** the kit in `C:\Users\loseu\Desktop\build-the-builder`

## 1. Goal

Today the builder (`examples/agent_builder.py` + `.claude/skills/build-phone-agent`) tests the phone agent it builds only on the 13 hand-written practice customers in `public-test-set.json`. Those customers follow Brief A and Brief B. The final briefs have other rules, so their expected records do not apply there, and the builder will have nothing to test against.

After this change the builder:

1. Writes its own test scenarios from the brief, following a documented template, **before** it writes the workflow.
2. Runs them (and, for Brief A/B, the public customers too) with `tools/benchmark.py`, which uses the same simulation, judge and ledger scoring as `tools/run_cases.py`.
3. Reads an analysis report and every transcript (passed cases too) against the whole brief, fixes the agent, and decides itself how many runs to make within the time budget.
4. At the end of a practice run, reviews its own trace (summarised thinking, tool calls, errors, timing), writes a retrospective, and updates the skill with lessons that hold for any brief.

## 2. Constraints found while designing

| Finding | Consequence |
|---|---|
| The bank mock (`/v1/practice/sessions`) opens a session only for the 13 known case ids. Any other id, and any customer or product data sent with the request, is rejected or ignored (verified by probing). | A generated scenario cannot invent a bank customer. It **borrows** one of the 13 practice customers as its `fixture`: identity answers, products, amounts, `now` (always `2026-10-14T11:00`) and, for PUB-10, the injected `create_promise` failure. Everything else (what the customer does, the expected records, the judge checks) is new. |
| `verify_identity.field` in `tools/openapi.json` is an enum. A final brief may change the identity fields. | `benchmark.py --check` compares the fixture's identity fields with the enum and refuses to run scenarios that cannot be played on the mock, with a clear message. |
| The trace written by `agent_builder.py` has thinking blocks with empty text. The SDK omits thinking text unless `thinking={"type": "adaptive", "display": "summarized"}` is set (verified with a one-turn probe: a summary is returned). | `agent_builder.py` sets that option. The builder can then read its own summarised thinking from the trace. |
| Trace lines carry no timestamp; only the first line has the start time. | Each trace line gets `at` (wall clock) and `t` (seconds since start). |
| Hackathon rules: one builder run takes 30 minutes at most, tests included; after the final briefs open only bug fixes may go into the builder, nothing from a final brief. | The skill gives the builder a time budget, not a fixed run count. Skill self-editing happens only when the run is started with `--self-improve` (practice runs), and only with lessons that are general. |
| The git repository is rooted at the user's home directory and has no usable history. | Skill edits made by the builder are listed in the retrospective file so they can be reviewed without git. |

### Lessons taken from τ^τ-bench (arXiv:2609.04611)

The paper scores a *developer agent* by deploying the customer-service agent it built against held-out simulated users — the hackathon's setup. Its findings, and what this design does about each:

| Finding (paper) | What we do |
|---|---|
| A case passes only when the database state **and** what was said to the user match the annotation; messaging is judged by one rubric per rule, with the evidence named. | Same shape as the hackathon's ledger + judge. `checks` are written one rule per line, with the evidence the judge should look for. |
| Developers "cheat themselves" with self-authored tests: in the worked example all ten probes passed while two-fifths of the held-out suite failed on policy branches the probes never reached; elsewhere failing assertions were weakened, a rule was invented and tested, a mock replaced the real API. | Rule-coverage matrix (`--check --rules`): every numbered rule must be cited by a case or listed as unreachable. The report marks cases edited between runs. The skill forbids weakening a test and testing against anything but the real simulation. |
| The evidence is searched, not read: developers grep a corpus instead of reading it, open under 5% of the records, and ship agents that do not know the policy. | The skill: read every brief file in full, no grep; for raw-material briefs (mail, policy extract, memo, code list) extract numbered atomic facts with source and date first; a later record governs an earlier one. |
| Inherited code is rewritten without ever being run; working parts get rebuilt from scratch. | The skill: when an agent for the slot or for the parent brief already exists, benchmark it before changing anything. |
| A one-line architecture hint ("route by intent, review tool calls") doubled a score; deterministic policy guards around the model help. | The skill: validate every write in code before the tool call (date, amount, product id); routes and code over prompts. |
| Quiet API defects (post-commit timeout, async completion, pagination, field rename, date drift) go unnoticed; developers that guessed shipped wrong recovery. | The template's coverage list includes a tool answer that needs care; `--check` validates against the tool API's enums so a changed field is caught before a run; the knowledge doc's idempotency rules apply. |
| Developers ask the client almost nothing and ship around requirements silently. | No client here. The final line lists the brief points the builder could not settle and the rules no case could reach. |
| Budget and build time go unused: runs stop with hours left and requirements open. | "How many runs": do not stop with time left while something fails, is flaky or is untested. |
| The simulated user discloses progressively and never invents facts; voice variants spell identifiers digit by digit. | Scripts rely on the agent asking; `style` variants in the cases. |
| Metrics printed beside the quality number (spend, penalty) are ignored. | The report prints the promised total on passed cases (the organisers' first tie-breaker) and the timing flags next to the score. |

## 3. Components

### 3.1 `docs/test-case-template.md` (new)

English, like the other kit docs. Explains how to write `tests/<slot>.cases.json`:

- How a case is played: the persona model gets the script and the fixture's identity answers; the judge model checks `checks` against the transcript; the ledger is compared with `expected` exactly.
- The JSON shape, with every field explained (see 3.2).
- Fixture rules: which data comes from the fixture and cannot be changed; PUB-10 always fails the first `create_promise`; PUB-11..13 are the only multi-product customers; `now` is the same for everyone, so dates are computed from it with the brief's calendar.
- Writing `script`: every fact the customer will say must be in it (amounts, dates, answers, wrong answers), in order; the persona knows nothing of the brief; "Verified." means both questions answered right; third-party cases set `third_party: true` and say who answers. The persona discloses progressively: it answers what it is asked and volunteers nothing, so a script that needs the agent to ask for something tests that the agent asks.
- Writing `expected`: outcome and reason exactly as the brief's outcome table; promises/notes/callbacks/transfers as sets; product ids by position (`p1`, `p2`, …); absolute dates `YYYY-MM-DD`, times `HH:MM`.
- Writing `checks`: one rule per line, observable in the transcript, with the evidence the judge should look for; patterns such as "X not said before Y", "tool called exactly once", "the read-back names …". The judge grades only what is listed, so a case can pass with violations its checks do not name; the transcript review (3.7) is there for those.
- `forbidden_tools`: tools that must never appear in the ledger (checked exactly, not by the judge).
- `rules` (required): the rules the expectation rests on, as `<file-stem>:<number>` (`brief-a:19`, `brief-b:6`). When the brief does not number its rules (raw material: a mail, a policy extract, a memo, a code list), the builder first writes `tests/<slot>.facts.md`: one numbered line per atomic fact (`12. …`), each naming the file and the date it comes from; when records disagree, the later dated one governs. Cases then cite `<slot>.facts:12`.
- Coverage: every numbered rule (or fact) is cited by at least one case, or the builder lists in its final line the rules no case can reach with the 13 fixtures; `--check --rules` prints the uncovered ones. Families to make sure of: happy path; identity failure; third party; date edges (deadline, weekend, holiday, vague period); amount edges (floor, below floor, partial); hardship; already paid; restructuring; tool failure (fixture PUB-10); a tool answer that needs care (`ok: false`, a `hint`, an error inside a 200 response); multi-product when the brief has it; out-of-scope question; customer insists on something outside the brief; one or two `style` variants. 10–20 cases; one case may cite several rules.
- Two complete examples, one easy and one hard.

### 3.2 `tests/<slot>.cases.json` (written by the builder)

A JSON list. `<slot>` is the brief file name without `.md`, the same slot as the workflow.

```json
{
  "id": "GEN-04",
  "fixture": "PUB-06",
  "title": "Haggles below the floor, then accepts the floor",
  "family": "Amounts",
  "level": "hard",
  "rules": ["brief-a:26", "brief-a:27"],
  "style": "corrects",
  "third_party": false,
  "script": "Verified. Cannot pay the full amount. Offers 50 today. When told that cannot be recorded, accepts the floor today and confirms at the read-back.",
  "expected": {
    "outcome": "promise", "reason": null,
    "promises": [{"product_id": "p1", "amount": 637.5, "date": "2026-10-14"}],
    "notes": [], "callbacks": [], "transfers": []
  },
  "checks": ["the agent says 50 cannot be recorded", "the floor is offered once", "create_promise called exactly once"],
  "forbidden_tools": ["transfer_to_agent"]
}
```

Required: `id` (unique, `GEN-nn`), `fixture`, `title`, `family`, `level` (`easy|medium|hard`), `rules` (non-empty), `script`, `expected`, `checks`. Optional: `brief` (defaults to the fixture's brief letter; only used for the persona tag), `style` (one of `run_cases.STYLES`), `third_party`, `forbidden_tools`. Not allowed: `variables`, `identity`, `products`, `faults` — `--check` reports them as errors, because they come from the fixture.

### 3.3 `tools/benchmark.py` (new)

```
python3 tools/benchmark.py --fixtures
python3 tools/benchmark.py --check --cases tests/<slot>.cases.json [--rules briefs/brief-a.md] [--rules tests/<slot>.facts.md]
python3 tools/benchmark.py <agent_id> --cases tests/<slot>.cases.json [--rules FILE ...] [--public A|B] [--only ID,ID] [--reps N] [--style S]
```

**`--fixtures`** prints the 13 practice customers from `public-test-set.json`: id, brief, name, `now`, identity answers, products with their ids (`p1`…) and all fields, faults, and the public case's title. No network.

**`--check`** validates the file without running it and prints a coverage summary (cases by family, by fixture, by outcome, styles used). With `--rules FILE` (repeatable) it extracts the numbered rules of each file — lines that start with `N.`; the id is `<file-stem>:<N>`, so `briefs/brief-a.md` gives `brief-a:1` … `brief-a:47` — and prints the rules cited by no case. A cited id that exists in no given file is an error. Errors (abort a run): missing or unknown fields, duplicate ids or ids colliding with public ids, unknown fixture, bank-data fields present, `product_id` not in the fixture, `outcome` / note `reason` / `queue` not in the enums of `tools/openapi.json`, bad date or time format, unknown `style` or tool name, empty `script` or `checks`, fixture identity fields not in the `verify_identity.field` enum. Warnings: `reason` empty for an outcome that the tool API says needs one (the exempt outcomes are read from `close_call.reason`'s description, never hard-coded).

**A run** performs `--check`, merges each case with its fixture's bank data, adds the public cases of `--public` if given, and calls `run_cases.run_once` (same personas, same simulation settings, same judge, same `score_ledger`). Then it adds the `forbidden_tools` check from the ledger calls, fetches the transcript of every call — passed or failed — writes the artefacts below, prints the report path, and prints the time used since the builder started (read from the newest trace's first line, when there is one).

Artefacts under `results/bench/<slot>/`, where `<slot>` is the cases file name without `.cases.json`:

- `history.jsonl` — one line per run: time, agent id, label, reps, per-case pass and reasons. The run number is the line count.
- `run-NN.json` — the full rows (tools, calls with args and results, judge reason, call id, slowest turn, ended reason).
- `run-NN/<case-id>.md` — one per case, passed or failed: the case's title, rules, result and reasons, then the user and assistant lines with the engine events that matter between them (`node_enter`, `function_call_start` args, `function_call_complete` result cut to 300 characters, `route_evaluated` as "from → target: reason"). No variable tables.
- `run-NN.transcripts.md` — all of the above in one file, failed cases first, one heading per case, so the builder can read a whole run in one go. With `--reps`, a case whose reps disagree gets one file per rep (`run-NN/<case-id>.rep<k>.md`), and the row shown in the report is the first failing rep's. Transcripts are kept compact: a tool call shows only its request body, a code step shows `(code)`, and a node change shows once, on its route line.
- `run-NN.md` and `latest.md` (copy) — the analysis report.
- One line appended to `results/log.jsonl`, like `run_cases.py`.

The report (`run-NN.md`):

1. Header: slot, agent id, run number, time, duration, style, reps.
2. Score: generated x/y, public p/q, total; the total amount promised on passed cases (the organisers' first tie-breaker); against the previous run: fixed, regressed, still failing.
3. History table: every case across all runs of this slot (✓ ✗ –), with a "flaky" mark when the reps of one run disagree or the case's outcome flipped twice over the last three runs (✓ ✗ ✓ or ✗ ✓ ✗), and a "changed" mark when the case's `script`, `expected` or `checks` differ from the previous run (a weakened test stays visible).
3a. Rule coverage, when `--rules` was given: the rules cited by no case.
4. Failure categories with counts: `outcome`, `promises`, `notes`, `callbacks`, `transfers`, `not_closed`, `before_identity`, `tools_while_unreached`, `forbidden_tool`, `conversation` (judge), plus the flags `hung_up` and `slow`.
5. Per failed case: title, family, level, fixture, rules, expected vs got (the `score_ledger` reasons and the judge's reason), the tool trace with arguments and any tool error, forbidden-tool hits, slowest turn and ended reason, transcript path.
5a. Per passed case, one line: turns, tool sequence, slowest turn, transcript path.
6. Timing: median slowest turn, hung-up calls, the slow-model warning as in `run_cases.py`.
7. What this run suggests — deterministic, from the data: regressions to fix first; failures to re-run with `--only`; flaky cases to re-run with `--reps`; cases changed since the previous run; whether everything passed once (a hint) or in two full runs in a row (an `--only` run in between neither counts nor breaks the streak; after an `--only` run that passes, the suggestion is one full run before finishing); styles not run yet; whether a full run still fits in the 30-minute budget (minutes used; the duration of the last full run per rep, with a 3-minute margin, and the cost of `--reps 2`); and a note when the model was slow, so a hang-up may pass on a re-run. The builder decides; the report lays out the options.

The report writer is a pure function over the run JSON and the history, so it can be tested without a simulation.

### 3.4 `tools/trace_review.py` (new)

```
python3 tools/trace_review.py [traces/<file>.jsonl] [--out reports/<file>.digest.md]
```

Defaults to the newest trace (the builder's own run, which is still being written). Writes a digest of at most ~120 KB (the builder reads it page by page) and prints its path and the totals.

- Header: start, model, briefs, `self_improve`, turns so far, elapsed (or "n/a" for old traces without `at`).
- Totals: tool calls by name, tool errors, benchmark and test runs (Bash commands with `benchmark.py` or `run_cases.py`), workflow saves (`save_workflow`), files written or edited, thinking tokens (sum of `thinking_tokens` deltas).
- Timeline, one entry per assistant message: `#n [+mm:ss]`, thinking summary (≤ 400 chars), text (≤ 300 chars), tool calls in compact form (Bash: first line of the command; Write/Edit: path and size), result: error text (≤ 300 chars) for errors, otherwise the length, plus any `PASS`/`FAIL`/`passed` lines from test output.
- Flags: identical commands run more than once, tool errors, test runs, edits made after the last test (untested changes).

### 3.5 `tools/run_cases.py` (small changes, CLI unchanged)

- Sessions are opened with `{"case": c.get("fixture", c["id"])}`.
- Persona creation moves from `main()` into `ensure_personas(cases, style) -> {case_id: persona_id}`; `main()` calls it.
- Each row also carries `calls` (the ledger's calls with args and results).

### 3.6 `examples/agent_builder.py` (small changes)

- `thinking={"type": "adaptive", "display": "summarized"}` in `ClaudeAgentOptions`.
- Every trace line gets `at` and `t`; the first line also records `self_improve`.
- New flag `--self-improve` (before the brief paths). When set, the prompt adds: "This is a practice run. When the build is done, do the Retrospective step of the skill." Without it the builder stops after the final benchmark, which is what the final needs.
- `max_turns` 150 → 300: scenario writing, several benchmark runs and the retrospective need more turns.

### 3.7 `.claude/skills/build-phone-agent/SKILL.md`

Steps become:

1. Note the time with `date`. A build may take 30 minutes at most, tests included.
2. Read every brief file in full, no searching: a rule can sit in any paragraph. Then `tools/openapi.json`. When a brief is raw material rather than a numbered list, write `tests/<slot>.facts.md` first (format in `docs/test-case-template.md`).
3. Read `docs/workflow-format.md`, `docs/tools-and-code.md`, `docs/banking-customer-service-knowledge.md`, `docs/test-case-template.md`.
4. Research the concepts the knowledge file does not cover (existing step).
5. Read `examples/base-agent.json`.
6. Write the test cases: `benchmark.py --fixtures`, then `tests/<slot>.cases.json` from the brief and the template, before the workflow. `benchmark.py --check --cases … --rules <each brief file and the facts file>`; fix every error; cover every uncovered rule or note why no fixture can reach it.
7. If `.freya-agents.json` already has an agent for this slot, or the brief builds on another brief whose agent is there, benchmark that agent first, before changing anything: the score of the inherited agent says what to keep.
8. Write the workflow (existing bullets, plus: validate every write in code before the tool call — the date against the calendar and the deadline, the amount against the floor and the full amount, the product id against `get_account`; the model's own arithmetic never reaches the bank).
9. Save it (existing).
10. Benchmark it: `benchmark.py <agent_id> --cases tests/<slot>.cases.json --rules …`, with `--public A` or `--public B` only when the brief is `briefs/brief-a.md` or `briefs/brief-b.md` (the public customers' expected records follow those briefs and no other). Foreground, wait.
11. Read `results/bench/<slot>/latest.md` and `run-NN.transcripts.md`, write `run-NN.review.md`, fix (sections "Reading a benchmark report" and "Transcript review").
12. Decide the number of runs yourself (section "How many runs").
13. Finish with one line: `workflow_id`, `agent_id`, the score of the last full run (generated and public), the number of runs, the rules no case reaches, and the brief points you could not settle.
14. Retrospective, only when the request asks for it (section "Retrospective").

New sections:

- **Reading a benchmark report.** For each failed case, read the rules it cites again and decide whether the agent or the case is wrong. Public cases are never wrong. Change a generated case only when the brief shows its expectation is wrong, and say so in the review file; never weaken a check or an expectation to make a run pass, and never test against anything but the real simulation. Find the cause in the transcript (`route_evaluated`, tool arguments, what the agent said). Fix the regressions first. Make the smallest fix; prefer routes, code and tool conditions over prompts. A flaky case counts as failing: the final runs every customer three times.
- **Transcript review.** After every full run, read `run-NN.transcripts.md` — passed cases too — against the whole brief, not only against the case's checks. For each case note: rules broken that no check named; anything the agent claimed without a tool result behind it (recorded, scheduled, transferred); turns a customer would find unclear; the turn before each hang-up; places where the customer's phrasing confused the agent. Write `results/bench/<slot>/run-NN.review.md`: one block per case with the findings, and at the end the fixes you decided on and the cases you will add for rules the run showed untested. A finding from a passed case is fixed with the same priority as a failure: the final customers' checks are not yours.
- **How many runs.** After every run you decide whether to run again, what to run, and when to stop. Decide from three things: the report's "What this run suggests" section, your transcript-review findings, and the clock. Write the decision and its reason at the end of the review file. Rules of thumb: a run takes 3–11 minutes; after a fix, re-run the failed cases with `--only`, then one full run before finishing to catch regressions; one pass is a hint, not proof, so when everything passes and time remains, run again (`--reps 2`, or a `--style` run) rather than stopping. Do not stop with time left while a case fails, is flaky, is untested after a change, or a review finding is unfixed. Stop when time is nearly out, when two consecutive full runs pass everything with no review findings, or when a fix round changed nothing.
- **Retrospective.** Run `trace_review.py`, read the digest. Write `reports/<slot>-retro.md`: score trend across the runs; what cost time or turns, with step numbers from the digest (repeated commands, errors, misread rules, guesses); lessons for any brief; lessons for this brief only. Then update the `## Lessons` section of this skill: one line per lesson; general only — no rule, number, date, name, product, queue, outcome value or holiday from any brief; at most 12 lines; merge, replace or drop old ones; touch no other section. List in the retro exactly which lesson lines were added, changed or removed.
- **`## Lessons`** — empty at first.

The existing "Banking knowledge" bullet "Do not write role files, guard files or test plans next to the workflow" becomes "Do not write role files or guard files. Test scenarios go in `tests/<slot>.cases.json` and nowhere else."

## 4. Data flow

```
brief ──► builder ──► tests/<slot>.cases.json ──► benchmark --check
                 └──► out/<slot>.workflow.json ──► freya.save_workflow ──► agent_id
benchmark <agent_id> --cases … [--public A]
   ├─ merge cases with fixtures (public-test-set.json)
   ├─ run_cases.ensure_personas → run_cases.run_once (Freya simulation + judge + ledger score)
   ├─ forbidden_tools check, transcripts of failed calls
   └─ results/bench/<slot>/{history.jsonl, run-NN.json, run-NN.md, latest.md, run-NN/*.transcript.md}
builder reads latest.md + run-NN.transcripts.md ──► writes run-NN.review.md ──► edits workflow / adds cases ──► save ──► benchmark (--only, then full) … until it stops
--self-improve: trace_review.py ──► reports/<trace>.digest.md ──► reports/<slot>-retro.md + SKILL.md ## Lessons
```

## 5. Error handling

- `--check` errors abort before any simulation; the message names the case id and the field.
- Fixture identity fields not in the `verify_identity` enum: an error for every case except third-party ones (they never reach `verify_identity`), with "this scenario cannot be played on the mock with this tool API"; the skill tells the builder to keep the playable cases and build the rest from the brief.
- An HTTP 5xx or a timeout from Freya or the bank: one clear line saying it is usually transient and to re-run the same command, instead of a traceback. The raw run record (`run-NN.json` with every rep's rows) and the history line are written before transcripts and the report are rendered, so a rendering failure cannot lose a finished simulation.
- Simulation failures (`status` not `completed`, missing judge verdict, transcript fetch errors) are reported per case as they are in `run_cases.py`; the report is still written.
- `trace_review.py` tolerates old traces (no `at`, empty thinking) and a trace that is still being written (partial last line is skipped).
- The builder is told that a `benchmark.py` crash is a bug to report in its final line, not something to work around by editing the tool.

## 6. Testing the tooling

- `--fixtures`: output lists 13 customers with product ids and the PUB-10 fault.
- `--check`: a deliberately broken file (duplicate id, unknown fixture, `products` present, bad enum, bad date, missing `rules`) reports each error; a good file passes and prints coverage.
- `--check --rules briefs/brief-a.md --rules briefs/brief-b.md`: 47 + 11 rule ids extracted; uncovered ones listed; a cited id that exists in no file is an error.
- Report writer: fed a fabricated run dict and a two-line history, it produces the sections above with fixed/regressed/flaky computed correctly.
- `trace_review.py` on `traces/20261010-213902.jsonl` (old format) and on a trace written by the new `agent_builder.py`.
- One real benchmark run with two or three generated cases against the existing Brief A agent (`c93d5852-…`), 3–5 minutes, checks the end-to-end path, the per-case transcript files (passed cases too), the bundle, the history and the "changed" mark on a second run after editing a case.
- A full `agent_builder.py --self-improve briefs/brief-a.md` run is the acceptance test; it costs about 30 minutes and is started by the user.

## 7. Out of scope

- A local bank mock or a chat-API test harness. The real simulation chain is what the organisers score.
- Changing `freya.py`, the agent model, or how `run_cases.py` is used from the command line.
- Automatic skill edits during final runs.

## 8. Open points

- None blocking. The number of generated cases (10–15) and the lesson cap (12 lines) are guidance in the skill and can be tuned after the first practice runs.
