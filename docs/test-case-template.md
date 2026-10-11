# Test cases for a phone agent

The builder writes `tests/<slot>.cases.json` before it writes the workflow: a JSON list of cases, one per scenario, in the shape of `public-test-set.json` plus three fields. `tools/benchmark.py` checks the file, runs it against the agent on Freya's simulator and scores it the way the organisers do. `<slot>` is the brief's file name without `.md`.

Every `--check` that passes, and every run, also writes `tests/<slot>.test-set.json`: the same cases with the fixture's `variables`, `identity`, `products` and `faults` merged in, in the key order of `public-test-set.json`, the generated fields (`fixture`, `rules`, `forbidden_tools`, ...) after them. It is derived: never edit it, edit the cases file and run `--check` again. It is what the simulator actually plays, and `python3 tools/run_cases.py <agent_id> --cases tests/<slot>.test-set.json` runs it with the kit's own runner.

## How a case is played

1. `benchmark.py` opens a session at the bank mock for the case's **fixture**, one of the 13 practice customers. The mock knows only those 13: their identity answers, products, amounts, `now` (`2026-10-14T11:00`, a Wednesday, the same for everyone) and, for PUB-10, a `create_promise` that fails the first time. `python3 tools/benchmark.py --fixtures` lists them with the product ids `get_account` returns (`p1`, `p2`, …).
2. A persona model plays the customer. It gets the fixture's name and identity answers and your `script`. It knows nothing else: not the brief, not the amounts, not the dates. It answers what it is asked and volunteers nothing; `run_cases.py` holds its exact instructions and the `style` variants.
3. The phone agent calls the bank's tools. Every call lands in the ledger.
4. Scoring. The ledger must equal `expected` exactly: outcome and reason, the set of promises, notes, callbacks and transfer queues; `close_call` must be the last call; `get_account` or `create_promise` before identity was verified fails the case; identity or account tools in a `not_reached` call fail it. A judge model reads the transcript against `checks`. Tools in `forbidden_tools` must not appear in the ledger. A case passes only when all of this holds.

## The shape

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
  "script": "Verified. Cannot pay the full amount. Offers 50 today. When told that cannot be recorded, accepts the minimum payment today and confirms at the read-back.",
  "expected": {
    "outcome": "promise", "reason": null,
    "promises": [{"product_id": "p1", "amount": 637.5, "date": "2026-10-14"}],
    "notes": [], "callbacks": [], "transfers": []
  },
  "checks": ["the agent says 50 cannot be recorded", "the floor is offered once", "create_promise called exactly once"],
  "forbidden_tools": ["transfer_to_agent"]
}
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique, `GEN-01`, `GEN-02`, … Never a public id. |
| `fixture` | yes | The practice customer whose bank data the case borrows. |
| `title` | yes | One line, what the customer does. |
| `family` | yes | The scenario family (see Coverage). Use `Third party` for someone else answering. |
| `level` | yes | `easy`, `medium` or `hard`. |
| `rules` | yes | The rules the expectation rests on, `<file-stem>:<number>`. |
| `script` | yes | What the customer does and says, in order, with every fact. |
| `expected` | yes | What the bank's records must show afterwards. |
| `checks` | yes | What the judge verifies in the transcript, one rule per line. |
| `style` | no | `pieces`, `corrects`, `talkative`, `asks_back` or `in_words`: how the customer talks. |
| `third_party` | no | `true` when someone other than the customer answers. |
| `forbidden_tools` | no | Tools that must never be called in this case. |
| `brief` | no | Only a tag; defaults to the fixture's brief letter. |

Do not write `variables`, `identity`, `products` or `faults`: they come from the fixture and `--check` rejects them.

## Choosing a fixture

- The identity answers, products, amounts, days late and floor fields are the fixture's. A scenario about three products needs PUB-11 or PUB-12; two products, PUB-13; a failing promise service, PUB-10 and nothing else. PUB-10 always fails the first `create_promise`, so every PUB-10 case is a tool-failure case.
- Dates are computed from `now`, 14 October 2026, 11:00, a Wednesday, with the brief's calendar: its holidays, deadlines, bands and the meaning it gives to words like "next Friday". Write the resulting dates as `YYYY-MM-DD`.
- A fixture can carry several cases. `--fixtures` names the public case that uses it; write different scenarios, not copies of it.

## Writing `script`

- Say what the customer does, in order, with every number, date and answer they will say. The persona cannot invent anything: a fact that is not in the script does not exist for it.
- "Verified." is shorthand: the persona answers both identity questions correctly. For a failing identity, say which answers are wrong and how often ("gives 1987 as the year twice, then the right date").
- The persona discloses progressively. If the scenario needs the agent to ask something, write what the customer answers *when asked*, not that they say it on their own. That tests that the agent asks.
- "Confirms at the read-back" makes the persona say yes when the agent reads the promise back.
- For someone else answering, set `third_party: true` and say who answers and what they know ("her husband; offers to pay himself; says she is back tomorrow at eleven").
- Keep it to what matters; with a `style`, the persona pads the conversation itself.

