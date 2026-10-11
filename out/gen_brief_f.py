"""Generate out/brief-f.workflow.json for Brief F (application and request intake)."""
import json, pathlib, sys

BASE = "https://freya-bank-mock.freyavoice.workers.dev/v1/"
TYPES = ["card_replacement", "address_change", "limit_increase"]

# ---------------------------------------------------------------- shared python (no braces pairs allowed)
HELPERS = r'''
import datetime, json, re
PHRASE = dict(card_replacement='card replacement', address_change='address change', limit_increase='credit card limit increase')
WORDS = dict(received='received and waiting', in_review='being reviewed', more_info_needed='waiting for information from you', approved='approved', rejected='not approved')
def to_list(v):
    if isinstance(v, str):
        s = v.strip()
        if s == '__none__' or s == '':
            return None
        try:
            v = json.loads(s)
        except Exception:
            try:
                v = json.loads(s.replace("'", '"').replace('True', 'true').replace('False', 'false').replace('None', 'null'))
            except Exception:
                return None
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, dict)]
    return None
def flat_list(prefix_re):
    found = dict()
    for k in list(vars.keys()):
        m = re.search(prefix_re + r'\.(\d+)\.(\w+)$', str(k))
        if m:
            i = int(m.group(1))
            if i not in found:
                found[i] = dict()
            found[i][m.group(2)] = vars.get(k)
    if not found:
        return None
    return [found[i] for i in sorted(found.keys())]
def spoken(s):
    s = str(s or '')
    return ' '.join(ch for ch in s if ch.strip())
def today_iso():
    return str(vars.get('now') or '')[:10]
'''

SETUP_CODE = HELPERS + r'''
try:
    vars['today_iso'] = today_iso()
    for k in ('created_any', 'status_any', 'noaction_reason', 'pending_type', 'cur_type', 'create_state', 'new_app_id', 'final_route'):
        vars[k] = ''
    vars['created_any'] = 'no'
    vars['status_any'] = 'no'
    vars['app_count'] = 0
except Exception as e:
    vars['setup_error'] = str(e)
'''

# after identity passes: decide what to do with the request
AFTER_VERIFY_CODE = HELPERS + r'''
try:
    rk = str(vars.get('request_kind') or '')
    sk = str(vars.get('second_kind') or '')
    if rk in PHRASE:
        vars['cur_type'] = rk
        vars['pending_type'] = sk if (sk in PHRASE and sk != rk) else ''
        vars['route_state'] = 'apply'
    elif rk == 'status_enquiry':
        vars['route_state'] = 'status'
    else:
        vars['route_state'] = 'unclear'
except Exception as e:
    vars['route_state'] = 'unclear'
    vars['route_error'] = str(e)
'''

# before each application: reset per-application state
PREP_APP_CODE = HELPERS + r'''
try:
    t = str(vars.get('cur_type') or '')
    vars['cur_type_phrase'] = PHRASE.get(t, t)
    n = int(float(vars.get('app_count') or 0)) + 1
    vars['app_count'] = n
    vars['existing_apps'] = '__none__'
    vars['recheck_apps'] = '__none__'
    vars['req_fields'] = '__none__'
    vars['create_state'] = 'pending'
    vars['new_app_id'] = ''
    vars['create_tries'] = 0
    who = (str(vars.get('title') or '') + ' ' + str(vars.get('last_name') or '')).strip()
    if n == 1:
        vars['check_line'] = 'Thank you, ' + who + ', you are verified. One moment while I check for an existing ' + vars['cur_type_phrase'] + ' application.'
    else:
        vars['check_line'] = 'Now your next request, the ' + vars['cur_type_phrase'] + '. One moment while I check for an existing application of this type.'
except Exception as e:
    vars['check_line'] = 'One moment while I check your existing applications.'
    vars['prep_error'] = str(e)
'''

EXISTING_EVAL_CODE = HELPERS + r'''
try:
    t = str(vars.get('cur_type') or '')
    apps = to_list(vars.get('existing_apps'))
    if apps is None:
        apps = flat_list(r'find_existing_response\.data\.applications') or flat_list(r'find_applications_response\.data\.applications')
    okv = str(vars.get('find_existing_response.data.ok') or vars.get('find_applications_response.data.ok') or '')
    if apps is None and okv.lower() != 'true':
        vars['existing_state'] = 'error'
    else:
        apps = apps or []
        block = None
        for a in apps:
            if str(a.get('type') or t) == t and str(a.get('status')) in ('more_info_needed', 'received', 'in_review'):
                if block is None or str(a.get('status')) == 'more_info_needed':
                    block = a
        if block is None:
            vars['existing_state'] = 'none'
        else:
            st = str(block.get('status'))
            vars['existing_id'] = str(block.get('application_id') or '')
            vars['existing_id_spoken'] = spoken(block.get('application_id'))
            vars['existing_status_words'] = WORDS.get(st, st)
            note = str(block.get('note') or '').strip()
            vars['existing_note'] = note if note else 'no further details were given'
            vars['existing_state'] = 'more_info' if st == 'more_info_needed' else 'blocking'
            vars['status_any'] = 'yes'
except Exception as e:
    vars['existing_state'] = 'error'
    vars['existing_error'] = str(e)
'''

