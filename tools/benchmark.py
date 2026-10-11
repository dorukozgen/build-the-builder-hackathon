"""Benchmark a phone agent on the scenarios the builder wrote. Same simulation, judge and ledger scoring as run_cases.py.

    python3 tools/benchmark.py --fixtures
    python3 tools/benchmark.py --check --cases tests/<slot>.cases.json [--rules briefs/brief-a.md] [--rules tests/<slot>.facts.md]
    python3 tools/benchmark.py <agent_id> --cases tests/<slot>.cases.json [--rules FILE ...] [--public A|B] [--only ID,ID] [--reps N] [--style S]

A generated case borrows the bank data of one practice customer, its `fixture`: identity answers, products, `now` and the
injected fault. The script, the expected records and the checks are the case's own. Format: docs/test-case-template.md.
Results go to results/bench/<slot>/: history.jsonl, run-NN.json, run-NN.md (latest.md is a copy), run-NN/<case>.md and
run-NN.transcripts.md with every conversation, passed cases too.
"""
import argparse, collections, datetime, hashlib, json, pathlib, re, shutil, sys, time, urllib.error
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the console and the builder read UTF-8
import freya
import run_cases
from run_cases import STYLES

BANK_FIELDS = ("variables", "identity", "products", "faults")        # come from the fixture, never from a generated case
REQUIRED = ("id", "fixture", "title", "family", "level", "rules", "script", "expected", "checks")
OPTIONAL = ("brief", "style", "third_party", "forbidden_tools", "backend")        # backend: state a self-hosted mock sets up for the case (existing records, faults)
LEVELS = ("easy", "medium", "hard")
EXPECTED_KEYS = ("outcome", "promises", "notes", "callbacks", "transfers")
RULE_LINE = re.compile(r"^\s*(\d+)\.\s")
TIME_RE = re.compile(r"^\d{2}:\d{2}$")
BUDGET_MIN = 30                                                      # a builder run, tests included


def load_fixtures(path=ROOT / "public-test-set.json"):
    """The practice customers by id. Their bank data is the only bank data the mock can play."""
    return {c["id"]: c for c in json.load(open(path, encoding="utf-8"))}


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


def check_cases(cases, fixtures, openapi, rule_ids=None):
    """Validate a cases file without running it. Returns (errors, warnings, coverage). Any error stops a run."""
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
            if k not in exp: err(f"expected.{k} missing")
        allowed = en.get("close_call", {}).get("outcome")
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
    """Types of the applications that successful create_application calls recorded, in call order."""
    return [str((c.get("args") or {}).get("type")) for c in calls if c.get("tool") == "create_application" and (c.get("result") or {}).get("ok")]


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


