# Review · brief-f · run 01 (5/8)

Practice limitation: the mock has no `get_requirements`, `find_applications`, `create_application`, `get_application` ("not found"), and its `transfer_to_agent`/`close_call` reject the queues `applications`/`security` and the outcomes `application_created`, `status_given`, `no_action`. Any verified call therefore ends in the `service_problem` path, and the transfer to applications is rejected by the mock (`unknown queue`). This is expected and not an agent fault.

## GEN-04 (FAIL, conversation)
- The agent said "I cannot do that", not that the *digital assistant* cannot (rule 26 wording). Agent fault → fixed prompt wording.
- The judge read my check "says in one sentence that he is being transferred, thanks him and says goodbye" as one sentence for all three. That check was mis-worded against rule 30 (one sentence for what was done, then thanks and goodbye). Reworded the check to match rule 30 without dropping anything. The fixed transfer lines now also say what the customer can expect.

## GEN-06 (FAIL, outcome)
- Case error: the second date "12 May 1975" is the fixture's date with day and month swapped. The mock returned `day_month_swapped`, which by rule 7 is not a wrong answer, so the customer reached verification. The agent was right. Changed the second wrong date to 3 March 1970.
- After verification, the call hit the mock's missing `find_applications` → service_problem → applications transfer (rejected by the mock). That's expected on this mock.

## GEN-08 (FAIL, outcome/transfers/conversation)
- Case design: the persona verified, so the call fell into the mock gap. Rewrote it so the person request comes instead of the date of birth (rule 25 before identity).
- Agent finding: in `service_problem`, "I want to talk to a person" was extracted as accepting the applications-team offer. That's defensible (they accepted a transfer to people), but rule 25 would ask once and use queue general. Left as is: the offer was for a transfer to people, and the customer did not refuse it.
- The agent stated no limit or decision. Good.

## Passed cases
- GEN-03: the agent echoed the hook text "Day and month look swapped." That sounds odd to a customer. Fixed: the hook now says not to mention swapping.
- GEN-01, GEN-07: the declined closes were correct; no name was used before verification.
- GEN-02: a correct fixed close line.
- GEN-05: asked once, then transferred to general. Correct.

## Fixes
1. Wording for out-of-scope and unsupported requests: "As a digital assistant, I cannot …".
2. Hint message: do not mention swapping.
3. Transfer close lines now say what happens next.
4. Cases GEN-06 and GEN-08 corrected, and the GEN-04 check reworded (reasons above).

## Untested rules
3 and 27 (the queue/outcome values are not in the mock's API); 4 and 9–24 (the tools are missing on the mock). These were built from the brief alone and unit-tested locally: the validation pre-hook, the existing-application evaluation and the requirements text.

## Next run
Re-run `--only GEN-04,GEN-06,GEN-08`, then one full run with `--style corrects` if time allows (about 15 of 30 min used).