REQ_EVAL_CODE = HELPERS + r'''
try:
    fl = to_list(vars.get('req_fields'))
    if fl is None:
        fl = flat_list(r'get_requirements_response\.data\.fields') or flat_list(r'load_requirements_response\.data\.fields')
    fl = [f for f in (fl or []) if f.get('name')]
    if not fl:
        vars['req_state'] = 'error'
        vars['req_text'] = 'unknown'
        vars['req_json'] = '[]'
    else:
        clean = []
        for f in fl:
            opts = f.get('options')
            if isinstance(opts, str):
                try:
                    opts = json.loads(opts.replace("'", '"'))
                except Exception:
                    opts = [o.strip() for o in opts.split(',') if o.strip()]
            if not isinstance(opts, list):
                opts = []
            req = f.get('required')
            req = (req is True) or (str(req).lower() == 'true')
            clean.append(dict(name=str(f.get('name')), question=str(f.get('question') or ''), format=str(f.get('format') or 'text'), options=[str(o) for o in opts], required=req))
        fmt_help = dict(text='free text, as the customer says it', digits='digits only', amount='a number above zero with at most two decimals, sent as a number', date='a date sent as YYYY-MM-DD; a date said only in numbers is day, then month, then year', postcode='exactly five digits', choice='one of the options, matched by meaning')
        lines = []
        reqd = [c for c in clean if c['required']]
        opt = [c for c in clean if not c['required']]
        lines.append('REQUIRED FIELDS, ask them in this order, one per turn, using the question text:')
        i = 0
        for c in reqd:
            i += 1
            s = str(i) + '. field name "' + c['name'] + '" | question: "' + c['question'] + '" | format: ' + c['format'] + ' (' + fmt_help.get(c['format'], c['format']) + ')'
            if c['options']:
                s += ' | options: ' + ', '.join(c['options'])
            lines.append(s)
        if opt:
            lines.append('OPTIONAL FIELDS (mention them once, together, after the required ones; take one only if the customer offers it):')
            for c in opt:
                s = '- field name "' + c['name'] + '" | question: "' + c['question'] + '" | format: ' + c['format'] + ' (' + fmt_help.get(c['format'], c['format']) + ')'
                if c['options']:
                    s += ' | options: ' + ', '.join(c['options'])
                lines.append(s)
        else:
            lines.append('There are no optional fields.')
        lines.append('Field names allowed in create_application.fields: ' + ', '.join(c['name'] for c in clean) + '. Nothing else.')
        vars['req_text'] = '\n'.join(lines)
        vars['req_json'] = json.dumps(clean)
        vars['req_state'] = 'ok'
except Exception as e:
    vars['req_state'] = 'error'
    vars['req_text'] = 'unknown'
    vars['req_json'] = '[]'
    vars['req_error'] = str(e)
'''

PRE_RECHECK_CODE = HELPERS + r'''
try:
    vars['recheck_apps'] = '__none__'
    vars['create_tries'] = int(float(vars.get('create_tries') or 0)) + 1
except Exception:
    pass
'''

RECHECK_EVAL_CODE = HELPERS + r'''
try:
    t = str(vars.get('cur_type') or '')
    today = today_iso()
    apps = to_list(vars.get('recheck_apps')) or []
    hit = None
    for a in apps:
        if str(a.get('type') or t) == t and str(a.get('created_on') or '')[:10] == today and a.get('application_id'):
            hit = a
    if hit is not None:
        vars['new_app_id'] = str(hit.get('application_id'))
        vars['recheck_state'] = 'found'
    else:
        vars['recheck_state'] = 'retry'
        vars['create_state'] = 'pending'
except Exception as e:
    vars['recheck_state'] = 'retry'
    vars['create_state'] = 'pending'
    vars['recheck_error'] = str(e)
'''

CREATED_CODE = HELPERS + r'''
try:
    vars['created_any'] = 'yes'
    vars['app_id_spoken'] = spoken(vars.get('new_app_id'))
except Exception:
    vars['app_id_spoken'] = spoken(vars.get('new_app_id'))
'''

MARK_SERVICE_ERROR_CODE = r'''
try:
    vars['noaction_reason'] = 'service_error'
except Exception:
    pass
'''

AFTER_APP_CODE = HELPERS + r'''
try:
    p = str(vars.get('pending_type') or '')
    if p in PHRASE and p != str(vars.get('cur_type') or ''):
        vars['cur_type'] = p
        vars['pending_type'] = ''
        vars['final_route'] = 'next'
    elif str(vars.get('created_any')) == 'yes':
        vars['final_route'] = 'created'
    elif str(vars.get('status_any')) == 'yes':
        vars['final_route'] = 'status'
    else:
        vars['final_route'] = 'service_error'
except Exception:
    vars['final_route'] = 'service_error'
'''

NOOP_CODE = "vars['announced'] = 'yes'\n"

for _c in (HELPERS, SETUP_CODE, AFTER_VERIFY_CODE, PREP_APP_CODE, EXISTING_EVAL_CODE, REQ_EVAL_CODE, PRE_RECHECK_CODE, RECHECK_EVAL_CODE, CREATED_CODE, AFTER_APP_CODE):
    assert "{{" not in _c and "}}" not in _c, "braces in code"

# ---------------------------------------------------------------- hooks
VERIFY_POST = r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        if not isinstance(d, dict):
            msg = 'The check service failed and nothing was counted. Say sorry, there was a technical problem, and ask the same question again.'
        else:
            left = d.get('wrong_answers_left')
            if d.get('all_verified') is True:
                msg = 'Both answers are verified. Say only: thank you.'
            elif d.get('hint') == 'day_month_swapped':
                msg = 'Day and month look swapped. This is NOT a wrong answer. Do not mention swapping. Just ask the customer to say the date of birth again with the month as a word. Then call verify_identity again.'
            elif d.get('ok') is False:
                msg = 'The answer could not be read and was NOT counted as wrong. Ask the same question again.'
            elif d.get('verified') is True:
                msg = 'Correct. Now ask the next security question: the last four digits of the phone number on file. Then call verify_identity with field phone_last4.'
            elif left is not None and str(left) == '0':
                msg = 'Third wrong answer. The check has failed.'
            else:
                msg = 'WRONG answer. Do not reveal the correct value. Say the answer does not match our records and ask the SAME question again.'
            d['what_to_do_next'] = msg
        if not isinstance(d, dict):
            result['what_to_do_next'] = msg
except Exception:
    pass
