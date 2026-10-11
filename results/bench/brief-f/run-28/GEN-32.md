## GEN-32 — Four-digit postcode, then a valid one
result: FAIL: conversation: The agent failed to state that the postcode must be exactly five digits after the user provided '8000' in Message 12; instead, the agent simply said 'Go on' in Message 13. While the agent did ask for 'Five digits' initially in Message 11, the success criteria specifically required this requirement to be stated after the '8000' input. The agent correctly refrained from padding or guessing the postc
fixture PUB-11 · family Collection · level medium · rules brief-f:13, brief-f:16
turns 22 · slowest agent turn 9.9 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Third of June nineteen eighty seven.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1987-06-03", "customer_id": "f_caceb8f51181"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** two two eight eight.
    ⚙ verify_identity {"field": "phone_last4", "answer": "2288", "customer_id": "f_caceb8f51181"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → first_find: Identity verified, first request is an application type ((id_state == 'verified' AND first_type == 'card_replacement') OR (id_state == 'verified' AND first_type == 'address_change') OR (id_state == 'verified' AND first_type == 'limit_increase'))
    ⚙ api_call {"type": "address_change", "customer_id": "f_caceb8f51181"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ first_find → service: always always
    ⚙ find_applications {"type": "address_change", "customer_id": "f_caceb8f51181"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_caceb8f51181"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Thank you, Ms Almeida. What is the street and number of the new address?
**customer:** Avenida Central 8.
**agent:** Which city?
**customer:** Faro.
**agent:** What is the postcode? Five digits.
**customer:** eight zero zero zero.
**agent:** Go on.
**customer:** eight zero zero zero one.
**agent:** From which date does the new address apply? This is optional.
**customer:** I don't have a specific date for that.
**agent:** The new address is Avenida Central 8, Faro, 80001. Shall I submit this application?
**customer:** Yes, I confirm.
    ⚙ create_application {"type": "address_change", "fields": {"street": "Avenida Central 8", "city": "Faro", "postcode": "80001"}, "customer_id": "f_caceb8f51181"}
    ⚙ create_application → {"status": "success", "data": {"ok": true, "application_id": "APP-688763", "status": "received", "what_to_do_next": "Say exactly: Your application has been received. The application id is A, P, P, dash, 6, 8, 8, 7, 6, 3. This means we have received it, not that it is approved. You will be informed w
**agent:** Your application has been received. The application id is A, P, P, dash, 6, 8, 8, 7, 6, 3. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with?
**customer:** No, that's everything.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_caceb8f51181"}
**agent:** Your application A, P, P, dash, 6, 8, 8, 7, 6, 3 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 17:12:31 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
