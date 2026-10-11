## GEN-04 — Wrong number
result: PASS
fixture PUB-07 · family Third party · level easy · rules brief-a:8
turns 3 · slowest agent turn 0.0 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Hello, I am a digital assistant calling from Freya Bank. This call is recorded. Am I speaking with Mr Ortiz?
**customer:** No, I am not Samuel Ortiz. You have the wrong number.
**agent:** I apologize for the mistake. Thank you for your time. Goodbye.
    ⚙ close_call {"reason": "wrong_number", "outcome": "not_reached", "customer_id": "c_d4d4f34e-0a9"}
    ⚙ close_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "Done."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ opening → end_call: close_call was called (close_call_success_count > 0 OR close_call_failure_count > 0)
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
