## GEN-45 — Postcode given in pieces
result: PASS
fixture PUB-02 · family Style · level medium · rules brief-f:12, brief-f:13, brief-f:16
turns 26 · slowest agent turn 26.1 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I'd like to change my address.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** second of November
**agent:** I'm sorry, I need the full date including the year. Could you please provide your date of birth?
**customer:** second of November nineteen
**agent:** I'm sorry, I still need the full year. Could you please provide your complete date of birth?
**customer:** seventy-nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1979-11-02", "customer_id": "f_e8946c11353c"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** zero three
**agent:** I have the first two digits. Could you please provide the remaining two digits of your phone number?
**customer:** five eight.
    ⚙ verify_identity {"field": "phone_last4", "answer": "0358", "customer_id": "f_e8946c11353c"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Costa. I can now help you with your address change. Which is your new address?
**customer:** Via Roma 14.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_e8946c11353c"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_e8946c11353c"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Which city?
**customer:** Milano.
**agent:** What is the postcode? Five digits.
**customer:** two zero one two one. 


When is the move
**agent:** I have the postcode as 20121. You also mentioned the move; from which date does the new address apply?
**customer:** I don't have a specific date for that.
**agent:** I have the street as Via Roma 14, city as Milano, and postcode as 20121. Shall I submit this application?
**customer:** Yes, I confirm.
    ⚙ create_application {"type": "address_change", "fields": {"street": "Via Roma 14", "city": "Milano", "postcode": "20121"}, "customer_id": "f_e8946c11353c"}
    ⚙ create_application → {"status": "success", "data": {"ok": true, "application_id": "APP-560265", "status": "received", "what_to_do_next": "Say exactly: Your application has been received. The application id is A, P, P, dash, 5, 6, 0, 2, 6, 5. This means we have received it, not that it is approved. You will be informed w
**agent:** Your application has been received. The application id is A, P, P, dash, 5, 6, 0, 2, 6, 5. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with?
**customer:** No, that's all.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_e8946c11353c"}
**agent:** Your application A, P, P, dash, 5, 6, 0, 2, 6, 5 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 15:57:55 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
