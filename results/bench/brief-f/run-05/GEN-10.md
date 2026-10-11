## GEN-10 — Insists on speaking to a human after being offered help once
result: PASS
fixture PUB-03 · family Human handoff · level easy · rules brief-f:25, brief-f:29, brief-f:30
turns 5 · slowest agent turn 3.9 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → intake: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I'd rather speak to a real person, please.
**agent:** I can help you with many requests. Would you like to see if I can assist you first?
**customer:** No, thank you. I specifically want to speak to a person.
    ⚙ transfer_to_agent {"queue": "general", "customer_id": "f_fc8deb305ada"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ intake → close_transfer_general: transferred to general (transfer_to_agent_args.queue == 'general' OR transfer_queue == 'general')
    ⚙ api_call {"reason": "human", "outcome": "transferred", "customer_id": "f_fc8deb305ada"}
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 00:01:16 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ close_transfer_general → end_call: always always
**agent:** I am transferring you now to a colleague in our general team, who will help you with your request. Thank you for calling Freya Bank, goodbye.
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
