## GEN-18 — Address change, reads back only the new address
result: FAIL: outcome (None, None), expected ('application_created', None); the call was not closed with close_call; conversation: The call failed to meet most of the success criteria due to technical errors. While identity was verified and find_applications was called, the process stopped there. 1) The agent did not ask for the street, city, and postcode individually. 2) There was no read-back of the address 'Rua das Flores 27, Porto, 40150'. 3) No application was created, meaning the application ID was not read back and the; applications [], expected ['address_change']
fixture PUB-11 · family Happy path · level easy · rules brief-f:5, brief-f:9, brief-f:12, brief-f:16, brief-f:19, brief-f:20
turns 12 · slowest agent turn 3.5 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I moved and need to change my postal address.
**agent:** I can help you with a change of your postal address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Three June nineteen eighty seven.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1987-06-03", "customer_id": "f_704e45b03932"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** Two two eight eight.
    ⚙ verify_identity {"field": "phone_last4", "answer": "2288", "customer_id": "f_704e45b03932"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Almeida. I can help you with that address change.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_704e45b03932"}
**agent:** I'm sorry, I'm having trouble accessing your records. Please wait a moment while I try again.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_704e45b03932"}
**agent:** I apologize, but I am still unable to access the system. Please hold while I transfer you to the applications team.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_704e45b03932"}
**agent:** I am very sorry, but I am experiencing technical difficulties and cannot complete your request or transfer your call. Please try calling us back later.
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_service_error → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"reason": "service_error", "outcome": "no_action", "customer_id": "f_704e45b03932"}
    ⚙ api_call {"reason": "service_error", "outcome": "no_action", "customer_id": "f_704e45b03932"}
    ↪ say_close → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** The application was not submitted because of a technical problem, so please call us again later. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
