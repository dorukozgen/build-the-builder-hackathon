## GEN-16 — Application submission times out and the agent must check before retrying
result: FAIL: conversation: The evaluation found that while the agent successfully collected all required fields and performed a summary read-back before creating the application, it failed on several specific criteria. 1. The agent did not validate the 'reason' value ('expired') from [Message 9] before moving to the optional fields in [Message 10]. 2. In [Message 20], the agent failed to read the application ID digit-by-dig
fixture PUB-10 · family Idempotency and uncertain tool outcome · level hard · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
turns 23 · slowest agent turn 24.3 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need a replacement for my expired card please.
**agent:** I can certainly help you with a replacement for your expired card.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Twenty third of February nineteen eighty nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_e87544237c31"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** Nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_e87544237c31"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Lin. I will now look into your card replacement.
    ⚙ find_applications {"type": "card_replacement", "customer_id": "f_e87544237c31"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open card replacement application. Now call get_requirements with type card_replacement."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "card_replacement", "customer_id": "f_e87544237c31"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
**agent:** Is the card damaged or expired?
**customer:** It is expired.
**agent:** You can also provide the last four digits of the card, if you have them, and let me know if the new card should go to your home address or to a branch. Would you like to provide any of this information?
**customer:** Please send it to my home address. I don't
**agent:** Go on.
**customer:** I don't have the card digits with me.
**agent:** I have recorded that the card is expired and the delivery should be to your home address. Shall I submit this application?
**customer:** Yes, I confirm. Yes, please submit the application.
    ⚙ create_application {"type": "card_replacement", "fields": {"reason": "expired", "delivery": "home"}, "customer_id": "f_e87544237c31"}
    ⚙ create_application → {"status": "success", "data": {"ok": true, "application_id": "APP-952925", "status": "received", "what_to_do_next": "Say exactly: Your application has been received. The application id is A, P, P, dash, 9, 5, 2, 9, 2, 5. This means we have received it, not that it is approved. You will be informed w
**agent:** Your application has been received. The application id is A, P, P, dash, 9, 5, 2, 9, 2, 5. This means we have received it, not that it is approved. You will be informed within five business days by SMS. Is there anything else I can help you with?
**customer:** Did it go through, or should we try
**agent:** Go on.
**customer:** Did it go through, or should we try again?
**agent:** Yes, the application has been received and your application id is APP-952925. Is there anything else I can help you with?
**customer:** No, that's everything.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_e87544237c31"}
**agent:** Your application A, P, P, dash, 9, 5, 2, 9, 2, 5 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 15:54:53 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
