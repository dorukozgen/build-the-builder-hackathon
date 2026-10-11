## GEN-45 — Postcode given in pieces
result: FAIL: outcome ('not_verified', 'failed'), expected ('application_created', None); conversation: The assistant never read back a postcode because the user failed the identity verification process. The conversation ended at Message 10 after multiple failed attempts to verify the user's date of birth, so the specific success criterion regarding postcode 20121 was not met.; applications [], expected ['address_change']
fixture PUB-02 · family Style · level medium · rules brief-f:12, brief-f:13, brief-f:16
turns 11 · slowest agent turn 14.4 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address on my account.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a change of your postal address; however, I first need to verify your identity, so please provide your date of birth.
**customer:** The second of November.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "0000-11-02", "customer_id": "f_c6b14e6e148d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 2, "all_verified": false, "what_to_do_next": "That answer is not correct. Do not reveal the right answer or give hints. Ask the same question again."}, "message": "Successfully executed POST request", "status_code": 
**agent:** That answer is not correct. Could you please provide your date of birth again?
**customer:** Nineteen seventy-nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "0000-00-1979", "customer_id": "f_c6b14e6e148d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": false, "error": "answer is not a date. Send it as YYYY-MM-DD.", "what_to_do_next": "The answer could not be checked. This is NOT a wrong answer. Ask the same security question again."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** I'm sorry, I couldn't process that. Could you please provide your full date of birth?
**customer:** The second of November.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "0000-11-02", "customer_id": "f_c6b14e6e148d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 1, "all_verified": false, "what_to_do_next": "That answer is not correct. Do not reveal the right answer or give hints. Ask the same question again."}, "message": "Successfully executed POST request", "status_code": 
**agent:** That answer is not correct. Could you please provide your date of birth again?
**customer:** The second of November.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "0000-11-02", "customer_id": "f_c6b14e6e148d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 0, "all_verified": false, "what_to_do_next": "The security check has failed. Say nothing about the account."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → id_failed: Identity check failed id_state == 'failed'
    ⚙ api_call {"reason": "failed", "outcome": "not_verified", "customer_id": "f_c6b14e6e148d"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ id_failed → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I am sorry, I could not verify your identity, so I cannot take the application on this call. You can call us back or visit a branch. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
