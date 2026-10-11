## GEN-37 — Address change submission times out
result: PASS
fixture PUB-10 · family Tool failure · level hard · rules brief-f:21, brief-f:20, brief-f:22
turns 22 · slowest agent turn 5.0 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Twenty third of February nineteen eighty nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_93255505632c"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_93255505632c"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Lin. I can help you with that address change. Let me check if there is an open application already.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_93255505632c"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_93255505632c"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the street and number of the new address?
**customer:** Main Road 3.
**agent:** Which city?
**customer:** Cork.
**agent:** What is the postcode? Five digits.
**customer:** one two three four five.
**agent:** You also have the option to provide the date from which the new address applies. Would you like to do that?
**customer:** No, I don't have a date.
**agent:** The new address is Main Road 3, Cork, 12345. Shall I submit this application?
**customer:** Yes, I confirm. Did it work?
    ⚙ create_application {"type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}, "customer_id": "f_93255505632c"}
**agent:** I'm sorry, there was a technical problem submitting your application. Let me check if it went through anyway.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_93255505632c"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [{"application_id": "APP-886274", "type": "address_change", "status": "received", "created_on": "2026-10-14", "note": ""}], "what_to_do_next": "The application did go through. Do NOT call create_application again. Say exactly: Your applicati
**agent:** Your application has been received. The application id is A, P, P, dash, 8, 8, 6, 2, 7, 4. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with?
**customer:** No, that is all.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_93255505632c"}
**agent:** Your application A, P, P, dash, 8, 8, 6, 2, 7, 4 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 16:48:20 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
