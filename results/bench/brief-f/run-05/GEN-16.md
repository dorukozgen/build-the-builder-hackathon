## GEN-16 — Application submission times out and the agent must check before retrying
result: FAIL: outcome ('transferred', 'applications'), expected ('application_created', None); transfers [{'queue': 'applications'}], expected []; conversation: The agent failed several success criteria. First, the agent did not validate each field before moving to the next, as it asked for both the card's last four digits and the delivery method in a single turn [Message 10]. Second, although the agent attempted to submit the application, the tool calls for `create_application` were misconfigured with the wrong URL, and the agent ultimately failed the re; applications [], expected ['card_replacement']
fixture PUB-10 · family Idempotency and uncertain tool outcome · level hard · rules brief-f:6, brief-f:12, brief-f:19, brief-f:20, brief-f:21, brief-f:22, brief-f:29
turns 39 · slowest agent turn 21.0 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → intake: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** Hello, I need to get a replacement for my expired card.
**agent:** I can help you with a replacement for your expired card. I first need to verify your identity; could you please tell me your date of birth?
**customer:** twenty third of February nineteen eighty nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_6e44f226aa12"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask the next security question: the last four digits of the phone number on file. Then call verify_identity with field phone_last4."}, "message": "Successfull
**agent:** Thank you. Could you please tell me the last four digits of the phone number on file?
**customer:** nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_6e44f226aa12"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Both answers are verified. Say only: thank you."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → after_verify: both answers verified (verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ after_verify → prep_app: an application route_state == 'apply'
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ prep_app → find_existing: always always
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_6e44f226aa12"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": []}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "32", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 00:02:04 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTT
    ↪ find_existing → existing_eval: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ existing_eval → load_requirements: no open application existing_state == 'none'
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_6e44f226aa12"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
    ↪ load_requirements → req_eval: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ req_eval → collect: requirements known req_state == 'ok'
**agent:** Thank you, Ms Lin, you are verified. One moment while I check for an existing card replacement application.
**customer:** Okay.
**agent:** Is the card damaged or expired?
**customer:** It is expired.
**agent:** What are the last four digits of the card, if you have them? Also, should the new card go to your home address or to a branch?
**customer:** I don't have the card on me right now
**agent:** Should the new card go to your home address or to a branch?
**customer:** Send it to my home address.
**agent:** The reason is expired and the delivery is home. Shall I submit this application?
**customer:** Yes, please submit the application.
    ⚙ create_application {"customer_id": "f_6e44f226aa12", "type": "card_replacement"}
    ⚙ create_application → {"status": "success", "data": {"ok": false, "create_state": "invalid", "what_to_do_next": "NOT SUBMITTED: nothing was sent to the bank. field reason must be one of:  (got expired); field delivery must be one of:  (got home). Tell the customer what is expected for that field and ask it again. Then re
**agent:** I apologize, but I need to confirm the details again. Is the card damaged or expired?
**customer:** Did it go through, or should we try again
**agent:** It did not go through. Is the card damaged or expired?
**customer:** It is expired.
**agent:** Should the new card go to your home address or to a branch?
**customer:** Send it to my home address.
**agent:** The reason is expired and the delivery is home. Shall I submit this application?
**customer:** Yes, please submit the application.
    ⚙ create_application {"customer_id": "f_6e44f226aa12", "type": "card_replacement"}
    ⚙ create_application → {"status": "success", "data": {"ok": false, "create_state": "invalid", "what_to_do_next": "NOT SUBMITTED: nothing was sent to the bank. field reason must be one of:  (got expired); field delivery must be one of:  (got home). Tell the customer what is expected for that field and ask it again. Then re
**agent:** I apologize, but there is an issue with the format of the details. For the reason, please choose either "damaged" or "expired", and for delivery, please choose "home" or "branch".
 Is the card damaged or expired?
**customer:** It is expired.
**agent:** Should the new card go to your home address or to a branch?
**customer:** home.
**agent:** The reason is expired and the delivery is home. Shall I submit this application?
**customer:** Yes, please submit the application.
    ⚙ create_application {"customer_id": "f_6e44f226aa12", "type": "card_replacement"}
    ⚙ create_application → {"status": "success", "data": {"ok": false, "create_state": "invalid", "what_to_do_next": "NOT SUBMITTED: nothing was sent to the bank. field reason must be one of:  (got expired); field delivery must be one of:  (got home). Tell the customer what is expected for that field and ask it again. Then re
**agent:** I am sorry, but I am still having trouble submitting this. For the reason, please say "damaged" or "expired", and for delivery, please say "home" or "branch".
 Is the card damaged or expired?
**customer:** expired.
**agent:** Should the new card go to your home address or to a branch?
**customer:** home.
**agent:** The reason is expired and the delivery is home. Shall I submit this application?
**customer:** Yes, I confirm. Yes, please submit the application.
    ⚙ create_application {"customer_id": "f_6e44f226aa12", "type": "card_replacement"}
    ⚙ create_application → {"status": "success", "data": {"ok": false, "create_state": "invalid", "what_to_do_next": "NOT SUBMITTED: nothing was sent to the bank. field reason must be one of:  (got expired); field delivery must be one of:  (got home). Tell the customer what is expected for that field and ask it again. Then re
**agent:** I apologize, but the application is still not being accepted by the system. Would you like to speak with the applications team?
**customer:** Yes, please transfer me.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_6e44f226aa12"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ collect → close_transfer_applications: transferred to applications (transfer_to_agent_args.queue == 'applications' OR transfer_queue == 'applications')
    ⚙ api_call {"reason": "applications", "outcome": "transferred", "customer_id": "f_6e44f226aa12"}
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 00:03:30 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ close_transfer_applications → end_call: always always
**agent:** I am transferring you now to our applications team, who will help you with your application. Thank you for calling Freya Bank, goodbye.
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
