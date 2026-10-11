"""Generate out/brief-e.workflow.json for Brief E (campaigns and product information).

    py -3 out/gen_brief_e.py            # BRIEF_E_BASE=<mock base url> to point the tools at a practice mock
"""
import json, os, pathlib

BASE = os.environ.get("BRIEF_E_BASE", "https://freya-bank-mock.freyavoice.workers.dev").rstrip("/") + "/v1/"
OPENING = ("Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. "
           "How can I help you today?")
RECEIVED = "This means we have received it, not that it is approved. The decision comes within five business days by SMS."
ELIGIBLE_LINE = "You meet the conditions we can check. The final decision is made on the application."

# ------------------------------------------------------------------ python hooks (no double braces anywhere)
HDR = r'''
def _v():
    try:
        return vars
    except Exception:
        return dict()
def _data(res):
    if isinstance(res, dict):
        d = res.get('data')
        if isinstance(d, dict):
            return d
    return None
def _ok(d):
    return isinstance(d, dict) and (d.get('ok') is True or str(d.get('ok')).lower() == 'true')
def _today():
    return str(_v().get('now') or '')[:10]
def _status(c):
    t = _today()
    f = str(c.get('valid_from') or '')[:10]
    e = str(c.get('valid_to') or '')[:10]
    if not t or not f or not e:
        return 'unknown'
    if t < f:
        return 'not_started'
    if t > e:
        return 'expired'
    return 'active'
'''

POST_VERIFY = HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    if d is None:
        result['what_to_do_next'] = 'The check did not go through. It is not a wrong answer. Ask the same question again.'
    elif not _ok(d):
        d['what_to_do_next'] = 'The answer could not be read. It is not a wrong answer. Ask the same question again.'
    elif str(d.get('all_verified')).lower() == 'true':
        d['what_to_do_next'] = 'Both answers are verified. Identity is confirmed.'
    elif d.get('hint') == 'day_month_swapped':
        d['what_to_do_next'] = 'Not a wrong answer. Ask for the date of birth again and ask the customer to say the month as a word.'
    elif str(d.get('wrong_answers_left')) == '0':
        d['what_to_do_next'] = 'Three wrong answers: the check has ended. Say that eligibility and applications cannot continue on this call, and that general information can still be given.'
    elif str(d.get('verified')).lower() == 'true':
        d['what_to_do_next'] = 'That answer is correct. Now ask the next security question: the last four digits of the phone number on file.'
    else:
        d['what_to_do_next'] = 'That answer did not match. Do not reveal the right value. Ask the same question once more.'
except Exception:
    pass
'''

POST_LIST = HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    if _ok(d) and isinstance(d.get('campaigns'), list):
        act = []
        for c in d['campaigns']:
            if isinstance(c, dict):
                c['status_today'] = _status(c)
                if c['status_today'] == 'active':
                    act.append(str(c.get('name')) + ' (' + str(c.get('product')) + ')')
        d['active_campaigns_today'] = act
        d['what_to_do_next'] = 'status_today says which campaigns are active today. Name only active ones, at most three for the product asked about; if more than three are active for it, ask first which product feature matters most. Mention a campaign the customer did not ask about only if the rules allow it.'
    elif d is not None:
        d['what_to_do_next'] = 'The campaign list could not be loaded. Say you do not have that information right now.'
except Exception:
    pass
'''

POST_GET = HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    if _ok(d):
        st = _status(d)
        d['status_today'] = st
        try:
            vars['e_informed'] = 'yes'
        except Exception:
            pass
        if st == 'expired':
            d['what_to_do_next'] = 'This campaign has ENDED. Say it ended on ' + str(d.get('valid_to')) + ' and that its terms are no longer available. Do not describe its conditions as available.'
        elif st == 'not_started':
            d['what_to_do_next'] = 'This campaign has NOT STARTED. Say it starts on ' + str(d.get('valid_from')) + '.'
        else:
            d['what_to_do_next'] = 'Active campaign. Answer only what was asked. When the conditions are asked for, read EVERY item of conditions and EVERY item of exclusions word for word, nothing added, rounded or softened. If the summary differs from the conditions, the conditions govern: say so.'
    elif d is not None:
        d['what_to_do_next'] = 'The campaign could not be loaded. Say you do not have that information right now.'
