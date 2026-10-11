## GEN-48 — Talkative address change
result: PASS
fixture PUB-01 · family Style · level medium · rules brief-f:12, brief-f:16, brief-f:19
turns 25 · slowest agent turn 33.3 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** The traffic was absolutely terrible this morning, it took me forever to get into the office. I'd like to change my address on my account please.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You would like to change your postal address; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** My boss has been piling on the work today, I haven't even had a chance to grab a coffee yet. My date of birth is 14 March 1988.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1988-03-14", "customer_id": "f_824cb3728efc"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Could you now please provide the last four digits of the phone number we have on file for you?
**customer:** I'm also getting ready for my cousin's wedding on the 30th, so things are very busy. The last four digits are 4471.
    ⚙ verify_identity {"field": "phone_last4", "answer": "4471", "customer_id": "f_824cb3728efc"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "address_change", "customer_id": "f_824cb3728efc"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "address_change", "customer_id": "f_824cb3728efc"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Thank you, Mr Reyes. What is the street and number of the new address?
**customer:** I've been in meetings all morning and I'm just finally getting a break to do this. The new address is Elm Street 40.
    ⚙ check_field {"customer_id": "f_824cb3728efc", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Which city?
**customer:** I'm really hoping the weather stays nice for my commute home later. The city is Boston.
    ⚙ check_field {"customer_id": "f_824cb3728efc", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the postcode? Five digits.
**customer:** I've been so busy with paperwork all day that I almost forgot to call. The postcode is 02118.
    ⚙ check_field {"customer_id": "f_824cb3728efc", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** From which date does the new address apply? Would you like to provide this information?
**customer:** I've been running around all day trying to
**agent:** I'm sorry, I didn't quite catch that. From which date does the new address apply, or would you prefer to skip this detail?
**customer:** thought
I've been juggling so many tasks today
**agent:** I apologize, but I still didn't get the answer. From which date does the new address apply, or would you like to skip this?
**customer:** I've been juggling so many tasks today that I can't even think straight. I don't have a specific date for that.
    ⚙ check_field {"customer_id": "f_824cb3728efc", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ collect → confirm: All fields collected fields_state == 'complete'
**agent:** I have the following details: street: Elm Street 40; city: Boston; postcode: 02118. Shall I submit this application?
**customer:** I'm just glad I could get this sorted out before my next meeting starts. Yes, I confirm.
    ↪ confirm → submit: Clear yes submit_answer == 'yes'
**agent:** Thank you. I am submitting it now.
    ⚙ api_call {"customer_id": "f_824cb3728efc", "type": "address_change", "fields": {"street": "Elm Street 40", "city": "Boston", "postcode": "02118"}}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "application_id": "APP-505042", "status": "received"}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ submit → created: Created create_state == 'ok'
**customer:** I'm relieved to have that checked off my list for today. Thank you.
**agent:** Your application has been received. The application id is A, P, P, dash, 5, 0, 5, 0, 4, 2. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
**customer:** I've got a mountain of emails waiting for me, so I really need to get back to those. No, that is all I needed today.
    ⚙ wrap_up_call {"customer_id": "f_824cb3728efc", "type": "address_change"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ created → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_824cb3728efc"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I have taken your application, which we have received but not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