'''

CREATE_PRE = HELPERS.replace("vars.get('now')", "vars.get('now')") + r'''
def check(fmt, v, opts):
    s = str(v).strip()
    if fmt == 'digits':
        s2 = re.sub(r'[\s-]', '', s)
        if re.fullmatch(r'[0-9]+', s2):
            return True, s2, ''
        return False, None, 'digits only'
    if fmt == 'amount':
        s2 = s.replace(',', '').replace(' ', '')
        if re.fullmatch(r'[0-9]+(\.[0-9]{1,2})?', s2) and float(s2) > 0:
            x = float(s2)
            return True, (int(x) if x == int(x) else x), ''
        return False, None, 'a number above zero with at most two decimals'
    if fmt == 'date':
        try:
            d = datetime.date.fromisoformat(s[:10])
            if len(s) != 10:
                raise ValueError('len')
            return True, d.isoformat(), ''
        except Exception:
            return False, None, 'a real date as YYYY-MM-DD'
    if fmt == 'postcode':
        s2 = s.replace(' ', '')
        if re.fullmatch(r'[0-9]{5}', s2):
            return True, s2, ''
        return False, None, 'exactly five digits'
    if fmt == 'choice':
        for o in opts:
            if s.lower() == str(o).lower():
                return True, str(o), ''
        return False, None, 'one of: ' + ', '.join(opts)
    if s:
        return True, s, ''
    return False, None, 'an answer'
try:
    b = config.get('body')
    if isinstance(b, dict):
        b['type'] = str(vars.get('cur_type') or b.get('type') or '')
        reqs = json.loads(str(vars.get('req_json') or '[]'))
        f = b.get('fields')
        if isinstance(f, str):
            try:
                f = json.loads(f)
            except Exception:
                f = dict()
        if not isinstance(f, dict):
            f = dict()
        errors = []
        clean = dict()
        if not reqs:
            errors.append('the requirements are not known')
        for r in reqs:
            n = r.get('name')
            v = f.get(n)
            if v is None or str(v).strip() == '':
                if r.get('required'):
                    errors.append('field ' + n + ' is missing')
                continue
            ok, nv, why = check(r.get('format'), v, r.get('options') or [])
            if ok:
                clean[n] = nv
            else:
                errors.append('field ' + n + ' must be ' + why + ' (got ' + str(v) + ')')
        if errors:
            vars['create_check'] = 'invalid: ' + '; '.join(errors)
            config['url'] = config.get('url', '').replace('create_application', 'get_requirements')
            config['body'] = dict(customer_id=b.get('customer_id'), type=b.get('type'))
        else:
            vars['create_check'] = 'ok'
            b['fields'] = clean
except Exception as e:
    try:
        vars['create_check'] = 'invalid: internal check error'
        config['url'] = config.get('url', '').replace('create_application', 'get_requirements')
        bb = config.get('body') if isinstance(config.get('body'), dict) else dict()
        config['body'] = dict(customer_id=bb.get('customer_id'), type=bb.get('type'))
    except Exception:
        pass
'''

CREATE_POST = r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        if isinstance(d, dict) and d.get('application_id') and d.get('ok') is not False:
            d['create_state'] = 'ok'
            d['what_to_do_next'] = 'Submitted. Do not say anything more; the system now tells the customer.'
        elif isinstance(d, dict) and ('fields' in d) and not d.get('application_id'):
            why = ''
            try:
                why = str(vars.get('create_check') or '').replace('invalid: ', '') + '.'
            except Exception:
                why = ''
            result['data'] = dict(ok=False, create_state='invalid', what_to_do_next='NOT SUBMITTED: nothing was sent to the bank. ' + (why or 'A field is missing or does not fit its format.') + ' Tell the customer what is expected for that field and ask it again. Then read every field back again and ask "Shall I submit this application?". Never say the application is received.')
        else:
            if isinstance(d, dict):
                d['create_state'] = 'failed'
                d['what_to_do_next'] = 'NOT CONFIRMED. Never say the application is received. Say only: one moment, I am checking.'
            else:
                result['data'] = dict(ok=False, create_state='failed', what_to_do_next='NOT CONFIRMED. Never say the application is received. Say only: one moment, I am checking.')
except Exception:
    pass
'''

GET_APP_POST = r'''
try:
    W = dict(received='received and waiting', in_review='being reviewed', more_info_needed='waiting for information from you', approved='approved', rejected='not approved')
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        if isinstance(d, dict) and d.get('ok') is not False and d.get('status'):
            st = str(d.get('status'))
            s = 'Tell the customer: the application is ' + W.get(st, st) + '.'
            if st == 'more_info_needed':
                s += ' Then read the note: ' + str(d.get('note') or '') + '.'
            s += ' Give no reason that the note does not contain and no date beyond "within five business days of the application".'
            d['status_in_words'] = W.get(st, st)
            d['what_to_do_next'] = s
        else:
            msg = 'NOT FOUND. Say no application with that id was found. Never confirm that id. Offer to look by type: ask which type of application it was (card replacement, address change or limit increase), then call find_applications with that type.'
            if isinstance(d, dict):
                d['what_to_do_next'] = msg
            else:
                result['data'] = dict(ok=False, what_to_do_next=msg)
except Exception:
    pass
'''

FIND_POST = r'''
try:
    W = dict(received='received and waiting', in_review='being reviewed', more_info_needed='waiting for information from you', approved='approved', rejected='not approved')
    if isinstance(result, dict):
        result.pop('header', None)
        d = result.get('data')
        if isinstance(d, dict) and isinstance(d.get('applications'), list):
            apps = [a for a in d.get('applications') if isinstance(a, dict)]
            if not apps:
                d['what_to_do_next'] = 'No application of that type was found. Say so.'
            else:
                parts = []
                for a in apps:
                    st = str(a.get('status'))
                    p = 'application ' + ' '.join(ch for ch in str(a.get('application_id')) if ch.strip()) + ' is ' + W.get(st, st)
                    if st == 'more_info_needed' and a.get('note'):
                        p += ': ' + str(a.get('note'))
                    parts.append(p)
                d['what_to_do_next'] = 'Read these to the customer, digit by digit for the ids: ' + '; '.join(parts) + '. Give no reason beyond the note and no date beyond "within five business days of the application".'
        else:
            msg = 'The lookup failed. Say you cannot check that right now.'
            if isinstance(d, dict):
                d['what_to_do_next'] = msg
            else:
                result['data'] = dict(ok=False, what_to_do_next=msg)
except Exception:
    pass
'''

