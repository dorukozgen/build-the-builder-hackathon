## GEN-30 — Rejected application, asks why and what the fee is
result: FAIL: outcome ('transferred', 'applications'), expected ('status_given', None); transfers [{'queue': 'applications'}], expected []; conversation: The agent failed one of the success criteria. While the agent correctly stated the application was 'not approved' [Message 6] and did not invent a fee, the agent failed to explain that it did not have information regarding the reason for the rejection. When the user asked 'Why?' [Message 7], the agent completely ignored the question and pivoted to asking if the card was damaged or expired [Message
fixture PUB-04 · family Status enquiry · level medium · rules brief-f:23, brief-f:28
turns 15 · slowest agent turn 15.4 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** What happened with my card application APP-774410?
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are asking for the status of your card application; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** Thirty January nineteen eighty four.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1984-01-30", "customer_id": "f_ed83870c4872"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, could you please provide the last four digits of the phone number on file?
**customer:** Two two one nine.
    ⚙ verify_identity {"field": "phone_last4", "answer": "2219", "customer_id": "f_ed83870c4872"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → status: Verified, status enquiry (id_state == 'verified' AND req_type == 'status')
    ⚙ get_application {"customer_id": "f_ed83870c4872", "application_id": "APP-774410"}
    ⚙ get_application → {"status": "success", "data": {"ok": true, "application_id": "APP-774410", "type": "card_replacement", "status": "rejected", "created_on": "2026-10-01", "note": "", "what_to_do_next": "Tell the customer exactly: \"Application A, P, P, dash, 7, 7, 4, 4, 1, 0 is not approved.\" Give no other reason an
**agent:** Ms Hoffmann, application A, P, P, dash, 7, 7, 4, 4, 1, 0 is not approved. Is there anything else I can help you with?
**customer:** Why? And what would a new card cost me?
    ↪ status → next_app: The customer raised another application or a status enquiry (next_type == 'card_replacement' OR next_type == 'address_change' OR next_type == 'limit_increase' OR next_type == 'status')
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ next_app → find_existing: always always
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_ed83870c4872"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [{"application_id": "APP-774410", "type": "card_replacement", "status": "rejected", "created_on": "2026-10-01", "note": ""}], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request",
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "card_replacement", "customer_id": "f_ed83870c4872"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "reason", "question": "Is the card damaged or expired?", "format": "choice", "options": ["damaged", "expired"], "required": true}, {"name": "card_last4", "question": "What are the last four digits of the card, if you have them?", "format
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Thank you, Ms Hoffmann. Is the card damaged or expired?
**customer:** I don't have the card yet.
**agent:** I'm sorry, but I need to know if the card is damaged or expired. Which one is it?
**customer:** Neither. I do not have a card.
**agent:** I'm sorry, but I can only take a replacement application if the card is damaged or expired. Would you like to speak with our applications team to request a new card?
**customer:** Yes, please.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_ed83870c4872"}
    ⚙ transfer_to_agent → {"status": "success", "data": {"ok": true, "what_to_do_next": "The transfer is under way."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ collect → close_transferred: A transfer went through transfer_state == 'done'
    ⚙ api_call {"reason": "applications", "outcome": "transferred", "customer_id": "f_ed83870c4872"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ close_transferred → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** I have transferred you to the applications team, who will take it from here and help you shortly. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