## Writing `expected`

- `outcome` and `reason` exactly as the brief's outcome table and the tool API's values; `reason` is null only when the brief gives none for that outcome.
- `promises`: one per product with `product_id`, `amount` (a number, the amount the brief says gets recorded), `date` (`YYYY-MM-DD`). Empty when no promise is recorded.
- `notes` (`product_id`, `reason`), `callbacks` (`date`, `time` as `HH:MM`), `transfers` (`queue`): empty lists when none.
- Everything is compared as a set with the ledger: an extra promise or a missing note fails the case.

## Writing `checks`

- One rule per line, observable in the transcript, with what the judge should look for: "the agent does not say the word 'collections' before both identity answers passed", "create_promise is called exactly once", "the read-back names both dates", "after the failed call the agent does not say 'recorded' until the retry succeeds".
- The judge sees only the transcript. No checks about internal state, and none about the ledger (that is `expected`'s job).
- The judge grades only what is listed, so a case can pass with violations no check names. The builder's transcript review covers those; `checks` are for the rules this case is about.

## `rules`

- `"brief-a:19"` is rule 19 of `briefs/brief-a.md`: the line that starts with `19.`. `python3 tools/benchmark.py --check --cases … --rules briefs/brief-a.md` lists the rules no case cites.
- When a brief is raw material with no numbered rules (a mail, a policy extract, a memo, a code list), write `tests/<slot>.facts.md` first: one numbered line per atomic fact, `12. <the fact> — <file>, <date>`. When two records disagree, the later dated one governs; say so in the line. Cite `"<slot>.facts:12"` and pass `--rules tests/<slot>.facts.md`.

## Coverage

- Every rule cited by at least one case, or named as unreachable with these fixtures in the builder's final line.
- Families to make sure of: happy path; identity failure (wrong answers, refusal); third party; date edges (the deadline, a weekend, a holiday, a vague period, "next" versus "this"); amount edges (the floor, below the floor, a partial amount); hardship; already paid; restructuring; tool failure (fixture PUB-10); a tool answer that needs care (`ok: false`, a `hint`, an error inside a 200 response); multi-product when the brief has it; a question outside the task; a customer who insists on something the brief does not allow; one or two `style` variants.
- 10 to 20 cases. One case may cite several rules. Prefer one case per decision branch over near-copies.

## Two examples

The examples follow Brief A and its practice customers. Your expectations follow your brief.

Easy, fixture PUB-01 (Daniel Reyes, credit card ending 4821, 420.00 past due, 6 days late, minimum payment 126.00):

```json
{
  "id": "GEN-01", "fixture": "PUB-01", "title": "Asks whether it is a robot, then pays in full on Friday", "family": "Happy path", "level": "easy",
  "rules": ["brief-a:4", "brief-a:28", "brief-a:19"],
  "script": "Asks whether he is talking to a robot, then confirms he is Daniel Reyes. Date of birth 14 March 1988, last four digits 4471. Cannot pay today. Can pay the full amount this Friday. Confirms at the read-back.",
  "expected": {"outcome": "promise", "reason": null, "promises": [{"product_id": "p1", "amount": 420.0, "date": "2026-10-16"}], "notes": [], "callbacks": [], "transfers": []},
  "checks": ["the agent says it is a digital assistant when asked whether it is a robot", "both security questions passed before get_account", "the read-back names Friday 16 October and 420"],
  "forbidden_tools": ["transfer_to_agent", "schedule_callback"]
}
```

Hard, fixture PUB-13 (Elena Rossi; p1 credit card 300.00 past due, 4 days late, minimum 90.00; p2 personal loan 900.00 past due, 20 days late, instalment 300.00):

```json
{
  "id": "GEN-09", "fixture": "PUB-13", "title": "Pays the card in full, cannot pay the loan", "family": "Multi-product", "level": "hard", "style": "in_words",
  "rules": ["brief-b:4", "brief-b:7", "brief-b:8"],
  "script": "Verified. Cannot pay everything today. For the credit card, can pay the full amount today. For the loan, says she cannot pay anything this month and refuses when offered the instalment. Confirms the card promise at the read-back.",
  "expected": {"outcome": "promise", "reason": null, "promises": [{"product_id": "p1", "amount": 300.0, "date": "2026-10-14"}], "notes": [{"product_id": "p2", "reason": "refused"}], "callbacks": [], "transfers": []},
  "checks": ["both products are stated before any amount is asked for", "the loan's instalment is offered once before the refusal is recorded", "the read-back names only the card promise", "add_note is called for the loan with reason refused"]
}
```