SIMPLE_POST = r'''
try:
    if isinstance(result, dict):
        result.pop('header', None)
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
    if isinstance(b, dict):
        o = b.get('outcome')
        if o != 'transferred':
            if str(vars.get('created_any')) == 'yes':
                b['outcome'] = 'application_created'
            elif str(vars.get('status_any')) == 'yes' and o in ('not_verified', 'no_action'):
                b['outcome'] = 'status_given'
        if b.get('outcome') in ('application_created', 'status_given'):
            b.pop('reason', None)
except Exception:
    pass
'''

HEADERS = {"type": "object", "properties": {"Content-Type": {"type": "string", "default": "application/json"}}}


def api_tool(name, desc, body_props, required, retries=0, post=None, pre=None, mapping=None):
    props = {"customer_id": {"type": "string", "default": "{{customer_id}}"}}
    props.update(body_props)
    t = {"type": "function", "config": {"timeoutMs": 12000, "maxRetries": retries},
         "function": {"name": name, "handler": "__function__:api_call", "description": desc,
                      "parameters": {"type": "object", "properties": {
                          "url": {"type": "string", "default": BASE + name},
                          "method": {"type": "string", "default": "POST"},
                          "headers": HEADERS,
                          "body": {"type": "object", "properties": props, "required": required}}}}}
    if post: t["post_process_code"] = post
    if pre: t["pre_process_code"] = pre
    if mapping: t["response_mapping"] = mapping
    return t


def close_tool(outcomes, reasons, desc_extra):
    return api_tool("close_call",
        "Ends the call record. CALL it exactly once, as the very last action, in the SAME message in which you say in one sentence what was done, thank the customer and say goodbye. " + desc_extra,
        {"outcome": {"type": "string", "enum": outcomes, "default": "{{close_outcome}}", "description": "One of: " + ", ".join(outcomes) + "."},
         "reason": {"type": "string", "enum": reasons, "default": "{{close_reason}}", "description": "One of: " + ", ".join(reasons) + "."}},
        ["outcome"], pre=CLOSE_PRE, post=SIMPLE_POST)


def transfer_tool(queues, desc):
    return api_tool("transfer_to_agent", desc,
        {"queue": {"type": "string", "enum": queues, "default": "{{transfer_queue_choice}}", "description": "One of: " + ", ".join(queues) + "."}},
        ["queue"], pre=TRANSFER_PRE, post=SIMPLE_POST)


def code_node(name, code, transitions, default, on_enter=None):
    return {"name": name, "node_type": "code", "passthrough": True, "passthrough_default_transition": default,
            "on_enter": on_enter or {"type": "silent"}, "disable_inactivity_monitor": True,
            "pre_actions": [{"type": "function", "function": {"name": "code_exec", "handler": "__function__:code_exec",
                "parameters": {"type": "object", "properties": {"code": {"type": "string", "default": code},
                                                                 "timeout_ms": {"type": "number", "default": 10000}}}}}],
            "transitions": transitions + [always(default)]}


def api_node(name, fn, body, mapping, transitions, default, on_enter=None, retries=2):
    props = {"customer_id": {"type": "string", "default": "{{customer_id}}"}}
    props.update(body)
    return {"name": name, "node_type": "api_request", "passthrough": True, "passthrough_default_transition": default,
            "on_enter": on_enter or {"type": "silent"}, "disable_inactivity_monitor": True,
            "pre_actions": [{"type": "function", "config": {"timeoutMs": 12000, "maxRetries": retries}, "function": {
                "name": fn, "handler": "__function__:api_call", "description": fn,
                "parameters": {"type": "object", "properties": {
                    "url": {"type": "string", "default": BASE + fn}, "method": {"type": "string", "default": "POST"},
                    "headers": HEADERS, "body": {"type": "object", "properties": props, "required": []}}}}}],
            "response_mapping": mapping, "suppress_tool_results": True,
            "transitions": transitions + [always(default)]}


def always(t):
    return {"target_node": t, "description": "always", "condition": {"operator": "always"}}


def var_or(desc, target, conds):
    return {"target_node": target, "description": desc, "condition": {"logic": "or", "conditions": conds}}


def eq(v, o):
    return {"variable": v, "operator": "equals", "operand": o}


def gt(v, n):
    return {"variable": v, "operator": "greater_than", "operand": n}


def is_true(v):
    return [eq(v, "true"), eq(v, "True")]


def close_node(name, outcome, reason, line):
    body = {"outcome": {"type": "string", "default": outcome}}
    if reason:
        body["reason"] = {"type": "string", "default": reason}
    on_enter = {"type": "tts", "text": line} if line else {"type": "silent"}
    return api_node(name, "close_call", body, [], [], "end_call", on_enter=on_enter, retries=1)


def xfer_node(name, queue, nxt, line):
    return api_node(name, "transfer_to_agent", {"queue": {"type": "string", "default": queue}}, [], [], nxt,
                    on_enter={"type": "tts", "text": line} if line else {"type": "silent"}, retries=1)


# ---------------------------------------------------------------- prompts
SYSTEM = """You are the digital assistant of Freya Bank, answering an inbound phone call. Speak English. Keep every turn to one or two short sentences. Ask one question at a time.
Your job: take applications (card replacement, address change, credit card limit increase) and answer status enquiries about applications. Receiving an application is not approving it. You decide nothing.
Rules that hold in every step:
- Before both security answers are verified, use no name and no title for the caller. After that, address them as {{title}} {{last_name}}.
- Never ask for a PIN, a password, a one-time code or a full card number. Never ask for anything the requirements do not list.
- If you cannot answer a question from a tool result, say you do not have that information. Never invent fees, dates, limits, decisions or reasons.
- Never say an application is received, submitted, approved or transferred, and never say an application id, unless a tool result in this call shows it.
- When a rule says to call a tool, call the tool; saying you did it is not enough. Call one tool per message.
- Tool results may contain what_to_do_next. Follow it. After every tool result, speak to the customer or call the next tool; never end a turn with nothing.
- A lost or stolen card, a transaction the customer does not recognise, or a code given to someone is a security matter: ask for no details.
- If the customer asks for a person: ask once whether you can help first. If they insist, call transfer_to_agent with queue general.
- Today is {{today_iso}}."""

