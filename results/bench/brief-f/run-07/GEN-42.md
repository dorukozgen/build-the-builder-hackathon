## GEN-42 — Invalid postcode three times, accepts the transfer
result: FAIL: outcome ('no_action', 'incomplete'), expected ('transferred', 'applications'); transfers [], expected [{'queue': 'applications'}]; conversation: The agent failed to meet the success criteria because it did not offer a transfer to the applications team after the third invalid postcode. The user provided invalid responses regarding the postcode in messages 11, 13, and 15. Following the third invalid response, the agent simply repeated the request for a five-digit postcode in message 16 and subsequently offered to end the call in message 18, 
fixture PUB-11 · family Collection · level hard · rules brief-f:13, brief-f:29
turns 21 · slowest agent turn 5.6 s · ended assistant-ended-call

    → node intake
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I'd like to change my address.
    ↪ intake → identity: The request type is known (req_type == 'card_replacement' OR req_type == 'address_change' OR req_type == 'limit_increase' OR req_type == 'status')
**agent:** You are requesting a change of your postal address; however, I first need to verify your identity, so could you please provide your date of birth?
**customer:** My date of birth is 3 June 1987.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1987-06-03", "customer_id": "f_d7556951cb76"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "That answer is correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. Now, could you please provide the last four digits of the phone number we have on file for you?
**customer:** The last four digits are 2288.
    ⚙ verify_identity {"field": "phone_last4", "answer": "2288", "customer_id": "f_d7556951cb76"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity is verified. Do not say anything more about the check."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → find_existing: Verified, application id_state == 'verified'
    ⚙ api_call {"type": "address_change", "customer_id": "f_d7556951cb76"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "No open application of this type. Continue."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ find_existing → load_requirements: No open application existing_state == 'none'
    ⚙ api_call {"type": "address_change", "customer_id": "f_d7556951cb76"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
    ↪ load_requirements → collect: Requirements loaded req_state == 'ok'
**agent:** Thank you, Ms Almeida. What is the street and number of the new address?
**customer:** Rua Nova 4.
    ⚙ check_field {"customer_id": "f_d7556951cb76", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** Which city?
**customer:** Braga.
    ⚙ check_field {"customer_id": "f_d7556951cb76", "type": "address_change"}
    ⚙ check_field → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the postcode? Five digits.
**customer:** I don't know it.
**agent:** The postcode is a required field. Could you please provide the five-digit postcode for the new address?
**customer:** 47.
**agent:** The postcode must be five digits. Could you please provide the full five-digit postcode?
**customer:** something with four.
**agent:** The postcode must be five digits. Could you please provide the full five-digit postcode?
**customer:** I really don't have it.
**agent:** I'm sorry, but the postcode is required to proceed with the address change. Would you like to provide it now, or should we end the call?
**customer:** I really don't have it.
    ⚙ wrap_up_call {"customer_id": "f_d7556951cb76", "type": "address_change"}
    ⚙ wrap_up_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The closing words are spoken for you. Say nothing."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ collect → closing: The call is to be closed wrap_state == 'go'
    ⚙ api_call {"reason": "incomplete", "outcome": "no_action", "customer_id": "f_d7556951cb76"}
    ⚙ api_call → {"status": "success", "data": {"ok": true, "what_to_do_next": "The call is closed. Say nothing more."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ closing → end: always always
    ⚙ end_call {"message_mode": "none"}
**agent:** The application was not submitted, and you can call us again whenever you are ready. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call → {"status": "success", "message": "Call ended"}
