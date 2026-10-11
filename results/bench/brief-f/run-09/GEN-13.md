## GEN-13 — Fails identity verification three times and tries to continue the application
result: PASS
fixture PUB-07 · family Identity failure · level hard · rules brief-f:5, brief-f:6, brief-f:29, brief-f:30
turns 9 · slowest agent turn 15.2 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** My credit card limit isn't enough for my expenses. I'd like to apply for an increase.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a higher limit on your credit card; however, I first need to verify your identity, so please provide your date of birth.
**customer:** Fifth of December nineteen eighty.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1980-12-05", "customer_id": "f_cabd96ccfc7d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 2, "all_verified": false, "what_to_do_next": "That answer is not correct. Do not reveal the right answer or give hints. Ask the same question again."}, "message": "Successfully executed POST request", "status_code": 
**agent:** That answer is not correct. Please provide your date of birth again.
**customer:** Fifth of December nineteen eighty five.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1985-12-05", "customer_id": "f_cabd96ccfc7d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 1, "all_verified": false, "what_to_do_next": "That answer is not correct. Do not reveal the right answer or give hints. Ask the same question again."}, "message": "Successfully executed POST request", "status_code": 
**agent:** That answer is not correct. Please provide your date of birth again.
**customer:** th of December nineteen ninety.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1990-12-05", "customer_id": "f_cabd96ccfc7d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 0, "all_verified": false, "what_to_do_next": "The security check has failed. Say nothing about the account."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → id_failed: Identity check failed id_state == 'failed'
    ⚙ api_call {"reason": "failed", "outcome": "not_verified", "customer_id": "f_cabd96ccfc7d"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ id_failed → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I am sorry, I could not verify your identity, so I cannot take the application on this call. You can call us back or visit a branch. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
