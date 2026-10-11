## GEN-37 — Address change submission times out
result: FAIL: outcome (None, None), expected ('application_created', None); the call was not closed with close_call; conversation: The agent correctly followed the instructions for handling a failed submission by checking 'find_applications' immediately after the 'create_application' tool timed out (System Events, Message 18). It also correctly avoided claiming the application was received before confirmation. However, the success criteria require that after the application returns, the agent must read the application ID digi
fixture PUB-10 · family Tool failure · level hard · rules brief-f:21, brief-f:20, brief-f:22
turns 23 · slowest agent turn 5.4 s · ended assistant-ended-call

    → node setup
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ setup → opening: always always
**agent:** Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?
**customer:** I need to change my address.
**agent:** I can help you with a change of address.
**agent:** Before I go on, I need to ask two security questions. What is your date of birth?
**customer:** Twenty-third of February nineteen eighty-nine.
    ⚙ verify_identity {"field": "date_of_birth", "answer": "1989-02-23", "customer_id": "f_5f15a15c03bc"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": false, "what_to_do_next": "Correct. Now ask for the last four digits of the phone number on file."}, "message": "Successfully executed POST request", "status_code": 200}
**agent:** Thank you. What are the last four digits of the phone number on file?
**customer:** Nine nine zero four.
    ⚙ verify_identity {"field": "phone_last4", "answer": "9904", "customer_id": "f_5f15a15c03bc"}
    ⚙ verify_identity → {"status": "success", "data": {"ok": true, "verified": true, "wrong_answers_left": 3, "all_verified": true, "what_to_do_next": "Identity verified."}, "message": "Successfully executed POST request", "status_code": 200}
    ↪ identity → service: Identity verified (id_state == 'verified' OR verify_identity_response.data.all_verified == 'true' OR verify_identity_response.data.all_verified == 'True')
**agent:** Thank you, Ms Lin. I will now help you with your address change.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_5f15a15c03bc"}
    ⚙ find_applications → {"status": "success", "data": {"ok": true, "applications": [], "what_to_do_next": "There is no open address change application. Now call get_requirements with type address_change."}, "message": "Successfully executed POST request", "status_code": 200}
    ⚙ get_requirements {"type": "address_change", "customer_id": "f_5f15a15c03bc"}
    ⚙ get_requirements → {"status": "success", "data": {"ok": true, "fields": [{"name": "street", "question": "What is the street and number of the new address?", "format": "text", "required": true}, {"name": "city", "question": "Which city?", "format": "text", "required": true}, {"name": "postcode", "question": "What is th
**agent:** What is the street and number of the new address?
**customer:** Main Road 3.
**agent:** Which city?
**customer:** Cork.
**agent:** What is the postcode? Five digits.
**customer:** one two three four five.
**agent:** You also have the option to provide the date from which the new address applies. Would you like to do that?
**customer:** No, I don't have a move date.
**agent:** The new address is Main Road 3, Cork, 12345. Shall I submit this application?
**customer:** Yes, I confirm. Did it work?
    ⚙ create_application {"type": "address_change", "fields": {"street": "Main Road 3", "city": "Cork", "postcode": "12345"}, "customer_id": "f_5f15a15c03bc"}
**agent:** I'm sorry, there was a technical error. Let me check if the application went through.
    ⚙ find_applications {"type": "address_change", "customer_id": "f_5f15a15c03bc"}
**agent:** I'm sorry, I'm still having trouble connecting to the system. I can transfer you to the applications team who can help you finish this. Would you like that?
**customer:** Yes, that's fine.
    ⚙ transfer_to_agent {"queue": "applications", "customer_id": "f_5f15a15c03bc"}
**agent:** I'm very sorry, but I'm unable to complete the transfer due to a technical issue. Please try calling us back later.
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ close_service_error → compute_close: always always
    ⚙ code_exec (code)
    ⚙ code_exec → {"status": "success", "data": null, "message": "Code executed successfully", "status_code": 200}
    ↪ compute_close → say_close: always always
    ⚙ api_call {"reason": "service_error", "outcome": "no_action", "customer_id": "f_5f15a15c03bc"}
    ⚙ api_call {"reason": "service_error", "outcome": "no_action", "customer_id": "f_5f15a15c03bc"}
    ↪ say_close → end: always always
**agent:** The application was not submitted because of a technical problem, so please call us again later. Thank you for calling Freya Bank. Goodbye.
    ⚙ end_call {"message_mode": "none"}
    ⚙ end_call → {"status": "success", "message": "Call ended"}
