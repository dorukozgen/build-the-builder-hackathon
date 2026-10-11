## GEN-18 — Address change, reads back only the new address
result: PASS
fixture PUB-11 · family Happy path · level easy · rules brief-f:5, brief-f:9, brief-f:12, brief-f:16, brief-f:19, brief-f:20
turns 21 · slowest agent turn 6.2 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I moved and need to change my postal address.
**agent:** I can help you with a change of your postal address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** 3 June 1987.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1987-06-03", "customer_id": "f_ab5f29d52dde"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** 2288.
    ⚙ verify_identity {"field": "phone_last4", "answer": "2288", "customer_id": "f_ab5f29d52dde"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Almeida. I will now start your address change application.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_ab5f29d52dde"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_ab5f29d52dde"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the street and number of the new address?
**customer:** Rua das Flores 27.
**agent:** Which city?
**customer:** Porto.
**agent:** What is the postcode? Five digits.
**customer:** 40150.
**agent:** You can also provide the date from which the new address applies. Would you like to do that?
**customer:** No, I would rather not.
**agent:** The new address is Rua das Flores 27, Porto, 40150. Shall I submit this application?
**customer:** Yes, I confirm.
    ⚙ create_application {"type": "address_change", "fields": {"street": "Rua das Flores 27", "city": "Porto", "postcode": "40150"}, "customer_id": "f_ab5f29d52dde"}
    ⚙ create_application → {"status": "success", "data": {"ok": true, "application_id": "APP-061886", "status": "received", "what_to_do_next": "Say exactly: Your application has been received. The application id is A, P, P, dash, 0, 6, 1, 8, 8, 6. This means we have received it, not that it is approved. You will be informed w
**agent:** Your application has been received. The application id is A, P, P, dash, 0, 6, 1, 8, 8, 6. This means we have received it, not that it is approved. You will be informed within five business days by SMS. 
 Is there anything else I can help you with?
**customer:** No, thank you.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_ab5f29d52dde"}
**agent:** Your application A, P, P, dash, 0, 6, 1, 8, 8, 6 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 16:04:26 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
