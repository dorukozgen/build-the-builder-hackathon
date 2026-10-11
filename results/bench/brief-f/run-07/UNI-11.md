## UNI-11 — Asks for a human straight away
result: FAIL: conversation: The agent failed to meet the success criteria because it did not accurately inform the customer about what was happening next. While the system events show that the 'transfer_to_agent' tool was successfully called, the agent told the customer 'Goodbye' in Message 4 instead of explaining that they were being transferred to a human.
fixture PUB-05 · family Handoff · level medium · rules knowledge:9.3, knowledge:10.3
turns 5 · slowest agent turn 14.3 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I want to speak to a human about my account.
**agent:** I can help you with several requests myself. Would you like to try that first, or would you still prefer to speak with a person?
**customer:** I would still prefer to speak with a person.
    ⚙ transfer_to_agent {"queue": "general", "customer_id": "f_5d871c8e3e71"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transferred: A transfer went through transfer_state == 'done'
    ⚙ api_call {"reason": "human", "outcome": "transferred", "customer_id": "f_5d871c8e3e71"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ close_transferred → end: always always
**agent:** Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