except Exception:
    pass
'''

POST_CONSENT = HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    if _ok(d):
        m = str(d.get('marketing')).lower() == 'true'
        vars['e_marketing'] = 'yes' if m else 'no'
        d['what_to_do_next'] = ('Marketing consent is given: after the customer question is fully answered you may mention at most ONE other active campaign for the same product, once.' if m else 'No marketing consent: answer only what was asked and propose nothing else.')
    elif d is not None:
        d['what_to_do_next'] = 'Consent could not be read. Treat it as no consent: propose nothing.'
except Exception:
    pass
'''

REASONS = {
    "existing_product": "you already have this product",
    "already_enrolled": "you are already in this campaign",
    "age": "the age condition is not met",
    "income_not_on_file": "we have no income information on file; a branch can add it",
    "account_status": "your account status does not allow it; the general team can explain",
}
POST_ELIG = HDR + "REASONS = " + repr(REASONS) + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    vars['e_elig_new'] = 'yes'
    if _ok(d) and str(d.get('eligible')).lower() == 'true':
        vars['e_elig_state'] = 'eligible'
        d['what_to_do_next'] = 'Say exactly: "''' + ELIGIBLE_LINE + r'''" Never say the customer qualifies or is approved. If the customer wants to apply, read back the campaign name and the product and ask "Shall I start the application?".'
    elif _ok(d):
        r = str(d.get('reason') or '')
        if r == 'not_checked':
            vars['e_elig_state'] = 'not_checked'
            d['what_to_do_next'] = 'Say the check could not be done now and offer a transfer to the sales team. Do not start an application.'
        else:
            vars['e_elig_state'] = 'not_eligible'
            vars['e_not_eligible'] = 'yes'
            d['what_to_do_next'] = 'Not eligible. Say: "' + REASONS.get(r, 'the conditions are not met') + '". Do not start an application and propose no other campaign unless the customer asks.'
    else:
        vars['e_elig_state'] = 'error'
        if d is not None:
            d['what_to_do_next'] = 'The check failed. Say the check could not be done now and offer a transfer to the sales team. Do not state any eligibility.'
except Exception:
    pass
'''

PRE_START = r'''
try:
    c = vars.get('e_campaign')
    b = config.get('body')
    if isinstance(b, dict) and c:
        b['campaign_id'] = c
except Exception:
    pass
'''

POST_START = HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    if _ok(d) and d.get('application_id'):
        a = str(d.get('application_id'))
        vars['e_applied'] = 'yes'
        vars['e_app_id'] = a
        words = dict(zip('0123456789-', ['zero','one','two','three','four','five','six','seven','eight','nine','dash']))
        vars['e_app_spoken'] = ', '.join(words.get(ch, ch) for ch in a if ch.strip())
        d['what_to_do_next'] = 'The application is received.'
    else:
        n = int(vars.get('e_app_fail') or 0) + 1
        vars['e_app_fail'] = n
        msg = 'The application was NOT started. Never say it was received. '
        msg += ('Call start_application once more now.' if n < 2 else 'Say it could not be started and offer a transfer to the sales team.')
        if d is not None:
            d['what_to_do_next'] = msg
        elif isinstance(result, dict):
            result['what_to_do_next'] = msg
except Exception:
    pass
'''

def post_transfer(queue):
    return HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    if _ok(d):
        vars['e_transfer_queue'] = '%s'
        d['what_to_do_next'] = 'The transfer is done. Say in one sentence what was done, thank the customer, say goodbye, then call close_call.'
    elif d is not None:
        d['what_to_do_next'] = 'The transfer failed. Say so.'
except Exception:
    pass
''' % queue

