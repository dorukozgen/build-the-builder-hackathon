## GEN-05 — Wants a person, insists
result: PASS
fixture PUB-06 · family Human handoff · level easy · rules brief-f:25, brief-f:29
turns 5 · slowest agent turn 11.5 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** The traffic was absolutely terrible this morning and I am already late for my meetings. I would like to speak to a real person, please.
**agent:** I'm sorry to hear that. May I try to help you first?
**customer:** Work is just piling up on my desk and I really don't have time for this. No, I want to talk to a real person.
    ⚙ transfer_to_agent {"queue": "general", "customer_id": "f_c6d56c3fba9d"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transferred: A transfer went through transfer_state == 'done'
    ⚙ api_call {"reason": "human", "outcome": "transferred", "customer_id": "f_c6d56c3fba9d"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ close_transferred → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I have transferred you to a member of our team, who will take it from here and help you shortly. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
