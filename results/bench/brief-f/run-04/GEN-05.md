## GEN-05 — Wants a person, insists
result: PASS
fixture PUB-06 · family Human handoff · level easy · rules brief-f:25, brief-f:29
turns 5 · slowest agent turn 3.3 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → intake: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I'd like to speak to a real person, please.
**agent:** I can help you with many requests. Would you like to see if I can assist you first?
**customer:** No, I really just want to talk to a person.
    ⚙ transfer_to_agent {"queue": "general", "customer_id": "c_a02401a9-ddc"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transfer_general: transferred to general (transfer_to_agent_args.queue == 'general' OR transfer_queue == 'general')
    ⚙ api_call {"reason": "human", "outcome": "transferred", "customer_id": "c_a02401a9-ddc"}
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Date": "Sat, 10 Oct 2026 23:31:18 GMT", "Content-Type": "application/json", "Content-Length": "11", "Connection": "keep-alive", "Report-To": "{\"group\":\"cf-nel\",\"max_age\"
    ↪ close_transfer_general → end_call: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I am transferring you now to a colleague in our general team, who will help you with your request. Thank you for calling Freya Bank, goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