PRE_CLOSE = r'''
try:
    b = config.get('body')
    if isinstance(b, dict):
        o = str(b.get('outcome') or '')
        r = b.get('reason')
        tq = str(vars.get('e_transfer_queue') or '')
        if tq:
            o = 'transferred'
            r = dict(sales='sales', general='human', security='security').get(tq, r)
        elif str(vars.get('e_applied') or '') == 'yes':
            o = 'applied'
        elif str(vars.get('e_not_eligible') or '') == 'yes':
            o = 'not_eligible'
        elif o == 'not_verified' and str(vars.get('e_informed') or '') == 'yes':
            o = 'informed'
        elif o == 'transferred':
            o = 'informed' if str(vars.get('e_informed') or '') == 'yes' else 'no_action'
            r = 'out_of_scope'
        elif o in ('applied', 'not_eligible'):
            o = 'informed'
        if o == 'not_verified':
            wl = str(vars.get('verify_identity_response.data.wrong_answers_left') or '')
            r = 'failed' if wl == '0' else (r if r in ('failed', 'declined') else 'declined')
        if o == 'no_action' and r not in ('out_of_scope', 'service_error'):
            r = 'service_error' if int(vars.get('e_app_fail') or 0) >= 2 else 'out_of_scope'
        b['outcome'] = o
        if o in ('informed', 'applied', 'not_eligible'):
            b.pop('reason', None)
        else:
            b['reason'] = r
except Exception:
    pass
'''

POST_CLOSE = HDR + r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
    d = _data(result)
    vars['e_closed'] = 'yes'
except Exception:
    pass
