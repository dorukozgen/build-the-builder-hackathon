"""Benchmark a phone agent on the scenarios the builder wrote. Same simulation, judge and ledger scoring as run_cases.py.

    python3 tools/benchmark.py --fixtures
    python3 tools/benchmark.py --check --cases tests/<slot>.cases.json [--rules briefs/brief-a.md] [--rules tests/<slot>.facts.md]
    python3 tools/benchmark.py <agent_id> --cases tests/<slot>.cases.json [--rules FILE ...] [--public A|B] [--only ID,ID] [--reps N] [--style S]

A generated case borrows the bank data of one practice customer, its `fixture`: identity answers, products, `now` and the
injected fault. The script, the expected records and the checks are the case's own. Format: docs/test-case-template-comprehensive.md.
Results go to results/bench/<slot>/: history.jsonl, run-NN.json, run-NN.md (latest.md is a copy), run-NN/<case>.md and
run-NN.transcripts.md with every conversation, passed cases too.
Every run also plays the universal cases of universal-test-set.json: behaviour any bank agent owes whatever its brief (prompt injection,
a third party, pressure to skip identity, honesty about what was done...). They borrow fixtures too and are judged on the conversation,
close_call coming last and identity first, never on the brief's records. `--only` leaves them out unless it names them; `--skip-universal`
leaves them out of a full run in a fix round between two full runs that play them.
Every report scores the agent statistically over all results of the same saved version of the agent (section "Statistics on this
version"): pass rates with Wilson intervals, flakiness, categories, a fix order and a hidden-brief estimate. See docs/statistical-benchmark-guide.md.
"""
import argparse, collections, datetime, hashlib, json, math, pathlib, re, shutil, sys, time, urllib.error, urllib.request
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the console and the builder read UTF-8
import freya
import run_cases
from run_cases import STYLES

BANK_FIELDS = ("variables", "identity", "products", "faults", "persona", "language")   # come from the fixture, never from a generated case
REQUIRED = ("id", "fixture", "title", "family", "level", "rules", "script", "expected", "checks")
OPTIONAL = ("brief", "style", "third_party", "forbidden_tools", "backend")        # backend: state a self-hosted mock sets up for the case (existing records, faults)
LEVELS = ("easy", "medium", "hard")
EXPECTED_KEYS = ("outcome", "promises", "notes", "callbacks", "transfers")
RULE_LINE = re.compile(r"^\s*(\d+)\.\s")
TIME_RE = re.compile(r"^\d{2}:\d{2}$")
BUDGET_MIN = 30                                                      # a builder run, tests included
FINAL_RUNS, HIDDEN_CASES = 3, 60                                     # the final plays each unseen customer 3 times and counts it only when all 3 pass


PUBLIC_SET = ROOT / "public-test-set.json"                           # the practice customers of the kit's briefs


def load_fixtures(path=PUBLIC_SET):
    """The practice customers by id. Their bank data is the only bank data the mock can play."""
    return {c["id"]: c for c in json.load(open(path, encoding="utf-8"))}


def fixtures_path(cases_path=None):
    """A brief that brings its own test customers has them in tests/<slot>.fixtures.json; the others use the practice customers."""
    own = ROOT / "tests" / f"{slot_of(cases_path)}.fixtures.json" if cases_path else None
    return own if own and own.exists() else PUBLIC_SET


def own_fixtures(cases_path=None):
    return fixtures_path(cases_path) != PUBLIC_SET


def load_openapi(path=ROOT / "tools" / "openapi.json"):
    return json.load(open(path, encoding="utf-8"))


def tool_names(openapi):
    return [p.strip("/") for p in openapi["paths"]]


def enums(openapi):
    """Allowed values from the tool API: {tool: {field: [values]}}, fields that have an enum only."""
    out = {}
    for path, ops in openapi["paths"].items():
        props = ops["post"]["requestBody"]["content"]["application/json"]["schema"].get("properties", {})
        out[path.strip("/")] = {k: v["enum"] for k, v in props.items() if "enum" in v}
    return out


def reason_exempt_outcomes(openapi):
    """Outcomes that need no `reason`, read from close_call.reason's description ("... except promise and paid"). Empty when it says nothing."""
    try:
        props = openapi["paths"]["/close_call"]["post"]["requestBody"]["content"]["application/json"]["schema"]["properties"]
        text, outcomes = props.get("reason", {}).get("description", ""), props.get("outcome", {}).get("enum", [])
    except (KeyError, TypeError, AttributeError): return set()
    m = re.search(r"except\s+(.+?)(?:[.;]|$)", text, re.I)
    if not m: return set()
    named = {w.strip() for w in re.split(r",|\band\b", m.group(1))}
    return {o for o in outcomes if o in named}


def extract_rules(path):
    """Rule ids of a numbered file: a line that starts with `N.` is rule N; `briefs/brief-a.md` gives `brief-a:N`."""
    path = pathlib.Path(path); ids = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = RULE_LINE.match(line)
        if m and f"{path.stem}:{m.group(1)}" not in ids: ids.append(f"{path.stem}:{m.group(1)}")
    return ids


def product_ids(fixture):
    """`get_account` numbers the products p1, p2, ... in the order the fixture lists them."""
    return [f"p{i + 1}" for i in range(len(fixture.get("products", [])))]


def is_date(s):
    try: datetime.date.fromisoformat(s); return True
    except (TypeError, ValueError): return False


def check_cases(cases, fixtures, openapi, rule_ids=None, own=False):
    """Validate a cases file without running it. Returns (errors, warnings, coverage). Any error stops a run. With `own` fixtures (the
    brief's own test customers) `expected` may leave out the records: the judge scores the conversation and the tool calls."""
    errors, warnings = [], []
    en, tools, exempt = enums(openapi), tool_names(openapi), reason_exempt_outcomes(openapi)
    if not isinstance(cases, list): return ["the cases file must be a JSON list"], [], {}
    objs = [c for c in cases if isinstance(c, dict)]
    counts = collections.Counter(c.get("id") for c in objs)
    for c in cases:
        if not isinstance(c, dict): errors.append("every case must be a JSON object"); continue
        cid = c.get("id") or "(no id)"
        err = lambda m: errors.append(f"{cid}: {m}")
        for k in REQUIRED:
            if k not in c: err(f"missing field `{k}`")
        for k in c:
            if k in BANK_FIELDS: err(f"`{k}` is bank data and comes from the fixture; remove it")
            elif k not in REQUIRED + OPTIONAL: err(f"unknown field `{k}`")
        if counts[c.get("id")] > 1: err("duplicate id")
        if cid in fixtures: err("id collides with a public case")
        if str(cid).startswith("UNI-"): err("UNI- ids belong to the universal cases, which every run plays already; do not copy them, name yours GEN-…")
        fx = fixtures.get(c.get("fixture"))
        if fx is None: err(f"unknown fixture {c.get('fixture')!r}; see --fixtures")
        if c.get("level") not in LEVELS: err(f"level must be one of {', '.join(LEVELS)}")
        if not c.get("script"): err("empty script")
        if not c.get("checks") or not all(isinstance(x, str) and x.strip() for x in c["checks"]): err("checks must be a non-empty list of sentences")
        if not c.get("rules") or not all(isinstance(x, str) and ":" in x for x in c["rules"]): err('rules must be a non-empty list like ["brief-a:19"]')
        if c.get("style") is not None and c["style"] not in STYLES: err(f"unknown style {c['style']!r}; one of {', '.join(sorted(STYLES))}")
        for t in c.get("forbidden_tools") or []:
            if t not in tools: err(f"forbidden_tools names a tool the API does not have: {t}")
        exp = c.get("expected")
        if not isinstance(exp, dict): err("expected must be an object"); continue
        for k in EXPECTED_KEYS:
            if k not in exp and not own: err(f"expected.{k} missing")
        allowed = en.get("close_call", {}).get("outcome")
        if own and exp.get("outcome") is None: allowed = exempt = None          # no record expected: nothing to check against the tool API
        if allowed and exp.get("outcome") not in allowed: err(f"expected.outcome {exp.get('outcome')!r} is not in the tool API: {allowed}")
        if exempt and exp.get("outcome") not in exempt and not exp.get("reason"):
            warnings.append(f"{cid}: expected.reason is empty for outcome {exp.get('outcome')!r}; the tool API wants a reason for every outcome but {sorted(exempt)}")
        pids = product_ids(fx) if fx else []
        for p in exp.get("promises") or []:
            if fx and p.get("product_id") not in pids: err(f"promise product_id {p.get('product_id')!r} is not one of {pids} (fixture {c.get('fixture')})")
            if not isinstance(p.get("amount"), (int, float)) or isinstance(p.get("amount"), bool): err("promise amount must be a number")
            if not is_date(p.get("date")): err(f"promise date {p.get('date')!r} must be YYYY-MM-DD")
        reasons = en.get("add_note", {}).get("reason")
        for n in exp.get("notes") or []:
            if fx and n.get("product_id") not in pids: err(f"note product_id {n.get('product_id')!r} is not one of {pids}")
            if reasons and n.get("reason") not in reasons: err(f"note reason {n.get('reason')!r} is not in the tool API: {reasons}")
        for cb in exp.get("callbacks") or []:
            if not is_date(cb.get("date")): err(f"callback date {cb.get('date')!r} must be YYYY-MM-DD")
            if not TIME_RE.match(str(cb.get("time"))): err(f"callback time {cb.get('time')!r} must be HH:MM")
        queues = en.get("transfer_to_agent", {}).get("queue")
        for t in exp.get("transfers") or []:
            if queues and t.get("queue") not in queues: err(f"transfer queue {t.get('queue')!r} is not in the tool API: {queues}")
        types = en.get("create_application", {}).get("type")
        for ap in exp.get("applications") or []:
            if types and ap.get("type") not in types: err(f"application type {ap.get('type')!r} is not in the tool API: {types}")
        fields = en.get("verify_identity", {}).get("field")
        if fx and fields and not c.get("third_party"):                       # a third-party call never reaches verify_identity
            extra = sorted(set(fx["identity"]) - set(fields))
            if extra: err(f"the fixture's identity fields {extra} are not in the tool API's verify_identity.field {fields}: this scenario cannot be played on the mock with this tool API")
    cov = {"cases": len(cases),
           "by_family": dict(collections.Counter(c.get("family") for c in objs)),
           "by_fixture": dict(collections.Counter(c.get("fixture") for c in objs)),
           "by_outcome": dict(collections.Counter((c.get("expected") or {}).get("outcome") for c in objs if isinstance(c.get("expected"), dict))),
           "styles": sorted({c.get("style") for c in objs if c.get("style")})}
    cited = {r for c in objs for r in (c.get("rules") or []) if isinstance(r, str)}
    if rule_ids is not None:
        cov["uncovered_rules"] = [r for r in rule_ids if r not in cited]
        for r in sorted(cited - set(rule_ids)): errors.append(f"rule {r} is cited but exists in no --rules file")
    return errors, warnings, cov


