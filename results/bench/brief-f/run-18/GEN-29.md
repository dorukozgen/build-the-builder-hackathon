## GEN-29 — Unknown id, then lookup by type
result: FAIL: outcome (None, None), expected ('status_given', None); the call was not closed with close_call; conversation: The success criteria were not met because the assistant failed to perform any application status lookup due to persistent technical issues (API connection errors during identity verification and transfer attempts). Specifically: - The agent never mentioned or checked application ID APP-111111. - The agent never mentioned or checked application ID APP-305577 or its status. - The conversation ended 
fixture PUB-02 · family Status enquiry · level medium · rules brief-f:24, brief-f:23, brief-f:22, brief-f:29
turns 14 · slowest agent turn 3.2 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I am calling to check the status of an application.
**agent:** I can help you with a status enquiry about an application.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** My date of birth is second of November nineteen seventy nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1979-11-02", "customer_id": "f_0fc74b2f17d2"}
**agent:** I'm sorry, I'm having trouble accessing the system right now. Could you please repeat your date of birth?
**customer:** My date of birth is second of November nineteen seventy nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1979-11-02", "customer_id": "f_0fc74b2f17d2"}
**agent:** I apologize, I am still experiencing a technical issue. Could you please try providing your date of birth one more time?
**customer:** My date of birth is second of November nineteen seventy nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1979-11-02", "customer_id": "f_0fc74b2f17d2"}
**agent:** I'm sorry, I'm still unable to verify your date of birth. Would you like to be transferred to the applications team?
**customer:** Yes, please.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_0fc74b2f17d2"}
**agent:** I'm sorry, I'm unable to complete the transfer at the moment. Please try calling back later.
**customer:** Thank you, goodbye.
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_done → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"reason": "out_of_scope", "outcome": "no_action", "customer_id": "f_0fc74b2f17d2"}
    ⚙ api_call {"reason": "out_of_scope", "outcome": "no_action", "customer_id": "f_0fc74b2f17d2"}
    ↪ say_close → end: always always
**agent:** I could not help with that on this call, and nothing was changed on your account. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
