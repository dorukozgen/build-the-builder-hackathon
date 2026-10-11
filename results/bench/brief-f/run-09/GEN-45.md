## GEN-45 — Postcode given in pieces
result: FAIL: outcome (None, None), expected ('application_created', None); the call was not closed with close_call
fixture PUB-02 · family Style · level medium · rules brief-f:12, brief-f:13, brief-f:16
turns 32 · slowest agent turn 19.7 s · ended customer-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** Hello, I would like to change my address.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a change of your postal address; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** The second of November.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "0000-11-02", "customer_id": "f_6108552f289d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": false, "wrong_answers_left": 2, "all_verified": false, "what_to_do_next": "That answer is not correct. Do not reveal the right answer or give hints. Ask the same question again."}, "message": "Successfully executed POST request", "status_code": 
**agent:** That answer is not correct. Could you please provide your date of birth again?
**customer:** Nineteen seventy-nine.
**agent:** I'm sorry, but I need your full date of birth, including the day and month. Could you please provide it?
**customer:** The second of November.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1979-11-02", "customer_id": "f_6108552f289d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 2, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, could you please provide the last four digits of the phone number we have on file for you?
**customer:** Zero three.
**agent:** I'm sorry, but I need the last four digits of your phone number. Could you please provide them?
**customer:** Five eight.
**agent:** I'm sorry, but I need the last four digits. Could you please provide all four digits of the phone number on file?
**customer:** Zero three five eight.
    ⚙ verify_identity {"field": "phone_last4", "answer": "0358", "customer_id": "f_6108552f289d"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 2, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "address_change", "customer_id": "f_6108552f289d"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "address_change", "customer_id": "f_6108552f289d"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Thank you, Ms Costa. What is the street and number of the new address?
**customer:** Via Roma 14.
    ⚙ check_field {"customer_id": "f_6108552f289d", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Which city?
**customer:** Milano.
    ⚙ check_field {"customer_id": "f_6108552f289d", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the postcode? Five digits.
**customer:** Two zero one.
**agent:** I'm sorry, the postcode must be five digits. Could you please provide the five-digit postcode?
**customer:** Two one.
**agent:** I'm sorry, the postcode must be five digits. Could you please provide the five-digit postcode?
**customer:** Two zero one two one.
    ⚙ check_field {"customer_id": "f_6108552f289d", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** From which date does the new address apply? Would you like to provide this information?
**customer:** I don't have a move date.
    ⚙ check_field {"customer_id": "f_6108552f289d", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ collect → confirm: All fields collected fields_state == 'complete'
**agent:** I have the following details: street Via Roma 14, city Milano, and postcode 20121. Shall I submit this application?
**customer:** Yes, I confirm.
    ↪ confirm → submit: Clear yes submit_answer == 'yes'
**agent:** Thank you. I am submitting it now.
    ⚙ api_call {"customer_id": "f_6108552f289d", "type": "address_change", "fields": {"street": "Via Roma 14", "city": "Milano", "postcode": "20121"}}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "application_id": "APP-857496", "status": "received"}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ submit → created: Created create_state == 'ok'
**customer:** Is there anything else?
**agent:** Your application has been received. The application id is A, P, P, dash, 8, 5, 7, 4, 9, 6. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
**customer:** No, thank you.
