## GEN-24 — Existing address application waits for proof, accepts transfer
result: FAIL: conversation: The agent failed to satisfy the first success criterion: it never mentioned that 'proof of address is needed'. However, it did satisfy the second criterion by asking the customer for permission to transfer and receiving an explicit 'Yes' before initiating the transfer. The call ended correctly via an assistant-initiated end action following the transfer.
fixture PUB-08 · family Existing application · level medium · rules brief-f:9, brief-f:10, brief-f:29
turns 16 · slowest agent turn 6.1 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** The twenty eighth of April nineteen ninety three.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1993-04-28", "customer_id": "f_83f2396695e1"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** The last four digits are three three one seven.
    ⚙ verify_identity {"field": "phone_last4", "answer": "3317", "customer_id": "f_83f2396695e1"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Schmidt. I can help you with that address change. Which address would you like to move to?
**customer:** I haven't decided on the exact location yet.
**agent:** I'm sorry, but the new address is a required field for this application. Which address would you like to move to?
**customer:** I don't have the new address yet.
**agent:** I'm sorry, but the new address is required to proceed. Which address would you like to move to?
**customer:** I don't have a new address to provide
**agent:** I am sorry, but I cannot proceed without a new address. Would you like to be transferred to the applications team?
**customer:** Yes, transfer me.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_83f2396695e1"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ service → compute_close: A transfer went through (xfer_queue == 'applications' OR xfer_queue == 'security' OR xfer_queue == 'general')
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"reason": "applications", "outcome": "transferred", "customer_id": "f_83f2396695e1"}
    ⚙ api_call → {"status": "success", "data": {"ok": true}, "message": "Successfully executed POST request", "status_code": 200, "header": {"Content-Length": "12", "Content-Type": "application/json", "Date": "Sun, 11 Oct 2026 16:47:26 GMT", "Ngrok-Agent-Ips": "176.41.224.110", "Server": "BaseHTTP/0.6 Python/3.14.3"
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I am passing your call to our applications team now, and a colleague will take it from here. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
