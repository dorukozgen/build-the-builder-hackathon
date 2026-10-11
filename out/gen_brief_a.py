"""Generate out/brief-a.workflow.json for Brief A."""
import json, pathlib

BASE = "https://freya-bank-mock.freyavoice.workers.dev/v1/"
HOLIDAYS = ["2026-10-26", "2026-11-11", "2026-11-26", "2026-12-25", "2027-01-01"]

# ---------------------------------------------------------------- code
FACTS_CODE = r'''
import datetime, json, re
HOL = HOLIDAYS_LIST
td = datetime.timedelta
def isbd(d):
    return d.weekday() < 5 and d.isoformat() not in HOL
def fmt(d):
    return d.strftime('%A') + ' ' + str(d.day) + ' ' + d.strftime('%B') + ' ' + str(d.year) + ' (' + d.isoformat() + ')'
def money(x):
    try:
        return '{:,.2f}'.format(float(x))
    except Exception:
        return str(x)
def to_list(v):
    if isinstance(v, str):
        s = v.strip()
        try:
            v = json.loads(s)
        except Exception:
            try:
                v = json.loads(s.replace("'", '"').replace('True', 'true').replace('False', 'false').replace('None', 'null'))
            except Exception:
                v = None
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, dict)]
    return []
def get_products():
    for key in ('products', 'load_account_response.data.products'):
        lst = to_list(vars.get(key))
        if lst:
            return lst
    found = dict()
    for k in list(vars.keys()):
        m = re.search(r'products\.(\d+)\.(\w+)$', str(k))
        if m:
            i = int(m.group(1))
            if i not in found:
                found[i] = dict()
            found[i][m.group(2)] = vars.get(k)
    return [found[i] for i in sorted(found.keys())]
try:
    now_s = str(vars.get('now') or '')
    try:
        nowdt = datetime.datetime.fromisoformat(now_s[:16])
    except Exception:
        nowdt = datetime.datetime.utcnow()
    today = nowdt.date()
    def nth_bd(n):
        d = today
        c = 0
        while c < n:
            d = d + td(days=1)
            if isbd(d):
                c += 1
        return d
    nbd = nth_bd(1)
    monday = today - td(days=today.weekday())
    def last_bd_of_week(mon):
        d = mon + td(days=4)
        while d >= mon and not isbd(d):
            d = d - td(days=1)
        return d
    lbw = last_bd_of_week(monday)
    if lbw <= today:
        lbw = last_bd_of_week(monday + td(days=7))
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    wk = []
    for i in range(7):
        wk.append('"this ' + names[i] + '" = ' + fmt(monday + td(days=i)) + '; "next ' + names[i] + '" = ' + fmt(monday + td(days=7 + i)))
    vars['today_text'] = fmt(today)
    vars['now_time'] = nowdt.strftime('%H:%M')
    vars['next_bd_text'] = fmt(nbd)
    cb = []
    cb.append('Now: ' + fmt(today) + ', time ' + nowdt.strftime('%H:%M') + '.')
    cb.append('Allowed callback days: today ' + today.isoformat() + ' (only times later than ' + nowdt.strftime('%H:%M') + ') or the next business day ' + fmt(nbd) + '. Allowed times: 10:00 to 19:00, both included.')
    cb.append('"Tomorrow" = ' + fmt(today + td(days=1)) + ('' if (today + td(days=1)) == nbd else ' which is NOT the next business day, so it is not allowed') + '.')
    cb.append('Times: "morning around eleven" = 11:00, "two in the afternoon" = 14:00, "half past three" = 15:30. Send time as HH:MM, 24 hour.')
    vars['callback_facts'] = '\n'.join(cb)
    prods = get_products()
    p = prods[0] if prods else None
    if p and p.get('product_id'):
        ptype = str(p.get('type') or '')
        if ptype == 'credit_card':
            phrase = 'credit card ending ' + str(p.get('card_last4') or '')
            floor = p.get('minimum_payment')
            floor_name = 'minimum payment'
        elif ptype == 'car_loan':
            phrase = 'car loan'
            floor = p.get('instalment_amount')
            floor_name = 'instalment amount'
        else:
            phrase = 'personal loan'
            floor = p.get('instalment_amount')
            floor_name = 'instalment amount'
        try:
            dl = int(float(p.get('days_late')))
        except Exception:
            dl = 0
        if dl <= 7:
            band = 'early'
            deadline = nth_bd(12)
            attempts = 1
        else:
            band = 'late'
            deadline = nth_bd(7)
            attempts = 2
        vars['product_id'] = str(p.get('product_id'))
        vars['product_phrase'] = phrase
        vars['past_due_text'] = money(p.get('past_due'))
        vars['days_late_text'] = str(dl)
        vars['floor_text'] = money(floor)
        vars['deadline_text'] = fmt(deadline)
        cal = []
        d = today
        while d <= deadline + td(days=10):
            tag = ''
            if d == today:
                tag = ' [TODAY]'
            if not isbd(d):
                kind = 'bank holiday' if d.isoformat() in HOL else 'weekend'
                if d <= deadline:
                    n = d + td(days=1)
                    while not isbd(n):
                        n = n + td(days=1)
                    cal.append(fmt(d) + tag + ': ' + kind + ', NOT allowed. Offer the next business day ' + fmt(n) + ' instead.')
                else:
                    cal.append(fmt(d) + tag + ': ' + kind + ', after the deadline, NOT allowed. Offer the deadline.')
            elif d <= deadline:
                cal.append(fmt(d) + tag + ': allowed' + (' (THE DEADLINE, latest allowed date)' if d == deadline else ''))
            else:
                cal.append(fmt(d) + ': after the deadline, NOT allowed. Offer the deadline ' + deadline.isoformat() + '.')
            d = d + td(days=1)
        a = []
        a.append('product_id: ' + str(p.get('product_id')))
        a.append('Product: ' + phrase)
        a.append('Full past-due amount: ' + money(p.get('past_due')) + ' (send as ' + str(float(p.get('past_due'))) + ')')
        a.append('Days late: ' + str(dl) + ' -> ' + band + ' band')
        a.append('Floor (' + floor_name + '): ' + money(floor) + ' (send as ' + str(float(floor)) + ')')
        a.append('Allowed amounts: from ' + money(floor) + ' up to ' + money(p.get('past_due')) + ', both included.')
        a.append('Deadline (latest promise date): ' + fmt(deadline))
        a.append('Persuasion attempts allowed: ' + str(attempts))
        a.append('Attempt 1 date (last business day of this week): ' + fmt(lbw))
        if attempts == 2:
            a.append('Attempt 2: the floor ' + money(floor) + ' on the deadline ' + fmt(deadline))
        else:
            a.append('There is NO attempt 2 for this customer.')
        vars['account_facts'] = '\n'.join(a)
        vars['date_facts'] = 'Today: ' + fmt(today) + '.\nCalendar (only dates marked allowed can be recorded):\n' + '\n'.join(cal) + '\nWeekday phrases:\n' + '\n'.join(wk)
        vars['account_state'] = 'ok'
    else:
        vars['account_state'] = 'missing'
        vars['account_facts'] = 'No account data.'
        vars['date_facts'] = 'Today: ' + fmt(today) + '.'
except Exception as e:
    vars['account_state'] = 'missing'
    vars['facts_error'] = str(e)
    for k in ('account_facts', 'date_facts', 'callback_facts', 'today_text', 'now_time', 'next_bd_text'):
        if not vars.get(k):
            vars[k] = 'unknown'
'''.replace("HOLIDAYS_LIST", repr(HOLIDAYS))
assert "{{" not in FACTS_CODE and "}}" not in FACTS_CODE