def build_run(meta, cases, reps_rows, history, turns_by_id, slot):
    """The run record. reps_rows: run_cases.run_once rows, one list per repetition; history: the slot's earlier runs."""
    last, n_reps = reps_rows[-1], len(reps_rows)
    rows = []
    for k, c in enumerate(cases):
        passes = sum(rep[k]["pass"] for rep in reps_rows); ok = passes == n_reps
        r = next((rep[k] for rep in reps_rows if not rep[k]["pass"]), last[k])      # the first failing rep is the one shown; else the last
        failed = [] if ok else r["failed"]
        prev, sig = previous_result(history, c["id"]), signature(c)
        slow_s = r.get("slowest_turn_s")
        rows.append({"id": c["id"], "title": c["title"], "family": c["family"], "level": c["level"], "fixture": c.get("fixture", c["id"]),
                     "rules": c.get("rules") or [], "public": "fixture" not in c, "pass": ok, "passes": passes, "runs": n_reps,
                     "failed": failed, "categories": classify(failed),
                     "flags": [f for f, on in (("hung_up", r.get("ended") == "customer-ended-call" and not ok), ("slow", (slow_s or 0) > 10)) if on],
                     "calls": r.get("calls") or [], "forbidden": r.get("forbidden") or [], "slowest_turn_s": slow_s, "ended": r.get("ended"),
                     "turns": turns_by_id.get(c["id"]), "transcript": f"results/bench/{slot}/run-{meta['n']:02d}/{c['id']}.md", "call_id": r.get("call_id"),
                     "flaky": flaky(case_history(history, c["id"]) + [ok], passes, n_reps),
                     "changed": bool(prev and prev.get("sig") and prev["sig"] != sig), "sig": sig, "promised": promised(r.get("calls") or [])})
    def was(cid):
        p = previous_result(history, cid); return None if p is None else p["pass"]
    waits = sorted(r["slowest_turn_s"] for r in rows if r["slowest_turn_s"] is not None)
    med = waits[len(waits) // 2] if waits else 0
    run = {**meta, "slot": slot, "reps": n_reps, "rows": rows,
           "fixed": [r["id"] for r in rows if r["pass"] and was(r["id"]) is False],
           "regressed": [r["id"] for r in rows if not r["pass"] and was(r["id"]) is True],
           "still_failing": [r["id"] for r in rows if not r["pass"] and was(r["id"]) is False],
           "promised_passed": round(sum(r["promised"] for r in rows if r["pass"]), 2),
           "median_slowest_s": med, "worst_slowest_s": waits[-1] if waits else 0, "slow": med > 10,
           "hung_up": sum("hung_up" in r["flags"] for r in rows), "all_pass": all(r["pass"] for r in rows),
           "styles_run": sorted({h["style"] for h in history if h.get("style")} | ({meta["style"]} if meta.get("style") else set()) | {c["style"] for c in cases if c.get("style")})}
    run["cases"] = {r["id"]: {"pass": r["pass"], "sig": r["sig"], "categories": r["categories"]} for r in rows}
    return run


def history_line(run):
    return {k: run[k] for k in ("n", "at", "agent_id", "seconds", "reps", "style", "only", "public", "all_pass", "cases")}


def suggest_next(run, history, minutes_used):
    """What the numbers say about the next run. The builder decides; this lays out the options. `history` ends with `run`."""
    rows, out = run["rows"], []
    failed = [r["id"] for r in rows if not r["pass"]]; fl = [r["id"] for r in rows if r["flaky"]]
    if run["regressed"]: out.append(f"Regressions first: {', '.join(run['regressed'])} passed before and fail now. Fix, then `--only {','.join(run['regressed'])}`.")
    hard = [i for i in failed if i not in fl and i not in run["regressed"]]
    if hard: out.append(f"Failing: {', '.join(hard)}. Read their transcripts, fix, re-run `--only {','.join(hard)}`, then a full run for regressions.")
    if fl: out.append(f"Flaky: {', '.join(fl)} passed in some runs and failed in others. Treat as failing; compare the transcripts of both outcomes; after a fix `--reps 2 --only {','.join(fl)}`.")
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
        if BUDGET_MIN - minutes_used - 3 < est: out.append(f"Time: {minutes_used:.0f} of {BUDGET_MIN} min used; a full run takes ~{est:.0f} min and does not fit with a 3-minute margin. `--only` on a few cases may; otherwise finish.")
        else: out.append(f"Time: {minutes_used:.0f} of {BUDGET_MIN} min used; a full run (~{est:.0f} min; `--reps 2` ~{2 * est:.0f} min) still fits with a 3-minute margin.")
    return out


def call_line(c):
    short = c["tool"].replace("verify_identity", "verify").replace("create_promise", "promise")
    args = c.get("args") or {}
    return short + (" " + json.dumps(args, ensure_ascii=False) if args else "") + ("" if (c.get("result") or {}).get("ok", True) else " ✖")


def write_report(slot, run, history):
    """The analysis report of one run, as markdown. `history` is every run of this slot, oldest first, this run last."""
    rows = run["rows"]; gen = [r for r in rows if not r["public"]]; pub = [r for r in rows if r["public"]]
    L = [f"# Benchmark {slot} · run {run['n']}", "",
         f"agent `{run['agent_id']}` · {run['at']} · {run['seconds']:.0f} s · reps {run['reps']} · style {run['style'] or 'none'}" + (" · `--only`" if run["only"] else ""), "",
         "## Score", "",
         f"- generated {sum(r['pass'] for r in gen)}/{len(gen)}" + (f" · public {sum(r['pass'] for r in pub)}/{len(pub)}" if pub else "") + f" · total {sum(r['pass'] for r in rows)}/{len(rows)}",
         f"- promised on passed cases: {run['promised_passed']:.2f} (the organisers' first tie-breaker)",
         f"- fixed since the previous run: {', '.join(run['fixed']) or 'none'}",
         f"- regressed: {', '.join(run['regressed']) or 'none'}",
         f"- still failing: {', '.join(run['still_failing']) or 'none'}", "",
         "## History", "", "| case | " + " | ".join(f"run {h['n']}" for h in history) + " | |", "|---|" + "---|" * len(history) + "---|"]
    current = {r["id"]: r for r in rows}; ids = list(current)
    for h in history: ids += [cid for cid in h["cases"] if cid not in ids]            # a case that left the file stays visible
    for cid in ids:
        marks = [("✓" if h["cases"][cid]["pass"] else "✗") if cid in h["cases"] else "–" for h in history]
        r = current.get(cid)
        notes = ", ".join(x for x in (("flaky" if r["flaky"] else ""), ("changed" if r["changed"] else "")) if x) if r else ("not in this run" if run["only"] else "removed")
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
          + (" · **the agent was slow in this run; a re-run may score higher**" if run["slow"] else ""), "",
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
    fixtures, openapi = load_fixtures(), load_openapi(a.openapi)
    gen = json.load(open(a.cases, encoding="utf-8"))
    rule_ids = rule_ids_from(a.rules)
    errors, warnings, cov = check_cases(gen, fixtures, openapi, rule_ids)
    print_check(errors, warnings, cov)
    if errors: sys.exit(2)
    write_test_set(a.cases, gen, fixtures)
    cases = [merge_with_fixture(c, fixtures) for c in gen]
    if a.public: cases += [c for c in fixtures.values() if c["brief"] == a.public]
    if a.only: cases = select_only(cases, a.only)
    slot = slot_of(a.cases); out = ROOT / "results" / "bench" / slot; out.mkdir(parents=True, exist_ok=True)
    history = load_history(out / "history.jsonl"); n = len(history) + 1
    ids = run_cases.ensure_personas(cases, a.style)
    reps_rows, total_s, n_reps = [], 0.0, max(1, a.reps)
    for rep in range(n_reps):
        rows, sim_id, it_id, status, took, med = run_cases.run_once(a.agent_id, cases, ids)
        for r, c in zip(rows, cases):
            r["forbidden"] = sorted({t for t in r["tools"] if t in (c.get("forbidden_tools") or [])})
            if r["forbidden"]: r["failed"].append("forbidden tool called: " + ", ".join(r["forbidden"])); r["pass"] = False
            more = applications_failed(c.get("expected") or {}, r.get("calls") or [])
            if more: r["failed"] += more; r["pass"] = False
        reps_rows.append(rows); total_s += took
        if n_reps > 1: print(f"-- rep {rep + 1} of {n_reps}: {sum(r['pass'] for r in rows)} / {len(rows)} passed, {took:.0f} s\n")
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
    meta = {"n": n, "at": time.strftime("%Y-%m-%d %H:%M:%S"), "agent_id": a.agent_id, "seconds": round(time.time() - t0), "style": a.style, "only": bool(a.only),
            "public": a.public, "uncovered_rules": cov.get("uncovered_rules"), "minutes_used": minutes_since_builder_start(),
            "simulation_id": sim_id, "iteration_id": it_id, "status": status}
    turns = {cid: sum(m.get("role") in ("user", "assistant") for m in call.get("messages") or []) for cid, call in calls.items()}
    rec = build_run(meta, cases, reps_rows, history, turns, slot)
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
    ap.add_argument("--openapi", default=str(ROOT / "tools" / "openapi.json"), help="the tool API file to validate against; default tools/openapi.json")
    ap.add_argument("--host", help="base URL of the bank mock that plays the cases (its /v1/practice endpoints), e.g. a tunnel to tools/mock_bank_f.py; default: the organisers' mock")
    a = ap.parse_args()
    if a.host:
        import score; score.HOST = a.host.rstrip("/")
    if a.fixtures: print_fixtures(load_fixtures()); return
    if not a.cases: ap.error("--cases is required")
    if a.check:
        fixtures, gen = load_fixtures(), json.load(open(a.cases, encoding="utf-8"))
        errors, warnings, cov = check_cases(gen, fixtures, load_openapi(a.openapi), rule_ids_from(a.rules))
        print_check(errors, warnings, cov)
        if not errors: print(f"test set: {write_test_set(a.cases, gen, fixtures)}")
        sys.exit(1 if errors else 0)
    if not a.agent_id: ap.error("an agent_id is required to run; use --check to validate only")
    try: run(a)
    except (RuntimeError, urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"Freya or the bank answered with an error: {e}\nThis is usually transient (a 5xx or a timeout): wait a minute and run the same command again. If it repeats, say so in your final line.")


if __name__ == "__main__": main()
