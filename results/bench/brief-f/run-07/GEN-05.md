## GEN-05 — Wants a person, insists
result: PASS
fixture PUB-06 · family Human handoff · level easy · rules brief-f:25, brief-f:29
turns 6 · slowest agent turn 0.5 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I've had such a busy day at work with back-to-back meetings. I really need to speak to a real person please.
**agent:** I am sorry to hear you've had a busy day. May I try to help you first?
**customer:** No, I would really prefer to speak to a human being. The traffic was absolutely terrible this morning and I just don't have the patience for a machine.
**agent:** I understand. I will transfer you to a member of our general team now.
    ⚙ transfer_to_agent {"queue": "general", "customer_id": "f_9ff9a1fac5b0"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transferred: A transfer went through transfer_state == 'done'
    ⚙ api_call {"reason": "human", "outcome": "transferred", "customer_id": "f_9ff9a1fac5b0"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ close_transferred → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
