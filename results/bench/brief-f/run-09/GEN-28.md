## GEN-28 — Status enquiry on an application in review
result: PASS
fixture PUB-01 · family Status enquiry · level easy · rules brief-f:5, brief-f:23, brief-f:29
turns 13 · slowest agent turn 6.5 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I want to know the status of my application.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting the status of your application; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** 14 March 1988.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1988-03-14", "customer_id": "f_9eb4c4b99e99"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, could you please provide the last four digits of the phone number on file?
**customer:** 4471.
    ⚙ verify_identity {"field": "phone_last4", "answer": "4471", "customer_id": "f_9eb4c4b99e99"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → status: Verified, status enquiry (id_state == 'verified' AND req_type == 'status')
**agent:** I can help you with that, Mr Reyes. Could you please provide your application ID?
**customer:** A P P 4 8 2 9 1 3.
    ⚙ get_application {"customer_id": "f_9eb4c4b99e99", "application_id": "APP-482913"}
    ⚙ get_application → {"status": "success", "data": {"ok": true, "application_id": "APP-482913", "type": "limit_increase", "status": "in_review", "created_on": "2026-10-12", "note": "", "what_to_do_next": "Tell the customer exactly: \"Application A, P, P, dash, 4, 8, 2, 9, 1, 3 is being reviewed.\" Give no other reason a
**agent:** Application A, P, P, dash, 4, 8, 2, 9, 1, 3 is being reviewed. Is there anything else I can help you with?
**customer:** When will I hear?
    ↪ status → next_app: The customer raised another application or a status enquiry (next_type == 'card_replacement' OR next_type == 'address_change' OR next_type == 'limit_increase' OR next_type == 'status')
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ next_app → status: Status enquiry next req_type == 'status'
**agent:** You will hear from us within five business days of the application. Is there anything else I can help you with?
**customer:** No, that is all for today.
    ⚙ wrap_up_call {"customer_id": "f_9eb4c4b99e99", "type": "card_replacement"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ status → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"outcome": "status_given", "customer_id": "f_9eb4c4b99e99"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I have given you the status of your application, and the applications team will keep you informed. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
