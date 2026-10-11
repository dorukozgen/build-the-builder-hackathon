"""The smallest builder that works end to end: one conversation node, the brief pasted in as its prompt, seven tools.

    python examples/minimal_builder.py briefs/brief-a.md                    ->  prints {workflow_id, agent_id}
    python examples/minimal_builder.py briefs/brief-a.md briefs/brief-b.md  ->  Brief B builds on Brief A, pass both

It is a place to start, not a good score. Everything that makes an agent reliable is missing on purpose:
date arithmetic in code, separate nodes per stage, counters, checks before recording.

The tool list below is typed by hand for Briefs A and B. A final brief has other fields and other allowed values,
so a real builder reads the tools from the brief and from the tool API file that comes with it.
"""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import freya

BANK = "https://freya-bank-mock.freyavoice.workers.dev/v1"

def tool(name, description, fields):
    """An HTTP tool the model can call. `customer_id` is filled by the platform from the call variable.
    Every other field has no value yet when the node is entered, so the model fills it."""
    props = {"customer_id": {"type": "string", "default": "{{customer_id}}"}}
    for f, (typ, desc, enum) in fields.items():
        props[f] = {"type": typ, "description": desc, "default": "{{" + f + "}}"} | ({"enum": enum} if enum else {})
    return {"type": "function", "config": {"timeoutMs": 10000, "maxRetries": 0},
            "function": {"name": name, "handler": "__function__:api_call", "description": description,
                         "parameters": {"type": "object", "properties": {
                             "url": {"type": "string", "default": f"{BANK}/{name}"}, "method": {"type": "string", "default": "POST"},
                             "headers": {"type": "object", "properties": {"Content-Type": {"type": "string", "default": "application/json"}}},
                             "body": {"type": "object", "properties": props, "required": list(fields)}}}}}

S, N = "string", "number"
TOOLS = [
    tool("verify_identity", "Check one security answer. Call it every time the customer answers a security question.",
         {"field": (S, "Which question was answered", ["date_of_birth", "phone_last4"]), "answer": (S, "date_of_birth: the date as YYYY-MM-DD. phone_last4: four digits.", None)}),
    tool("get_account", "Get the customer's late products. Call it once, right after both security questions passed.", {}),
    tool("create_promise", "Record a payment promise. Call it only after the customer confirmed the read-back.",
         {"product_id": (S, "product_id from get_account", None), "amount": (N, "Promised amount", None), "date": (S, "Promised date, YYYY-MM-DD", None)}),
    tool("add_note", "Brief B only: record why a product ended without a promise.",
         {"product_id": (S, "product_id from get_account", None), "reason": (S, "Why there is no promise", ["refused", "hardship", "dispute", "paid", "service_error"])}),
    tool("schedule_callback", "Book a callback when someone else answered.", {"date": (S, "YYYY-MM-DD", None), "time": (S, "HH:MM, 24 hour", None)}),
    tool("transfer_to_agent", "Hand the call to a person.", {"queue": (S, "Which team", ["restructuring", "general", "support"])}),
]
CLOSE = tool("close_call", "End the call with its outcome. Always the last tool you call, after you said goodbye.",
             {"outcome": (S, "Outcome from the table in the brief", ["promise", "paid", "transferred", "no_promise", "not_verified", "not_reached"]),
              "reason": (S, "Reason from the table in the brief. Leave it out for promise and paid.", None)})
CLOSE["function"]["parameters"]["properties"]["body"]["required"] = ["outcome"]
# A tool's JSON response is stored as <tool_name>_response, with the body under `data`.
# The transition below reads it to see that the call is over.

def build(brief_text):
    task = ("You are on a phone call. Follow the brief below exactly.\n\n"
            "Call variables: customer_id={{customer_id}}, first_name={{first_name}}, last_name={{last_name}}, title={{title}}, now={{now}}.\n\n"
            "When a rule says to use a tool, call the tool. Saying that you did something is not enough.\n\n# BRIEF\n\n" + brief_text)
    return {
        "initial_node": "call",
        "system_prompt": "You are Freya Bank's digital assistant on an outbound phone call. Speak English. Keep every turn to one or two short sentences.",
        "nodes": {
            "call": {"name": "call", "node_type": "conversation", "task_message": task, "tools": TOOLS + [CLOSE], "max_node_turns": 60,
                     "transitions": [{"target_node": "hang_up", "description": "close_call succeeded",
                                      "condition": {"logic": "or", "conditions": [{"variable": "close_call_response.data.ok", "operator": "equals", "operand": o} for o in ("true", "True")]}}]},
            "hang_up": {"name": "hang_up", "node_type": "end_call", "on_enter": {"type": "silent"}, "disable_inactivity_monitor": True, "transitions": [],
                        "terminal": {"type": "function", "function": {"name": "hang_up", "handler": "__function__:end_call",
                                     "parameters": {"type": "object", "properties": {"message_mode": {"type": "string", "default": "none"}}}}}},
        },
        "global_nodes": {},
        "test_variables": {"customer_id": "c_test", "first_name": "Daniel", "last_name": "Reyes", "title": "Mr", "now": "2026-10-14T11:00"},
    }

if __name__ == "__main__":
    briefs = [pathlib.Path(x) for x in sys.argv[1:] if not x.startswith("--")]
    wf = build("\n\n".join(b.read_text() for b in briefs))
    if "--print" in sys.argv: print(json.dumps(wf, indent=1)); sys.exit()
    print(json.dumps(freya.save_workflow("+".join(b.stem for b in briefs), wf)))   # first run creates, later runs update the same workflow
