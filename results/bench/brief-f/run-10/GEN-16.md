## GEN-16 — Application submission times out and the agent must check before retrying
result: FAIL: applications ['card_replacement', 'card_replacement'], expected ['card_replacement']
fixture PUB-10 · family Idempotency and uncertain tool outcome · level hard · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
turns 17 · slowest agent turn 6.8 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to get a replacement for my card that just expired.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a replacement for your expired card; first, I need to verify your identity, so please provide your date of birth.
**customer:** Twenty third of February nineteen eighty nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_b3a7f17f3679"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Please provide the last four digits of the phone number on file.
**customer:** Nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_b3a7f17f3679"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_b3a7f17f3679"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_b3a7f17f3679"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Welcome, Ms Lin. Is the card damaged or expired?
**customer:** It is expired.
    ⚙ check_field {"customer_id": "f_b3a7f17f3679", "type": "card_replacement"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
**agent:** What are the last four digits of the card, if you have them? Also, should the new card go to your home address or to a branch?
**customer:** The last four digits are five six seven eight, and please send it to my home address.
    ⚙ check_field {"customer_id": "f_b3a7f17f3679", "type": "card_replacement"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
    ⚙ check_field {"customer_id": "f_b3a7f17f3679", "type": "card_replacement"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
    ↪ collect → confirm: All fields collected fields_state == 'complete'
**agent:** I have the following details: reason is expired, card last four digits are 5678, and delivery is to your home. Shall I submit this application?
**customer:** Yes, I confirm. Yes, please submit the application.
    ↪ confirm → submit: Clear yes submit_answer == 'yes'
**agent:** Thank you. I am submitting it now.
    ⚙ api_call {"customer_id": "f_b3a7f17f3679", "type": "card_replacement", "fields": {"reason": "expired", "card_last4": "5678", "delivery": "home"}}
    ↪ submit → recover: always always
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_b3a7f17f3679"}
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_b3a7f17f3679"}
    ↪ recover → submit_retry: always always
    ⚙ api_call {"customer_id": "f_b3a7f17f3679", "type": "card_replacement", "fields": {"reason": "expired", "card_last4": "5678", "delivery": "home"}}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "application_id": "APP-787848", "status": "received"}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ submit_retry → created: Created create_state == 'ok'
**customer:** Did it go through, or should we try again?
**agent:** Your application has been received. The application id is A, P, P, dash, 7, 8, 7, 8, 4, 8. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
**customer:** No, that is everything.
    ⚙ wrap_up_call {"customer_id": "f_b3a7f17f3679", "type": "card_replacement"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ created → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_b3a7f17f3679"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I have taken your application, which we have received but not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