INTAKE_TASK = """The opening was already spoken: "Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?"

STEP 1: WHAT THE CUSTOMER WANTS
Supported applications:
- card replacement: a new card to replace a DAMAGED or EXPIRED card. (A LOST or STOLEN card is NOT this: it is a security matter.)
- address change: a new postal address.
- limit increase: a higher limit on a credit card.
Also supported: a status enquiry about an application the customer already made.
- Work out which one it is and name it back in plain words, for example "a replacement for your damaged card" or "a question about the status of an application". Ask at most two clarifying questions.
- If the customer raises several applications, name them all back and say you will take them one at a time, in that order.
- Unsupported application (anything else they want to apply for, such as a new card, a loan, a mortgage, a new account): say "As a digital assistant, I cannot take that application on this call" and offer a transfer to the applications team. If they accept, call transfer_to_agent with queue applications. If they decline, say in one sentence that nothing was submitted, thank them, say goodbye and call close_call with outcome no_action, reason unsupported.
- Out of scope (not an application and not a status enquiry: a balance, a payment, a money transfer, a complaint, anything else): say "As a digital assistant, I cannot help with that on this call" and offer a transfer to the general team. If they accept, call transfer_to_agent with queue general. If they decline, say in one sentence that nothing was done, thank them, say goodbye and call close_call with outcome no_action, reason out_of_scope.
- Questions about fees, how long it takes, or whether it will be approved: say you do not have that information. Never guess.
- For a limit increase, never mention a current limit, a new limit or a likely decision.

STEP 2: SECURITY QUESTIONS (only after you named back a supported application or a status enquiry)
- In the same message in which you name the request back, say you first need to verify their identity and ask for their date of birth.
- Call verify_identity with field date_of_birth and answer as YYYY-MM-DD, whatever way it was said. A date given only in numbers is day, then month, then year (11 02 1979 = 1979-02-11). Words: "2 November 1979" = 1979-11-02.
- Then ask for the last four digits of the phone number on file. Call verify_identity with field phone_last4 and four digits.
- Call verify_identity once for every answer. Follow what_to_do_next exactly.
- If the customer will not answer a security question: explain once that these questions protect their account, and ask again. If they still refuse, say in one sentence that the application cannot be taken without the check, thank them, say goodbye and call close_call with outcome not_verified, reason declined.

Do not call any other tool here. Never ask for application details here."""

CLARIFY_TASK = """The customer is verified. Address them as {{title}} {{last_name}}.
It is not yet clear which request they want. Ask which one: a card replacement (damaged or expired card), an address change, a credit card limit increase, or the status of an application they already made. Ask at most two clarifying questions.
- If it is an unsupported application: say the digital assistant cannot take that application on this call and offer a transfer to the applications team. Accept: call transfer_to_agent with queue applications. Decline: say in one sentence that nothing was submitted, thank them, say goodbye and call close_call with outcome no_action, reason unsupported.
- If it is out of scope: say the digital assistant cannot do that and offer a transfer to the general team. Accept: call transfer_to_agent with queue general. Decline: say in one sentence that nothing was done, thank them, say goodbye and call close_call with outcome no_action, reason out_of_scope.
Call no other tool."""

COLLECT_TASK = """The customer is verified. Address them as {{title}} {{last_name}}. There is no open {{cur_type_phrase}} application, so a new one can be taken.

{{req_text}}

HOW TO COLLECT
- Ask the required fields in the order above, one per turn, using the question text.
- After the required fields, mention the optional fields once, together, and take one only if the customer offers it.
- Check every answer against its format before moving on. If it does not fit, say what is expected and ask the same question again. Count the answers that do not fit, per field. After the third answer that does not fit the same field, offer a transfer to the applications team: if they accept, call transfer_to_agent with queue applications; if they decline, say in one sentence that the application was not submitted, thank them, say goodbye and call close_call with outcome no_action, reason incomplete.
- Never fill a field yourself, never guess, and never reuse a value given for another field.
- Limit increase: the requested amount is exactly what the customer says. Never state the current limit, a new limit or the likely decision.
- Address change: never read an old address aloud. Read back only the new one.
- If the customer changes a value, replace it and read it back again.

SUBMITTING
- When all required fields are collected, read every collected field back and ask exactly: "Shall I submit this application?"
- Only after a clear yes, call create_application with fields: an object of field name to value, using only the field names listed above. Send dates as YYYY-MM-DD, amounts as numbers, digits and postcodes as digits only, and choices as the exact option text.
- If create_application returns what_to_do_next, follow it exactly.
- Never say the application is received or say any id yourself; the system announces it.
- Questions you cannot answer from the tools (fees, timing, approval): say you do not have that information."""

RETRY_TASK = """The first create_application call for this {{cur_type_phrase}} application did not go through, and a check showed no application was created today.
In ONE message: say there was a technical problem and that you are submitting it once more, and call create_application again with exactly the same fields as the last create_application call. Do not ask the customer anything first.
Never say the application is received or say any id yourself."""

MORE_INFO_TASK = """The customer is verified. Address them as {{title}} {{last_name}}.
You told the customer that they already have a {{cur_type_phrase}} application, number {{existing_id_spoken}}, which is waiting for information from them ({{existing_note}}), that the applications team is waiting for that information and that you cannot add it on this call, and you offered a transfer to the applications team.
- If they accept: call transfer_to_agent with queue applications.
- If they decline: say "All right." and nothing else; do not call close_call.
- Never take the missing information yourself and never create a new application."""

OFFER_TASK = """The customer is verified. Address them as {{title}} {{last_name}}.
You told the customer that the {{cur_type_phrase}} application could not be submitted or checked because of a technical problem, and offered a transfer to the applications team.
- If they accept: call transfer_to_agent with queue applications.
- If they decline: say "All right." and nothing else; do not call close_call.
Never say the application was received."""

