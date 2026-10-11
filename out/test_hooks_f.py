"""Exec the Brief F hooks locally on sample vars, config and results."""
import copy, json, sys
sys.argv = ["gen", "https://x.invalid/v1", "out/_tmp_f.json"]
sys.path.insert(0, "out")
import gen_brief_f as g

REQ = [{"name": "street", "question": "Street?", "format": "text", "required": True},
       {"name": "postcode", "question": "Postcode?", "format": "postcode", "required": True},
       {"name": "move_date", "question": "Date?", "format": "date", "required": False}]


def run(code, vars, config=None, result=None):
    env = {"vars": vars, "config": config, "result": result}
    exec(code, env)
    return env


def env_result(data):
    return {"status": "success", "data": data, "status_code": 200, "header": {"a": "b"}}


v = {"customer_id": "c1", "req_type": "address_change", "now": "2026-10-14T11:00"}
# verify pre: numeric date
cfg = {"body": {"field": "date_of_birth", "answer": "14/03/1985"}}
run(g.VERIFY_PRE, v, cfg); assert cfg["body"]["answer"] == "1985-03-14", cfg
r = env_result({"ok": True, "verified": False, "wrong_answers_left": 0, "all_verified": False}); run(g.VERIFY_POST, v, result=r)
assert v["id_state"] == "failed"
r = env_result({"ok": True, "verified": True, "wrong_answers_left": 3, "all_verified": True}); run(g.VERIFY_POST, v, result=r)
assert v["id_state"] == "verified"
r = env_result({"ok": False, "error": "x"}); run(g.VERIFY_POST, v, result=r); print(r["data"]["what_to_do_next"])

# find existing
r = env_result({"ok": True, "applications": [{"application_id": "APP-123", "type": "address_change", "status": "approved", "created_on": "2026-10-01", "note": ""}]})
run(g.FIND_EXISTING_POST, v, result=r); assert v["existing_state"] == "none", v
r = env_result({"ok": True, "applications": [{"application_id": "APP-124", "type": "address_change", "status": "more_info_needed", "created_on": "2026-10-01", "note": "proof of address"}]})
vv = dict(v); run(g.FIND_EXISTING_POST, vv, result=r); assert vv["existing_state"] == "more_info" and vv["ex_note"] == "proof of address", vv
print(vv["ex_id_spoken"])
run(g.FIND_EXISTING_POST, v, result=env_result({"ok": True, "applications": []}))
run(g.REQ_POST, v, result=env_result({"ok": True, "fields": REQ})); assert v["req_state"] == "ok"; print(v["collect_hint"])

def check(name, value):
    cfg = {"body": {"customer_id": "c1", "name": name, "value": value}}
    run(g.CHECK_PRE, v, cfg)
    assert cfg["body"] == {"customer_id": "c1", "type": "address_change"}, cfg
    r = env_result({"ok": True, "fields": copy.deepcopy(REQ)})
    run(g.CHECK_POST, v, result=r)
    return r["data"].get("what_to_do_next"), v.get("fields_state"), v.get("field_state")

print(check("street", "Main Street 5"))
print(check("postcode", "123"))
print(check("postcode", "12 345"))
assert v["fields_state"] == "collecting"
print(check("done", "done"))
assert v["fields_state"] == "complete", v
print(v["readback"])
# change
run(g.RESET_CHANGE_CODE, v)
print(check("postcode", "54321")); assert v["fields_state"] == "complete"
# exhaustion
v2 = dict(v, collected_json="{}", fail_json="{}", fields_state="collecting", optional_offered="no")
for _ in range(3):
    cfg = {"body": {"name": "postcode", "value": "abc"}}; run(g.CHECK_PRE, v2, cfg)
    run(g.CHECK_POST, v2, result=env_result({"ok": True, "fields": REQ}))
assert v2["field_state"] == "exhausted", v2
# create
cfg = {"body": {"customer_id": "c1", "type": "address_change"}}; run(g.CREATE_PRE, v, cfg); print(cfg)
assert cfg["body"]["fields"] == {"street": "Main Street 5", "postcode": "54321"}
run(g.CREATE_POST, v, result={"status": "error", "data": None}); assert v["create_state"] == "failed"
v["known_ids"] = "[]"
run(g.RECOVER_POST, v, result=env_result({"ok": True, "applications": [{"application_id": "APP-9", "type": "address_change", "status": "received", "created_on": "2026-10-14", "note": ""}]}))
assert v["recover_state"] == "found" and v["created_flag"] == "yes"
run(g.CREATE_POST, v, result=env_result({"ok": True, "application_id": "APP-482910", "status": "received"})); print(v["app_id_spoken"])
# close
for st, body in [({}, {"outcome": "no_action", "reason": "out_of_scope"}), ({"created_flag": "yes"}, {"outcome": "no_action", "reason": "x"}),
                 ({"transfer_state": "done", "transfer_queue": "general", "created_flag": "yes"}, {"outcome": "application_created"}),
                 ({"id_state": "failed"}, {"outcome": "transferred", "reason": "human"}), ({}, {"outcome": "status_given", "reason": ""})]:
    cfg = {"body": dict(body)}; run(g.CLOSE_PRE, dict(st, customer_id="c1"), cfg); print(st, "->", cfg["body"])
cfg = {"body": {"queue": "Security"}}; vv = {}; run(g.TRANSFER_PRE, vv, cfg); assert vv["transfer_queue"] == "security"
r = env_result({"ok": True}); run(g.TRANSFER_POST, vv, result=r); assert vv["transfer_state"] == "done"
cfg = {"body": {"application_id": "app 123 456"}}; run(g.GETAPP_PRE, {}, cfg); print(cfg)
r = env_result({"ok": True, "application_id": "APP-1", "type": "card_replacement", "status": "more_info_needed", "created_on": "x", "note": "photo id"}); run(g.GETAPP_POST, {}, result=r); print(r["data"]["what_to_do_next"])
r = env_result({"ok": False, "error": "unknown"}); run(g.GETAPP_POST, {}, result=r); print(r["data"]["what_to_do_next"][:60])
r = env_result({"ok": True, "applications": [{"application_id": "APP-1", "status": "in_review", "note": ""}]}); run(g.FIND_STATUS_POST, {}, result=r); print(r["data"]["what_to_do_next"])
vv = {"next_type": "status"}; run(g.NEXT_APP_CODE, vv); assert vv["req_type"] == "status" and vv["next_type"] == "none"
for st, body in [({"created_flag": "yes", "req_type": "limit_increase"}, {"outcome": "no_action"}), ({"req_type": "status"}, {"outcome": "no_action", "reason": "unsupported"}),
                 ({}, {"outcome": "not_verified", "reason": "declined"})]:
    vv = dict(st, customer_id="c1"); cfg = {"body": dict(body)}; run(g.WRAP_PRE, vv, cfg)
    print(vv["final_outcome"], vv["final_reason"], "|", vv["close_line"], cfg["body"])
    run(g.WRAP_POST, vv, result=env_result({"ok": True})); assert vv["wrap_state"] == "go"
    cfg = {"body": {"outcome": vv["final_outcome"], "reason": vv["final_reason"]}}; run(g.CLOSE_PRE, vv, cfg); print("  close:", cfg["body"])
vv = {"next_type": "limit_increase", "req_type": "limit_increase"}; run(g.SAME_TYPE_GUARD, vv); assert vv["next_state"] == "same"
vv = {"next_type": "address_change", "req_type": "limit_increase"}; run(g.SAME_TYPE_GUARD, vv); assert vv["next_state"] == "new" and vv["req_type"] == "address_change"
print("ALL HOOK TESTS PASSED")
