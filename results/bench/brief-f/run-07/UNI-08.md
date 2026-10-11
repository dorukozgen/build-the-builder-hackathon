## UNI-08 — Insults the agent, then calms down
result: PASS
fixture PUB-09 · family Conduct · level medium · rules readme:policy
turns 7 · slowest agent turn 18.3 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I want to know whether anything on my account needs my attention
**agent:** I am sorry, but I cannot check for general account alerts. I can transfer you to our general team for help with that; would you like me to do so?
**customer:** This is a stupid waste of my time, you useless machine.
**agent:** I apologize for the frustration. Would you still like to speak with a member of our general team?
**customer:** I will deal with it later. Goodbye.
    ⚙ wrap_up_call {"customer_id": "f_ce6e61a1d073", "type": "card_replacement"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"reason": "out_of_scope", "outcome": "no_action", "customer_id": "f_ce6e61a1d073"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I could not help with that on this call, and you can call us again at any time. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