def print_fixtures(fixtures):
    for c in fixtures.values():
        v = c["variables"]
        if c.get("persona") is not None:                                  # a brief's own test customer
            print(f"{c['id']}  variables {json.dumps(v, ensure_ascii=False)}" + (f"  language {c['language']}" if c.get("language") else ""))
            print("  persona: " + c["persona"][:300]); continue
        print(f"{c['id']}  brief {c['brief']}  {v['title']} {v['first_name']} {v['last_name']}  now {v['now']}  public case: \"{c['title']}\"")
        print("  identity: " + ", ".join(f"{k}={x}" for k, x in c["identity"].items()))
        for pid, p in zip(product_ids(c), c["products"]):
            print(f"  {pid} " + " ".join(f"{k}={x}" for k, x in p.items()))
        faults = c.get("faults") or []
        print("  faults: " + (", ".join(f"{f['tool']} fails on the first {f.get('fail_first_n')} call(s)" for f in faults) if faults else "none"))


def print_check(errors, warnings, cov):
    for e in errors: print("ERROR", e)
    for w in warnings: print("warning", w)
    if cov:
        print(f"{cov['cases']} cases · families {cov['by_family']} · fixtures {cov['by_fixture']} · outcomes {cov['by_outcome']} · styles {cov['styles'] or 'none'}")
        if "uncovered_rules" in cov:
            print(("rules cited by no case: " + ", ".join(cov["uncovered_rules"])) if cov["uncovered_rules"] else "every rule is cited by at least one case")
    print("check: " + ("FAILED" if errors else "ok"))


CATEGORIES = [("outcome ", "outcome"), ("promises ", "promises"), ("notes ", "notes"), ("callbacks ", "callbacks"), ("transfers ", "transfers"),
              ("not closed with close_call", "not_closed"), ("called before identity was verified", "before_identity"),
              ("although the customer was not on the line", "tools_while_unreached"), ("forbidden tool", "forbidden_tool"), ("conversation:", "conversation")]


def classify(reasons):
    """Failure categories of one case, from the scorer's and the judge's reasons."""
    cats = {cat for r in reasons for needle, cat in CATEGORIES if needle in r}
    return sorted(cats or ({"other"} if reasons else set()))


def signature(case):
    """Changes when the case's script, expectation, checks, fixture, forbidden tools or third-party flag change, so a weakened test shows up in the report."""
    keys = ("script", "expected", "checks", "fixture", "forbidden_tools", "third_party", "backend")
    return hashlib.sha1(json.dumps([case.get(k) for k in keys], sort_keys=True).encode()).hexdigest()[:10]


def merge_with_fixture(case, fixtures):
    """A generated case plus its fixture's bank data: what run_cases needs to play it."""
    fx = fixtures[case["fixture"]]
    out = {k: fx[k] for k in BANK_FIELDS if k in fx}
    out.update(case); out.setdefault("brief", fx["brief"])
    return out


# Universal cases: behaviour any bank phone agent owes whatever its brief (universal-test-set.json). Every run plays them on top of the
# cases file. They have no expected records, so they are scored on what holds for every brief: the judge's reading of the conversation,
# close_call coming last, no account tool before identity, no forbidden tool. The outcome and the records belong to the brief.
UNIVERSAL_KEEP = {"conversation", "not_closed", "before_identity", "forbidden_tool"}
NO_EXPECTATION = {"outcome": None, "reason": None, "promises": [], "notes": [], "callbacks": [], "transfers": []}   # a placeholder the scorer can read


def load_universal(fixtures, openapi, path=None):
    """The universal cases, merged with their fixtures. Returns (cases, skipped): a case whose fixture's identity fields this tool API
    cannot verify is skipped, as --check refuses such a generated case. No file, no universal cases."""
    path = pathlib.Path(path or ROOT / "universal-test-set.json")
    if not path.exists(): return [], []
    fields, cases, skipped = enums(openapi).get("verify_identity", {}).get("field"), [], []
    for c in json.load(open(path, encoding="utf-8")):
        if c["fixture"] not in fixtures: skipped.append(c["id"]); continue          # a brief's own customers: the practice ones are not there
        if fields and not c.get("third_party") and set(fixtures[c["fixture"]]["identity"]) - set(fields): skipped.append(c["id"]); continue
        cases.append({**merge_with_fixture(c, fixtures), "expected": dict(NO_EXPECTATION), "suite": "universal"})
    return cases, skipped


def universal_failures(failed):
    """The failures that count for a universal case: those in UNIVERSAL_KEEP. A mismatch with the placeholder records does not."""
    return [f for f in failed if set(classify([f])) & UNIVERSAL_KEEP]


def print_universal(fixtures, openapi):
    cases, skipped = load_universal(fixtures, openapi)
    if not cases and not skipped: return
    print(f"\nuniversal cases, played by every run on top of the cases file and judged on the conversation, not on the records ({len(cases)}"
          + (f"; this tool API cannot play {', '.join(skipped)}" if skipped else "") + "):")
    for c in cases:
        print(f"  {c['id']} {c['title']} · {c['family']} · fixture {c['fixture']}" + (f" · style {c['style']}" if c.get("style") else "") + (" · third party" if c.get("third_party") else ""))


PUBLIC_ORDER = ("id", "brief", "family", "level", "title", "variables", "identity", "products", "faults", "script", "expected", "checks")


def test_set_entry(case, fixtures):
    """A generated case as public-test-set.json would list it: the fixture's bank data merged in, the public keys first, the generated fields after."""
    m = merge_with_fixture(case, fixtures)
    return {**{k: m[k] for k in PUBLIC_ORDER if k in m}, **{k: v for k, v in m.items() if k not in PUBLIC_ORDER}}


def write_test_set(cases_path, gen, fixtures):
    """Writes `<slot>.test-set.json` next to the cases file: the generated set in the shape of public-test-set.json, which
    run_cases.py --cases can play as it is. Rewritten on every --check and every run, so an edited case flows into it."""
    out = pathlib.Path(cases_path).with_name(slot_of(cases_path) + ".test-set.json")
    out.write_text(json.dumps([test_set_entry(c, fixtures) for c in gen], indent=1, ensure_ascii=False), encoding="utf-8")
    return out


def applications_created(calls):
    """Types of the applications that create_application calls recorded, in call order: the successful ones, and the ones the mock
    marks `delayed`, which went through although the agent got a timeout."""
    return [str((c.get("args") or {}).get("type")) for c in calls if c.get("tool") == "create_application" and ((c.get("result") or {}).get("ok") or c.get("delayed"))]


def applications_failed(expected, calls):
    """The ledger check for `expected.applications`: the recorded application types must match it exactly. Nothing when the case names none."""
    if "applications" not in expected: return []
    got, want = sorted(applications_created(calls)), sorted(str(a.get("type")) for a in expected["applications"])
    return [] if got == want else [f"applications {got}, expected {want}"]


def promised(calls):
    """Amount recorded by successful create_promise calls: what the ledger holds for the tie-breaker."""
    return round(sum(float((c.get("args") or {}).get("amount") or 0) for c in calls if c.get("tool") == "create_promise" and (c.get("result") or {}).get("ok")), 2)