STATUS_TASK = """The customer is verified. Address them as {{title}} {{last_name}}. They want the status of an application.
- Ask for the application id if you do not have it. Call get_application with the id exactly as the customer gives it (no spaces).
- Report the status only in these words: received = "received and waiting"; in_review = "being reviewed"; more_info_needed = "waiting for information from you", followed by the note; approved = "approved"; rejected = "not approved". Follow what_to_do_next.
- Give no reason that the note does not contain, and no date beyond "within five business days of the application".
- If the id is not found: say so and offer to look by type. If they name the type, call find_applications with it (card_replacement, address_change or limit_increase) and read the ids and statuses found.
- Never confirm an id you did not see in a tool result.
- When the customer has their answer and wants nothing more: say in one sentence what you told them, thank them, say goodbye and call close_call with outcome status_given.
- If they ask for something you cannot do here, say the digital assistant cannot do that and offer a transfer to the general team; accept: call transfer_to_agent with queue general."""

# ---------------------------------------------------------------- tools
verify_tool = api_tool("verify_identity",
    "Check one security answer. CALL it every time the customer gives a date of birth or phone digits.",
    {"field": {"type": "string", "enum": ["date_of_birth", "phone_last4"], "default": "{{verify_field}}", "description": "date_of_birth or phone_last4."},
     "answer": {"type": "string", "default": "{{verify_answer}}", "description": "date_of_birth as YYYY-MM-DD (numbers only = day, month, year). phone_last4 as four digits."}},
    ["field", "answer"], post=VERIFY_POST)

create_tool = api_tool("create_application",
    "Submit the application. CALL it only after you read every field back and the customer said a clear yes to \"Shall I submit this application?\".",
    {"type": {"type": "string", "default": "{{cur_type}}"},
     "fields": {"type": "object", "default": "{{app_fields}}", "description": "Object of field name to value, only the field names from the requirements. Dates YYYY-MM-DD, amounts as numbers."}},
    ["fields"], pre=CREATE_PRE, post=CREATE_POST,
    mapping=[{"path": "data.create_state", "variable": "create_state"}, {"path": "data.application_id", "variable": "new_app_id"}])

get_app_tool = api_tool("get_application",
    "Look up one application by its id. CALL it as soon as the customer gives an application id.",
    {"application_id": {"type": "string", "default": "{{asked_app_id}}", "description": "The id exactly as the customer gave it, without spaces."}},
    ["application_id"], post=GET_APP_POST)

find_tool = api_tool("find_applications",
    "List the customer's applications of one type. CALL it when an id was not found and the customer names the type.",
    {"type": {"type": "string", "enum": TYPES, "default": "{{lookup_type}}", "description": "One of: " + ", ".join(TYPES) + "."}},
    ["type"], post=FIND_POST)


def transfer_routes():
    return [
        var_or("transferred to security", "close_transfer_security", [eq("transfer_to_agent_args.queue", "security"), eq("transfer_queue", "security")]),
        var_or("transferred to applications", "close_transfer_applications", [eq("transfer_to_agent_args.queue", "applications"), eq("transfer_queue", "applications")]),
        var_or("transferred to general", "close_transfer_general", [eq("transfer_to_agent_args.queue", "general"), eq("transfer_queue", "general")]),
    ]


closed_route = var_or("close_call was called", "end_call", [gt("close_call_success_count", 0), gt("close_call_failure_count", 0)])

offer_extraction = [{"name": "offer_answer", "type": "string", "enum_values": ["accept", "decline"],
                     "description": "The customer's answer to the offered transfer to the applications team: accept or decline. Empty if they have not answered it.",
                     "min_confidence": 0.7}]

kind_desc = ("The FIRST request the caller raised: card_replacement = a new card for a damaged or expired card (NOT lost or stolen); "
             "address_change = a new postal address; limit_increase = a higher credit card limit; status_enquiry = asks about the status of an application already made; "
             "other = anything else (another application, a balance, a payment, a complaint, a lost or stolen card). Empty if not yet clear.")

