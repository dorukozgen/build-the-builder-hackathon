## GEN-44 — Limit amount in words
result: PASS
fixture PUB-12 · family Style · level medium · rules brief-f:12, brief-f:15, brief-f:19
turns 16 · slowest agent turn 13.4 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I would like to increase my credit limit.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a higher limit on your credit card; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** the nineteenth of October one nine eight three.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1983-10-19", "customer_id": "f_ec10e149e811"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Could you now please provide the last four digits of the phone number we have on file for you?
**customer:** four four one zero.
    ⚙ verify_identity {"field": "phone_last4", "answer": "4410", "customer_id": "f_ec10e149e811"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "limit_increase", "customer_id": "f_ec10e149e811"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "limit_increase", "customer_id": "f_ec10e149e811"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Thank you, Mr Bell. What limit would you like, as an amount?
**customer:** seven thousand five hundred.
    ⚙ check_field {"customer_id": "f_ec10e149e811", "type": "limit_increase"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
**agent:** Would you like to provide any of these optional details: the last four digits of the card, or your monthly net income?
**customer:** No, thank you.
    ⚙ check_field {"customer_id": "f_ec10e149e811", "type": "limit_increase"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
    ↪ collect → confirm: All fields collected fields_state == 'complete'
**agent:** I have the requested limit as 7500. Shall I submit this application?
**customer:** Yes, I confirm.
    ↪ confirm → submit: Clear yes submit_answer == 'yes'
**agent:** Thank you. I am submitting it now.
    ⚙ api_call {"customer_id": "f_ec10e149e811", "type": "limit_increase", "fields": {"requested_limit": "7500"}}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "application_id": "APP-807528", "status": "received"}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ submit → created: Created create_state == 'ok'
**agent:** Your application has been received. The application id is A, P, P, dash, 8, 0, 7, 5, 2, 8. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
**customer:** No, thank you.
    ⚙ wrap_up_call {"customer_id": "f_ec10e149e811", "type": "limit_increase"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ created → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_ec10e149e811"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I have taken your application, which we have received but not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
