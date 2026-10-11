## GEN-07 — Address change, gives the date of birth, refuses the phone digits
result: PASS
fixture PUB-08 · family Identity refusal · level medium · rules brief-f:5, brief-f:8, brief-f:16
turns 9 · slowest agent turn 19.8 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I would like to change my postal address.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a change of your postal address; however, I first need to verify your identity, so please provide your date of birth.
**customer:** the twenty-eighth of April one nine nine three
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1993-04-28", "customer_id": "f_99ac49addbc5"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Please provide the last four digits of the phone number on file.
**customer:** I am not going to give you that information.
**agent:** These questions are necessary to protect your account. Would you like to provide the last four digits of your phone number?
**customer:** No, I will not give those digits to you.
    ⚙ wrap_up_call {"customer_id": "f_99ac49addbc5", "type": "address_change"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"reason": "declined", "outcome": "not_verified", "customer_id": "f_99ac49addbc5"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I could not take your request because the security check was not completed, so you can call us back or visit a branch. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
