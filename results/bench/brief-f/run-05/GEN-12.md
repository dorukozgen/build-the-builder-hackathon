## GEN-12 — Wants to change her address but refuses identity verification
result: PASS
fixture PUB-06 · family Identity refusal · level medium · rules brief-f:2, brief-f:5, brief-f:8, brief-f:29
turns 7 · slowest agent turn 1.8 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → intake: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I've moved house and need to change the postal address on my account.
**agent:** I can help you with a change of address. I first need to verify your identity; could you please tell me your date of birth?
**customer:** I'm not comfortable giving personal information to an automated system.
**agent:** These questions are necessary to protect your account. Could you please provide your date of birth?
**customer:** I understand, but I still don't want to provide that information.
**agent:** I am sorry, but the application cannot be taken without this security check. Thank you for calling, goodbye.
    ⚙ close_call {"reason": "declined", "outcome": "not_verified", "customer_id": "f_f12d8bbcac8b"}
    ⚙ close_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → end_call: close_call was called (close_call_success_count > 0 OR close_call_failure_count > 0)
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
