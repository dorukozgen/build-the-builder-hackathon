# Review, runs 23 to 26 (agent af6616bb, versions 1 to 3)

## Run 23 (v1, full): 61 / 63, universal 13 / 13
- GEN-24: agent wrong. After identity it skipped find_applications and get_requirements and asked an invented "which address" question (rules 9, 12). Fix: the first request's type is extracted at the opening and find_applications runs engine-side in a passthrough node (first_find) before the service step.
- GEN-50: case wrong in wording. The agent re-read 4500 and waited for yes; the judge took "after the first 'no'" to mean the customer's "No, thank you" to the optional fields. The check now says what rules 17 and 19 require, no weaker.

## Run 24 (v2, --only 6): 6 / 6
- Finding: the model calls find_applications a second time after the engine's call. That is a needless ledger entry. A prompt fix was attempted, but its Edit failed, so it never reached v3. Still open.

## Run 25 (v2, full): 38 / 40 scored, 23 not played (the tunnel refused connections at 16 calls at a time)
- GEN-33: agent wrong. A customer reading out their own PIN set off the security global ("code given to someone"). Fix in v3: the intent now names a code given to another person and excludes data read to the assistant.
- GEN-10: judge reading. The transfer tool ran, and then the engine spoke the fixed closing line. The judge read the line as a claim made before the tool and the engine's end_call as coming after close_call. Not settled. A possible fix: speak a short "I will transfer you now" before the tool call.

## Run 26 (v3, --only 5): 4 / 5. GEN-33 passes; GEN-10 still fails as above.

## Decision
The clock is at 26 of 30 min, so there is no further run. v3 has no full run. 23 cases are unplayed on v2/v3 after run 23.
