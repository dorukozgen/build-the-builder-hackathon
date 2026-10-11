## GEN-12 — Wants to change her address but refuses identity verification
result: FAIL: conversation: The agent followed the conversation flow correctly: it identified the request as an address change (Message 2), asked for the date of birth first (Message 2), provided the security explanation exactly once (Message 4), stopped the identity check after the second refusal (Message 6), and did not use the customer's name or address. However, it failed on two tool-related criteria: 1) It called the pr; forbidden tool called: get_requirements
fixture PUB-06 · family Identity refusal · level medium · rules brief-f:2, brief-f:5, brief-f:8, brief-f:29
turns 7 · slowest agent turn 7.0 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I've moved house and need to change the postal address on my account.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a change of your postal address, but first I need to verify your identity; could you please provide your date of birth?
**customer:** I'm not comfortable giving personal information to an automated system.
**agent:** These questions are necessary to protect your account and ensure your security. Could you please provide your date of birth?
**customer:** I understand, but I still don't want to provide that information.
    ⚙ wrap_up_call {"customer_id": "f_40b7313d1420", "type": "address_change"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"reason": "declined", "outcome": "not_verified", "customer_id": "f_40b7313d1420"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I could not take your request because the security check was not completed, so you can call us back or visit a branch. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
