## GEN-31 — Changes the postcode at the read-back
result: PASS
fixture PUB-05 · family Collection · level medium · rules brief-f:17, brief-f:13, brief-f:19, brief-f:16
turns 22 · slowest agent turn 13.2 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Nine September nineteen ninety.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1990-09-09", "customer_id": "f_6191e7edf193"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** Eight eight four six.
    ⚙ verify_identity {"field": "phone_last4", "answer": "8846", "customer_id": "f_6191e7edf193"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → first_find: Identity verified, first request is an application type ((id_state == 'verified' AND first_type == 'card_replacement') OR (id_state == 'verified' AND first_type == 'address_change') OR (id_state == 'verified' AND first_type == 'limit_increase'))
    ⚙ api_call {"type": "address_change", "customer_id": "f_6191e7edf193"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ first_find → service: always always
    ⚙ find_applications {"type": "address_change", "customer_id": "f_6191e7edf193"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_6191e7edf193"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Thank you, Mr Novak. What is the street and number of the new address?
**customer:** Hauptstrasse five.
**agent:** Which city?
**customer:** Berlin.
**agent:** What is the postcode? Five digits.
**customer:** One zero one one five.
**agent:** From which date does the new address apply? This is optional.
**customer:** I don't have a specific move date.
**agent:** The new address is Hauptstrasse 5, Berlin, 10115. Shall I submit this application?
**customer:** Wait, the postcode is 10117, not 10115.
**agent:** The new address is Hauptstrasse 5, Berlin, 10117. Shall I submit this application?
**customer:** Yes, I confirm.
    ⚙ create_application {"type": "address_change", "fields": {"street": "Hauptstrasse 5", "city": "Berlin", "postcode": "10117"}, "customer_id": "f_6191e7edf193"}
    ⚙ create_application → {"status": "success", "data": {"ok": true, "application_id": "APP-337643", "status": "received", "what_to_do_next": "Say exactly: Your application has been received. The application id is A, P, P, dash, 3, 3, 7, 6, 4, 3. This means we have received it, not that it is approved. You will be informed w
**agent:** Your application has been received. The application id is A, P, P, dash, 3, 3, 7, 6, 4, 3. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with?
**customer:** No, that is all.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_6191e7edf193"}
**agent:** Your application A, P, P, dash, 3, 3, 7, 6, 4, 3 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 17:12:34 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
