## GEN-01 — Wants an address change, refuses the security questions twice
result: PASS
fixture PUB-01 · family Identity refusal · level easy · rules brief-f:1, brief-f:2, brief-f:5, brief-f:8, brief-f:29
turns 7 · slowest agent turn 9.0 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** Hello, I have moved house and I would like to change my postal address.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You would like to change your postal address; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** I do not want to give personal details on the phone.
**agent:** These questions are necessary to protect your account. Could you please provide your date of birth?
**customer:** I am still not comfortable sharing my personal information over the phone.
    ⚙ wrap_up_call {"customer_id": "f_b02a98cd44bc", "type": "address_change"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"reason": "declined", "outcome": "not_verified", "customer_id": "f_b02a98cd44bc"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I could not take your request because the security check was not completed, so you can call us back or visit a branch. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