'''

# ------------------------------------------------------------------ tool builders
def api_tool(name, path, desc, fields=None, required=None, post="", pre="", baked=None, timeout=12000):
    props = {"customer_id": {"type": "string", "default": "{{customer_id}}"}}
    for k, spec in (fields or {}).items():
        spec = dict(spec); var = spec.pop("var", k)
        props[k] = {**spec, "default": "{{%s}}" % var}
    for k, v in (baked or {}).items():
        props[k] = {"type": "string", "default": v}
    t = {"type": "function", "config": {"timeoutMs": timeout, "maxRetries": 0},
         "function": {"name": name, "handler": "__function__:api_call", "description": desc,
                      "parameters": {"type": "object", "properties": {
                          "url": {"type": "string", "default": BASE + path},
                          "method": {"type": "string", "default": "POST"},
                          "headers": {"type": "object", "properties": {"Content-Type": {"type": "string", "default": "application/json"}}},
                          "body": {"type": "object", "properties": props, "required": required or []}}}}}
    if pre: t["pre_process_code"] = pre
    if post: t["post_process_code"] = post
    return t


def T_verify():
    return api_tool("verify_identity", "verify_identity",
                    "Check ONE security answer. CALL it every time the customer answers a security question, before you say anything about the answer.",
                    {"field": {"type": "string", "enum": ["date_of_birth", "phone_last4"], "description": "date_of_birth or phone_last4", "var": "id_field"},
                     "answer": {"type": "string", "description": "date_of_birth as YYYY-MM-DD (a date said only in numbers is day, then month, then year); phone_last4 as exactly four digits", "var": "id_answer"}},
                    ["field", "answer"], post=POST_VERIFY)

def T_list():
    return api_tool("list_campaigns", "list_campaigns",
                    "List Freya Bank's campaigns. CALL it when the customer does not know a campaign name, asks what campaigns exist for a product, or wants a product and you must check whether it has a campaign.",
                    post=POST_LIST)

def T_get():
    return api_tool("get_campaign", "get_campaign",
                    "Get one campaign's full details. CALL it before you say anything about a campaign's conditions, exclusions, fees, dates or how to apply.",
                    {"campaign_id": {"type": "string", "description": "campaign_id exactly as list_campaigns returned it", "var": "cmp_id"}},
                    ["campaign_id"], post=POST_GET)

def T_consent():
    return api_tool("get_consent", "get_consent",
                    "Read the customer's marketing consent. CALL it before you mention ANY campaign the customer did not ask about.",
                    post=POST_CONSENT)

def T_elig():
    return api_tool("check_eligibility", "check_eligibility",
                    "Check the customer's eligibility for one campaign. CALL it when the customer asks whether they can get a campaign, or wants to apply.",
                    {"campaign_id": {"type": "string", "description": "campaign_id exactly as list_campaigns returned it", "var": "elig_cmp_id"}},
                    ["campaign_id"], post=POST_ELIG)

def T_start():
    return api_tool("start_application", "start_application",
                    "Start the application for the campaign whose eligibility check just passed. CALL it only after you read back the campaign name and product, asked \"Shall I start the application?\" and the customer said a clear yes.",
                    {"campaign_id": {"type": "string", "description": "campaign_id of the campaign that passed check_eligibility", "var": "e_campaign"}},
                    ["campaign_id"], pre=PRE_START, post=POST_START)

def T_transfer(name, queue, desc):
    return api_tool(name, "transfer_to_agent", desc, baked={"queue": queue}, post=post_transfer(queue))

def T_sales():
    return T_transfer("transfer_to_sales", "sales", "Transfer the call to the sales team. CALL it only after the customer accepted a transfer to the sales team.")

def T_general():
    return T_transfer("transfer_to_general", "general", "Transfer the call to the general team (a person). CALL it when the customer accepted a transfer for a complaint, or insists on a person after you asked once whether you can help.")

def T_close():
    return api_tool("close_call", "close_call",
                    "End the call record. CALL it exactly once, as the very last tool call, right after your one-sentence summary, thanks and goodbye.",
                    {"outcome": {"type": "string", "enum": ["informed", "not_eligible", "applied", "transferred", "not_verified", "no_action"],
                                 "description": "informed: information given, nothing else. not_eligible: eligibility false (not not_checked). applied: application received. transferred: a transfer was done. not_verified: identity failed or declined and nothing else handled. no_action: nothing done (declined a transfer, or the application failed twice).", "var": "close_outcome"},
                     "reason": {"type": "string", "enum": ["sales", "human", "security", "failed", "declined", "out_of_scope", "service_error", ""],
                                "description": "transferred: sales, human or security. not_verified: failed (three wrong answers) or declined. no_action: out_of_scope or service_error. Empty for informed, not_eligible, applied.", "var": "close_reason"}},
                    ["outcome"], pre=PRE_CLOSE, post=POST_CLOSE)


def cond_eq(var, *vals):
    return {"logic": "or", "conditions": [{"variable": var, "operator": "equals", "operand": v} for v in vals]}

def cond_and(*cs):
    return {"logic": "or", "conditions": [{"logic": "and", "conditions": list(cs)}]}

def eq(var, val): return {"variable": var, "operator": "equals", "operand": val}

CLOSED = {"target_node": "end", "description": "close_call was recorded", "condition": {"logic": "or", "conditions": [eq("e_closed", "yes"), eq("close_call_response.data.ok", "true"), eq("close_call_response.data.ok", "True")]}}

def conv(name, task, tools, transitions, on_enter=None, first_only=False):
    n = {"name": name, "node_type": "conversation", "task_message": task, "tools": tools,
         "transitions": [CLOSED] + transitions, "max_node_turns": 60}
    if on_enter: n["on_enter"] = on_enter
    if first_only: n["on_enter_first_entry_only"] = True
    return n

def code_node(name, code, target):
    return {"name": name, "node_type": "code", "passthrough": True, "passthrough_default_transition": target,
            "on_enter": {"type": "silent"}, "disable_inactivity_monitor": True,
            "pre_actions": [{"type": "function", "function": {"name": "code_exec", "handler": "__function__:code_exec",
                             "parameters": {"type": "object", "properties": {"code": {"type": "string", "default": code}, "timeout_ms": {"type": "number", "default": 10000}}}}}],
            "transitions": [{"target_node": target, "description": "always", "condition": {"operator": "always"}}]}


# ------------------------------------------------------------------ prompts
SYSTEM = f"""You are the digital assistant of Freya Bank answering the phone. Customers call about Freya Bank's products and campaigns. Speak English, one to three short sentences per turn, one question at a time. Correct information is the goal, not a sale.
Today is {{{{now}}}} (the call variable `now`). Judge campaign dates only against it, never against the real clock.

Hard rules in every step:
- Every fact about a campaign comes from a tool result in this call (list_campaigns, get_campaign). Never mention a rate, fee, bonus, limit or date the tool did not return. Never add, round, shorten or soften a condition. When the conditions are asked for, read every item of `conditions` and every item of `exclusions`.
- If a campaign's summary and its conditions disagree, the conditions govern; say that the detailed conditions are what counts.
- A personal question about rates, fees or limits ("what rate would I get", "how much would I pay"): say personal terms are set when an application is decided; quote the `fees` text only as the general terms.
- If the customer misunderstands a condition, correct it once with the tool's words; if they insist, do not argue.
- Several questions: answer them one at a time, in the order asked.
- Never propose or mention a campaign the customer did not ask about, unless get_consent returned marketing true in this call; then at most one other active campaign for the same product, once, after their own question is answered. If the customer asks why you suggest nothing, or wants to change their marketing preference: it can be changed in the mobile app or at a branch; you cannot change it.
- Never say "you qualify", "you are approved" or guarantee approval. Never state an eligibility the check did not return.
- A complaint about a campaign (a bonus not received, a condition applied differently): do not argue, promise nothing, offer a transfer to the general team. Accepted: call transfer_to_general. Declined: close as no_action, out_of_scope.
- A request for a person: ask once whether you can help first. If they insist, call transfer_to_general.
- A product with no campaign in list_campaigns that the customer wants: say applications for it are handled by the sales team and offer the transfer. Accepted: call transfer_to_sales. Declined: close as no_action, out_of_scope.
- A question the tools cannot answer: say you do not have that information.
- Never claim something was done (received, transferred, checked) without the tool result saying so. If a tool fails, say so.
- After every tool result, speak to the customer or call the next tool; never end a turn with nothing. Follow the `what_to_do_next` field of a tool result.
- Ending: when the customer has nothing else, say in one sentence what was done and what they can expect, thank them and say goodbye, then call close_call (exactly once, the last tool call)."""

INFO_PRE = """The caller is NOT verified. Use no name. Give general product and campaign information without any security questions.
Find out which product or campaign the customer means and name it back. If they do not know a name, call list_campaigns and read the names of the active campaigns for the product they mention, at most three; if more than three are active, first ask which product feature they care about. Call get_campaign before giving any campaign fact.
Propose nothing the customer did not ask about.
If the customer wants to know whether THEY are eligible, wants to apply, or asks about their own marketing preference status, call start_security_check: it asks the security questions. Do not ask them yourself and do not call it for general information.
A lost or stolen card, an unrecognised transaction or a code given to someone is handled automatically; ask no details."""

IDENTITY = """Before eligibility, an application or consent can be handled, ask two security questions, one at a time: first the date of birth, then the last four digits of the phone number on file. Call verify_identity after EACH answer: date_of_birth as YYYY-MM-DD however it was said (a date given only in numbers is day, then month, then year); phone_last4 as four digits. Never reveal or hint at the right answer. Use no name yet.
If the customer asks why: explain once that the questions protect their account.
If they still refuse after that explanation, call skip_security_check (general information can still be given).
Do not give eligibility or application answers in this step."""

LIMITED = """Identity is NOT verified on this call (the check failed or the customer declined it). Eligibility checks, applications and consent cannot be handled on this call; say so if asked. Use no name.
General product and campaign information may still be given: call list_campaigns or get_campaign as needed. Propose nothing the customer did not ask about.
If the customer wants nothing else, say in one sentence what happened, thank them, say goodbye and call close_call: outcome informed if you gave campaign information, otherwise not_verified with reason failed (three wrong answers) or declined (refused the questions)."""

VERIFIED = """The customer is verified. Address them as {{title}} {{last_name}}.
Continue with what the customer asked. For eligibility or an application, call check_eligibility with the campaign_id (call list_campaigns first if you do not have it).
Before mentioning any campaign the customer did not ask about, call get_consent.
If check_eligibility says not_checked or fails, offer a transfer to the sales team; accepted: call transfer_to_sales.
An application can be started only after a passing eligibility check; never start one otherwise.
If the customer wants nothing else, summarise in one sentence, thank them, say goodbye and call close_call."""

ELIGIBLE = """The customer is verified ({{title}} {{last_name}}) and the eligibility check for campaign {{e_campaign}} PASSED. If you have not yet said it, say exactly: '""" + ELIGIBLE_LINE + """' Never say they qualify or are approved.
If the customer wants to apply: read back the campaign name and the product and ask exactly "Shall I start the application?". Call start_application only after a clear yes. If start_application fails, call it once more; if it fails again, say it could not be started and offer a transfer to the sales team (accepted: transfer_to_sales; declined: close as no_action, service_error).
If the customer asks about another campaign's eligibility, call check_eligibility for it. Before mentioning any campaign the customer did not ask about, call get_consent.
If the customer wants nothing else, summarise in one sentence, thank them, say goodbye and call close_call."""

APPLIED = """The application was received, application id {{e_app_id}}; you have read it back. Do not start another application.
Answer any further question with the tools. If the customer wants nothing else: say in one sentence that the application was received and the decision comes within five business days by SMS, thank them, say goodbye and call close_call with outcome applied."""

APP_FAILED = """The application could NOT be started (two attempts failed). Never say it was received. Say it could not be started and offer a transfer to the sales team. Accepted: call transfer_to_sales. Declined: say in one sentence what happened, thank them, say goodbye and call close_call with outcome no_action, reason service_error."""

SEC_CODE = "vars['e_security'] = 'yes'\n"
MARK_ELIG = r'''
try:
    vars['e_elig_new'] = 'no'
    c = vars.get('check_eligibility_args.campaign_id') or vars.get('elig_cmp_id')
    if c:
        vars['e_campaign'] = str(c)
