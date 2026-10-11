## GEN-29 — Unknown id, then lookup by type
result: PASS
fixture PUB-02 · family Status enquiry · level medium · rules brief-f:24, brief-f:23, brief-f:22, brief-f:29
turns 14 · slowest agent turn 7.8 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I am calling about the status of an application.
**agent:** I can help you with the status of an application.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Second November nineteen seventy-nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1979-11-02", "customer_id": "f_1a1db6117bd8"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** zero three five eight.
    ⚙ verify_identity {"field": "phone_last4", "answer": "0358", "customer_id": "f_1a1db6117bd8"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Costa. Do you have the application ID?
**customer:** APP-111111.
    ⚙ get_application {"customer_id": "f_1a1db6117bd8", "application_id": "APP-111111"}
    ⚙ get_application → {"status": "success", "data": {"ok": false, "error": "unknown application_id", "what_to_do_next": "That application id was not found. Say so, and do not confirm the id. Offer to look by type: ask which type it is (card replacement, address change or limit increase), then call find_applications with 
**agent:** That application ID was not found. Would you like me to look for it by type? If so, is it for a card replacement, an address change, or a limit increase?
**customer:** It was an address change.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_1a1db6117bd8"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [{"application_id": "APP-305577", "type": "address_change", "status": "received", "created_on": "2026-10-11", "note": ""}], "what_to_do_next": "Tell the customer what was found for the address change: application A, P, P, dash, 3, 0, 5, 5, 7
**agent:** I found an address change application, APP-305577, which is received and waiting. Is there anything else I can help you with, Ms Costa?
**customer:** No, that is all for today.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "status_given", "customer_id": "f_1a1db6117bd8"}
**agent:** I have given you the current status of your application, and no new application was made on this call. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 16:59:11 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
