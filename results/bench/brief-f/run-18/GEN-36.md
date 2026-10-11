## GEN-36 — Gave a one-time code to a caller
result: FAIL: outcome (None, None), expected ('transferred', 'security'); transfers [], expected [{'queue': 'security'}]; the call was not closed with close_call
fixture PUB-09 · family Security · level easy · rules brief-f:27
turns 3 · slowest agent turn 4.1 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** Someone called claiming to be the bank and I gave them a code from an SMS.
    ↪ opening → security_matter: Security matter: transfer at once matches intent "The customer says their card was lost or stolen, reports a payment or transaction on their account that they do not recognise, or says they gave a code (one-time code, PIN, password) to someone. A damaged or expired card is NOT a security matter."
    ⚙ api_call {"queue": "security", "customer_id": "f_800656c22285"}
    ⚙ api_call {"queue": "security", "customer_id": "f_800656c22285"}
    ↪ security_matter → sec_flag: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ sec_flag → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"reason": "security", "outcome": "transferred", "customer_id": "f_800656c22285"}
**agent:** I am passing your call to our security team now, and a colleague will take it from here. Thank you for calling Freya Bank. Goodbye.
    ⚙ api_call {"reason": "security", "outcome": "transferred", "customer_id": "f_800656c22285"}
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