def transcript_md(case, row, call):
    """One case's conversation with the engine events between the lines. `call` is freya.get_call's result, or {}."""
    msgs = call.get("messages") or []
    turns = sum(m.get("role") in ("user", "assistant") for m in msgs)
    L = [f"## {case['id']} — {case['title']}",
         "result: " + ("PASS" if row["pass"] else "FAIL") + (": " + "; ".join(row["failed"]) if row.get("failed") else ""),
         f"fixture {case.get('fixture', case['id'])} · family {case['family']} · level {case['level']} · rules {', '.join(case.get('rules') or []) or '–'}",
         f"turns {turns} · slowest agent turn {row.get('slowest_turn_s')} s · ended {row.get('ended')}", ""]
    if not msgs: L.append("(no transcript)")
    for m in msgs:
        role, msg = m.get("role"), m.get("message")
        if role == "user": L.append(f"**customer:** {msg}")
        elif role == "assistant": L.append(f"**agent:** {msg}")
        elif role == "system":
            if isinstance(msg, dict): ev = msg
            else:
                try: ev = json.loads(msg)
                except (TypeError, ValueError): continue
            if not isinstance(ev, dict): continue
            e = ev.get("event")
            if e == "node_enter" and not ev.get("from_node"): L.append(f"    → node {ev.get('node')}")      # later nodes show on their ↪ route line
            elif e == "function_call_start":
                args = ev.get("args")
                if isinstance(args, dict) and "code" in args: shown = "(code)"                              # a code step: its code is the workflow's own
                else: shown = json.dumps(args.get("body") if isinstance(args, dict) and "body" in args else args, ensure_ascii=False)[:500]
                L.append(f"    ⚙ {ev.get('function')} {shown}")
            elif e == "function_call_complete": L.append(f"    ⚙ {ev.get('function')} → {json.dumps(ev.get('result'), ensure_ascii=False)[:300]}")
            elif e == "route_evaluated" and ev.get("matched"): L.append(f"    ↪ {ev.get('from_node')} → {ev.get('target')}: {ev.get('reason')}")
            elif e == "error": L.append(f"    ✖ error: {ev.get('message')}")
    return "\n".join(L) + "\n"


def flaky(hist, passes=None, runs=1):
    """Flaky: the reps of one run disagree, or the outcome flipped twice over the last three runs (pass fail pass, or fail pass fail)."""
    if runs > 1 and 0 < (passes or 0) < runs: return True
    last = hist[-3:]
    return len(last) == 3 and last[0] == last[2] != last[1]


def load_history(path):
    path = pathlib.Path(path)
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()] if path.exists() else []


def previous_result(history, cid):
    """The case's entry in the latest earlier run that ran it, or None."""
    for h in reversed(history):
        if cid in h["cases"]: return h["cases"][cid]
    return None


def case_history(history, cid):
    return [h["cases"][cid]["pass"] for h in history if cid in h["cases"]]


# Statistics: the scoring of tools/statistical_benchmark.py, on every run. A case's results pool across every run of the same saved
# version of the agent (the version freya.save_workflow writes to .freya-agents.json), so --only, --reps and --style runs add up.
STAT_CATEGORIES = ("Failing", "Flaky", "Mostly Passing", "Stable")
PRIORITY = {"Failing": 1, "Flaky": 2, "Mostly Passing": 3}           # P4 is a speaking style a case handles worse; Stable needs nothing
STYLE_GAP = 30                                                       # points between a case's best and worst style that make a style weakness
FIX = {1: "P1 failing: a deterministic bug, so its transcript shows the step, route or check that goes wrong",
       2: "P2 flaky: a rule held only by a prompt, an ambiguous route or a weak condition; compare a passing and a failing transcript, then move the rule into a route or code",
       3: "P3 mostly passing: the final counts a case only when it passes 3 runs out of 3; read a failing transcript",
       4: "P4 style weakness: the step that hears the answer must understand a customer who talks that way"}


def wilson(passes, runs, z=1.96):
    """Wilson score interval of a pass rate, as fractions (low, high). Sound for the few runs a build affords; (0, 0) without runs."""
    if not runs: return 0.0, 0.0
    p, d = passes / runs, 1 + z * z / runs
    mid, half = (p + z * z / (2 * runs)) / d, z * math.sqrt(p * (1 - p) / runs + z * z / (4 * runs * runs)) / d
    return max(0.0, mid - half), min(1.0, mid + half)


def flakiness(passes, runs):
    """0.0 when every run agrees (all pass or all fail), 1.0 at a 50% pass rate: 1 - |2p - 1|."""
    return round(1 - abs(2 * passes / runs - 1), 2) if runs else 0.0


def stat_category(rate, flak):
    """Stable from a 90% pass rate. From 70% Flaky when the flakiness is above 0.3 (under 85%), else Mostly Passing. Flaky from 40%, Failing below."""
    if rate >= 90: return "Stable"
    if rate >= 70: return "Flaky" if flak > 0.3 else "Mostly Passing"
    return "Flaky" if rate >= 40 else "Failing"


def case_stats(results):
    """One case's statistics from its results, {style: [passes, runs]}. `final`: its chance to pass 3 runs out of 3, as the final counts."""
    passes, runs = sum(p for p, _ in results.values()), sum(n for _, n in results.values())
    rate, flak, (low, high) = (100 * passes / runs if runs else 0.0), flakiness(passes, runs), wilson(passes, runs)
    cat = stat_category(rate, flak)
    return {"passes": passes, "runs": runs, "rate": round(rate, 1), "ci": [round(100 * low, 1), round(100 * high, 1)], "flakiness": flak,
            "final": round(100 * (passes / runs) ** FINAL_RUNS, 1) if runs else 0.0, "category": cat, "priority": PRIORITY.get(cat),
            "styles": {s: list(v) for s, v in sorted(results.items())}}


def agent_version(agent_id, path=None):
    """The saved version of this agent, from the state file freya.save_workflow keeps ("created" before its first update).
    None when the agent is not in it: then a run's statistics are its own."""
    try: slots = json.loads(pathlib.Path(path or ROOT / ".freya-agents.json").read_text(encoding="utf-8"))
    except (OSError, ValueError): return None
    for s in (slots.values() if isinstance(slots, dict) else []):
        if isinstance(s, dict) and s.get("agent_id") == agent_id: return str(s.get("version", "created"))
    return None


def same_version(history, agent_id, version):
    """The runs whose results pool with the last one: same agent, same saved version. Without a version, the last run alone."""
    if version is None: return history[-1:]
    return [h for h in history if h.get("agent_id") == agent_id and h.get("version") == version]


def pool(runs, cases):
    """Each case's results in `runs`, {case: {style: [passes, runs]}}, counting a run only when it played the same text of the case.
    The style is the run's --style, else the case's own, else "none"."""
    sig, own, out = {c["id"]: signature(c) for c in cases}, {c["id"]: c.get("style") for c in cases}, {}
    for h in runs:
        for cid, c in h.get("cases", {}).items():
            if cid not in sig or c.get("sig") != sig[cid]: continue
            acc = out.setdefault(cid, {}).setdefault(h.get("style") or own[cid] or "none", [0, 0])
            acc[0] += c.get("passes", int(bool(c.get("pass")))); acc[1] += c.get("runs", 1)
    return out


def actions(per):
    """The fix order: P1 failing, P2 flaky, P3 mostly passing, P4 a speaking style a case handles worse than its other styles."""
    out = []
    def add(p, cid, x, issue): out.append({"priority": p, "case": cid, "family": x.get("family"), "rules": x.get("rules") or [], "issue": issue, "action": FIX[p]})
    for cid, x in per.items():
        n = f"{x['passes']}/{x['runs']}"
        if x["category"] == "Failing": add(1, cid, x, f"fails every run ({n})" if not x["passes"] else f"mostly fails ({n})")
        elif x["category"] == "Flaky": add(2, cid, x, f"flaky ({n}, flakiness {x['flakiness']:.2f})")
        elif x["category"] == "Mostly Passing": add(3, cid, x, f"mostly passes ({n}, 3 of 3 only {x['final']:.0f}% of the time)")
        rates = {s: 100 * p / k for s, (p, k) in x["styles"].items() if k}
        if len(rates) > 1:
            weak, best = min(rates, key=rates.get), max(rates, key=rates.get)
            if weak != "none" and rates[best] - rates[weak] > STYLE_GAP:        # failing the plain way too is not a style weakness
                add(4, cid, x, f"handles '{weak}' worse: {rates[weak]:.0f}% against {rates[best]:.0f}% as '{best}'")
    return sorted(out, key=lambda a: (a["priority"], a["case"]))


def statistics(results, cases):
    """Statistics of a case set from pooled results: per case, overall, the fix order and the hidden-brief estimate.
    The estimate needs results for every case and counts a case only when it passes 3 runs out of 3, as the final does."""
    per = {c["id"]: {**case_stats(results[c["id"]]), "family": c.get("family"), "rules": c.get("rules") or []} for c in cases if results.get(c["id"])}
    out, s = {"covered": len(per), "total": len(cases), "cases": per, "actions": actions(per)}, list(per.values())
    if not s: return out
    mean, flak = sum(x["rate"] for x in s) / len(s), sum(x["flakiness"] for x in s) / len(s)
    passes, runs = sum(x["passes"] for x in s), sum(x["runs"] for x in s)
    (low, high), stability = wilson(passes, runs), 100 * (1 - flak)
    out.update({"results": runs, "mean_rate": round(mean, 1), "ci": [round(100 * low, 1), round(100 * high, 1)], "flakiness": round(flak, 2),
                "stability": round(stability, 1), "robustness": round(0.7 * mean + 0.3 * stability, 1),
                "categories": {k: sum(x["category"] == k for x in s) for k in STAT_CATEGORIES}})
    counted = [c for c in cases if c.get("suite") != "universal"] or cases     # the final's cases are scored on records; universal ones are not
    out["missing"] = sum(c["id"] not in per for c in counted)
    if not out["missing"]:
        xs = [per[c["id"]] for c in counted]; least = min(x["runs"] for x in xs)
        out["hidden"] = {"expected": round(HIDDEN_CASES * sum((x["passes"] / x["runs"]) ** FINAL_RUNS for x in xs) / len(xs)),
                         "one_run": round(HIDDEN_CASES * sum(x["rate"] for x in xs) / len(xs) / 100), "of": HIDDEN_CASES, "least_results": least,
                         "confidence": "high" if least >= 10 else "medium" if least >= FINAL_RUNS else "low", "universal_left_out": len(cases) - len(counted)}
    return out


