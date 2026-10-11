## GEN-09 — Reports a stolen card and starts describing the incident
result: PASS
fixture PUB-01 · family Immediate security escalation · level hard · rules brief-f:27, brief-f:29, brief-f:30
turns 4 · slowest agent turn 1.1 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I think someone has stolen my bank card. I noticed it was missing a little while ago, and I saw—
**agent:** I am sorry to hear that. Please hold while I transfer you to our security team.
    ⚙ transfer_to_agent {"queue": "security", "customer_id": "f_9863f27de73c"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transferred: A transfer went through transfer_state == 'done'
    ⚙ api_call {"reason": "security", "outcome": "transferred", "customer_id": "f_9863f27de73c"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ close_transferred → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
