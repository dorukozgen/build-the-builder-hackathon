## GEN-24 — Existing address application waits for proof, accepts transfer
result: PASS
fixture PUB-08 · family Existing application · level medium · rules brief-f:9, brief-f:10, brief-f:29
turns 9 · slowest agent turn 24.8 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You would like to change your postal address; first, I need to verify your identity, so please provide your date of birth.
**customer:** Twenty-eighth of April nineteen ninety-three.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1993-04-28", "customer_id": "f_43ac5522cd78"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, please provide the last four digits of the phone number on file.
**customer:** Three three one seven.
    ⚙ verify_identity {"field": "phone_last4", "answer": "3317", "customer_id": "f_43ac5522cd78"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "address_change", "customer_id": "f_43ac5522cd78"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [{"application_id": "APP-203344", "type": "address_change", "status": "more_info_needed", "created_on": "2026-10-10", "note": "Proof of address needed."}], "what_to_do_next": "An open application exists. Do not create another one."}, "messag
    ↪ find_existing → existing_more_info: Open application waiting for information existing_state == 'more_info'
**agent:** Thank you, Ms Schmidt, you are verified. You already have an application of this type, number A, P, P, dash, 2, 0, 3, 3, 4, 4. It is waiting for information from you: Proof of address needed.. The applications team is waiting for that information, and I cannot add it on this call. Would you like me to transfer you to the applications team?
**customer:** Yes, transfer me.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_43ac5522cd78"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ existing_more_info → close_transferred: A transfer went through transfer_state == 'done'
    ⚙ api_call {"reason": "applications", "outcome": "transferred", "customer_id": "f_43ac5522cd78"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ close_transferred → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
