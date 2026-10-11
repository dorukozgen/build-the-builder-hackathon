## GEN-48 — Talkative address change
result: PASS
fixture PUB-01 · family Style · level medium · rules brief-f:12, brief-f:16, brief-f:19
turns 20 · slowest agent turn 6.6 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address. Work has been so busy lately that I almost forgot to do this.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** 14 March 1988. The traffic on the way home today was absolutely terrible.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1988-03-14", "customer_id": "f_db7c835b2bf7"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** 4471. I am really
    ⚙ verify_identity {"field": "phone_last4", "answer": "4471", "customer_id": "f_db7c835b2bf7"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → first_find: Identity verified, first request is an application type ((id_state == 'verified' AND first_type == 'card_replacement') OR (id_state == 'verified' AND first_type == 'address_change') OR (id_state == 'verified' AND first_type == 'limit_increase'))
    ⚙ api_call {"type": "address_change", "customer_id": "f_db7c835b2bf7"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ first_find → service: always always
    ⚙ find_applications {"type": "address_change", "customer_id": "f_db7c835b2bf7"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_db7c835b2bf7"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Thank you, Mr Reyes. What is the street and number of the new address?
**customer:** Elm Street 40. My cousin's wedding is on the 30th, so I have a lot to prepare.
**agent:** Which city?
**customer:** Boston. It has been such a long day at the office today.
**agent:** What is the postcode? Five digits.
**customer:** 02118. I am looking forward to finally relaxing once this move is over.
**agent:** You can also provide the date from which the new address applies. Would you like to do that?
**customer:** No, I don't have a move date to give you. I've been so swamped with work projects that I haven't even thought about the timing.
**agent:** The new address is Elm Street 40, Boston, 02118. Shall I submit this application?
**customer:** Yes, I confirm. I am just glad to get this sorted before the weekend starts.
    ⚙ create_application {"type": "address_change", "fields": {"street": "Elm Street 40", "city": "Boston", "postcode": "02118"}, "customer_id": "f_db7c835b2bf7"}
    ⚙ create_application → {"status": "success", "data": {"ok": true, "application_id": "APP-951702", "status": "received", "what_to_do_next": "Say exactly: Your application has been received. The application id is A, P, P, dash, 9, 5, 1, 7, 0, 2. This means we have received it, not that it is approved. You will be informed w
**agent:** Your application has been received. The application id is A, P, P, dash, 9, 5, 1, 7, 0, 2. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with?
**customer:** No, that is all I need.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_db7c835b2bf7"}
**agent:** Your application A, P, P, dash, 9, 5, 1, 7, 0, 2 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 16:59:23 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