# ---------------------------------------------------------------- hooks
VERIFY_POST = r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        msg = ''
        if not isinstance(d, dict):
            msg = 'The check service failed and nothing was counted. Say sorry, there was a technical problem, and ask the same question again.'
        else:
            left = d.get('wrong_answers_left')
            if d.get('all_verified') is True:
                msg = 'Both answers are verified.'
            elif d.get('hint') == 'day_month_swapped':
                msg = 'Day and month look swapped. This is NOT counted as a wrong answer. Ask the customer to say their date of birth again with the month as a word, for example 14 March 1988. Then call verify_identity again.'
            elif d.get('ok') is False:
                msg = 'The answer could not be read and was NOT counted as wrong. Ask the customer to repeat it.'
            elif d.get('verified') is True:
                msg = 'Correct. Now ask the next security question: the last four digits of the phone number on file. Then call verify_identity with field phone_last4.'
            elif left is not None and str(left) == '0':
                msg = 'Third wrong answer. The check has failed.'
            else:
                msg = 'WRONG answer. Do not reveal the correct value. Say the answer does not match our records and ask the SAME question again.'
        if isinstance(d, dict):
            d['what_to_do_next'] = msg
        else:
            result['what_to_do_next'] = msg
except Exception:
    pass
'''

PROMISE_POST = r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        ok = isinstance(d, dict) and d.get('ok') is True
        if ok:
            msg = 'RECORDED.'
        else:
            msg = 'NOT RECORDED. The promise was NOT recorded. Never say it is recorded. Tell the customer there was a technical problem and that you are trying once more, and in the same message call create_promise again with the same amount and date.'
        if isinstance(d, dict):
            d['what_to_do_next'] = msg
        else:
            result['what_to_do_next'] = msg
except Exception:
    pass
'''

