## GEN-37 — Address change submission times out
result: FAIL: outcome (None, None), expected ('application_created', None); the call was not closed with close_call; applications ['address_change', 'address_change'], expected ['address_change']
fixture PUB-10 · family Tool failure · level hard · rules brief-f:21, brief-f:20, brief-f:22
turns 20 · slowest agent turn 12.2 s · ended customer-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You would like to change your postal address; however, I first need to verify your identity, so please provide your date of birth.
**customer:** Twenty-third of February nineteen eighty-nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_7c9384287c25"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, please provide the last four digits of the phone number on file.
**customer:** nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_7c9384287c25"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "address_change", "customer_id": "f_7c9384287c25"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "address_change", "customer_id": "f_7c9384287c25"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Hello Ms Lin. What is the street and number of the new address?
**customer:** Main Road 3.
    ⚙ check_field {"customer_id": "f_7c9384287c25", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Which city?
**customer:** Cork.
    ⚙ check_field {"customer_id": "f_7c9384287c25", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the postcode? Five digits.
**customer:** one two three four five.
    ⚙ check_field {"customer_id": "f_7c9384287c25", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** From which date does the new address apply? Would you like to provide this detail?
**customer:** I do not have a move date.
    ⚙ check_field {"customer_id": "f_7c9384287c25", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ collect → confirm: All fields collected fields_state == 'complete'
**agent:** I have the details: street: Main Road 3; city: Cork; postcode: 12345. Shall I submit this application?
**customer:** Yes, I confirm.
    ↪ confirm → submit: Clear yes submit_answer == 'yes'
**agent:** Thank you. I am submitting it now.
    ⚙ api_call {"customer_id": "f_7c9384287c25", "type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}}
    ↪ submit → recover: always always
    ⚙ api_call {"type": "address_change", "customer_id": "f_7c9384287c25"}
    ⚙ api_call {"type": "address_change", "customer_id": "f_7c9384287c25"}
    ↪ recover → submit_retry: always always
    ⚙ api_call {"customer_id": "f_7c9384287c25", "type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "application_id": "APP-496811", "status": "received"}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ submit_retry → created: Created create_state == 'ok'
**customer:** Did it work?
**agent:** Your application has been received. The application id is A, P, P, dash, 4, 9, 6, 8, 1, 1. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
    ↪ created → next_app: The customer raised another application or a status enquiry (next_type == 'card_replacement' OR next_type == 'address_change' OR next_type == 'limit_increase' OR next_type == 'status')
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ next_app → status: Status enquiry next req_type == 'status'
**customer:** No, that is all.
    ⚙ wrap_up_call {"customer_id": "f_7c9384287c25", "type": "card_replacement"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ✖ error: The model returned no speakable content
    ✖ error: The model returned no speakable content
