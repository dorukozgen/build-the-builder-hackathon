"""Unit-test the brief-e hooks with fake vars/results."""
import json, pathlib
wf = json.loads(pathlib.Path(__file__).with_name("brief-e.workflow.json").read_text(encoding="utf-8"))
tools = {}
for n in wf["nodes"].values():
    for t in n.get("tools", []):
        tools[t["function"]["name"]] = t
for k, t in tools.items():
    for h in ("pre_process_code", "post_process_code"):
        assert "{{" not in t.get(h, "") and "}}" not in t.get(h, ""), (k, h)

def post(name, data, v):
    r = {"status": "success", "data": data, "header": {}}
    exec(tools[name]["post_process_code"], {"result": r, "vars": v})
    return r

def pre(name, body, v):
    c = {"body": body}
    exec(tools[name]["pre_process_code"], {"config": c, "vars": v})
    return c["body"]

v = {"now": "2026-10-14T11:00"}
r = post("list_campaigns", {"ok": True, "campaigns": [{"name": "A", "product": "credit_card", "valid_from": "2026-10-01", "valid_to": "2026-10-14"},
                                                      {"name": "B", "product": "credit_card", "valid_from": "2026-10-15", "valid_to": "2026-12-01"},
                                                      {"name": "C", "product": "credit_card", "valid_from": "2026-01-01", "valid_to": "2026-10-13"}]}, v)
print([c["status_today"] for c in r["data"]["campaigns"]], r["data"]["active_campaigns_today"])
r = post("get_campaign", {"ok": True, "valid_from": "2026-01-01", "valid_to": "2026-10-13"}, v); print(r["data"]["what_to_do_next"], v.get("e_informed"))
for d in [{"ok": True, "verified": False, "wrong_answers_left": 2, "all_verified": False, "hint": "day_month_swapped"},
          {"ok": True, "verified": True, "wrong_answers_left": 3, "all_verified": False},
          {"ok": True, "verified": False, "wrong_answers_left": 0, "all_verified": False},
          {"ok": False, "error": "x"}]:
    print(post("verify_identity", d, v)["data"]["what_to_do_next"][:70])
v2 = {}; post("check_eligibility", {"ok": True, "eligible": False, "reason": "age"}, v2); print(v2)
v3 = {}; r = post("check_eligibility", {"ok": True, "eligible": True}, v3); print(v3, r["data"]["what_to_do_next"][:60])
v4 = {}; r = post("start_application", {"ok": False, "error": "x"}, v4); r = post("start_application", None, v4); print(v4, r.get("what_to_do_next"))
v5 = {}; post("start_application", {"ok": True, "application_id": "APP-1234"}, v5); print(v5)
print(pre("start_application", {"campaign_id": "zzz"}, {"e_campaign": "cmp1"}))
print(pre("close_call", {"outcome": "informed"}, {"e_transfer_queue": "general"}))
print(pre("close_call", {"outcome": "informed", "reason": ""}, {}))
print(pre("close_call", {"outcome": "not_verified", "reason": "declined"}, {"verify_identity_response.data.wrong_answers_left": "0"}))
print(pre("close_call", {"outcome": "not_verified", "reason": ""}, {}))
print(pre("close_call", {"outcome": "not_verified", "reason": "failed"}, {"e_informed": "yes"}))
print(pre("close_call", {"outcome": "informed"}, {"e_applied": "yes", "e_not_eligible": "yes"}))
print(pre("close_call", {"outcome": "no_action", "reason": ""}, {"e_app_fail": 2}))
v6 = {}; post("transfer_to_sales", {"ok": True}, v6); print(v6)