SIMPLE_POST = r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        ok = isinstance(d, dict) and d.get('ok') is True
        msg = 'Done.' if ok else 'FAILED. Nothing was recorded. Tell the customer it did not work and try once more.'
        if isinstance(d, dict):
            d['what_to_do_next'] = msg
        else:
            result['what_to_do_next'] = msg
except Exception:
    pass
'''

TRANSFER_PRE = r'''
try:
    b = config.get('body')
    if isinstance(b, dict) and b.get('queue'):
        vars['transfer_queue'] = str(b.get('queue'))
except Exception:
    pass
'''

CLOSE_PRE = r'''
try:
    b = config.get('body')
    if isinstance(b, dict) and b.get('outcome') in ('promise', 'paid'):
        b.pop('reason', None)
except Exception:
    pass
'''

HEADERS = {"type": "object", "properties": {"Content-Type": {"type": "string", "default": "application/json"}}}


def api_tool(name, desc, body_props, required, cfg_retries=0, post=None, pre=None, mapping=None):
    props = {"customer_id": {"type": "string", "default": "{{customer_id}}"}}
    props.update(body_props)
    t = {
        "type": "function",
        "config": {"timeoutMs": 12000, "maxRetries": cfg_retries},
        "function": {
            "name": name,
            "handler": "__function__:api_call",
            "description": desc,
            "parameters": {"type": "object", "properties": {
                "url": {"type": "string", "default": BASE + name},
                "method": {"type": "string", "default": "POST"},
                "headers": HEADERS,
                "body": {"type": "object", "properties": props, "required": required},
            }},
        },
    }
    if post:
        t["post_process_code"] = post
    if pre:
        t["pre_process_code"] = pre
    if mapping:
        t["response_mapping"] = mapping
    return t


def close_tool(outcomes, reasons, desc_extra):
    return api_tool(
        "close_call",
        "Ends the call record. CALL it exactly once, as the very last action, in the SAME message in which you thank the customer and say goodbye. " + desc_extra,
        {
            "outcome": {"type": "string", "enum": outcomes, "default": "{{close_outcome}}",
                        "description": "One of: " + ", ".join(outcomes) + "."},
            "reason": {"type": "string", "enum": reasons, "default": "{{close_reason}}",
                       "description": "One of: " + ", ".join(reasons) + ". Leave out only for outcome paid."},
        },
        ["outcome"], pre=CLOSE_PRE, post=SIMPLE_POST)


def transfer_tool(queues, desc):
    return api_tool("transfer_to_agent", desc,
                    {"queue": {"type": "string", "enum": queues, "default": "{{transfer_queue_choice}}",
                               "description": "One of: " + ", ".join(queues) + "."}},
                    ["queue"], pre=TRANSFER_PRE, post=SIMPLE_POST)


def code_node(name, nxt_transitions, default):
    return {
        "name": name, "node_type": "code", "passthrough": True,
        "passthrough_default_transition": default,
        "on_enter": {"type": "silent"}, "disable_inactivity_monitor": True,
        "pre_actions": [{"type": "function", "function": {
            "name": "code_exec", "handler": "__function__:code_exec",
            "parameters": {"type": "object", "properties": {
                "code": {"type": "string", "default": FACTS_CODE},
                "timeout_ms": {"type": "number", "default": 10000}}}}}],
        "transitions": nxt_transitions + [always(default)],
    }


def always(t):
    return {"target_node": t, "description": "always", "condition": {"operator": "always"}}


def var_or(desc, target, conds):
    return {"target_node": target, "description": desc, "condition": {"logic": "or", "conditions": conds}}


def eq(v, o):
    return {"variable": v, "operator": "equals", "operand": o}


def is_true(v):
    return [eq(v, "true"), eq(v, "True")]


def gt(v, n):
    return {"variable": v, "operator": "greater_than", "operand": n}


def close_node(name, outcome, reason, line):
    body = {"customer_id": {"type": "string", "default": "{{customer_id}}"},
            "outcome": {"type": "string", "default": outcome}}
    if reason:
        body["reason"] = {"type": "string", "default": reason}
    return {
        "name": name, "node_type": "api_request", "passthrough": True,
        "passthrough_default_transition": "end_call",
        "on_enter": {"type": "tts", "text": line}, "disable_inactivity_monitor": True,
        "pre_actions": [{"type": "function", "config": {"timeoutMs": 12000, "maxRetries": 1}, "function": {
            "name": "close_call", "handler": "__function__:api_call", "description": "Close the call.",
            "parameters": {"type": "object", "properties": {
                "url": {"type": "string", "default": BASE + "close_call"},
                "method": {"type": "string", "default": "POST"}, "headers": HEADERS,
                "body": {"type": "object", "properties": body, "required": []}}}}}],
        "transitions": [always("end_call")],
    }


# ---------------------------------------------------------------- prompts
SYSTEM = """You are Freya Bank's digital assistant on an outbound phone call. Speak English. Keep every turn to one or two short sentences. Ask one question at a time.
Address the customer as {{title}} {{last_name}}.
Rules that hold in every step:
- If asked whether you are a robot or an AI: say you are Freya Bank's digital assistant, then continue where you were.
- If asked whether this is a scam: say they can verify this call by phoning Freya Bank's customer service number, then continue where you were.
- If you cannot answer a question from the tool results, say you do not have that information. Never invent figures, dates, reasons or terms.
- Never offer a discount, a waiver, an instalment plan or any other term.
- Never ask the customer how much they can pay.
- When a rule says to call a tool, call the tool. Saying you did it is not enough. Call one tool per message.
- Every tool result contains what_to_do_next. Follow it. After every tool result, speak to the customer or call the next tool; never end a turn with nothing.
- Never say something is recorded, booked or transferred unless the tool result says ok true.
- The call variables: customer {{first_name}} {{last_name}} ({{title}}). The current date and time come from the facts below, never from your own clock."""

OPENING_TASK = """The opening line was already spoken: you said you are a digital assistant calling from Freya Bank, that the call is recorded, and asked "Am I speaking with {{title}} {{last_name}}?".
Until both security answers are verified, never say "collections", "debt", "payment", "late", any amount or any product. If asked what the call is about, say you can explain only after a short security check.

STEP 1: WHO IS ON THE LINE
- Confirmation is ONLY: "yes", "that's me", "speaking", or the customer's own name. "Hello", "go ahead", "who is this" are NOT confirmation.
- If not confirmed: answer any question first (robot, scam), then ask "Am I speaking with {{title}} {{last_name}}?" once more. If it is still unclear after that second ask, thank them, say goodbye and call close_call with outcome not_reached, reason unclear.
- Someone else answers (a relative, a colleague, anyone not {{title}} {{last_name}}): do not say why you are calling and say nothing about any account, even if they ask or offer to pay. Never ask them security questions. Ask when {{title}} {{last_name}} can be reached.
  Callback facts:
{{callback_facts}}
  If the day and time they give are inside the allowed window, call schedule_callback with date (YYYY-MM-DD) and time (HH:MM). If they give a time or day outside the window, ask once for another time inside it (10:00 to 19:00, today or the next business day). If the second answer is also outside, do not schedule: thank them, say goodbye and call close_call with outcome not_reached, reason no_callback.
- The number does not belong to the customer: apologise, say goodbye and call close_call with outcome not_reached, reason wrong_number.
- The customer has died: say exactly "I am sorry for your loss." Ask nothing else. Say goodbye and call close_call with outcome not_reached, reason deceased.

STEP 2: SECURITY QUESTIONS (only after {{title}} {{last_name}} confirmed)
- Ask first for the date of birth. Call verify_identity with field date_of_birth and answer as YYYY-MM-DD, whatever way it was said. A date given only as numbers is day, then month, then year (05/03/1988 = 1988-03-05). Words: "14 March 1988" = 1988-03-14.
- Then ask for the last four digits of the phone number on file. Call verify_identity with field phone_last4 and four digits.
- Call verify_identity once for every answer. Follow what_to_do_next in the result exactly (ask again, ask the month as a word, or go to the next question).
- If the customer does not want to answer, or asks what the call is about instead of answering: explain once that these questions protect their account, and ask again. If they refuse a second time or ask again what the call is about, thank them, say goodbye and call close_call with outcome not_verified, reason declined.
- If the customer says twice they do not want to talk: thank them, say goodbye and call close_call with outcome not_verified, reason declined.
- If the customer asks for a human: ask once whether you can help first. If they insist, call transfer_to_agent with queue general.

Do not call any other tool here. Never call close_call for a verified customer."""

COLLECTION_TASK = """The customer has passed the security check. You already told them: you are calling from the collections team about a late payment on their {{product_phrase}}, the past-due amount {{past_due_text}}, {{days_late_text}} days late, and asked "Can you make this payment today?".

ACCOUNT FACTS
{{account_facts}}

DATE FACTS
{{date_facts}}

AMOUNT RULES
- The agent proposes every amount. Never ask "how much can you pay?".
- Customer proposes an amount from the floor up to the full amount (both included): accept it.
- Customer proposes an amount below the floor: say it cannot be recorded and offer the floor once. If they do not accept the floor, that is a flat refusal.
- Customer says the full amount is too much: offer the floor, once, and say that the rest stays overdue. If they refuse the floor, that is a flat refusal.

DATE RULES
- A promise date must be an allowed date in the calendar above (today or later, a business day, not after the deadline).
- Weekend day or bank holiday not after the deadline: offer the next business day shown in the calendar.
- Date after the deadline: say the latest date you can record is the deadline ({{deadline_text}}) and offer it. If they refuse the deadline, that is a flat refusal.
- Vague period ("next week", "end of the month", "when my salary comes", "the week after next"): ask once for the exact day. If they still give none, propose the deadline.
- "next <weekday>" and "this <weekday>": use the weekday phrases above.

PERSUASION (count attempts carefully)
- A date or an amount the customer proposes is never a refusal: handle it with the rules above.
- A flat refusal or a non-answer uses one persuasion attempt. "No" to paying today with no date and no amount is a flat refusal.
- Attempt 1: propose the full past-due amount (or the floor, if they already said the full amount is too much) on the attempt 1 date from the account facts.
- Attempt 2 (only if the account facts allow 2 attempts): propose the floor on the deadline.
- When the allowed attempts are used up and they still refuse: stop. Do not repeat an offer they already refused. Thank them, say goodbye and call close_call with outcome no_promise, reason refused.
- If the customer says twice they do not want to talk: thank them, say goodbye and call close_call with outcome no_promise, reason refused.

CONFIRMING
- When an amount and an allowed date are agreed, read back the product, the amount and the date, and ask "Do you confirm?".
- Only after a clear yes, call create_promise with amount (a number, e.g. 420.0) and date (YYYY-MM-DD). If they change the amount or date, check it against the rules and read it back again.
- If create_promise does not return ok true, say there was a technical problem and call create_promise once more with the same values. Never say the promise is recorded unless ok is true.

OTHER SITUATIONS (these come before persuasion)
- Illness, a death in the family or job loss: say one short sentence of sympathy. Make NO persuasion attempt. Offer to connect them with the customer support team. If they accept, call transfer_to_agent with queue support. If they decline, thank them, say goodbye and call close_call with outcome no_promise, reason hardship. If they still name a date or amount themselves, handle it as a promise.
- "I already paid" (this past-due amount): say payments can take one business day to appear, take no promise, thank them, say goodbye and call close_call with outcome paid.
- "This debt is not mine", "I never had this product", or the product was closed or paid off in the past: do not argue, take no promise, thank them, say goodbye and call close_call with outcome no_promise, reason dispute.
- A new payment plan or lower instalments: do not describe any plan. Say you will connect them with the team that handles this and call transfer_to_agent with queue restructuring.
- A request for a human: ask once whether you can help first. If they insist, call transfer_to_agent with queue general.
- Questions you cannot answer from these facts: say you do not have that information."""

# ---------------------------------------------------------------- nodes
verify_tool = api_tool(
    "verify_identity",
    "Check one security answer. CALL it every time the customer gives a date of birth or phone digits.",
    {"field": {"type": "string", "enum": ["date_of_birth", "phone_last4"], "default": "{{verify_field}}",
               "description": "date_of_birth or phone_last4."},
     "answer": {"type": "string", "default": "{{verify_answer}}",
                "description": "date_of_birth as YYYY-MM-DD (numbers only = day, month, year). phone_last4 as four digits."}},
    ["field", "answer"], post=VERIFY_POST)

callback_tool = api_tool(
    "schedule_callback",
    "Book a callback for the customer. CALL it as soon as the person gives a day and time inside the allowed window.",
    {"date": {"type": "string", "default": "{{callback_date}}", "description": "YYYY-MM-DD"},
     "time": {"type": "string", "default": "{{callback_time}}", "description": "HH:MM, 24 hour, 10:00 to 19:00"}},
    ["date", "time"], post=SIMPLE_POST)

promise_tool = api_tool(
    "create_promise",
    "Record the payment promise. CALL it only after the customer said a clear yes to your read-back. Call it again once if the first call did not return ok true.",
    {"product_id": {"type": "string", "default": "{{product_id}}"},
     "amount": {"type": "number", "default": "{{promise_amount}}", "description": "Agreed amount as a number, e.g. 420.0"},
     "date": {"type": "string", "default": "{{promise_date}}", "description": "Agreed date as YYYY-MM-DD, an allowed date from the calendar"}},
    ["amount", "date"], post=PROMISE_POST, mapping=[{"path": "data.promise_id", "variable": "promise_id"}])

def transfer_routes():
    return [
        var_or("transferred to restructuring", "close_restructuring",
               [eq("transfer_to_agent_args.queue", "restructuring"), eq("transfer_queue", "restructuring")]),
        var_or("transferred to support", "close_support",
               [eq("transfer_to_agent_args.queue", "support"), eq("transfer_queue", "support")]),
        var_or("transferred to general", "close_human",
               [eq("transfer_to_agent_args.queue", "general"), eq("transfer_queue", "general")]),
    ]

closed_route = var_or("close_call was called", "end_call",
                      [gt("close_call_success_count", 0), gt("close_call_failure_count", 0)])

nodes = {
    "setup": code_node("setup", [], "opening"),
    "opening": {
        "name": "opening", "node_type": "conversation",
        "on_enter": {"type": "tts", "text": "Hello, I am a digital assistant calling from Freya Bank. This call is recorded. Am I speaking with {{title}} {{last_name}}?"},
        "on_enter_first_entry_only": True,
        "task_message": OPENING_TASK,
        "tools": [verify_tool, callback_tool,
                  transfer_tool(["general"], "Hand the call to a person. CALL it only when the customer insists on a human after you asked once whether you can help."),
                  close_tool(["not_reached", "not_verified"], ["unclear", "no_callback", "wrong_number", "deceased", "declined"],
                             "not_reached: unclear, no_callback, wrong_number, deceased. not_verified: declined.")],
        "max_node_turns": 40,
        "transitions": [
            var_or("both answers verified", "load_account", is_true("verify_identity_response.data.all_verified")),
            var_or("three wrong answers", "close_failed", [eq("verify_identity_response.data.wrong_answers_left", "0")]),
            var_or("callback booked", "close_callback", is_true("schedule_callback_response.data.ok")),
        ] + transfer_routes() + [closed_route],
    },
    "load_account": {
        "name": "load_account", "node_type": "api_request", "passthrough": True,
        "passthrough_default_transition": "prepare", "on_enter": {"type": "silent"},
        "disable_inactivity_monitor": True,
        "pre_actions": [{"type": "function", "config": {"timeoutMs": 12000, "maxRetries": 2}, "function": {
            "name": "get_account", "handler": "__function__:api_call", "description": "Get the late products.",
            "parameters": {"type": "object", "properties": {
                "url": {"type": "string", "default": BASE + "get_account"},
                "method": {"type": "string", "default": "POST"}, "headers": HEADERS,
                "body": {"type": "object", "properties": {"customer_id": {"type": "string", "default": "{{customer_id}}"}}, "required": []}}}}}],
        "response_mapping": [{"path": "data.products", "variable": "products"}],
        "suppress_tool_results": True,
        "transitions": [always("prepare")],
    },
    "prepare": code_node("prepare", [var_or("account ready", "collection", [eq("account_state", "ok")])], "close_account_error"),
    "collection": {
        "name": "collection", "node_type": "conversation",
        "on_enter": {"type": "tts", "text": "Thank you, {{title}} {{last_name}}. I am calling from the collections team about a late payment on your {{product_phrase}}. The past-due amount is {{past_due_text}}, and it is {{days_late_text}} days late. Can you make this payment today?"},
        "on_enter_first_entry_only": True,
        "task_message": COLLECTION_TASK,
        "tools": [promise_tool,
                  transfer_tool(["restructuring", "support", "general"],
                                "Hand the call to a person. restructuring: the customer asks for a new plan or lower instalments. support: a hardship customer accepted the support team. general: the customer insists on a human."),
                  close_tool(["no_promise", "paid"], ["refused", "hardship", "dispute"],
                             "no_promise with refused, hardship or dispute; paid (no reason) when the customer already paid.")],
        "max_node_turns": 40,
        "transitions": [
            var_or("promise recorded", "close_promise",
                   [{"variable": "promise_id", "operator": "is_set"}] + is_true("create_promise_response.data.ok")),
            var_or("promise failed twice", "close_service_error",
                   [gt("create_promise_success_count", 1), gt("create_promise_failure_count", 1),
                    {"logic": "and", "conditions": [gt("create_promise_success_count", 0), gt("create_promise_failure_count", 0)]}]),
        ] + transfer_routes() + [closed_route],
    },
    "close_promise": close_node("close_promise", "promise", None,
        "Thank you, your promise is recorded. You will receive a text message confirming this promise. Thank you for your time, goodbye."),
    "close_service_error": close_node("close_service_error", "no_promise", "service_error",
        "I am sorry, I could not record your promise because of a technical problem. Thank you for your time, goodbye."),
    "close_failed": close_node("close_failed", "not_verified", "failed",
        "I am sorry, I could not verify your identity. Please use the Freya Bank mobile app or visit a branch. Thank you for your time, goodbye."),
    "close_callback": close_node("close_callback", "not_reached", "callback",
        "Thank you, we will call back then. Goodbye."),
    "close_restructuring": close_node("close_restructuring", "transferred", "restructuring",
        "I am connecting you with our team now. Thank you, goodbye."),
    "close_support": close_node("close_support", "transferred", "support",
        "I am connecting you with our customer support team now. Thank you, goodbye."),
    "close_human": close_node("close_human", "transferred", "human",
        "I am connecting you with a colleague now. Thank you, goodbye."),
    "close_account_error": close_node("close_account_error", "no_promise", "service_error",
        "I am sorry, I cannot access your account details right now because of a technical problem. Thank you for your time, goodbye."),
    "end_call": {
        "name": "end_call", "node_type": "end_call", "on_enter": {"type": "silent"},
        "disable_inactivity_monitor": True, "transitions": [],
        "terminal": {"type": "function", "function": {
            "name": "call_closed", "handler": "__function__:end_call",
            "parameters": {"type": "object", "properties": {"message_mode": {"type": "string", "default": "none"}}}}},
    },
}

wf = {
    "initial_node": "setup",
    "system_prompt": SYSTEM,
    "nodes": nodes,
    "global_nodes": {},
    "test_variables": {"customer_id": "c_test", "first_name": "Daniel", "last_name": "Reyes", "title": "Mr", "now": "2026-10-14T11:00"},
}

out = pathlib.Path(__file__).with_name("brief-a.workflow.json")
out.write_text(json.dumps(wf, indent=1))
print("wrote", out)