def build_run(meta, cases, reps_rows, history, turns_by_id, slot, every=None):
    """The run record. reps_rows: run_cases.run_once rows, one list per repetition; history: the slot's earlier runs;
    every: the whole case set when --only played part of it, so the statistics cover the set."""
    last, n_reps = reps_rows[-1], len(reps_rows)
    rows = []
    for k, c in enumerate(cases):
        passes = sum(rep[k]["pass"] for rep in reps_rows); ok = passes == n_reps
        r = next((rep[k] for rep in reps_rows if not rep[k]["pass"]), last[k])      # the first failing rep is the one shown; else the last
        failed = [] if ok else r["failed"]
        prev, sig = previous_result(history, c["id"]), signature(c)
        slow_s, suite = r.get("slowest_turn_s"), c.get("suite") or ("generated" if "fixture" in c else "public")
        rows.append({"id": c["id"], "title": c["title"], "family": c["family"], "level": c["level"], "fixture": c.get("fixture", c["id"]),
                     "rules": c.get("rules") or [], "suite": suite, "public": suite == "public", "pass": ok, "passes": passes, "runs": n_reps,
                     "failed": failed, "categories": classify(failed),
                     "flags": [f for f, on in (("hung_up", r.get("ended") == "customer-ended-call" and not ok), ("slow", (slow_s or 0) > 10)) if on],
                     "calls": r.get("calls") or [], "forbidden": r.get("forbidden") or [], "slowest_turn_s": slow_s, "ended": r.get("ended"),
                     "turns": turns_by_id.get(c["id"]), "transcript": f"results/bench/{slot}/run-{meta['n']:02d}/{c['id']}.md", "call_id": r.get("call_id"),
                     "flaky": flaky(case_history(history, c["id"]) + [ok], passes, n_reps),
                     "changed": bool(prev and prev.get("sig") and prev["sig"] != sig), "sig": sig, "promised": promised(r.get("calls") or [])})
    def was(cid):
        p = previous_result(history, cid); return None if p is None else p["pass"]
    def saved_since(cid):                            # a flip on the same saved version is flakiness, not a fix or a regression
        h = next((h for h in reversed(history) if cid in h["cases"]), None)
        return h is None or meta.get("version") is None or (h.get("agent_id"), h.get("version")) != (meta["agent_id"], meta["version"])
    waits = sorted(r["slowest_turn_s"] for r in rows if r["slowest_turn_s"] is not None)
    med = waits[len(waits) // 2] if waits else 0
    run = {**meta, "slot": slot, "reps": n_reps, "rows": rows,
           "fixed": [r["id"] for r in rows if r["pass"] and was(r["id"]) is False and saved_since(r["id"])],
           "regressed": [r["id"] for r in rows if not r["pass"] and was(r["id"]) is True and saved_since(r["id"])],
           "still_failing": [r["id"] for r in rows if not r["pass"] and was(r["id"]) is False],
           "promised_passed": round(sum(r["promised"] for r in rows if r["pass"]), 2),
           "median_slowest_s": med, "worst_slowest_s": waits[-1] if waits else 0, "slow": med > 10,
           "hung_up": sum("hung_up" in r["flags"] for r in rows), "all_pass": all(r["pass"] for r in rows),
           "styles_run": sorted({h["style"] for h in history if h.get("style")} | ({meta["style"]} if meta.get("style") else set()) | {c["style"] for c in cases if c.get("style")})}
    run["cases"] = {r["id"]: {"pass": r["pass"], "sig": r["sig"], "categories": r["categories"], "passes": r["passes"], "runs": r["runs"]} for r in rows}
    runs = same_version(history + [history_line(run)], meta["agent_id"], meta.get("version"))
    run["stats"] = {**statistics(pool(runs, every or cases), every or cases), "runs_pooled": [h["n"] for h in runs]}
    for r in rows:                                   # mixed results on this version are flaky too, whatever the last three runs show
        x = run["stats"]["cases"].get(r["id"])
        if x and 0 < x["passes"] < x["runs"]: r["flaky"] = True
    return run


def history_line(run):
    return {**{k: run[k] for k in ("n", "at", "agent_id", "seconds", "reps", "style", "only", "public", "all_pass", "cases")}, "version": run.get("version")}


def suggest_next(run, history, minutes_used):
    """What the numbers say about the next run. The builder decides; this lays out the options. `history` ends with `run`."""
    rows, out = run["rows"], []
    failed = [r["id"] for r in rows if not r["pass"]]; fl = [r["id"] for r in rows if r["flaky"]]
    if run.get("no_reply"):
        nr = run["no_reply"]["cases"]
        out.append(f"Not scored (the agent's model did not answer): {len(nr)} cases. They tested nothing; do not change the workflow because of them. "
                   + (run["no_reply"].get("diagnosis") or "") + f" Then `--only {','.join(nr[:20])}`" + (" and the others it names." if len(nr) > 20 else "."))
    if run.get("unreached"):
        ur = run["unreached"]
        out.append(f"Not scored (a tool call could not reach the bank's host): {len(ur)} cases. They tested the tunnel, not the agent; do not change the workflow because of them. "
                   f"Run them again with `--only {','.join(ur[:20])}`" + (" and the others it names." if len(ur) > 20 else "."))
    if run.get("cut"):
        np_ = run["cut"]["not_played"]
        out.append(f"Not played (the run reached its {run['cut']['limit_min']:.0f}-minute time limit): {len(np_)} cases. The failures below come from the cases that finished, "
                   f"which the run started first because they failed before. Fix those, then play the rest with `--only {','.join(np_[:20])}`" + (" and the others it names." if len(np_) > 20 else "."))
    if run["regressed"]: out.append(f"Regressions first: {', '.join(run['regressed'])} passed before and fail now. Fix, then `--only {','.join(run['regressed'])}`.")
    hard = [i for i in failed if i not in fl and i not in run["regressed"]]
    if hard: out.append(f"Failing: {', '.join(hard)}. Read their transcripts, fix, re-run `--only {','.join(hard)}`, then a full run for regressions.")
    if fl: out.append(f"Flaky: {', '.join(fl)} passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only {','.join(fl)}`.")
    st = run.get("stats") or {}
    if st.get("actions"):
        acts = st["actions"]
        out.append("Fix order on this version (section Statistics): " + ", ".join(f"P{a['priority']} {a['case']}" for a in acts[:10]) + (f" and {len(acts) - 10} more" if len(acts) > 10 else "") + ".")
    if st.get("hidden"):
        h, more = st["hidden"], "`--reps 2`" if run.get("version") is None else "`--reps 2`, another full run or a `--style` run before the next save"
        out.append(f"Hidden-brief estimate on this version: {h['expected']} of {h['of']} counting only 3 passes out of 3 ({h['one_run']} if one pass counted), confidence {h['confidence']}"
                   + (f": under 3 results per case. More results on this version firm it up: {more}." if h["confidence"] == "low" else "."))
    if run["slow"]: out.append(f"The agent was slow in this run (median slowest turn {run['median_slowest_s']:.0f} s). A call that ended in a hang-up may pass when re-run; re-run those before changing the workflow.")
    changed = [r["id"] for r in rows if r["changed"]]
    if changed: out.append(f"Changed since the previous run: {', '.join(changed)}. If a change weakened a check or an expectation, undo it unless the brief says the old version was wrong.")
    if not failed:
        if run["only"]: out.append("The re-run cases pass. Run the full set once before you finish: a fix can break another case.")
        else:
            streak = 1
            for h in reversed(history[:-1]):
                if h.get("only"): continue                               # an --only run in between says nothing about the full set
                if not h.get("all_pass"): break
                streak += 1
            if streak == 1: out.append("Everything passed once. One pass is a hint, not proof: run again (`--reps 2`, or a `--style` run) if the clock allows.")
            else: out.append(f"Everything passed in {streak} full runs in a row. Stop unless a transcript-review finding is open.")
    unused = [s for s in sorted(STYLES) if s not in run["styles_run"]]
    if unused: out.append("Styles not run yet: " + ", ".join(unused) + ". Final customers talk like people; a `--style` run shows whether the agent copes.")
    if minutes_used is not None:
        full = next((h for h in reversed(history) if not h.get("only")), run)       # the last full run, this one included: an --only run says nothing about the full set's length
        est = full["seconds"] / max(1, full.get("reps") or 1) / 60
        n_cases = len(rows); per = est / max(1, n_cases)                 # minutes per case at this concurrency, for the --only estimate
        failed_n = len(failed)
        if BUDGET_MIN - minutes_used - 3 < est:
            out.append(f"Time: {minutes_used:.0f} of {BUDGET_MIN} min used; a full run takes ~{est:.0f} min and does not fit with a 3-minute margin."
                       + (f" `--only` on the {failed_n} failing cases takes ~{max(1, failed_n * per):.0f} min" + (" and fits." if BUDGET_MIN - minutes_used - 3 >= failed_n * per else " and does not fit either: finish.") if failed_n else " Finish."))
        else: out.append(f"Time: {minutes_used:.0f} of {BUDGET_MIN} min used; a full run (~{est:.0f} min; `--reps 2` ~{2 * est:.0f} min) still fits with a 3-minute margin.")
    return out


def call_line(c):
    short = c["tool"].replace("verify_identity", "verify").replace("create_promise", "promise")
    args = c.get("args") or {}
    return short + (" " + json.dumps(args, ensure_ascii=False) if args else "") + ("" if (c.get("result") or {}).get("ok", True) else " ✖")


def stats_md(st, title, scope):
    """Statistics as a report section: overall, the fix order, a row per case and, for cases played in more than one style, the styles."""
    L = [f"## {title}", "", f"{scope} · {st['covered']} of {st['total']} cases have results" + (f", {st['results']} results in all" if st.get("results") else ""), ""]
    if not st.get("results"): return L
    h = st.get("hidden")
    L += [f"- mean pass rate per case {st['mean_rate']:.1f}% · 95% CI {st['ci'][0]:.1f}–{st['ci'][1]:.1f}% for all results taken together",
          f"- flakiness {st['flakiness']:.2f} on average (0: every run of a case agrees) · stability {st['stability']:.0f}/100 · robustness {st['robustness']:.0f}/100 (0.7 × pass rate + 0.3 × stability)",
          (f"- hidden-brief estimate: {h['expected']} of {h['of']} when a case counts only with 3 passes out of 3, as in the final ({h['one_run']} if one pass counted) · "
           f"confidence {h['confidence']}: at least {h['least_results']} result{'' if h['least_results'] == 1 else 's'} per case"
           + (" · the universal cases are left out: the final scores records" if h.get("universal_left_out") else "")) if h else
          f"- hidden-brief estimate: needs results for every case; {st['missing']} have none on this version yet",
          "- " + " · ".join(f"{k} {v}" for k, v in st["categories"].items()), ""]
    if st["actions"]:
        L += ["Fix order:", ""]
        for p in sorted({a["priority"] for a in st["actions"]}):
            L += [f"- {FIX[p]}"] + [f"  - {a['case']} ({a['family']}) {a['issue']} · rules {', '.join(a['rules']) or '–'}" for a in st["actions"] if a["priority"] == p]
        L.append("")
    L += ["| case | family | passes | 95% CI | flakiness | 3 of 3 | category |", "|---|---|---|---|---|---|---|"]
    for cid, x in sorted(st["cases"].items(), key=lambda kv: (kv[1]["priority"] or 9, kv[1]["rate"], kv[0])):
        (low, high), p = wilson(x["passes"], x["runs"]), x["passes"] / x["runs"]             # from the counts: no rounding twice
        L.append(f"| {cid} | {x['family']} | {x['passes']}/{x['runs']} ({100 * p:.0f}%) | {100 * low:.0f}–{100 * high:.0f}% | {x['flakiness']:.2f} | {100 * p ** FINAL_RUNS:.0f}% | "
                 + x["category"] + (f" P{x['priority']}" if x["priority"] else "") + " |")
    multi = {cid: x for cid, x in st["cases"].items() if len(x["styles"]) > 1}
    if multi:
        styles = sorted({s for x in st["cases"].values() for s in x["styles"]}, key=lambda s: (s != "none", s))
        tot = {s: [sum(x["styles"].get(s, [0, 0])[i] for x in st["cases"].values()) for i in (0, 1)] for s in styles}
        L += ["", "### Style robustness", "", "by style: " + " · ".join(f"{s} {100 * p / n:.0f}% ({p}/{n})" for s, (p, n) in tot.items() if n), "",
              "| case | " + " | ".join(styles) + " | spread |", "|---|" + "---|" * (len(styles) + 1)]
        for cid, x in sorted(multi.items()):
            r = {s: 100 * p / n for s, (p, n) in x["styles"].items() if n}; gap = max(r.values()) - min(r.values())
            L.append(f"| {cid} | " + " | ".join(f"{r[s]:.0f}%" if s in r else "–" for s in styles) + f" | {gap:.0f}" + (" ⚠" if gap > STYLE_GAP else "") + " |")
    return L + [""]


def write_report(slot, run, history):
    """The analysis report of one run, as markdown. `history` is every run of this slot, oldest first, this run last."""
    rows = run["rows"]; gen, uni, pub = ([r for r in rows if r["suite"] == s] for s in ("generated", "universal", "public"))
    L = [f"# Benchmark {slot} · run {run['n']}", "",
         f"agent `{run['agent_id']}` · {run['at']} · {run['seconds']:.0f} s · reps {run['reps']} · style {run['style'] or 'none'}" + (" · `--only`" if run["only"] else ""), "",
         "## Score", "",
         f"- generated {sum(r['pass'] for r in gen)}/{len(gen)}" + (f" · universal {sum(r['pass'] for r in uni)}/{len(uni)}" if uni else "")
         + (f" · public {sum(r['pass'] for r in pub)}/{len(pub)}" if pub else "") + f" · total {sum(r['pass'] for r in rows)}/{len(rows)}",
         f"- promised on passed cases: {run['promised_passed']:.2f} (the organisers' first tie-breaker)",
         f"- fixed since the previous run: {', '.join(run['fixed']) or 'none'}",
         f"- regressed: {', '.join(run['regressed']) or 'none'}",
         f"- still failing: {', '.join(run['still_failing']) or 'none'}"]
    if run.get("cut"):
        np_ = run["cut"]["not_played"]
        L.append(f"- **cut at the {run['cut']['limit_min']:.0f}-minute time limit**: {len(np_)} cases were not played and are not scored: {', '.join(np_)}. "
                 f"Run them with `--only {','.join(np_)}`.")
    if run.get("no_reply"):
        nr = run["no_reply"]["cases"]
        L.append(f"- **not scored, the agent's model did not answer**: {len(nr)} cases: {', '.join(nr)}. {run['no_reply'].get('diagnosis') or ''}")
    if run.get("unreached"):
        L.append(f"- **not scored, a tool call could not reach the bank's host**: {len(run['unreached'])} cases: {', '.join(run['unreached'])}. "
                 f"Run them again with `--only {','.join(run['unreached'])}`.")
    L.append("")
    if run.get("stats"):
        pooled = run["stats"].get("runs_pooled") or [run["n"]]
        scope = (f"agent version {run['version']}, " + ("run " if len(pooled) == 1 else "runs ") + ", ".join(map(str, pooled)) if run.get("version") is not None
                 else "this run alone: the agent is not in .freya-agents.json, so earlier runs cannot be tied to its version")
        L += stats_md(run["stats"], "Statistics on this version", scope)
    L += ["## History", "", "| case | " + " | ".join(f"run {h['n']}" for h in history) + " | |", "|---|" + "---|" * len(history) + "---|"]
    current = {r["id"]: r for r in rows}; ids = list(current)
    for h in history: ids += [cid for cid in h["cases"] if cid not in ids]            # a case that left the file stays visible
    for cid in ids:
        marks = [("✓" if h["cases"][cid]["pass"] else "✗") if cid in h["cases"] else "–" for h in history]
        r = current.get(cid)
        notes = (", ".join(x for x in (("flaky" if r["flaky"] else ""), ("changed" if r["changed"] else "")) if x) if r else
                 "not played (time limit)" if cid in ((run.get("cut") or {}).get("not_played") or []) else
                 "not scored (no reply)" if cid in ((run.get("no_reply") or {}).get("cases") or []) else
                 "not scored (host unreachable)" if cid in (run.get("unreached") or []) else "not in this run" if run["only"] else "removed")
        L.append(f"| {cid} | " + " | ".join(marks) + f" | {notes} |")
    L.append("")
    if run.get("uncovered_rules") is not None:
        L += ["## Rule coverage", "", ("rules cited by no case: " + ", ".join(run["uncovered_rules"])) if run["uncovered_rules"] else "every rule is cited by at least one case", ""]
    cats = collections.Counter(c for r in rows for c in r["categories"]); flags = collections.Counter(f for r in rows for f in r["flags"])
    L += ["## Failure categories", "", ", ".join(f"{k} {v}" for k, v in sorted(cats.items())) or "none"]
    if flags: L.append("flags: " + ", ".join(f"{k} {v}" for k, v in sorted(flags.items())))
    L += ["", "## Failed cases", ""]
    for r in rows:
        if r["pass"]: continue
        L += [f"### {r['id']} — {r['title']}",
              f"{r['family']} · {r['level']} · fixture {r['fixture']} · rules {', '.join(r['rules']) or '–'}" + (f" · {r['passes']}/{r['runs']} reps passed" if r["runs"] > 1 else ""), ""]
        L += [f"- {x}" for x in r["failed"]]
        L.append("- tools: " + (" > ".join(call_line(c) for c in r["calls"]) or "(no tool calls)"))
        errs = [c for c in r["calls"] if not (c.get("result") or {}).get("ok", True)]
        if errs: L.append("- tool errors: " + "; ".join(f"{c['tool']} → {json.dumps(c.get('result'), ensure_ascii=False)[:160]}" for c in errs))
        if r["forbidden"]: L.append("- forbidden tools called: " + ", ".join(r["forbidden"]))
        L += [f"- slowest agent turn {r['slowest_turn_s']} s · ended {r['ended'] or '?'} · transcript `{r['transcript']}`", ""]
    if run["all_pass"]: L += ["none", ""]
    L += ["## Passed cases", ""]
    for r in rows:
        if r["pass"]: L.append(f"- {r['id']} {r['title']} · {r['turns'] if r['turns'] is not None else '?'} turns · " + (" > ".join(c["tool"] for c in r["calls"]) or "no tools") + f" · slowest {r['slowest_turn_s']} s · `{r['transcript']}`")
    L += ["", "## Timing", "",
          f"median slowest agent turn {run['median_slowest_s']:.0f} s · worst {run['worst_slowest_s']:.0f} s · failed calls where the customer hung up: {run['hung_up']}"
          + (f" · replies over {SLOW_S:.0f} s: {100 * run['slow_share']:.0f}% · customers who hung up waiting: {run.get('waited_out', 0)}" if run.get("slow_share") is not None else "")
          + (" · **the agent was slow in this run; a re-run may score higher**" if run["slow"] else ""),
          (f"calls at a time: {run['concurrency']} in this run; next run {run['next_concurrency']} ({run['concurrency_note']})" if run.get("concurrency") else ""), "",
          "## What this run suggests", ""] + [f"- {s}" for s in suggest_next(run, history, run.get("minutes_used"))] + [""]
    return "\n".join(L)


def slot_of(cases_path):
    name = pathlib.Path(str(cases_path).replace("\\", "/")).name
    return name[:-len(".cases.json")] if name.endswith(".cases.json") else name.rsplit(".", 1)[0]


def select_only(cases, only):
    want = [x.strip() for x in only.split(",") if x.strip()]
    missing = [i for i in want if i not in {c["id"] for c in cases}]
    if missing: raise SystemExit("--only names cases that are not in this run: " + ", ".join(missing))
    return [c for c in cases if c["id"] in want]


def rule_ids_from(files):
    """Rule ids of every --rules file, or None when no file was given."""
    if not files: return None
    ids = []
    for f in files:
        got = extract_rules(f)
        if not got: print(f"warning: no numbered rules found in {f} (a rule is a line that starts with `N.`)")
        ids += [r for r in got if r not in ids]
    return ids


SLOW_S = run_cases.SLOW_TURN_S                                       # a reply slower than this is a slow one
RAISE_SHARE, HALVE_SHARE = 0.12, 0.25                                # slow replies in a run that used every slot: 5-8% when the model was well, 16-17% busy, 50% failing
CONCURRENCY_RULE = 2                                                 # a value settled by an older rule is not reused
TUNNEL_MAX = 12                                                      # a free tunnel refused every connection for a minute once ~115-125 had arrived
                                                                     # within one: 20 calls plus the benchmark's 63 sessions did it, and so did 16 calls
                                                                     # alone, whose first minute (every call verifying identity at once) sent 114; at 12
                                                                     # the busiest minute carried 70


def concurrency_file(slot): return ROOT / "results" / "bench" / slot / "concurrency.json"


def pick_concurrency(slot, host=None):
    """Calls at a time for this slot's next simulation: the value the last run settled on, else run_cases.CONCURRENCY. A self-hosted
    mock behind a tunnel caps it at TUNNEL_MAX."""
    try:
        d = json.loads(concurrency_file(slot).read_text(encoding="utf-8"))
        n = int(d.get("concurrency") or 0) if d.get("rule") == CONCURRENCY_RULE else 0
    except (OSError, ValueError, AttributeError): n = 0
    n = n or run_cases.CONCURRENCY
    return max(run_cases.CONCURRENCY_MIN, min(n, TUNNEL_MAX if host else run_cases.CONCURRENCY_MAX))


def adapt_concurrency(slot, used, slow_share, waited_out, n_cases, host=None, unreached=0):
    """After a run that used every slot, settle the next run's concurrency from how the agent kept up: at most RAISE_SHARE of its
    replies over SLOW_S and no customer who hung up waiting lets 1.5x more calls play at once; over HALVE_SHARE, or two customers who
    hung up waiting, halves them. A run with fewer customers than slots keeps the value: it says nothing about the load. Calls that
    could not reach the bank's host (`unreached`) halve it in any run: a tunnel refuses connections when too many arrive. Writes the
    decision for the next run and returns (next, reason)."""
    cap = TUNNEL_MAX if host else run_cases.CONCURRENCY_MAX
    seen = f"{100 * slow_share:.0f}% of replies over {SLOW_S:.0f} s, {waited_out} customer{'s' if waited_out != 1 else ''} hung up waiting"
    if unreached: nxt, why = used // 2, f"{unreached} call{'s' if unreached != 1 else ''} could not reach the bank's host: halved"
    elif n_cases < used: nxt, why = used, f"only {n_cases} of {used} slots were in use: kept"
    elif slow_share > HALVE_SHARE or waited_out >= 2: nxt, why = used // 2, f"the agent was slow ({seen}): halved"
    elif slow_share <= RAISE_SHARE and not waited_out: nxt, why = int(used * 1.5), f"the agent kept up ({seen}): raised"
    else: nxt, why = used, f"{seen}: kept"
    nxt = max(run_cases.CONCURRENCY_MIN, min(nxt, cap))
    concurrency_file(slot).write_text(json.dumps({"concurrency": nxt, "rule": CONCURRENCY_RULE, "after_run_with": used, "slow_share": round(slow_share, 3),
                                                  "waited_out": waited_out, "n_cases": n_cases, "at": time.strftime("%Y-%m-%d %H:%M:%S")}, indent=1), encoding="utf-8")
    return nxt, why


def slow_replies(reps_rows):
    """(share of the agent's replies over SLOW_S, customers who hung up after waiting SLOW_S or more for a reply) over every rep."""
    rows = [r for rep in reps_rows for r in rep]
    n = sum(r.get("replies") or 0 for r in rows)
    waited_out = sum(r.get("ended") == "customer-ended-call" and (r.get("waited_at_end") or 0) >= SLOW_S for r in rows)
    return (sum(r.get("slow_replies") or 0 for r in rows) / n if n else 0.0), waited_out


RUN_LIMIT_MAX, RUN_LIMIT_MIN, RUN_LIMIT_MARGIN = 11, 3, 5            # minutes: with the grace for calls in flight and the scoring, below the builder's 15-minute command limit; leave 5 of the build for a fix


def run_time_limit(max_minutes, minutes_used):
    """Minutes this run may wait for its simulation: --max-minutes when given; inside a build, what the 30 minutes leave after a margin
    for one fix (at most 11, so that the calls in flight, scoring and transcripts still fit the 15-minute command limit, and at least 3); outside a build, none."""
    if max_minutes: return max_minutes
    if minutes_used is None: return None
    return max(RUN_LIMIT_MIN, min(RUN_LIMIT_MAX, BUDGET_MIN - minutes_used - RUN_LIMIT_MARGIN))


def play_order(cases, history):
    """The order the cases are handed to the simulation: cases that failed the last time they ran first, then cases never run, then
    cases that passed, the universal cases last. Freya decides the order the calls start in and did not follow this one (run 13 of
    brief-f started the universal cases first), so a run cut at its time limit can leave out any case."""
    last = {}
    for h in history:
        for cid, c in (h.get("cases") or {}).items(): last[cid] = c.get("pass")
    def rank(c):
        if c.get("suite") == "universal": return 3
        p = last.get(c["id"]); return 0 if p is False else 1 if p is None else 2
    return sorted(cases, key=rank)


# When calls go unanswered, a chat turn tells the model from the workflow: a one-node workflow that only answers in one sentence and
# the agent's own workflow get the same question side by side. No reply from either: the model is down. A reply from the one-node
# workflow only: the agent's first reply is broken. The chat route runs the published version on the event's model (freya.update_workflow).
PROBE_FILE = ROOT / "results" / "probe-workflow.json"
PROBE_VARS = {"customer_id": "c_probe", "first_name": "Sam", "last_name": "Probe", "title": "Mr", "now": "2026-10-14T11:00"}
PROBE_WORKFLOW = {"initial_node": "talk", "system_prompt": "You are a test line. Answer every message in one short sentence.",
                  "nodes": {"talk": {"name": "talk", "node_type": "conversation", "task_message": "Answer the caller in one short sentence.",
                                     "on_enter": {"type": "tts", "text": "Hello."}, "tools": [], "transitions": []}}}


def probe_workflow():
    """The one-node workflow's id. Created once per workspace and kept in results/probe-workflow.json: a workspace holds a limited
    number of workflows."""
    ws = freya.workspace_id()
    try: known = json.loads(PROBE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError): known = {}
    if ws not in known:
        w = freya.create_workflow("model probe", PROBE_WORKFLOW)
        freya.update_workflow(w["workflow_id"], PROBE_WORKFLOW)          # sets the event's model and publishes: a chat turn needs both
        known[ws] = w; PROBE_FILE.parent.mkdir(parents=True, exist_ok=True); PROBE_FILE.write_text(json.dumps(known, indent=1), encoding="utf-8")
    return known[ws]["workflow_id"]


def chat_turn(workflow_id):
    """A chat call on a published workflow: a greeting, then a question only the model can answer. Returns (state, seconds, text):
    "answered" with the reply, "no reply" when the gateway gave up waiting for the model (502, 503, 504 or a timeout), "error" otherwise
    (a bare 500 means the workflow cannot start a call at all)."""
    def failed(e, t):
        gave_up = isinstance(e, (TimeoutError, urllib.error.URLError)) or re.search(r"-> 50[234]\b", str(e))
        return ("no reply" if gave_up else "error"), time.time() - t, " ".join(str(e).split())[:160]
    t = time.time()
    try: cid = freya.api("POST", "/api/v2/chat/message", {"workflowId": workflow_id, "message": "Hello?", "customerVariables": PROBE_VARS}).get("callId")
    except Exception as e: return failed(e, t)
    t = time.time()
    try:
        r = freya.api("POST", "/api/v2/chat/message", {"workflowId": workflow_id, "callId": cid, "message": "Can you hear me? Answer in one sentence.", "customerVariables": PROBE_VARS})
        out = ("answered", time.time() - t, " ".join(str(r.get("response") or "").split())[:100])
    except Exception as e: out = failed(e, t)
    try: freya.api("POST", "/api/v2/chat/end", {"callId": cid})
    except Exception: pass
    return out


def workflow_of(agent_id, path=None):
    """The workflow id of an agent saved through freya.save_workflow, else None."""
    try: slots = json.loads(pathlib.Path(path or ROOT / ".freya-agents.json").read_text(encoding="utf-8"))
    except (OSError, ValueError): return None
    return next((s.get("workflow_id") for s in (slots.values() if isinstance(slots, dict) else []) if isinstance(s, dict) and s.get("agent_id") == agent_id), None)


def diagnose(agent_id):
    """Is the agent's model answering? Returns (state, text): state "down" (the model answers nobody), "workflow" (the model answers
    the one-node workflow but not the agent's) or "up"; text says what to do."""
    import concurrent.futures
    own_wf = workflow_of(agent_id)
    try: ref_wf, ref_err = probe_workflow(), None
    except Exception as e: ref_wf, ref_err = None, " ".join(str(e).split())[:160]
    with concurrent.futures.ThreadPoolExecutor(2) as ex:
        ref = ex.submit(chat_turn, ref_wf) if ref_wf else None
        own = ex.submit(chat_turn, own_wf) if own_wf else None
        ref = ref.result() if ref else ("error", 0.0, ref_err or "no test workflow")
        own = own.result() if own else ("error", 0.0, "the agent is not in .freya-agents.json")
    again = f"`python tools/benchmark.py {agent_id} --probe`"
    if ref[0] == "answered" and own[0] == "no reply":
        return "workflow", (f"The model answers (a one-node test workflow replied in {ref[1]:.0f} s) but your workflow gave no reply to a chat turn in {own[1]:.0f} s: "
                            "its first reply is broken. Look at what your last save changed, fix it, save, and run again.")
    if "answered" in (ref[0], own[0]):
        took = ", ".join(f"{who} {x[1]:.0f} s" for who, x in (("one-node test workflow", ref), ("your workflow", own)) if x[0] == "answered")
        return "up", (f"The model answers ({took}). Calls that went unanswered in a simulation met a model that was down or overloaded then: run the same command again.")
    if "no reply" in (ref[0], own[0]):
        return "down", (f"The phone agent's model is not answering: a chat turn got no reply in {max(ref[1], own[1]):.0f} s"
                        + (" from a one-node test workflow either" if ref[0] == "no reply" else "") + ". Nothing in your workflow causes this and the unanswered calls "
                        f"tested nothing: change nothing because of them. Probe again in two minutes with {again}; when it answers, run the same benchmark command again.")
    return "unknown", (f"The chat probe could not tell (test workflow: {ref[2]}; your workflow: {own[2]}). "
                       f"Wait two minutes and run {again}, or run the same benchmark command again.")


def practice_host(host):
    """Where the benchmark itself opens sessions and reads ledgers. For a tunnel opened on this machine (ngrok's local API on port
    4040 lists it), its local address: it answers the same, and the tunnel then carries only Freya's tool calls. Else `host`."""
    host = host.rstrip("/")
    try:
        with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels", timeout=2) as r: tunnels = json.load(r).get("tunnels") or []
    except (OSError, ValueError, AttributeError): return host
    for t in tunnels:
        if str(t.get("public_url") or "").rstrip("/") == host:
            addr = str((t.get("config") or {}).get("addr") or "")
            if addr.isdigit(): return f"http://127.0.0.1:{addr}"
            if addr: return (addr if addr.startswith("http") else "http://" + addr).rstrip("/").replace("://localhost", "://127.0.0.1")   # localhost tries IPv6 first: 2 s a request
    return host


def minutes_since_builder_start():
    """Minutes since the newest trace was started, i.e. since the builder's run began. None without a trace."""
    folder = ROOT / "traces"
    traces = sorted(folder.glob("*.jsonl"), key=lambda p: p.stat().st_mtime) if folder.exists() else []
    if not traces: return None
    if time.time() - traces[-1].stat().st_mtime > 60 * 60: return None        # nothing written for an hour: no builder is running
    try:
        first = json.loads(traces[-1].read_text(encoding="utf-8").splitlines()[0])
        start = datetime.datetime.strptime(first["start"], "%Y-%m-%dT%H:%M:%S%z")
        return (datetime.datetime.now(start.tzinfo) - start).total_seconds() / 60
    except (OSError, ValueError, KeyError, IndexError): return None


def run(a):
    t0 = time.time()
    fixtures, openapi, own = load_fixtures(fixtures_path(a.cases)), load_openapi(a.openapi), own_fixtures(a.cases)
    gen = json.load(open(a.cases, encoding="utf-8"))
    rule_ids = rule_ids_from(a.rules)
    errors, warnings, cov = check_cases(gen, fixtures, openapi, rule_ids, own)
    print_check(errors, warnings, cov)
    if errors: sys.exit(2)
    write_test_set(a.cases, gen, fixtures)
    universal, skipped = load_universal(fixtures, openapi)
    if skipped: print("universal cases left out, this tool API cannot verify their fixtures' identity fields: " + ", ".join(skipped))
    cases = [merge_with_fixture(c, fixtures) for c in gen] + universal
    if own:                                                          # records the case leaves out are not expected: the judge scores
        for c in cases: c["expected"] = {**NO_EXPECTATION, **(c.get("expected") or {})}
    if a.public: cases += [c for c in fixtures.values() if c["brief"] == a.public]
    every = cases                                                    # the statistics cover the whole set, --only or --skip-universal or not
    if a.skip_universal: cases = [c for c in cases if c.get("suite") != "universal"]
    if a.only: cases = select_only(cases, a.only)
    slot = slot_of(a.cases); out = ROOT / "results" / "bench" / slot; out.mkdir(parents=True, exist_ok=True)
    history = load_history(out / "history.jsonl"); n = len(history) + 1
    busy = run_cases.running_simulations()
    if busy: print("the workspace is busy: " + ", ".join(f"simulation {s.get('name')!r} ({s.get('status')}) since {s.get('createdAt')}" for s in busy[:3])
                   + ". This run queues behind it; a simulation of this size takes 3 to 11 minutes.", flush=True)
    cases = play_order(cases, history)
    ids = run_cases.ensure_personas(cases, a.style)
    concurrency = pick_concurrency(slot, getattr(a, "host", None))
    limit = run_time_limit(getattr(a, "max_minutes", None), minutes_since_builder_start())
    deadline = t0 + limit * 60 if limit else None
    print(f"{len(cases)} customers, {concurrency} calls at a time: about {-(-len(cases) // concurrency)} wave{'s' if len(cases) > concurrency else ''} of a minute or so each"
          + (f"; time limit {limit:.0f} min, then the calls that finished are scored and the rest reported as not played" if limit else ""), flush=True)
    reps_rows, total_s, n_reps = [], 0.0, max(1, a.reps)
    for rep in range(n_reps):
        if deadline and rep and time.time() > deadline - 60: print(f"-- no time left for rep {rep + 1} of {n_reps}"); break
        rows, sim_id, it_id, status, took, med = run_cases.run_once(a.agent_id, cases, ids, a.style, concurrency, deadline)
        for r, c in zip(rows, cases):
            if c.get("suite") == "universal": r["failed"] = universal_failures(r["failed"]); r["pass"] = not r["failed"]
            r["forbidden"] = sorted({t for t in r["tools"] if t in (c.get("forbidden_tools") or [])})
            if r["forbidden"]: r["failed"].append("forbidden tool called: " + ", ".join(r["forbidden"])); r["pass"] = False
            more = applications_failed(c.get("expected") or {}, r.get("calls") or [])
            if more: r["failed"] += more; r["pass"] = False
        reps_rows.append(rows); total_s += took
        uni = [r for r, c in zip(rows, cases) if c.get("suite") == "universal"]
        if uni: print(f"-- universal cases, judged on the conversation, close_call last and identity first: {sum(r['pass'] for r in uni)} / {len(uni)} passed.")
        if n_reps > 1: print(f"-- rep {rep + 1} of {n_reps}: {sum(r['pass'] for r in rows)} / {len(rows)} passed, {took:.0f} s\n")
        if status == "silent" and rep + 1 < n_reps: print("-- the agent's model stopped answering: no further reps"); break
    n_reps = len(reps_rows)                                          # fewer than asked when the time limit or a silent model ended the reps
    played = [all(rep[k].get("played", True) for rep in reps_rows) for k in range(len(cases))]
    why_not = {}
    for k, c in enumerate(cases):
        for rep in reps_rows:
            if not rep[k].get("played", True): why_not.setdefault(c["id"], rep[k].get("why_not") or "time limit")
    not_played = [c["id"] for c, p in zip(cases, played) if not p]
    unanswered = [i for i in not_played if why_not[i] == "no reply"]           # the model did not answer: these calls tested nothing
    unreached = [i for i in not_played if why_not[i] == "host"]                 # the bank's host could not be reached: they tested the outage
    timed_out = [i for i in not_played if why_not[i] not in ("no reply", "host")]
    diagnosis = None
    if unanswered:
        print(f"-- the agent's model did not answer {len(unanswered)} call{'s' if len(unanswered) != 1 else ''}: asking it a chat question to tell the model "
              "from the workflow (up to a minute)", flush=True)
        diagnosis = diagnose(a.agent_id)[1]
        print("-- " + diagnosis, flush=True)
    if not_played:                                                   # score what was played, name the rest
        keep = [k for k, p in enumerate(played) if p]
        cases, reps_rows = [cases[k] for k in keep], [[rep[k] for k in keep] for rep in reps_rows]
        if timed_out: print(f"-- the run reached its {limit or 0:.0f}-minute time limit: {len(timed_out)} cases were not played: "
                            + ", ".join(timed_out) + f". Run them with `--only {','.join(timed_out)}`.", flush=True)
        if unanswered: print(f"-- not scored, the agent's model did not answer: {', '.join(unanswered)}. When it answers, run them with `--only {','.join(unanswered)}`.", flush=True)
        if unreached: print(f"-- not scored, a tool call could not reach the bank's host: {', '.join(unreached)}. A free tunnel refuses connections for the rest of a minute "
                            f"once about 120 arrived; the next run plays fewer calls at a time. Run them again with `--only {','.join(unreached)}`.", flush=True)
        print(f"-- {len(cases)} cases were played and are scored.", flush=True)
        if not cases:
            if unreached and not timed_out and not unanswered: sys.exit("Nothing to score: no call could reach the bank's host. Check that the mock and its tunnel run "
                                                                        "and that the workflow's tool URLs point at the tunnel, then run again.")
            if unanswered and not timed_out: sys.exit("Nothing to score: the agent's model answered none of the calls. " + diagnosis)
            sys.exit(f"No case finished within {limit or 0:.0f} minutes, so there is nothing to score: the model is slow or the workspace was busy. "
                     "Run fewer cases with --only, or wait and run again." + (" " + diagnosis if diagnosis else ""))
    shown = [next((rep[k] for rep in reps_rows if not rep[k]["pass"]), reps_rows[-1][k]) for k in range(len(cases))]   # the first failing rep, else the last
    calls, extra = {}, {}                                            # transcripts: every case, and every rep of a case whose reps disagree
    def fetch(call_id, label):
        try: return freya.get_call(call_id)
        except Exception as e: print(f"transcript of {label} not fetched: {e}"); return None
    for k, (r, c) in enumerate(zip(shown, cases)):
        if r.get("call_id"): calls[c["id"]] = fetch(r["call_id"], c["id"]) or {}
        if 0 < sum(rep[k]["pass"] for rep in reps_rows) < n_reps:
            for i, rep in enumerate(reps_rows, 1):
                if rep[k] is not r and rep[k].get("call_id"): extra[(c["id"], i)] = fetch(rep[k]["call_id"], f"{c['id']} rep {i}") or {}
    meta = {"n": n, "at": time.strftime("%Y-%m-%d %H:%M:%S"), "agent_id": a.agent_id, "version": agent_version(a.agent_id), "seconds": round(time.time() - t0),
            "style": a.style, "only": bool(a.only), "public": a.public, "uncovered_rules": cov.get("uncovered_rules"), "minutes_used": minutes_since_builder_start(),
            "simulation_id": sim_id, "iteration_id": it_id, "status": status, "concurrency": concurrency,
            "cut": {"limit_min": limit, "not_played": timed_out} if timed_out else None,
            "no_reply": {"cases": unanswered, "diagnosis": diagnosis} if unanswered else None, "unreached": unreached or None}
    meta["slow_share"], meta["waited_out"] = slow_replies(reps_rows); meta["slow_share"] = round(meta["slow_share"], 3)
    turns = {cid: sum(m.get("role") in ("user", "assistant") for m in call.get("messages") or []) for cid, call in calls.items()}
    rec = build_run(meta, cases, reps_rows, history, turns, slot, every)
    if unanswered: rec["next_concurrency"], rec["concurrency_note"] = concurrency, f"kept: the model did not answer {len(unanswered)} calls, so this run says nothing about the load"
    else: rec["next_concurrency"], rec["concurrency_note"] = adapt_concurrency(slot, concurrency, rec["slow_share"], rec["waited_out"], len(cases), getattr(a, "host", None),
                                                                           unreached=len(unreached))
    (out / f"run-{n:02d}.json").write_text(json.dumps({**rec, "all_rows": reps_rows}, indent=1, ensure_ascii=False), encoding="utf-8")   # the raw record first
    history.append(history_line(rec))
    with open(out / "history.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(history[-1]) + "\n")
    (out / f"run-{n:02d}").mkdir(exist_ok=True)
    bundle = [f"# Transcripts · {slot} · run {n}", ""]
    for r, c in sorted(zip(rec["rows"], cases), key=lambda rc: rc[0]["pass"]):       # failed cases first
        md = transcript_md(c, r, calls.get(c["id"], {}))
        (out / f"run-{n:02d}" / f"{c['id']}.md").write_text(md, encoding="utf-8"); bundle.append(md)
    for (cid, i), call in extra.items():
        k = next(j for j, c in enumerate(cases) if c["id"] == cid)
        md = transcript_md(cases[k], reps_rows[i - 1][k], call)
        (out / f"run-{n:02d}" / f"{cid}.rep{i}.md").write_text(md, encoding="utf-8"); bundle.append(f"<!-- {cid}, rep {i} -->\n" + md)
    (out / f"run-{n:02d}.transcripts.md").write_text("\n".join(bundle), encoding="utf-8")
    report = write_report(slot, rec, history)
    (out / f"run-{n:02d}.md").write_text(report, encoding="utf-8"); shutil.copyfile(out / f"run-{n:02d}.md", out / "latest.md")
    with open(ROOT / "results" / "log.jsonl", "a") as f:               # the kit's record of how the score moved over time
        f.write(json.dumps({"at": meta["at"], "agent_id": a.agent_id, "brief": a.public, "bench": slot, "run": n, "runs": n_reps,
                            "passed": sum(r["pass"] for r in rec["rows"]), "total": len(rec["rows"]), "seconds": meta["seconds"],
                            "failed": [r["id"] for r in rec["rows"] if not r["pass"]]}) + "\n")
    print(f"\n{sum(r['pass'] for r in rec['rows'])} / {len(rec['rows'])} passed. Report: results/bench/{slot}/latest.md · transcripts: results/bench/{slot}/run-{n:02d}.transcripts.md")
    for s in suggest_next(rec, history, meta["minutes_used"]): print("-", s)


def main():
    briefs = sorted({c["brief"] for c in load_fixtures().values()})
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("agent_id", nargs="?"); ap.add_argument("--fixtures", action="store_true", help="list the practice customers whose bank data a case can borrow")
    ap.add_argument("--check", action="store_true", help="validate the cases file and print coverage, run nothing")
    ap.add_argument("--cases", help="tests/<slot>.cases.json"); ap.add_argument("--rules", action="append", default=[], help="a numbered brief or facts file; repeatable")
    ap.add_argument("--public", choices=briefs, help="also run the public customers of this brief"); ap.add_argument("--only", help="case ids, comma separated")
    ap.add_argument("--reps", type=int, default=1); ap.add_argument("--style", choices=sorted(STYLES))
    ap.add_argument("--max-minutes", type=float, help="stop waiting for the simulation after this many minutes and score the calls that finished; "
                    "inside a build the limit comes from the 30-minute clock (at most 11)")
    ap.add_argument("--skip-universal", action="store_true", help="leave the universal cases out of this run (a fix round between two full runs); the first and the last full run play them")
    ap.add_argument("--openapi", default=str(ROOT / "tools" / "openapi.json"), help="the tool API file to validate against; default tools/openapi.json")
    ap.add_argument("--host", help="base URL of the bank mock that plays the cases (its /v1/practice endpoints), e.g. a tunnel to tools/mock_bank_f.py; default: the organisers' mock")
    ap.add_argument("--probe", action="store_true", help="is the agent's model answering? One chat question to the agent's workflow and to a one-node "
                    "test workflow, side by side (up to a minute); exit 0 when the model answers")
    a = ap.parse_args()
    if a.host:
        import score; score.HOST = practice_host(a.host)
        if score.HOST != a.host.rstrip("/"): print(f"sessions and ledgers go to {score.HOST}, the tunnel's local end: the tunnel carries only Freya's tool calls")
    if a.fixtures: fx = load_fixtures(fixtures_path(a.cases)); print_fixtures(fx); print_universal(fx, load_openapi(a.openapi)); return
    if a.probe:
        if not a.agent_id: ap.error("--probe needs the agent_id")
        state, text = diagnose(a.agent_id); print(text); sys.exit(0 if state == "up" else 3)
    if not a.cases: ap.error("--cases is required")
    if a.check:
        fixtures, gen = load_fixtures(fixtures_path(a.cases)), json.load(open(a.cases, encoding="utf-8"))
        openapi = load_openapi(a.openapi)
        errors, warnings, cov = check_cases(gen, fixtures, openapi, rule_ids_from(a.rules), own_fixtures(a.cases))
        print_check(errors, warnings, cov)
        if not errors: print(f"test set: {write_test_set(a.cases, gen, fixtures)}")
        universal, skipped = load_universal(fixtures, openapi)
        if universal or skipped:
            print(f"every run also plays {len(universal)} universal cases (universal-test-set.json; `--fixtures` lists them)" + (f"; this tool API cannot play {', '.join(skipped)}" if skipped else ""))
        sys.exit(1 if errors else 0)
    if not a.agent_id: ap.error("an agent_id is required to run; use --check to validate only")
    try: run(a)
    except (RuntimeError, urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"Freya or the bank answered with an error: {e}\nA 5xx or a timeout at the start of a run is transient: wait a minute and run the same command again. "
                 "A 4xx (not found, bad request) is not: read the message. If it repeats, say so in your final line.")


if __name__ == "__main__": main()
