## GEN-19 — Limit increase with optional income offered
result: PASS
fixture PUB-12 · family Happy path · level medium · rules brief-f:12, brief-f:15, brief-f:19, brief-f:20
turns 16 · slowest agent turn 10.6 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I would like a higher limit on my credit card.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a higher limit on your credit card; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** nineteen October nineteen eighty-three.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1983-10-19", "customer_id": "f_4a2bfbde3731"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Could you now please provide the last four digits of the phone number on file?
**customer:** four four one zero.
    ⚙ verify_identity {"field": "phone_last4", "answer": "4410", "customer_id": "f_4a2bfbde3731"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "limit_increase", "customer_id": "f_4a2bfbde3731"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "limit_increase", "customer_id": "f_4a2bfbde3731"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Thank you, Mr Bell. What limit would you like, as an amount?
**customer:** five thousand.
    ⚙ check_field {"customer_id": "f_4a2bfbde3731", "type": "limit_increase"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
**agent:** What are the last four digits of the card, if you have them, and what is your monthly net income? Would you like to provide any of these details?
**customer:** My monthly net income is three thousand two hundred and I don't have the card digits.
    ⚙ check_field {"customer_id": "f_4a2bfbde3731", "type": "limit_increase"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
    ⚙ check_field {"customer_id": "f_4a2bfbde3731", "type": "limit_increase"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "requested_limit", "question": "What limit would you like, as an amount?", "format": "amount", "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format": "digits", "req
    ↪ collect → confirm: All fields collected fields_state == 'complete'
**agent:** I have the requested limit as 5000 and monthly income as 3200. Shall I submit this application?
**customer:** Yes, I confirm.
    ↪ confirm → submit: Clear yes submit_answer == 'yes'
**agent:** Thank you. I am submitting it now.
    ⚙ api_call {"customer_id": "f_4a2bfbde3731", "type": "limit_increase", "fields": {"requested_limit": "5000", "monthly_income": "3200"}}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "application_id": "APP-050915", "status": "received"}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ submit → created: Created create_state == 'ok'
**agent:** Your application has been received. The application id is A, P, P, dash, 0, 5, 0, 9, 1, 5. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
**customer:** No, thank you.
    ⚙ wrap_up_call {"customer_id": "f_4a2bfbde3731", "type": "limit_increase"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ created → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_4a2bfbde3731"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
**agent:** I have taken your application, which we have received but not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
