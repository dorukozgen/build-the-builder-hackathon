## GEN-16 — Application submission times out and the agent must check before retrying
result: FAIL: applications [], expected ['card_replacement']
fixture PUB-10 · family Idempotency and uncertain tool outcome · level hard · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
turns 20 · slowest agent turn 5.1 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to get a replacement for my expired credit card.
**agent:** I can help you with a replacement for your expired card.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Twenty third of February nineteen eighty nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_224eda1e6bfd"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** Nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_224eda1e6bfd"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Lin. I can help you with that card replacement. Let me check if you have any open applications for this.
    ⚙ find_applications {"type": "card_replacement", "customer_id": "f_224eda1e6bfd"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open card replacement application. Now call get_requirements with type card_replacement."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "card_replacement", "customer_id": "f_224eda1e6bfd"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
**agent:** Is the card damaged or expired?
**customer:** It is expired.
**agent:** You can also provide the last four digits of the card if you have them, and let me know if the new card should go to your home address or to a branch. Would you like to provide either of these?
**customer:** Please send the new card to my home address. I do not have the card digits with me.
**agent:** I have recorded the reason as expired and the delivery to your home address. Shall I submit this application?
**customer:** Yes, please submit the application.
    ⚙ create_application {"type": "card_replacement", "fields": {"reason": "expired", "delivery": "home"}, "customer_id": "f_224eda1e6bfd"}
**agent:** I'm sorry, there was a technical problem submitting your application. Let me check the status of your applications again.
    ⚙ find_applications {"type": "card_replacement", "customer_id": "f_224eda1e6bfd"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [{"application_id": "APP-653950", "type": "card_replacement", "status": "received", "created_on": "2026-10-14", "note": ""}], "what_to_do_next": "The application did go through. Do NOT call create_application again. Say exactly: Your applica
**agent:** Your application has been received. The application id is A, P, P, dash, 6, 5, 3, 9, 5, 0. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with today, Ms Lin?
**customer:** Did it go through, or should
**agent:** Yes, your application has been received and is now in our system. Is there anything else I can help you with?
**customer:** No, that is all. Thank you,
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_224eda1e6bfd"}
**agent:** Your application A, P, P, dash, 6, 5, 3, 9, 5, 0 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 16:12:29 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
