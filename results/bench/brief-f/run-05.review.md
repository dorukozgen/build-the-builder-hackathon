# brief-f · run 5 review (manual run, 16 cases, own mock through an ngrok tunnel)

Score 13/16. Runs 1–4 were the builder's own, on the organisers' mock, with 8 cases that never reached the application tools.
Run 5 adds GEN-09…GEN-16 (from `cases-to-run.json`) and plays all 16 against `tools/mock_bank_f.py` (brief-f's seven tools,
`tools/openapi-f.json`), so the core flow ran end to end for the first time. The "changed" marks on GEN-01…08 are an artefact:
the case signature now includes the `backend` field, which changed every hash once; the cases themselves were not edited.

## Failed cases

- **GEN-09** stolen card → security. The agent recognised the matter and started `transfer_to_agent` with queue `security`
  (transcript shows the call, no result), but the mock log shows only the session and `close_call` for this customer: the
  transfer request never arrived. The `security_transfer` node fires the transfer as a pre-action and moves on with an
  `always` transition before the call completes. Fix: route on the transfer's result (`transfer_to_agent_response.data.ok`)
  before closing, as the other transfer paths do. Agent defect (brief-f rule 27).
- **GEN-15** vague amounts. The agent asked for the amount a fourth time before offering the transfer; rule 13 says after
  three answers that do not fit. Fix: count invalid answers per field in code, not in the prompt. The judge's second point
  ("close_call not last") refers to Freya's own `end_call` event after `close_call`; every passed case has the same event, so
  it is judge noise, not a finding.
- **GEN-16** timeout idempotency. `create_application` never reached the bank: the workflow's own pre-validation rejected
  `reason=expired` and `delivery=home` with "must be one of:  (got …)", an empty options list. The requirements come back as
  `fields[].options` (a JSON array); the validation code reads the options from the flattened variable table and gets
  nothing. Fix: parse `fields` from the `get_requirements` result once in code and keep the `options` arrays. Until then the
  timeout fault (PUB-10's first `create_application` is slow but goes through) cannot be exercised. Also: two fields were
  asked in one turn (rule 12). Agent defect.

## Passed cases worth a look

- GEN-14 (duplicate prevention) passed: `find_applications` saw the seeded `in_review` application and the agent reported it
  without creating another. The `backend` mechanism works.
- GEN-04/05/08/10/11: transfers to `general` and the human-handoff wording are fine.

## Case changes

None of the 16 cases conflicts with `tools/openapi-f.json`; none was edited for this run. GEN-14's `backend` and
GEN-14/15/16's `expected.applications` were added when the cases were merged, before the run.

## Next run

Not run: the three failures are workflow fixes the builder has to make, not case fixes. To repeat the run: start
`python tools/mock_bank_f.py`, open `ngrok http 8765`, put the new tunnel host into the workflow's tool URLs and
`tools/openapi-f.json`, save the workflow, then
`python tools/benchmark.py <agent_id> --cases tests/brief-f.cases.json --rules briefs/brief-f.md --openapi tools/openapi-f.json --host <tunnel>`.