except Exception:
    pass
'''
RESET_ELIG = "vars['e_elig_new'] = 'no'\n"

ELIG_TRUE = cond_and(eq("e_elig_new", "yes"), eq("e_elig_state", "eligible"))
ELIG_OTHER = cond_and(eq("e_elig_new", "yes"), {"variable": "e_elig_state", "operator": "not_equals", "operand": "eligible"})
INFO_TOOLS = lambda: [T_list(), T_get(), T_sales(), T_general(), T_close()]
VER_TOOLS = lambda: [T_list(), T_get(), T_consent(), T_elig(), T_sales(), T_general(), T_close()]

def tool_transition(target, desc):
    return {"target_node": target, "description": desc, "is_tool_call": True,
            "condition": {"operator": "matches_intent", "description": desc}}

nodes = {
    "info": conv("info", INFO_PRE, INFO_TOOLS(), [
        tool_transition("identity", "start_security_check: the customer asks about their OWN eligibility, wants to apply, or asks about their own marketing consent"),
    ], on_enter={"type": "tts", "text": OPENING}, first_only=True),
    "identity": conv("identity", IDENTITY, [T_verify(), T_sales(), T_general(), T_close()], [
        {"target_node": "verified", "description": "identity verified", "condition": cond_eq("verify_identity_response.data.all_verified", "true", "True")},
        {"target_node": "limited", "description": "three wrong answers", "condition": cond_eq("verify_identity_response.data.wrong_answers_left", "0")},
        tool_transition("limited", "skip_security_check: the customer refused the security questions again after one explanation"),
    ], on_enter={"type": "llm", "prompt": "Say briefly that for this you first need two security questions, then ask for the date of birth. Use no name."}, first_only=True),
    "limited": conv("limited", LIMITED, INFO_TOOLS(), [],
                    on_enter={"type": "llm", "prompt": "If the security check failed with three wrong answers, say that eligibility and applications cannot continue on this call but general information can still be given. If the customer declined, say you can give general information only. Then ask if there is anything else."}, first_only=True),
    "verified": conv("verified", VERIFIED, VER_TOOLS(), [
        {"target_node": "mark_eligible", "description": "eligibility passed", "condition": ELIG_TRUE},
    ], on_enter={"type": "llm", "prompt": "Thank the customer by title and last name, say the identity is confirmed, then continue with their request: for eligibility or an application call check_eligibility now with the campaign_id (list_campaigns first if needed)."}, first_only=True),
    "mark_eligible": code_node("mark_eligible", MARK_ELIG, "eligible"),
    "eligible": conv("eligible", ELIGIBLE, VER_TOOLS()[:-3] + [T_start(), T_sales(), T_general(), T_close()], [
        {"target_node": "applied", "description": "application received", "condition": cond_eq("e_applied", "yes")},
        {"target_node": "app_failed", "description": "application failed twice", "condition": {"logic": "or", "conditions": [{"variable": "e_app_fail", "operator": "greater_than", "operand": 1}]}},
        {"target_node": "mark_eligible", "description": "another eligibility passed", "condition": ELIG_TRUE},
        {"target_node": "reset_elig", "description": "another eligibility did not pass", "condition": ELIG_OTHER},
    ], on_enter={"type": "llm", "prompt": "Say exactly: \"" + ELIGIBLE_LINE + "\" Then, if the customer already asked to apply, read back the campaign name and product and ask \"Shall I start the application?\"; otherwise ask whether they would like to apply or need anything else."}),
    "reset_elig": code_node("reset_elig", RESET_ELIG, "verified"),
    "applied": conv("applied", APPLIED, [T_list(), T_get(), T_consent(), T_sales(), T_general(), T_close()], [],
                    on_enter={"type": "tts", "text": "Your application is received. Your application number is {{e_app_spoken}}. " + RECEIVED + " Is there anything else I can help you with?"}, first_only=True),
    "app_failed": conv("app_failed", APP_FAILED, [T_sales(), T_close()], [],
                       on_enter={"type": "tts", "text": "I am sorry, the application could not be started. I can transfer you to our sales team, who can help with it. Would you like that?"}, first_only=True),
    "xfer_security": {"name": "xfer_security", "node_type": "api_request", "passthrough": True, "passthrough_default_transition": "end",
                      "on_enter": {"type": "tts", "text": "I am transferring you to our security team now. Thank you for calling Freya Bank, goodbye."},
                      "disable_inactivity_monitor": True,
                      "pre_actions": [
                          {**api_tool("transfer_security", "transfer_to_agent", "Transfer to security.", baked={"queue": "security"}), "config": {"timeoutMs": 12000, "maxRetries": 1}},
                          api_tool("close_security", "close_call", "Close.", baked={"outcome": "transferred", "reason": "security"}),
                      ],
                      "transitions": [{"target_node": "end", "description": "always", "condition": {"operator": "always"}}]},
    "end": {"name": "end", "node_type": "end_call", "on_enter": {"type": "silent"}, "disable_inactivity_monitor": True, "transitions": [],
            "terminal": {"type": "function", "function": {"name": "call_closed", "handler": "__function__:end_call",
                         "parameters": {"type": "object", "properties": {"message_mode": {"type": "string", "default": "none"}}}}}},
}
for n in nodes["xfer_security"]["pre_actions"]:
    n.pop("pre_process_code", None); n.pop("post_process_code", None)

workflow = {
    "initial_node": "info",
    "system_prompt": SYSTEM,
    "nodes": nodes,
    "global_nodes": {
        "security": {
            "name": "security", "description": "A security matter: lost or stolen card, unrecognised transaction, a code given to someone",
            "condition": {"operator": "matches_intent", "description": "The customer reports a lost or stolen card, a transaction they do not recognise, or that they gave a code or password to someone"},
            "task_message": "Ask no details. No tool call in this turn.",
            "on_enter": {"type": "silent"}, "passthrough": True, "passthrough_default_transition": "xfer_security",
            "excluded_nodes": ["end", "xfer_security"],
            "transitions": [{"target_node": "xfer_security", "description": "always", "condition": {"operator": "always"}}],
        }
    },
    "test_variables": {"customer_id": "c_test", "first_name": "Daniel", "last_name": "Reyes", "title": "Mr", "now": "2026-10-14T11:00"},
}

out = pathlib.Path(__file__).with_name("brief-e.workflow.json")
out.write_text(json.dumps(workflow, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "base", BASE)