nodes = {
    "setup": code_node("setup", SETUP_CODE, [], "intake"),
    "intake": {
        "name": "intake", "node_type": "conversation",
        "on_enter": {"type": "tts", "text": "Thank you for calling Freya Bank. You are speaking with a digital assistant and this call is recorded. How can I help you today?"},
        "on_enter_first_entry_only": True,
        "task_message": INTAKE_TASK,
        "tools": [verify_tool,
                  transfer_tool(["applications", "general"], "Hand the call to a person. applications: an unsupported application and the customer accepted. general: out of scope and the customer accepted, or the customer insists on a person."),
                  close_tool(["not_verified", "no_action"], ["declined", "unsupported", "out_of_scope"],
                             "not_verified with declined (refused the security questions). no_action with unsupported or out_of_scope (declined the transfer).")],
        "extraction_schema": [
            {"name": "request_kind", "type": "string", "enum_values": TYPES + ["status_enquiry", "other"], "description": kind_desc, "min_confidence": 0.6},
            {"name": "second_kind", "type": "string", "enum_values": TYPES,
             "description": "A SECOND, different supported application the caller also wants in this call (card_replacement, address_change, limit_increase). Empty if they raised only one.", "min_confidence": 0.7},
        ],
        "max_node_turns": 40,
        "transitions": [
            var_or("both answers verified", "after_verify", is_true("verify_identity_response.data.all_verified")),
            var_or("three wrong answers", "close_failed", [eq("verify_identity_response.data.wrong_answers_left", "0")]),
        ] + transfer_routes() + [closed_route],
    },
    "after_verify": code_node("after_verify", AFTER_VERIFY_CODE, [
        var_or("an application", "prep_app", [eq("route_state", "apply")]),
        var_or("a status enquiry", "status", [eq("route_state", "status")]),
    ], "clarify"),
    "clarify": {
        "name": "clarify", "node_type": "conversation",
        "on_enter": {"type": "llm"}, "on_enter_first_entry_only": True,
        "task_message": CLARIFY_TASK,
        "tools": [transfer_tool(["applications", "general"], "Hand the call to a person. applications: an unsupported application and the customer accepted. general: out of scope and accepted, or the customer insists on a person."),
                  close_tool(["no_action"], ["unsupported", "out_of_scope"], "no_action with unsupported or out_of_scope.")],
        "extraction_schema": [{"name": "request_kind", "type": "string", "enum_values": TYPES + ["status_enquiry", "other"], "description": kind_desc, "min_confidence": 0.6}],
        "max_node_turns": 20,
        "transitions": [
            var_or("request known", "after_verify", [eq("request_kind", t) for t in TYPES + ["status_enquiry"]]),
        ] + transfer_routes() + [closed_route],
    },
    "prep_app": code_node("prep_app", PREP_APP_CODE, [], "find_existing"),
    "find_existing": api_node("find_existing", "find_applications", {"type": {"type": "string", "default": "{{cur_type}}"}},
                              [{"path": "data.applications", "variable": "existing_apps"}], [], "existing_eval",
                              on_enter={"type": "tts", "text": "{{check_line}}"}),
    "existing_eval": code_node("existing_eval", EXISTING_EVAL_CODE, [
        var_or("no open application", "load_requirements", [eq("existing_state", "none")]),
        var_or("open application", "announce_existing", [eq("existing_state", "blocking")]),
        var_or("waiting for information", "more_info", [eq("existing_state", "more_info")]),
    ], "service_problem"),
    "announce_existing": code_node("announce_existing", NOOP_CODE, [], "after_app",
        on_enter={"type": "tts", "text": "You already have a {{cur_type_phrase}} application, number {{existing_id_spoken}}. It is {{existing_status_words}}, so I cannot create another one."}),
    "more_info": {
        "name": "more_info", "node_type": "conversation",
        "on_enter": {"type": "tts", "text": "You already have a {{cur_type_phrase}} application, number {{existing_id_spoken}}. It is waiting for information from you: {{existing_note}}. The applications team is waiting for that information, and I cannot add it on this call. Would you like me to transfer you to the applications team?"},
        "on_enter_first_entry_only": True,
        "task_message": MORE_INFO_TASK,
        "tools": [transfer_tool(["applications", "general"], "Hand the call to a person. applications: the customer accepted the offered transfer. general: the customer insists on a person.")],
        "extraction_schema": offer_extraction,
        "max_node_turns": 10, "max_turn_transition": "after_app",
        "transitions": transfer_routes() + [
            var_or("accepted", "xfer_applications", [eq("offer_answer", "accept")]),
            var_or("declined", "after_app", [eq("offer_answer", "decline")]),
        ],
    },
    "load_requirements": api_node("load_requirements", "get_requirements", {"type": {"type": "string", "default": "{{cur_type}}"}},
                                  [{"path": "data.fields", "variable": "req_fields"}], [], "req_eval"),
    "req_eval": code_node("req_eval", REQ_EVAL_CODE, [var_or("requirements known", "collect", [eq("req_state", "ok")])], "service_problem"),
    "collect": {
        "name": "collect", "node_type": "conversation",
        "on_enter": {"type": "llm", "prompt": "Say there is no open application of this type, so you can take a new one, and ask the first required question."},
        "task_message": COLLECT_TASK,
        "tools": [create_tool,
                  transfer_tool(["applications", "general"], "Hand the call to a person. applications: after three answers that do not fit the same field, the customer accepted. general: the customer insists on a person."),
                  close_tool(["no_action"], ["incomplete", "out_of_scope"], "no_action with incomplete (declined the transfer after three answers that did not fit).")],
        "max_node_turns": 60,
        "transitions": [
            var_or("submitted", "created", [eq("create_state", "ok")]),
            var_or("submit failed", "pre_recheck", [eq("create_state", "failed"),
                {"logic": "and", "conditions": [gt("create_application_failure_count", 0), eq("create_state", "pending")]}]),
        ] + transfer_routes() + [closed_route],
    },
    "pre_recheck": code_node("pre_recheck", PRE_RECHECK_CODE, [], "recheck"),
    "recheck": api_node("recheck", "find_applications", {"type": {"type": "string", "default": "{{cur_type}}"}},
                        [{"path": "data.applications", "variable": "recheck_apps"}], [], "recheck_eval", retries=1),
    "recheck_eval": code_node("recheck_eval", RECHECK_EVAL_CODE, [var_or("it went through", "created", [eq("recheck_state", "found")])], "retry_submit"),
    "retry_submit": {
        "name": "retry_submit", "node_type": "conversation",
        "on_enter": {"type": "llm"}, "on_enter_first_entry_only": True,
        "task_message": RETRY_TASK,
        "tools": [create_tool],
        "max_node_turns": 6, "max_turn_transition": "submit_failed",
        "transitions": [
            var_or("submitted", "created", [eq("create_state", "ok")]),
            var_or("failed again", "submit_failed", [eq("create_state", "failed"), eq("create_state", "invalid"), gt("create_application_failure_count", 1)]),
        ],
    },
    "submit_failed": {
        "name": "submit_failed", "node_type": "conversation",
        "on_enter": {"type": "tts", "text": "I am sorry, the {{cur_type_phrase}} application was not submitted because of a technical problem. Would you like me to transfer you to the applications team?"},
        "on_enter_first_entry_only": True,
        "task_message": OFFER_TASK,
        "tools": [transfer_tool(["applications", "general"], "Hand the call to a person. applications: the customer accepted the offered transfer. general: the customer insists on a person.")],
        "extraction_schema": offer_extraction,
        "max_node_turns": 10, "max_turn_transition": "mark_service_error",
        "transitions": transfer_routes() + [
            var_or("accepted", "xfer_applications", [eq("offer_answer", "accept")]),
            var_or("declined", "mark_service_error", [eq("offer_answer", "decline")]),
        ],
    },
    "service_problem": {
        "name": "service_problem", "node_type": "conversation",
        "on_enter": {"type": "tts", "text": "I am sorry, because of a technical problem I cannot take the {{cur_type_phrase}} application on this call. Would you like me to transfer you to the applications team?"},
        "on_enter_first_entry_only": True,
        "task_message": OFFER_TASK,
        "tools": [transfer_tool(["applications", "general"], "Hand the call to a person. applications: the customer accepted the offered transfer. general: the customer insists on a person.")],
        "extraction_schema": offer_extraction,
        "max_node_turns": 10, "max_turn_transition": "mark_service_error",
        "transitions": transfer_routes() + [
            var_or("accepted", "xfer_applications", [eq("offer_answer", "accept")]),
            var_or("declined", "mark_service_error", [eq("offer_answer", "decline")]),
        ],
    },
    "mark_service_error": code_node("mark_service_error", MARK_SERVICE_ERROR_CODE, [], "after_app"),
    "created": code_node("created", CREATED_CODE, [], "announce_created"),
    "announce_created": code_node("announce_created", NOOP_CODE, [], "after_app",
        on_enter={"type": "tts", "text": "Your {{cur_type_phrase}} application has been received. Your application id is {{app_id_spoken}}. This means we have received it, not that it is approved. You will be informed within five business days by SMS."}),
    "after_app": code_node("after_app", AFTER_APP_CODE, [
        var_or("next application", "prep_app", [eq("final_route", "next")]),
        var_or("created", "close_created", [eq("final_route", "created")]),
        var_or("status given", "close_status", [eq("final_route", "status")]),
    ], "close_service_error"),
    "status": {
        "name": "status", "node_type": "conversation",
        "on_enter": {"type": "llm", "prompt": "Thank the customer by title and last name for verifying, and ask for the application id if they have not given it yet; if they already gave it, call get_application with it."},
        "on_enter_first_entry_only": True,
        "task_message": STATUS_TASK,
        "tools": [get_app_tool, find_tool,
                  transfer_tool(["general"], "Hand the call to a person. general: out of scope and accepted, or the customer insists on a person."),
                  close_tool(["status_given"], ["none"], "status_given after the status was given.")],
        "max_node_turns": 30,
        "transitions": transfer_routes() + [closed_route],
    },
    "xfer_applications": xfer_node("xfer_applications", "applications", "close_xfer_applications", None),
    "close_xfer_applications": close_node("close_xfer_applications", "transferred", "applications",
        "I am transferring you now to our applications team, who will help you with your application. Thank you for calling Freya Bank, goodbye."),
    "close_transfer_applications": close_node("close_transfer_applications", "transferred", "applications",
        "I am transferring you now to our applications team, who will help you with your application. Thank you for calling Freya Bank, goodbye."),
    "close_transfer_general": close_node("close_transfer_general", "transferred", "human",
        "I am transferring you now to a colleague in our general team, who will help you with your request. Thank you for calling Freya Bank, goodbye."),
    "close_transfer_security": close_node("close_transfer_security", "transferred", "security",
        "I am transferring you to our security team now. Thank you for calling Freya Bank, goodbye."),
    "close_failed": close_node("close_failed", "not_verified", "failed",
        "I am sorry, I could not verify your identity, so the application cannot be taken on this call. You can call us back or visit a branch. Thank you for calling Freya Bank, goodbye."),
    "close_created": close_node("close_created", "application_created", None,
        "To sum up, your application has been received and you will be informed within five business days by SMS. Thank you for calling Freya Bank, goodbye."),
    "close_status": close_node("close_status", "status_given", None,
        "To sum up, I have given you the status of your existing application, so no new application was created. Thank you for calling Freya Bank, goodbye."),
    "close_service_error": close_node("close_service_error", "no_action", "service_error",
        "To sum up, the application was not submitted because of a technical problem; you can call us again later. Thank you for calling Freya Bank, goodbye."),
    "end_call": {
        "name": "end_call", "node_type": "end_call", "on_enter": {"type": "silent"},
        "disable_inactivity_monitor": True, "transitions": [],
        "terminal": {"type": "function", "function": {"name": "call_closed", "handler": "__function__:end_call",
                     "parameters": {"type": "object", "properties": {"message_mode": {"type": "string", "default": "none"}}}}},
    },
}

