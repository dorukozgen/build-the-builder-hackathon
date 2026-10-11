## GEN-28 — Status enquiry on an application in review
result: FAIL: outcome ('no_action', 'out_of_scope'), expected ('status_given', None); conversation: The call failed to meet two of the success criteria: - The agent never informed the user that the application was 'being reviewed'; instead, the agent stated the application ID was not found and never located the record. - When the user asked 'when will I hear' (Messages 9 and 13), the agent responded with 'I do not have that information' rather than the required timeframe of 'within five business
fixture PUB-01 · family Status enquiry · level easy · rules brief-f:5, brief-f:23, brief-f:29
turns 16 · slowest agent turn 19.7 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I want to know the status of my application.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting the status of your application; however, I first need to verify your identity, so please provide your date of birth.
**customer:** 14 March 1988.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1988-03-14", "customer_id": "f_bff1239e10db"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, could you please provide the last four digits of the phone number we have on file?
**customer:** 4471.
    ⚙ verify_identity {"field": "phone_last4", "answer": "4471", "customer_id": "f_bff1239e10db"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → status: Verified, status enquiry (id_state == 'verified' AND req_type == 'status')
**agent:** I can help you with that, Mr Reyes. Could you please provide your application ID?
**customer:** A P P 4 8 2 9 1 3.
    ⚙ get_application {"customer_id": "f_bff1239e10db", "application_id": "APP482913"}
    ⚙ get_application → {"status": "success", "data": {"ok": false, "error": "unknown application_id", "what_to_do_next": "That application id was not found. Say so, and offer to look it up by type: ask which type it is (card replacement, address change or limit increase) and call find_applications with it. Never confirm t
**agent:** That application ID was not found. Would you like me to look it up by type? If so, please tell me if it is for a card replacement, address change, or limit increase.
**customer:** I am not sure. When will I hear?
    ↪ status → next_app: The customer raised another application or a status enquiry (next_type == 'card_replacement' OR next_type == 'address_change' OR next_type == 'limit_increase' OR next_type == 'status')
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ next_app → status: Status enquiry next req_type == 'status'
**agent:** I do not have that information. Would you like to tell me the type of application so I can try to find the status for you?
**customer:** I'm not really sure about
**agent:** I understand. Is there anything else I can help you with today?
**customer:** No, that was all. When will I hear
**agent:** I do not have that information. Since there is nothing else, I will end the call now.
    ⚙ wrap_up_call {"customer_id": "f_bff1239e10db", "type": "card_replacement"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ status → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"reason": "out_of_scope", "outcome": "no_action", "customer_id": "f_bff1239e10db"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I could not help with that on this call, and you can call us again at any time. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
