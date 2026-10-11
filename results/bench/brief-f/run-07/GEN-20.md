## GEN-20 — Wants a mortgage application, accepts the transfer
result: FAIL: outcome (None, None), expected ('transferred', 'applications'); the call was not closed with close_call
fixture PUB-13 · family Unsupported · level easy · rules brief-f:2, brief-f:3, brief-f:29
turns 5 · slowest agent turn 29.7 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I want to apply for a mortgage.
**agent:** I cannot take that application on this call. Would you like me to transfer you to the applications team?
**customer:** Yes, please transfer me.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_cc7044322f10"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transferred: A transfer went through transfer_state == 'done'
    ↪ close_transferred → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