security_global = api_node("security_transfer", "transfer_to_agent", {"queue": {"type": "string", "default": "security"}}, [], [],
                           "close_security_silent",
                           on_enter={"type": "tts", "text": "That is a security matter, so I am transferring you to our security team right away. Thank you for calling Freya Bank, goodbye."},
                           retries=1)
security_global["description"] = "Transfers a security matter to the security team at once"
security_global["condition"] = {"operator": "matches_intent",
    "description": "The caller says a card is lost or stolen, reports a transaction they do not recognise, or says they gave a code to someone."}
security_global["excluded_nodes"] = [k for k in nodes if nodes[k]["node_type"] != "conversation"] + ["retry_submit"]
nodes["close_security_silent"] = close_node("close_security_silent", "transferred", "security", None)
security_global["excluded_nodes"].append("close_security_silent")

wf = {
    "initial_node": "setup",
    "system_prompt": SYSTEM,
    "nodes": nodes,
    "global_nodes": {"security_transfer": security_global},
    "test_variables": {"customer_id": "c_test", "first_name": "Daniel", "last_name": "Reyes", "title": "Mr", "now": "2026-10-14T11:00"},
}

# sanity: every target exists
keys = set(nodes) | {"__previous__"}
for k, n in list(nodes.items()) + [("security_transfer", security_global)]:
    for t in n.get("transitions", []):
        if t["target_node"] not in keys:
            sys.exit(f"bad target {t['target_node']} in {k}")
    if n.get("passthrough_default_transition") and n["passthrough_default_transition"] not in keys:
        sys.exit(f"bad default in {k}")
    if n.get("max_turn_transition") and n["max_turn_transition"] not in keys:
        sys.exit(f"bad max_turn_transition in {k}")

out = pathlib.Path(__file__).with_name("brief-f.workflow.json")
out.write_text(json.dumps(wf, indent=1))
print("wrote", out, len(nodes), "nodes")
