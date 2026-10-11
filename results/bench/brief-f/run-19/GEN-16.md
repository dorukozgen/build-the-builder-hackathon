## GEN-16 — Application submission times out and the agent must check before retrying
result: FAIL: outcome (None, None), expected ('application_created', None); the call was not closed with close_call; conversation: The agent failed to meet several success criteria: 1. The agent did not validate the 'reason' field value ('expired' provided in Message 9) before moving on to collect optional fields in Message 10. 2. The close_call tool (executed via api_call) was not the last tool call; it was followed by end_call. 3. The close_call tool was called twice (initial call and a retry) rather than exactly once. Howe
fixture PUB-10 · family Idempotency and uncertain tool outcome · level hard · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
turns 20 · slowest agent turn 7.0 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** Hi, I need a replacement for my card because it expired.
**agent:** I can help you with a replacement for your expired card.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Twenty-third of February nineteen eighty-nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_04e76138f54c"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_04e76138f54c"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Lin. I will now look into the card replacement for you.
    ⚙ find_applications {"type": "card_replacement", "customer_id": "f_04e76138f54c"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open card replacement application. Now call get_requirements with type card_replacement."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "card_replacement", "customer_id": "f_04e76138f54c"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
**agent:** Is the card damaged or expired?
**customer:** It's expired.
**agent:** You also have the option to provide the last four digits of the card, if you have them, and specify if the new card should go to your home address or to a branch. Would you like to provide either of these?
**customer:** I would like it sent to my home address
**agent:** You would like the card replacement because it is expired and you would like it sent to your home address. Shall I submit this application?
**customer:** Yes, I confirm. Yes, please submit the application.
    ⚙ create_application {"type": "card_replacement", "fields": {"reason": "expired", "delivery": "home"}, "customer_id": "f_04e76138f54c"}
**agent:** I'm sorry, there was a technical problem and I couldn't submit your application. Let me check if it went through.
    ⚙ find_applications {"type": "card_replacement", "customer_id": "f_04e76138f54c"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [{"application_id": "APP-501828", "type": "card_replacement", "status": "received", "created_on": "2026-10-14", "note": ""}], "what_to_do_next": "The application did go through. Do NOT call create_application again. Say exactly: Your applica
**agent:** Your application has been received. The application id is A, P, P, dash, 5, 0, 1, 8, 2, 8. This means we have received it, not that it is approved. You will be informed within five business days by SMS.
 Is there anything else I can help you with?
**customer:** Did it go through, or should we try again?
**agent:** Your application has been received. The application id is A, P, P, dash, 5, 0, 1, 8, 2, 8.
 Is there anything else I can help you with?
**customer:** No, that is all I needed. Thank you.
    ↪ service → close_done: The customer needs nothing more nothing_more == 'yes'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_04e76138f54c"}
**agent:** Your application A, P, P, dash, 5, 0, 1, 8, 2, 8 has been received, not approved, and you will be informed within five business days by SMS. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call {"outcome": "application_created", "customer_id": "f_04e76138f54c"}
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
