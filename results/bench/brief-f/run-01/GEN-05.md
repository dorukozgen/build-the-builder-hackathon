## GEN-05 — Wants a person, insists
result: PASS
fixture PUB-06 · family Human handoff · level easy · rules brief-f:25, brief-f:29
turns 5 · slowest agent turn 1.5 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → intake: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** Traffic was terrible this morning, and I'm already so behind on my emails. I want to speak to a real person.
**agent:** I can help you with several requests myself. Would you like to see if I can assist you first?
**customer:** Work has been absolutely non-stop today and I just don't have the patience for a machine. No, I want to speak to a person.
    ⚙ transfer_to_agent {"queue": "general", "customer_id": "c_ea6af003-a3d"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transfer_general: transferred to general (transfer_to_agent_args.queue == 'general' OR transfer_queue == 'general')
    ⚙ api_call {"reason": "human", "outcome": "transferred", "customer_id": "c_ea6af003-a3d"}
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Date": "Sat, 10 Oct 2026 23:22:34 GMT", "Content-Type": "application/json", "Content-Length": "11", "Connection": "keep-alive", "Report-To": "{\"group\":\"cf-nel\",\"max_age\"
    ↪ close_transfer_general → end_call: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I am transferring you to a colleague now. Thank you for calling Freya Bank, goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
