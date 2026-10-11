# Scenario Benchmark and Self-Improvement Loop — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the builder its own test loop: it writes scenarios from the brief, `tools/benchmark.py` runs them on the real Freya simulation and writes an analysis report plus every transcript, the builder reads those, fixes the agent and decides how many runs to make; on practice runs it reviews its own trace with `tools/trace_review.py` and updates the skill's lessons.

**Architecture:** Two new stdlib-only Python tools next to `tools/run_cases.py`, which they reuse (`benchmark.py` imports `run_cases.ensure_personas` and `run_cases.run_once`; nothing in the simulation path is duplicated). Scenarios borrow a practice customer's bank data (`fixture`) because the bank mock plays only its 13 known customers. Pure functions (`check_cases`, `build_run`, `write_report`, `suggest_next`, `transcript_md`, `digest`) carry the logic and are unit-tested; the two network functions (`run`, `main`) are thin. The skill and a template doc tell the builder how to use them.

**Tech Stack:** Python 3.14 (3.10+ required by the kit), standard library + `python-dotenv` (already required), `claude-agent-sdk` 0.2.165 (already installed), `pytest` 9 for the tool tests. Windows, Git Bash / PowerShell; use `python` in commands here (the kit's docs and the skill say `python3`, which also resolves on this machine).

**Spec:** `docs/superpowers/specs/2026-10-10-scenario-benchmark-design.md` — read it first; the plan argues from it.

**No commit steps:** the kit sits inside a git repository rooted at the user's home directory with no usable history, and the user commits when they want. Do not run `git commit`.

## Global Constraints

- Tools and skill are brief-agnostic: no rule, number, date, name, product, queue, outcome value or holiday from any brief goes into `tools/*.py`, `examples/agent_builder.py` or `.claude/skills/build-phone-agent/SKILL.md`. Enum values are read from `tools/openapi.json` at run time, never hard-coded.
- `tools/run_cases.py` keeps its command line and its output format; only the three internal changes of Task 1.
- `freya.py`, the agent model (`AGENT_LLM`) and `public-test-set.json` are not changed.
- Generated cases live only in `tests/<slot>.cases.json` (optionally `tests/<slot>.facts.md`); benchmark results only under `results/bench/<slot>/`; retrospectives and digests under `reports/`.
- Bank data of a generated case (`variables`, `identity`, `products`, `faults`) comes from its fixture; a case that carries them is rejected.
- A full builder run is 30 minutes at most, tests included (hackathon rule). The builder decides the number of runs; the tools print what the builder needs for that decision (minutes used, last run's duration, suggestions).
- The builder edits the skill only on `--self-improve` runs, only the `## Lessons` section, at most 12 lines, general lessons only.
- Every network call goes through `freya.py` or `score.http`, as `run_cases.py` does today. The tools never call the bank mock's `/practice/sessions` with anything but a known case id.
- Run all tool tests with `python -m pytest tools/tests -q` from the kit folder (`C:\Users\loseu\Desktop\build-the-builder`).

## Review Focus

1. A cases file that is a JSON object, or a list with a non-object entry → `--check` reports it in words and exits non-zero, no traceback. (Task 2: `test_check_not_a_list`, `test_check_reports_each_error`.)
2. A simulation run where a case has no `call_id` (the judge never ran, or the call failed to start) → the run still writes the report, the history line and a transcript file that says "no transcript". (Task 3: `test_transcript_md_without_call`, `test_build_run_without_call_id`.)
3. A trace that is still being written (partial last line) or an old trace without `t` and without thinking text → `trace_review.py` digests what is there and says `elapsed n/a`. (Task 5: `test_digest_on_synthetic_trace`, `test_digest_on_real_old_trace`.)
4. A `--rules` file with no numbered lines, or with a list that restarts its numbering → ids deduplicated, a warning printed for a file that yields no rule. (Task 2: `test_extract_rules`; Task 4: `test_rule_ids_from_warns`.)
5. `--only` naming an id that is not in the run → stop with a message naming it, not an empty simulation that burns five minutes. (Task 4: `test_select_only`.)

---

## File structure

| File | Responsibility |
|---|---|
| `tools/run_cases.py` (modify) | Simulation runner, unchanged CLI. Gains `ensure_personas()`, fixture sessions, `calls` in rows. |
| `tools/benchmark.py` (create) | Case validation, fixture listing, rule coverage, running cases through `run_cases`, artefacts, report, suggestions. |
| `tools/trace_review.py` (create) | Digest of a builder trace for the retrospective. |
| `tools/tests/test_run_cases.py`, `test_benchmark.py`, `test_trace_review.py`, `test_agent_builder.py` (create) | pytest unit tests of the pure functions. |
| `examples/agent_builder.py` (modify) | Thinking summaries in the trace, timestamps per line, `--self-improve`, `max_turns`. |
| `docs/test-case-template.md` (create) | How the builder writes `tests/<slot>.cases.json` and `tests/<slot>.facts.md`. |
| `.claude/skills/build-phone-agent/SKILL.md` (rewrite) | The builder's process with the new steps and sections. |
| `README.md` (modify) | Three table rows and two lines in the ten-minute start. |

---

### Task 1: `run_cases.py` — personas as a function, fixture sessions, calls in rows

**Files:**
- Modify: `tools/run_cases.py` (lines 49–62 `main()` persona block; line 86 sessions; line 98 rows)
- Create: `tools/tests/__init__.py` (empty) and `tools/tests/test_run_cases.py`

**Interfaces:**
- Consumes: `freya.create_personas(list) -> {"personas": [{"id": ...}]}`, `persona_for(case, ident, style)` (existing).
- Produces: `ensure_personas(cases, style=None, store=ROOT / ".personas.json") -> dict[case_id, persona_id]`; `run_once(agent_id, cases, ids)` rows now carry `"calls": led["calls"]` (each call: `{"n", "tool", "args", "status", "result"}`); sessions open on `c.get("fixture", c["id"])`.

- [ ] **Step 1: Write the failing test**

Create `tools/tests/__init__.py` (empty) and `tools/tests/test_run_cases.py`:

```python
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import run_cases

CASE = {"id": "T-01", "title": "t", "brief": "A", "family": "Happy path", "level": "easy", "script": "s", "checks": ["c"],
        "variables": {"first_name": "A", "last_name": "B", "title": "Mr", "now": "2026-10-14T11:00"},
        "identity": {"date_of_birth": "1990-01-01", "phone_last4": "1234"}}


def test_ensure_personas_creates_once_then_caches(tmp_path, monkeypatch):
    calls = []
    def fake_create(personas):
        calls.append(personas)
        return {"personas": [{"id": f"pid-{len(calls)}-{i}"} for i, _ in enumerate(personas)]}
    monkeypatch.setattr(run_cases.freya, "create_personas", fake_create)
    store = tmp_path / "personas.json"
    assert run_cases.ensure_personas([CASE], None, store) == {"T-01": "pid-1-0"}
    assert run_cases.ensure_personas([CASE], None, store) == {"T-01": "pid-1-0"}      # same text: cached, not created again
    assert len(calls) == 1
    assert run_cases.ensure_personas([CASE], "pieces", store) == {"T-01": "pid-2-0"}  # a style changes the text: new persona
    assert len(calls) == 2
    assert len(json.load(open(store))) == 2
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest tools/tests/test_run_cases.py -q`
Expected: FAIL with `AttributeError: module 'run_cases' has no attribute 'ensure_personas'`.

- [ ] **Step 3: Add `ensure_personas` and use it in `main()`**

In `tools/run_cases.py`, after `persona_for` (after line 47) add:

```python
def ensure_personas(cases, style=None, store=ROOT / ".personas.json"):
    """One persona per case, created on first use and cached in `store`. Returns {case_id: persona_id}.
    A persona is recreated whenever its text changes, so an edited case never runs with a stale customer."""
    ident = {c["id"]: {"identity": c["identity"]} for c in cases}
    store = pathlib.Path(store); ids = json.load(open(store)) if store.exists() else {}
    spec = {c["id"]: persona_for(c, ident[c["id"]], style) for c in cases}
    key = {i: i + ":" + hashlib.sha1(json.dumps(p, sort_keys=True).encode()).hexdigest()[:10] for i, p in spec.items()}
    new = [c for c in cases if key[c["id"]] not in ids]
    if new:
        made = freya.create_personas([spec[c["id"]] for c in new])["personas"]
        ids.update({key[c["id"]]: p["id"] for c, p in zip(new, made)}); json.dump(ids, open(store, "w"), indent=1)
    return {c["id"]: ids[key[c["id"]]] for c in cases}
```

In `main()` replace the block from `    ident = {c["id"]: {"identity": c["identity"]} for c in cases}` down to and including `    ids = {c["id"]: ids[key[c["id"]]] for c in cases}` with one line:

```python
    ids = ensure_personas(cases, a.style)
```

- [ ] **Step 4: Fixture sessions and calls in rows**

In `run_once`, change the sessions line to:

```python
    # a generated case borrows a practice customer's bank data through `fixture` (tools/benchmark.py); a public case is its own fixture
    sessions = {c["id"]: http("/v1/practice/sessions", {"case": c.get("fixture", c["id"])})["variables"] for c in cases}
```

and in the `rows.append({...})` call add `"calls": led["calls"],` after `"tools": [x["tool"] for x in led["calls"]],`.

- [ ] **Step 5: Run the test and a syntax check**

Run: `python -m pytest tools/tests/test_run_cases.py -q && python -c "import ast; ast.parse(open('tools/run_cases.py').read()); print('ok')"`
Expected: `1 passed`, `ok`. Also `python tools/run_cases.py --help` prints the usage (argparse still intact).

---

### Task 2: `benchmark.py` part 1 — fixtures, tool API enums, rule extraction, `--check`

**Files:**
- Create: `tools/benchmark.py`
- Create: `tools/tests/test_benchmark.py`

**Interfaces:**
- Consumes: `run_cases.STYLES`; `public-test-set.json`; `tools/openapi.json`.
- Produces (used by Tasks 3–4 and the skill): `load_fixtures(path) -> dict[id, case]`, `load_openapi(path) -> dict`, `tool_names(openapi) -> list[str]`, `enums(openapi) -> {tool: {field: [values]}}`, `extract_rules(path) -> list[str]` (ids `<stem>:<N>`), `product_ids(fixture) -> ["p1", ...]`, `check_cases(cases, fixtures, openapi, rule_ids=None) -> (errors, warnings, coverage)`, `print_fixtures(fixtures)`, `print_check(errors, warnings, coverage)`.

- [ ] **Step 1: Write the failing tests**

Create `tools/tests/test_benchmark.py`:

```python
import copy, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import benchmark as B

GOOD = {"id": "GEN-01", "fixture": "PUB-06", "title": "Accepts the floor", "family": "Amounts", "level": "hard", "rules": ["brief-a:26"],
        "script": "Verified. Says the full amount is too much. Accepts the minimum payment today and confirms.",
        "expected": {"outcome": "promise", "reason": None, "promises": [{"product_id": "p1", "amount": 637.5, "date": "2026-10-14"}],
                     "notes": [], "callbacks": [], "transfers": []},
        "checks": ["the floor is offered once"]}


def test_fixtures_and_product_ids():
    fx = B.load_fixtures()
    assert len(fx) == 13 and B.product_ids(fx["PUB-13"]) == ["p1", "p2"] and B.product_ids(fx["PUB-01"]) == ["p1"]


def test_enums_and_tool_names():
    api = B.load_openapi()
    assert B.tool_names(api) == ["verify_identity", "get_account", "create_promise", "add_note", "schedule_callback", "transfer_to_agent", "close_call"]
    assert "promise" in B.enums(api)["close_call"]["outcome"] and "refused" in B.enums(api)["add_note"]["reason"]


def test_extract_rules(tmp_path):
    a = B.extract_rules(ROOT / "briefs" / "brief-a.md")
    assert len(a) == 47 and a[0] == "brief-a:1" and a[-1] == "brief-a:47"
    assert len(B.extract_rules(ROOT / "briefs" / "brief-b.md")) == 11
    f = tmp_path / "memo.md"; f.write_text("no numbers here\n1. one\n2. two\n1. one again\n", encoding="utf-8")
    assert B.extract_rules(f) == ["memo:1", "memo:2"]
    g = tmp_path / "empty.md"; g.write_text("# nothing\n", encoding="utf-8")
    assert B.extract_rules(g) == []


def test_check_good_case_passes():
    errors, warnings, cov = B.check_cases([GOOD], B.load_fixtures(), B.load_openapi())
    assert errors == [] and warnings == []
    assert cov["cases"] == 1 and cov["by_fixture"] == {"PUB-06": 1} and cov["by_outcome"] == {"promise": 1} and cov["styles"] == []


def test_check_reports_each_error():
    bad = [dict(GOOD, id="GEN-01", fixture="PUB-99"),
           dict(GOOD, id="GEN-01", products=[], level="hot", style="shouty", rules=[], forbidden_tools=["pay"],
                expected={"outcome": "wrong", "reason": None,
                          "promises": [{"product_id": "p9", "amount": "x", "date": "14/10/2026"}],
                          "notes": [{"product_id": "p1", "reason": "bored"}],
                          "callbacks": [{"date": "2026-10-15", "time": "11"}], "transfers": [{"queue": "vip"}]}),
           "not an object"]
    errors, _, _ = B.check_cases(bad, B.load_fixtures(), B.load_openapi())
    text = "\n".join(errors)
    for needle in ["unknown fixture 'PUB-99'", "duplicate id", "`products` is bank data", "level must be", "unknown style 'shouty'",
                   "rules must be", "names a tool the API does not have: pay", "expected.outcome 'wrong'", "product_id 'p9'",
                   "amount must be a number", "must be YYYY-MM-DD", "note reason 'bored'", "must be HH:MM", "transfer queue 'vip'",
                   "every case must be a JSON object"]:
        assert needle in text, needle


def test_check_not_a_list():
    assert B.check_cases({"id": "x"}, {}, B.load_openapi())[0] == ["the cases file must be a JSON list"]


def test_check_warns_on_missing_reason():
    c = dict(GOOD, expected=dict(GOOD["expected"], outcome="no_promise", reason=None, promises=[]))
    errors, warnings, _ = B.check_cases([c], B.load_fixtures(), B.load_openapi())
    assert errors == [] and any("reason is empty" in w for w in warnings)


def test_rule_coverage():
    rules = ["brief-a:1", "brief-a:2", "brief-a:26"]
    errors, _, cov = B.check_cases([GOOD], B.load_fixtures(), B.load_openapi(), rules)
    assert errors == [] and cov["uncovered_rules"] == ["brief-a:1", "brief-a:2"]
    errors, _, _ = B.check_cases([dict(GOOD, rules=["brief-a:99"])], B.load_fixtures(), B.load_openapi(), rules)
    assert any("brief-a:99 is cited but exists in no --rules file" in e for e in errors)


def test_identity_fields_must_match_tool_api():
    api = copy.deepcopy(B.load_openapi())
    api["paths"]["/verify_identity"]["post"]["requestBody"]["content"]["application/json"]["schema"]["properties"]["field"]["enum"] = ["postcode", "birth_year"]
    errors, _, _ = B.check_cases([GOOD], B.load_fixtures(), api)
    assert any("cannot be played on the mock" in e for e in errors)
```

- [ ] **Step 2: Run them to verify they fail**

Run: `python -m pytest tools/tests/test_benchmark.py -q`
Expected: `ModuleNotFoundError: No module named 'benchmark'`.

- [ ] **Step 3: Create `tools/benchmark.py` with part 1**

```python
"""Benchmark a phone agent on the scenarios the builder wrote. Same simulation, judge and ledger scoring as run_cases.py.

    python3 tools/benchmark.py --fixtures
    python3 tools/benchmark.py --check --cases tests/<slot>.cases.json [--rules briefs/brief-a.md] [--rules tests/<slot>.facts.md]
    python3 tools/benchmark.py <agent_id> --cases tests/<slot>.cases.json [--rules FILE ...] [--public A|B] [--only ID,ID] [--reps N] [--style S]

A generated case borrows the bank data of one practice customer, its `fixture`: identity answers, products, `now` and the
injected fault. The script, the expected records and the checks are the case's own. Format: docs/test-case-template.md.
Results go to results/bench/<slot>/: history.jsonl, run-NN.json, run-NN.md (latest.md is a copy), run-NN/<case>.md and
run-NN.transcripts.md with every conversation, passed cases too.
"""
import argparse, collections, datetime, hashlib, json, pathlib, re, shutil, sys, time
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "tools"))
import freya
import run_cases
from run_cases import STYLES

BANK_FIELDS = ("variables", "identity", "products", "faults")        # come from the fixture, never from a generated case
REQUIRED = ("id", "fixture", "title", "family", "level", "rules", "script", "expected", "checks")
OPTIONAL = ("brief", "style", "third_party", "forbidden_tools")
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
    en, tools = enums(openapi), tool_names(openapi)
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
        if exp.get("outcome") not in ("promise", "paid") and not exp.get("reason"):
            warnings.append(f"{cid}: expected.reason is empty for outcome {exp.get('outcome')!r}; the tool API wants a reason for it")
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
        fields = en.get("verify_identity", {}).get("field")
        if fx and fields:
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
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest tools/tests/test_benchmark.py -q`
Expected: `9 passed`.

- [ ] **Step 5: Try the fixtures listing by hand**

Temporarily append to the file (Task 4 replaces this with the real `main`):

```python
if __name__ == "__main__":
    print_fixtures(load_fixtures())
```

Run: `python tools/benchmark.py`
Expected: 13 blocks; `PUB-10` shows `faults: create_promise fails on the first 1 call(s)`; `PUB-13` shows `p1` and `p2`.

---

### Task 3: `benchmark.py` part 2 — pure analysis: classify, signature, merge, transcripts, history, run record, report, suggestions

**Files:**
- Modify: `tools/benchmark.py` (append below `print_check`)
- Modify: `tools/tests/test_benchmark.py` (append tests)

**Interfaces:**
- Consumes: rows from `run_cases.run_once` (`id, pass, failed, tools, calls, call_id, slowest_turn_s, ended`), calls from `freya.get_call` (`messages[]` with `role`, `message`).
- Produces: `classify(reasons) -> list[str]`, `signature(case) -> str`, `merge_with_fixture(case, fixtures) -> dict`, `promised(calls) -> float`, `transcript_md(case, row, call) -> str`, `flaky(hist, passes=None, runs=1) -> bool`, `load_history(path) -> list`, `previous_result(history, cid) -> dict|None`, `case_history(history, cid) -> list[bool]`, `build_run(meta, cases, reps_rows, history, turns_by_id, slot) -> run`, `history_line(run) -> dict`, `suggest_next(run, history, minutes_used) -> list[str]`, `write_report(slot, run, history) -> str`.
- The **run record** `run` has: `n, at, agent_id, seconds, style, only, public, uncovered_rules, minutes_used, slot, reps, rows, fixed, regressed, still_failing, promised_passed, median_slowest_s, worst_slowest_s, slow, hung_up, all_pass, styles_run, cases`. A **row** has: `id, title, family, level, fixture, rules, public, pass, passes, runs, failed, categories, flags, calls, forbidden, slowest_turn_s, ended, turns, transcript, call_id, flaky, changed, sig, promised`.
- `history` passed to `write_report`/`suggest_next` is every run of the slot oldest first **with the current run last**; `history` passed to `build_run` is the earlier runs only.

- [ ] **Step 1: Write the failing tests**

Append to `tools/tests/test_benchmark.py`:

```python
def case(cid, fixture="PUB-01", **kw):
    c = {"id": cid, "fixture": fixture, "title": "t " + cid, "family": "Happy path", "level": "easy", "rules": ["brief-a:1"], "script": "s",
         "expected": {"outcome": "promise", "reason": None, "promises": [{"product_id": "p1", "amount": 420.0, "date": "2026-10-14"}],
                      "notes": [], "callbacks": [], "transfers": []}, "checks": ["c"]}
    c.update(kw); return c


PROMISE = {"n": 1, "tool": "create_promise", "args": {"product_id": "p1", "amount": 420.0, "date": "2026-10-14"}, "status": 200, "result": {"ok": True}}
FAILED_PROMISE = {"n": 1, "tool": "create_promise", "args": {"product_id": "p1", "amount": 420.0, "date": "2026-10-14"}, "status": 503, "result": {"ok": False, "error": "service unavailable"}}
CLOSE = {"n": 2, "tool": "close_call", "args": {"outcome": "promise"}, "status": 200, "result": {"ok": True}}


def row(cid, ok, failed=(), calls=(), ended="assistant-ended-call", slow=5.0, call_id="call-1"):
    return {"id": cid, "pass": ok, "failed": list(failed), "tools": [c["tool"] for c in calls], "calls": list(calls),
            "call_id": call_id, "slowest_turn_s": slow, "ended": ended}


def hist(n, results):
    """One history line. results: {cid: (pass, sig)}"""
    return {"n": n, "at": "", "agent_id": "a", "seconds": 100, "style": None, "only": False, "public": None,
            "all_pass": all(p for p, _ in results.values()), "cases": {cid: {"pass": p, "sig": s, "categories": []} for cid, (p, s) in results.items()}}


def test_classify():
    assert B.classify(["outcome ('no_promise', 'x'), expected ('promise', None)"]) == ["outcome"]
    assert B.classify(["get_account called before identity was verified", "conversation: said collections"]) == ["before_identity", "conversation"]
    assert B.classify(["the call was not closed with close_call", "forbidden tool called: transfer_to_agent"]) == ["forbidden_tool", "not_closed"]
    assert B.classify(["something new"]) == ["other"] and B.classify([]) == []


def test_merge_with_fixture_and_promised():
    fx = B.load_fixtures()
    m = B.merge_with_fixture(case("GEN-01", fixture="PUB-13"), fx)
    assert m["identity"] == fx["PUB-13"]["identity"] and m["products"] == fx["PUB-13"]["products"] and m["brief"] == "B" and m["id"] == "GEN-01"
    assert B.promised([PROMISE, FAILED_PROMISE, CLOSE]) == 420.0


def test_signature_changes_with_expectation():
    a, b = case("GEN-01"), case("GEN-01")
    b["expected"]["promises"][0]["amount"] = 1.0
    assert B.signature(a) != B.signature(b) and B.signature(a) == B.signature(case("GEN-01", title="other title"))


def test_flaky():
    assert B.flaky([True, False, True]) and B.flaky([False, True, False])
    assert not B.flaky([False, True]) and not B.flaky([True, False]) and not B.flaky([False, True, True]) and not B.flaky([True, True, True])
    assert B.flaky([True], passes=1, runs=2) and not B.flaky([True], passes=2, runs=2)


def test_build_run_fixed_regressed_flaky_changed():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i), fx) for i in ("GEN-01", "GEN-02", "GEN-03", "GEN-04")]
    sig = {c["id"]: B.signature(c) for c in cases}
    history = [hist(1, {"GEN-01": (False, sig["GEN-01"]), "GEN-02": (True, "oldsig"), "GEN-03": (True, sig["GEN-03"]), "GEN-04": (True, sig["GEN-04"])}),
               hist(2, {"GEN-01": (False, sig["GEN-01"]), "GEN-02": (True, "oldsig"), "GEN-03": (True, sig["GEN-03"]), "GEN-04": (False, sig["GEN-04"])})]
    rows = [row("GEN-01", True, calls=[PROMISE, CLOSE]),
            row("GEN-02", False, ["outcome x"], ended="customer-ended-call", slow=12.0),
            row("GEN-03", False, ["promises y"]),
            row("GEN-04", True, calls=[PROMISE, CLOSE])]
    meta = {"n": 3, "at": "now", "agent_id": "a", "seconds": 200, "style": None, "only": False, "public": None, "uncovered_rules": ["brief-a:2"], "minutes_used": 12.0}
    run = B.build_run(meta, cases, [rows], history, {"GEN-01": 8}, "slot")
    assert run["fixed"] == ["GEN-01", "GEN-04"] and run["regressed"] == ["GEN-02", "GEN-03"] and run["still_failing"] == []
    r = {x["id"]: x for x in run["rows"]}
    assert r["GEN-02"]["changed"] is True and r["GEN-03"]["changed"] is False
    assert r["GEN-04"]["flaky"] is True and r["GEN-01"]["flaky"] is False and r["GEN-02"]["flaky"] is False
    assert r["GEN-02"]["flags"] == ["hung_up", "slow"] and r["GEN-01"]["flags"] == []
    assert run["promised_passed"] == 840.0 and r["GEN-01"]["turns"] == 8 and r["GEN-02"]["turns"] is None
    assert r["GEN-01"]["transcript"] == "results/bench/slot/run-03/GEN-01.md"
    assert run["median_slowest_s"] == 5.0 and run["worst_slowest_s"] == 12.0 and run["slow"] is False and run["hung_up"] == 1
    assert run["cases"]["GEN-02"] == {"pass": False, "sig": sig["GEN-02"], "categories": ["outcome"]}
    line = B.history_line(run)
    assert set(line) == {"n", "at", "agent_id", "seconds", "style", "only", "public", "all_pass", "cases"} and line["all_pass"] is False


def test_build_run_reps_disagree():
    fx = B.load_fixtures(); cases = [B.merge_with_fixture(case("GEN-01"), fx)]
    good, bad = row("GEN-01", True, calls=[PROMISE, CLOSE]), row("GEN-01", False, ["outcome z"])
    run = B.build_run({"n": 1, "at": "", "agent_id": "a", "seconds": 1, "style": None, "only": False, "public": None, "uncovered_rules": None, "minutes_used": None},
                      cases, [bad, good], [], {}, "slot")
    r = run["rows"][0]
    assert r["pass"] is False and r["passes"] == 1 and r["runs"] == 2 and r["flaky"] is True and r["failed"] == ["outcome z"]


def test_build_run_without_call_id():
    fx = B.load_fixtures(); cases = [B.merge_with_fixture(case("GEN-01"), fx)]
    run = B.build_run({"n": 1, "at": "", "agent_id": "a", "seconds": 1, "style": None, "only": False, "public": None, "uncovered_rules": None, "minutes_used": None},
                      cases, [[row("GEN-01", False, ["conversation: no verdict"], call_id=None, slow=None)]], [], {}, "slot")
    r = run["rows"][0]
    assert r["call_id"] is None and r["flags"] == [] and run["median_slowest_s"] == 0


def test_transcript_md_and_without_call():
    c = case("GEN-01"); r = row("GEN-01", False, ["outcome x"], calls=[PROMISE], slow=4.2)
    call = {"messages": [
        {"role": "assistant", "message": "Hello, this is Freya Bank."},
        {"role": "system", "message": json.dumps({"event": "node_enter", "node": "identity", "from_node": "start", "reason": "first"})},
        {"role": "user", "message": "Yes, speaking."},
        {"role": "system", "message": json.dumps({"event": "function_call_start", "function": "create_promise", "args": {"body": {"amount": 420}}})},
        {"role": "system", "message": json.dumps({"event": "function_call_complete", "function": "create_promise", "result": {"ok": True}})},
        {"role": "system", "message": json.dumps({"event": "route_evaluated", "matched": True, "from_node": "promise", "target": "close", "reason": "tool ok"})},
        {"role": "system", "message": json.dumps({"event": "route_evaluated", "matched": False, "from_node": "promise", "target": "retry", "reason": "no"})},
        {"role": "system", "message": "not json"}]}
    md = B.transcript_md(c, r, call)
    assert md.startswith("## GEN-01 — t GEN-01\nresult: FAIL: outcome x\n")
    assert "**agent:** Hello, this is Freya Bank." in md and "**customer:** Yes, speaking." in md
    assert "→ node identity (from start: first)" in md and '⚙ create_promise {"body": {"amount": 420}}' in md and '⚙ create_promise → {"ok": true}' in md
    assert "↪ promise → close: tool ok" in md and "retry" not in md and "turns 2" in md
    assert "(no transcript)" in B.transcript_md(c, r, {})


def test_write_report_and_suggestions():
    fx = B.load_fixtures()
    cases = [B.merge_with_fixture(case(i), fx) for i in ("GEN-01", "GEN-02")]
    sig = {c["id"]: B.signature(c) for c in cases}
    history = [hist(1, {"GEN-01": (True, sig["GEN-01"]), "GEN-02": (True, sig["GEN-02"])}), hist(2, {"GEN-01": (True, sig["GEN-01"]), "GEN-02": (False, sig["GEN-02"])})]
    rows = [row("GEN-01", True, calls=[PROMISE, CLOSE]), row("GEN-02", True, calls=[PROMISE, CLOSE])]
    meta = {"n": 3, "at": "now", "agent_id": "agent-x", "seconds": 300, "style": None, "only": False, "public": None, "uncovered_rules": ["brief-a:7"], "minutes_used": 20.0}
    run = B.build_run(meta, cases, [rows], history, {}, "slot")
    full = history + [B.history_line(run)]
    text = B.write_report("slot", run, full)
    for needle in ["# Benchmark slot · run 3", "generated 2/2 · total 2/2", "promised on passed cases: 840.00", "fixed since the previous run: GEN-02",
                   "| GEN-02 | ✓ | ✗ | ✓ | flaky |", "rules cited by no case: brief-a:7", "## Passed cases", "- GEN-01 t GEN-01", "## What this run suggests"]:
        assert needle in text, needle
    s = "\n".join(B.suggest_next(run, full, 20.0))
    assert "Flaky: GEN-02" in s and "Everything passed once" in s and "a full run (~5 min) still fits" in s
    # two full passes in a row, little time left
    full2 = [hist(1, {"GEN-01": (True, sig["GEN-01"]), "GEN-02": (True, sig["GEN-02"])}), B.history_line(run)]
    s2 = "\n".join(B.suggest_next(run, full2, 27.0))
    assert "2 full runs in a row" in s2 and "does not fit" in s2
    # failures and regressions
    rows3 = [row("GEN-01", False, ["outcome q"]), row("GEN-02", True, calls=[PROMISE, CLOSE])]
    run3 = B.build_run(dict(meta, n=4), cases, [rows3], full, {}, "slot")
    s3 = "\n".join(B.suggest_next(run3, full + [B.history_line(run3)], None))
    assert "Regressions first: GEN-01" in s3 and "--only GEN-01" in s3 and "Time:" not in s3
    text3 = B.write_report("slot", run3, full + [B.history_line(run3)])
    assert "### GEN-01 — t GEN-01" in text3 and "regressed: GEN-01" in text3
```

- [ ] **Step 2: Run them to verify they fail**

Run: `python -m pytest tools/tests/test_benchmark.py -q`
Expected: the new tests fail with `AttributeError: module 'benchmark' has no attribute 'classify'` (and similar); the 9 earlier ones pass.

- [ ] **Step 3: Append part 2 to `tools/benchmark.py`**

Remove the temporary `if __name__ == "__main__":` block from Task 2, then append:

```python
CATEGORIES = [("outcome ", "outcome"), ("promises ", "promises"), ("notes ", "notes"), ("callbacks ", "callbacks"), ("transfers ", "transfers"),
              ("not closed with close_call", "not_closed"), ("called before identity was verified", "before_identity"),
              ("although the customer was not on the line", "tools_while_unreached"), ("forbidden tool", "forbidden_tool"), ("conversation:", "conversation")]


def classify(reasons):
    """Failure categories of one case, from the scorer's and the judge's reasons."""
    cats = {cat for r in reasons for needle, cat in CATEGORIES if needle in r}
    return sorted(cats or ({"other"} if reasons else set()))


def signature(case):
    """Changes when the case's script, expectation or checks change, so a weakened test shows up in the report."""
    return hashlib.sha1(json.dumps([case.get("script"), case.get("expected"), case.get("checks")], sort_keys=True).encode()).hexdigest()[:10]


def merge_with_fixture(case, fixtures):
    """A generated case plus its fixture's bank data: what run_cases needs to play it."""
    fx = fixtures[case["fixture"]]
    out = {k: fx[k] for k in BANK_FIELDS if k in fx}
    out.update(case); out.setdefault("brief", fx["brief"])
    return out


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
            try: ev = json.loads(msg)
            except (TypeError, ValueError): continue
            e = ev.get("event")
            if e == "node_enter": L.append(f"    → node {ev.get('node')} (from {ev.get('from_node')}: {ev.get('reason')})")
            elif e == "function_call_start": L.append(f"    ⚙ {ev.get('function')} {json.dumps(ev.get('args'), ensure_ascii=False)[:500]}")
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
        r = last[k]; passes = sum(rep[k]["pass"] for rep in reps_rows); ok = passes == n_reps
        failed = next((rep[k]["failed"] for rep in reps_rows if not rep[k]["pass"]), [])
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
    return {k: run[k] for k in ("n", "at", "agent_id", "seconds", "style", "only", "public", "all_pass", "cases")}


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
        streak = 1
        for h in reversed(history[:-1]):
            if h.get("only") or not h.get("all_pass"): break
            streak += 1
        if streak == 1: out.append("Everything passed once. One pass is a hint, not proof: run again (`--reps 2`, or a `--style` run) if the clock allows.")
        else: out.append(f"Everything passed in {streak} full runs in a row. Stop unless a transcript-review finding is open.")
    unused = [s for s in sorted(STYLES) if s not in run["styles_run"]]
    if unused: out.append("Styles not run yet: " + ", ".join(unused) + ". Final customers talk like people; a `--style` run shows whether the agent copes.")
    if minutes_used is not None:
        need = run["seconds"] / 60
        if BUDGET_MIN - minutes_used < need: out.append(f"Time: {minutes_used:.0f} of {BUDGET_MIN} min used; a full run took {need:.0f} min and does not fit. `--only` on a few cases may; otherwise finish.")
        else: out.append(f"Time: {minutes_used:.0f} of {BUDGET_MIN} min used; a full run (~{need:.0f} min) still fits.")
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
    for r in rows:
        marks = [("✓" if h["cases"][r["id"]]["pass"] else "✗") if r["id"] in h["cases"] else "–" for h in history]
        notes = ", ".join(x for x in (("flaky" if r["flaky"] else ""), ("changed" if r["changed"] else "")) if x)
        L.append(f"| {r['id']} | " + " | ".join(marks) + f" | {notes} |")
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
```

- [ ] **Step 4: Run the tests**

Run: `python -m pytest tools/tests/test_benchmark.py -q`
Expected: `18 passed`. If `test_write_report_and_suggestions` fails on the `| GEN-02 | ✓ | ✗ | ✓ | flaky |` line, check that `history_line(run)` was appended to the history before calling `write_report` (the table has one column per history entry, this run included).

---

### Task 4: `benchmark.py` part 3 — the run command and `main`, then one real run

**Files:**
- Modify: `tools/benchmark.py` (append)
- Modify: `tools/tests/test_benchmark.py` (append)
- Create (temporary, deleted at the end of the task): `tests/_verify.cases.json`

**Interfaces:**
- Consumes: `run_cases.ensure_personas`, `run_cases.run_once`, `freya.get_call`, everything from Tasks 2–3.
- Produces: `slot_of(cases_path) -> str`, `select_only(cases, only) -> list` (raises `SystemExit` with a message for unknown ids), `rule_ids_from(files) -> list|None` (prints a warning for a file without numbered lines), `minutes_since_builder_start() -> float|None`, `run(args)`, `main()`.

- [ ] **Step 1: Write the failing tests**

Append to `tools/tests/test_benchmark.py`:

```python
import pytest


def test_slot_of():
    assert B.slot_of("tests/brief-a.cases.json") == "brief-a" and B.slot_of("tests\\final-1.cases.json") == "final-1" and B.slot_of("x.json") == "x"


def test_select_only():
    cases = [case("GEN-01"), case("GEN-02")]
    assert [c["id"] for c in B.select_only(cases, "GEN-02")] == ["GEN-02"]
    with pytest.raises(SystemExit) as e: B.select_only(cases, "GEN-02,GEN-09")
    assert "GEN-09" in str(e.value)


def test_rule_ids_from_warns(tmp_path, capsys):
    f = tmp_path / "memo.md"; f.write_text("nothing numbered\n", encoding="utf-8")
    assert B.rule_ids_from([str(ROOT / "briefs" / "brief-b.md"), str(f)]) == [f"brief-b:{i}" for i in range(1, 12)]
    assert "no numbered rules found in" in capsys.readouterr().out
    assert B.rule_ids_from([]) is None


def test_minutes_since_builder_start(tmp_path, monkeypatch):
    monkeypatch.setattr(B, "ROOT", tmp_path)
    assert B.minutes_since_builder_start() is None
    (tmp_path / "traces").mkdir()
    import datetime as dt
    start = (dt.datetime.now().astimezone() - dt.timedelta(minutes=7)).strftime("%Y-%m-%dT%H:%M:%S%z")
    (tmp_path / "traces" / "t.jsonl").write_text(json.dumps({"start": start}) + "\n", encoding="utf-8")
    assert 6.9 < B.minutes_since_builder_start() < 7.5
```

- [ ] **Step 2: Run them to verify they fail**

Run: `python -m pytest tools/tests/test_benchmark.py -q`
Expected: the four new tests fail with `AttributeError`.

- [ ] **Step 3: Append part 3 to `tools/benchmark.py`**

```python
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
    try:
        first = json.loads(traces[-1].read_text(encoding="utf-8").splitlines()[0])
        start = datetime.datetime.strptime(first["start"], "%Y-%m-%dT%H:%M:%S%z")
        return (datetime.datetime.now(start.tzinfo) - start).total_seconds() / 60
    except (OSError, ValueError, KeyError, IndexError): return None


def run(a):
    fixtures, openapi = load_fixtures(), load_openapi()
    gen = json.load(open(a.cases, encoding="utf-8"))
    rule_ids = rule_ids_from(a.rules)
    errors, warnings, cov = check_cases(gen, fixtures, openapi, rule_ids)
    print_check(errors, warnings, cov)
    if errors: sys.exit(2)
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
        reps_rows.append(rows); total_s += took
        if n_reps > 1: print(f"-- rep {rep + 1} of {n_reps}: {sum(r['pass'] for r in rows)} / {len(rows)} passed, {took:.0f} s\n")
    calls = {}                                                      # transcripts of the last repetition, passed cases too
    for r, c in zip(reps_rows[-1], cases):
        if r.get("call_id"):
            try: calls[c["id"]] = freya.get_call(r["call_id"])
            except Exception as e: print(f"transcript of {c['id']} not fetched: {e}")
    meta = {"n": n, "at": time.strftime("%Y-%m-%d %H:%M:%S"), "agent_id": a.agent_id, "seconds": round(total_s), "style": a.style, "only": bool(a.only),
            "public": a.public, "uncovered_rules": cov.get("uncovered_rules"), "minutes_used": minutes_since_builder_start(),
            "simulation_id": sim_id, "iteration_id": it_id, "status": status}
    turns = {cid: sum(m.get("role") in ("user", "assistant") for m in call.get("messages") or []) for cid, call in calls.items()}
    rec = build_run(meta, cases, reps_rows, history, turns, slot)
    (out / f"run-{n:02d}").mkdir(exist_ok=True)
    bundle = [f"# Transcripts · {slot} · run {n}", ""]
    for r, c in sorted(zip(rec["rows"], cases), key=lambda rc: rc[0]["pass"]):       # failed cases first
        md = transcript_md(c, r, calls.get(c["id"], {}))
        (out / f"run-{n:02d}" / f"{c['id']}.md").write_text(md, encoding="utf-8"); bundle.append(md)
    (out / f"run-{n:02d}.transcripts.md").write_text("\n".join(bundle), encoding="utf-8")
    (out / f"run-{n:02d}.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False), encoding="utf-8")
    history.append(history_line(rec))
    with open(out / "history.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(history[-1]) + "\n")
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
    a = ap.parse_args()
    if a.fixtures: print_fixtures(load_fixtures()); return
    if not a.cases: ap.error("--cases is required")
    if a.check:
        errors, warnings, cov = check_cases(json.load(open(a.cases, encoding="utf-8")), load_fixtures(), load_openapi(), rule_ids_from(a.rules))
        print_check(errors, warnings, cov); sys.exit(1 if errors else 0)
    if not a.agent_id: ap.error("an agent_id is required to run; use --check to validate only")
    run(a)


if __name__ == "__main__": main()
```

- [ ] **Step 4: Run all tool tests**

Run: `python -m pytest tools/tests -q`
Expected: all pass (`test_run_cases` 1, `test_benchmark` 22).

- [ ] **Step 5: `--fixtures` and `--check` by hand**

Run: `python tools/benchmark.py --fixtures | head -8` → the PUB-01 block.

Create `tests/_verify.cases.json` (the folder `tests/` does not exist yet; create it):

```json
[
  {
    "id": "GEN-01", "fixture": "PUB-01", "title": "Pays the full amount this Friday", "family": "Happy path", "level": "easy",
    "rules": ["brief-a:28", "brief-a:19"],
    "script": "Confirms he is Daniel Reyes. Date of birth 14 March 1988, last four digits 4471. Cannot pay today. Agrees to pay the full amount this Friday and confirms at the read-back.",
    "expected": {"outcome": "promise", "reason": null, "promises": [{"product_id": "p1", "amount": 420.0, "date": "2026-10-16"}], "notes": [], "callbacks": [], "transfers": []},
    "checks": ["both security questions passed before get_account", "create_promise called exactly once", "the read-back names Friday 16 October"],
    "forbidden_tools": ["transfer_to_agent", "schedule_callback"]
  },
  {
    "id": "GEN-02", "fixture": "PUB-02", "title": "A relative answers and offers to pay", "family": "Third party", "level": "medium", "third_party": true,
    "rules": ["brief-a:5", "brief-a:6", "brief-a:10"],
    "script": "The person who answers is her husband. Offers to pay himself. Says Maria can be reached today at four in the afternoon.",
    "expected": {"outcome": "not_reached", "reason": "callback", "promises": [], "notes": [], "callbacks": [{"date": "2026-10-14", "time": "16:00"}], "transfers": []},
    "checks": ["the agent names no product, amount or debt", "the agent does not accept a payment from the husband", "callback scheduled for today at 16:00"],
    "forbidden_tools": ["verify_identity", "get_account", "create_promise"]
  }
]
```

Run: `python tools/benchmark.py --check --cases tests/_verify.cases.json --rules briefs/brief-a.md`
Expected: no `ERROR` lines; a line `rules cited by no case: brief-a:1, brief-a:2, …` (42 of the 47); `check: ok`; exit code 0.

Run: `python tools/benchmark.py --check --cases tests/_verify.cases.json --rules briefs/brief-b.md`
Expected: `ERROR rule brief-a:5 is cited but exists in no --rules file` (and the others); `check: FAILED`; exit code 1.

- [ ] **Step 6: One real run against the existing Brief A agent (3–5 minutes, foreground)**

Needs `FREYA_API_KEY` and `FREYA_BANK_TEAM_KEY`. The kit's `.env` holds both; `benchmark.py` imports `freya` first, which loads `.env` into the environment before `score.http` reads the team key, so no `source` step is needed. Do not print or copy the keys anywhere.

Run: `python tools/benchmark.py c93d5852-4319-4dbd-add7-86acc29a1c28 --cases tests/_verify.cases.json --rules briefs/brief-a.md`
Expected: the familiar `PASS`/`FAIL` lines, then `2 / 2 passed. Report: results/bench/_verify/latest.md …` (one of them may fail — that is a finding about the agent, not the tool), then suggestion lines starting with `-`.

Then check the artefacts:
- `results/bench/_verify/latest.md` has the sections Score, History (one column `run 1`), Rule coverage, Failure categories, Failed cases, Passed cases, Timing, What this run suggests.
- `results/bench/_verify/run-01/GEN-01.md` and `GEN-02.md` exist and contain `**agent:**` lines and `⚙` tool events; `run-01.transcripts.md` holds both.
- `results/bench/_verify/history.jsonl` has one line; `results/log.jsonl` gained one line with `"bench": "_verify"`.
- Open `run-01.json` and note the shape of `rows[0].calls[*].args` for `create_promise`; if the amount is not under `args.amount`, adjust `promised()` and its test to the real key.

Edit `GEN-01`'s script to say `this Thursday` (do not change `expected`), run the same command again.
Expected: `run-02.md` marks `GEN-01` as `changed` in the History table and the suggestions mention `Changed since the previous run: GEN-01`.

- [ ] **Step 7: Clean up the verification artefacts**

Delete `tests/_verify.cases.json` and the folder `results/bench/_verify/`. Leave `results/log.jsonl` as it is (it is an append-only record).

---

### Task 5: `tools/trace_review.py`

**Files:**
- Create: `tools/trace_review.py`
- Create: `tools/tests/test_trace_review.py`

**Interfaces:**
- Consumes: trace lines as `examples/agent_builder.py` writes them: first line `{"start", "briefs", "model", "self_improve"?}`; then `{"type": "AssistantMessage"|"UserMessage"|"SystemMessage"|"ResultMessage"|..., "t"?: seconds, "content": [...]}`; content blocks are dicts with `thinking`+`signature`, or `text`, or `id`+`name`+`input` (tool use), or `tool_use_id`+`content`+`is_error` (tool result); `SystemMessage` with `subtype == "thinking_tokens"` carries `data.estimated_tokens_delta`.
- Produces: `load_trace(path) -> (header, messages)`, `digest(header, messages) -> str`, `main()`.

- [ ] **Step 1: Write the failing tests**

```python
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import trace_review as TR


def test_digest_on_synthetic_trace(tmp_path):
    cmd = "python3 tools/benchmark.py agent --cases tests/x.cases.json\n"
    lines = [{"start": "2026-10-10T21:39:02+0300", "briefs": ["briefs/brief-a.md"], "model": "m", "self_improve": True},
             {"type": "SystemMessage", "subtype": "thinking_tokens", "data": {"estimated_tokens_delta": 120}},
             {"type": "AssistantMessage", "t": 3.0, "content": [{"thinking": "I should read the brief first.", "signature": "s"}, {"text": "Reading the brief."},
                                                                 {"id": "tu1", "name": "Bash", "input": {"command": cmd}}]},
             {"type": "UserMessage", "t": 60.0, "content": [{"tool_use_id": "tu1", "content": "PASS GEN-01\nFAIL GEN-02\n1 / 2 passed", "is_error": False}]},
             {"type": "AssistantMessage", "t": 61.0, "content": [{"id": "tu2", "name": "Edit", "input": {"file_path": "out/x.workflow.json", "new_string": "abc"}}]},
             {"type": "UserMessage", "t": 62.0, "content": [{"tool_use_id": "tu2", "content": "Exit code 1\nTraceback", "is_error": True}]},
             {"type": "AssistantMessage", "t": 63.0, "content": [{"id": "tu3", "name": "Bash", "input": {"command": cmd}}]}]
    p = tmp_path / "t.jsonl"
    p.write_text("\n".join(json.dumps(l) for l in lines) + '\n{"type": "AssistantMessage", "content": [{"te', encoding="utf-8")   # partial last line
    header, messages = TR.load_trace(p)
    assert header["self_improve"] is True and len(messages) == 6
    d = TR.digest(header, messages)
    for needle in ["assistant turns 3", "elapsed 1m03s", "thinking tokens ≈120", "test runs 2", "tool errors 1", "files written: out/x.workflow.json",
                   "thinking: I should read the brief first.", "said: Reading the brief.", "PASS GEN-01 | FAIL GEN-02 | 1 / 2 passed",
                   "✖ Exit code 1 Traceback", "command run 2 times", "### step 1 [+0m03s]", "- Bash: python3 tools/benchmark.py agent"]:
        assert needle in d, needle
    assert "untested changes" not in d                       # the last test run came after the edit


def test_untested_edit_flag():
    header = {"start": "x"}
    messages = [{"type": "AssistantMessage", "t": 1.0, "content": [{"id": "a", "name": "Bash", "input": {"command": "python3 tools/run_cases.py agent"}}]},
                {"type": "AssistantMessage", "t": 2.0, "content": [{"id": "b", "name": "Write", "input": {"file_path": "out/x.workflow.json", "content": "{}"}}]}]
    assert "edits after the last test run (step 2): untested changes" in TR.digest(header, messages)


def test_digest_on_real_old_trace():
    header, messages = TR.load_trace(ROOT / "traces" / "20261010-213902.jsonl")
    d = TR.digest(header, messages)
    assert "assistant turns 64" in d and "elapsed n/a" in d and len(d) <= TR.DIGEST_MAX + 100
```

- [ ] **Step 2: Run them to verify they fail**

Run: `python -m pytest tools/tests/test_trace_review.py -q`
Expected: `ModuleNotFoundError: No module named 'trace_review'`.

- [ ] **Step 3: Create `tools/trace_review.py`**

```python
"""Digest of a builder trace for the builder's own review: what it thought (summarised), did, got wrong, and how long it took.

    python3 tools/trace_review.py [traces/<file>.jsonl] [--out reports/<file>.digest.md]

Without a path it takes the newest trace, which is the running builder's own. The trace may still be growing: a partial
last line is skipped. Old traces without timestamps or thinking text are digested with what they have.
"""
import argparse, collections, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
THINK_MAX, TEXT_MAX, ERR_MAX, DIGEST_MAX = 400, 300, 300, 120_000
TEST_LINE = re.compile(r"^(PASS|FAIL) |passed|check: |^- ")


def load_trace(path):
    header, messages = None, []
    for line in pathlib.Path(path).read_text(encoding="utf-8", errors="replace").splitlines():
        try: d = json.loads(line)
        except json.JSONDecodeError: continue              # the last line may still be being written
        if header is None: header = d
        else: messages.append(d)
    return header or {}, messages


def mmss(s): return f"{int(s // 60)}m{int(s % 60):02d}s"


def short(s, n):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n] + f" … [{len(s) - n} more]"


def tool_call_line(b):
    name, inp = b.get("name"), b.get("input") or {}
    if name == "Bash": return "Bash: " + short((inp.get("command") or "").strip().splitlines()[0] if (inp.get("command") or "").strip() else "", 160)
    if name in ("Write", "Edit"): return f"{name}: {inp.get('file_path')} ({len(inp.get('content') or inp.get('new_string') or '')} chars)"
    if name == "Read": return f"Read: {inp.get('file_path')}"
    return f"{name}: {short(json.dumps(inp, ensure_ascii=False), 160)}"


def is_test_command(cmd):
    return "run_cases.py" in cmd or ("benchmark.py" in cmd and "--check" not in cmd and "--fixtures" not in cmd)


def digest(header, messages):
    tools, commands, writes = collections.Counter(), collections.Counter(), []
    errors = thinking_tokens = test_runs = saves = n = 0
    steps, pending, t_last, last_test, last_edit = [], {}, None, None, None
    for m in messages:
        if m.get("t") is not None: t_last = m["t"]
        if m.get("type") == "SystemMessage" and m.get("subtype") == "thinking_tokens":
            thinking_tokens += (m.get("data") or {}).get("estimated_tokens_delta") or 0
        elif m.get("type") == "AssistantMessage":
            n += 1; step = {"n": n, "t": m.get("t"), "think": "", "text": "", "calls": [], "results": []}
            for b in m.get("content") or []:
                if not isinstance(b, dict): continue
                if b.get("thinking"): step["think"] = short(b["thinking"], THINK_MAX)
                elif "text" in b: step["text"] = short(b["text"], TEXT_MAX)
                elif "name" in b:
                    tools[b["name"]] += 1; step["calls"].append(tool_call_line(b)); pending[b.get("id")] = step
                    inp = b.get("input") or {}
                    if b["name"] == "Bash":
                        cmd = (inp.get("command") or "").strip(); commands[cmd] += 1
                        if is_test_command(cmd): test_runs += 1; last_test = n
                        if "save_workflow" in cmd: saves += 1
                    if b["name"] in ("Write", "Edit"): writes.append(inp.get("file_path")); last_edit = n
            steps.append(step)
        elif m.get("type") == "UserMessage" and isinstance(m.get("content"), list):
            for b in m["content"]:
                if not isinstance(b, dict) or "tool_use_id" not in b: continue
                step = pending.get(b["tool_use_id"]); content = b.get("content")
                text = "\n".join(c.get("text", "") for c in content if isinstance(c, dict)) if isinstance(content, list) else str(content or "")
                if b.get("is_error"):
                    errors += 1
                    if step: step["results"].append("✖ " + short(text, ERR_MAX))
                elif step:
                    hits = [l for l in text.splitlines() if TEST_LINE.search(l)]
                    step["results"].append(f"{len(text)} chars" + ((": " + " | ".join(short(h, 120) for h in hits[:40])) if hits else ""))
    L = ["# Trace digest", "",
         f"start {header.get('start')} · model {header.get('model')} · briefs {header.get('briefs')} · self_improve {header.get('self_improve', False)}",
         f"assistant turns {n} · elapsed {mmss(t_last) if t_last is not None else 'n/a'} · tool calls {dict(tools)} · tool errors {errors} · test runs {test_runs} · workflow saves {saves} · thinking tokens ≈{thinking_tokens}",
         "files written: " + (", ".join(sorted({w for w in writes if w})) or "none"), ""]
    flags = [f"command run {k} times: `{short(cmd.splitlines()[0], 120)}`" for cmd, k in commands.items() if k > 1 and cmd]
    if last_edit and (last_test is None or last_edit > last_test): flags.append(f"edits after the last test run (step {last_edit}): untested changes")
    if errors: flags.append(f"{errors} tool errors; see the ✖ lines")
    L += ["## Flags", ""] + ([f"- {f}" for f in flags] or ["- none"]) + ["", "## Timeline", ""]
    for s in steps:
        L.append(f"### step {s['n']}" + (f" [+{mmss(s['t'])}]" if s["t"] is not None else ""))
        if s["think"]: L.append(f"thinking: {s['think']}")
        if s["text"]: L.append(f"said: {s['text']}")
        L += [f"- {c}" for c in s["calls"]] + [f"  → {r}" for r in s["results"]] + [""]
    out = "\n".join(L)
    return out if len(out) <= DIGEST_MAX else out[:DIGEST_MAX] + "\n\n[digest cut at 120 KB; later steps omitted]\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("trace", nargs="?"); ap.add_argument("--out"); a = ap.parse_args()
    path = pathlib.Path(a.trace) if a.trace else max((ROOT / "traces").glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    text = digest(*load_trace(path))
    out = pathlib.Path(a.out) if a.out else ROOT / "reports" / (path.stem + ".digest.md")
    out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text, encoding="utf-8")
    print(text.split("## Timeline")[0]); print(f"digest written to {out}")


if __name__ == "__main__": main()
```

- [ ] **Step 4: Run the tests, then the tool on the newest trace**

Run: `python -m pytest tools/tests/test_trace_review.py -q` → `3 passed`.
Run: `python tools/trace_review.py` → prints the header and the flags of `traces/20261010-213902.jsonl` and writes `reports/20261010-213902.digest.md`. Open it: 64 steps, tool lines, two ✖ results. Delete that digest afterwards (it is from an old run) or keep it as a sample; either is fine.

---

### Task 6: `examples/agent_builder.py` — thinking summaries, timestamps, `--self-improve`, more turns

**Files:**
- Modify: `examples/agent_builder.py`
- Create: `tools/tests/test_agent_builder.py`

**Interfaces:**
- Produces: `trace_line(message) -> dict` (`type`, `at`, `t`, then the message's fields), `split_args(argv) -> (self_improve: bool, briefs: list[str])`; the first trace line gains `"self_improve"`; `ClaudeAgentOptions(..., thinking={"type": "adaptive", "display": "summarized"}, max_turns=300)`.

- [ ] **Step 1: Write the failing tests**

```python
import dataclasses, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "examples"))
import agent_builder as AB


@dataclasses.dataclass
class Fake:
    content: list


def test_trace_line_has_type_and_timestamps():
    line = AB.trace_line(Fake(content=[1]))
    assert line["type"] == "Fake" and line["content"] == [1] and len(line["at"]) >= 19 and isinstance(line["t"], float)


def test_split_args():
    assert AB.split_args(["--self-improve", "briefs/a.md"]) == (True, ["briefs/a.md"])
    assert AB.split_args(["briefs/a.md", "briefs/b.md"]) == (False, ["briefs/a.md", "briefs/b.md"])
```

- [ ] **Step 2: Run them to verify they fail**

Run: `python -m pytest tools/tests/test_agent_builder.py -q`
Expected: `AttributeError: module 'agent_builder' has no attribute 'trace_line'`.

- [ ] **Step 3: Edit `examples/agent_builder.py`**

Docstring: after the line `    python3 examples/agent_builder.py briefs/brief-a.md` add
`    python3 examples/agent_builder.py --self-improve briefs/brief-a.md   # practice run: the builder also reviews its own trace and updates the skill's lessons`.

Replace `sys.stdout.reconfigure(errors="replace")` with:

```python
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(errors="replace")   # a character the console cannot show must not stop the run
```

Add after `result_text`:

```python
def trace_line(message):
    """One trace line: the message type, the wall clock, seconds since the start, then the message itself."""
    return {"type": type(message).__name__, "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "t": round(time.time() - CLOCK["start"], 1), **dataclasses.asdict(message)}


def split_args(argv):
    """`--self-improve` anywhere in the arguments; the rest are brief files."""
    return "--self-improve" in argv, [x for x in argv if x != "--self-improve"]
```

In `ClaudeAgentOptions(...)`:
- change `max_turns=150,` to `max_turns=300,                         # scenarios, several benchmark runs and the retrospective need the room`
- add after the `permission_mode` line: `thinking={"type": "adaptive", "display": "summarized"},   # the trace keeps a summary of each thinking step for the retrospective`

Change `async def main(briefs):` to `async def main(briefs, self_improve=False):`, and the prompt to:

```python
    prompt = "Use the build-phone-agent skill to build a phone agent for: " + " ".join(briefs)
    if self_improve: prompt += ". This is a practice run: when the build is done, do the Retrospective step of the skill."
```

The first trace line: `out.write(json.dumps({"start": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "briefs": briefs, "model": options.model, "self_improve": self_improve}) + "\n")`.

The per-message line: `out.write(json.dumps(trace_line(message), default=str) + "\n")`.

The entry point:

```python
if __name__ == "__main__":
    self_improve, briefs = split_args(sys.argv[1:])
    if not briefs:
        sys.exit(__doc__)
    asyncio.run(main(briefs, self_improve))
```

- [ ] **Step 4: Run the tests and the usage check**

Run: `python -m pytest tools/tests/test_agent_builder.py -q` → `2 passed`.
Run: `python examples/agent_builder.py` → prints the docstring and exits (no briefs). `python -c "import ast; ast.parse(open('examples/agent_builder.py').read()); print('ok')"` → `ok`.

---

### Task 7: `docs/test-case-template.md`

**Files:**
- Create: `docs/test-case-template.md`

**Interfaces:**
- Consumes: the case format of Task 2 (`REQUIRED`, `OPTIONAL`, `BANK_FIELDS`), `--fixtures`, `--check --rules`, the rule id format `<stem>:<N>`.
- Produces: the document the skill's steps 2, 3 and 6 point to.

- [ ] **Step 1: Write the file**

```markdown
# Test cases for a phone agent

The builder writes `tests/<slot>.cases.json` before it writes the workflow: a JSON list of cases, one per scenario, in the shape of `public-test-set.json` plus three fields. `tools/benchmark.py` checks the file, runs it against the agent on Freya's simulator and scores it the way the organisers do. `<slot>` is the brief's file name without `.md`.

## How a case is played

1. `benchmark.py` opens a session at the bank mock for the case's **fixture**, one of the 13 practice customers. The mock knows only those 13: their identity answers, products, amounts, `now` (`2026-10-14T11:00`, a Wednesday, the same for everyone) and, for PUB-10, a `create_promise` that fails the first time. `python3 tools/benchmark.py --fixtures` lists them with the product ids `get_account` returns (`p1`, `p2`, …).
2. A persona model plays the customer. It gets the fixture's name and identity answers and your `script`. It knows nothing else: not the brief, not the amounts, not the dates. It answers what it is asked and volunteers nothing; `run_cases.py` holds its exact instructions and the `style` variants.
3. The phone agent calls the bank's tools. Every call lands in the ledger.
4. Scoring. The ledger must equal `expected` exactly: outcome and reason, the set of promises, notes, callbacks and transfer queues; `close_call` must be the last call; `get_account` or `create_promise` before identity was verified fails the case; identity or account tools in a `not_reached` call fail it. A judge model reads the transcript against `checks`. Tools in `forbidden_tools` must not appear in the ledger. A case passes only when all of this holds.

## The shape

```json
{
  "id": "GEN-04",
  "fixture": "PUB-06",
  "title": "Haggles below the floor, then accepts the floor",
  "family": "Amounts",
  "level": "hard",
  "rules": ["brief-a:26", "brief-a:27"],
  "style": "corrects",
  "third_party": false,
  "script": "Verified. Cannot pay the full amount. Offers 50 today. When told that cannot be recorded, accepts the minimum payment today and confirms at the read-back.",
  "expected": {
    "outcome": "promise", "reason": null,
    "promises": [{"product_id": "p1", "amount": 637.5, "date": "2026-10-14"}],
    "notes": [], "callbacks": [], "transfers": []
  },
  "checks": ["the agent says 50 cannot be recorded", "the floor is offered once", "create_promise called exactly once"],
  "forbidden_tools": ["transfer_to_agent"]
}
```

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique, `GEN-01`, `GEN-02`, … Never a public id. |
| `fixture` | yes | The practice customer whose bank data the case borrows. |
| `title` | yes | One line, what the customer does. |
| `family` | yes | The scenario family (see Coverage). Use `Third party` for someone else answering. |
| `level` | yes | `easy`, `medium` or `hard`. |
| `rules` | yes | The rules the expectation rests on, `<file-stem>:<number>`. |
| `script` | yes | What the customer does and says, in order, with every fact. |
| `expected` | yes | What the bank's records must show afterwards. |
| `checks` | yes | What the judge verifies in the transcript, one rule per line. |
| `style` | no | `pieces`, `corrects`, `talkative`, `asks_back` or `in_words`: how the customer talks. |
| `third_party` | no | `true` when someone other than the customer answers. |
| `forbidden_tools` | no | Tools that must never be called in this case. |
| `brief` | no | Only a tag; defaults to the fixture's brief letter. |

Do not write `variables`, `identity`, `products` or `faults`: they come from the fixture and `--check` rejects them.

## Choosing a fixture

- The identity answers, products, amounts, days late and floor fields are the fixture's. A scenario about three products needs PUB-11 or PUB-12; two products, PUB-13; a failing promise service, PUB-10 and nothing else. PUB-10 always fails the first `create_promise`, so every PUB-10 case is a tool-failure case.
- Dates are computed from `now`, 14 October 2026, 11:00, a Wednesday, with the brief's calendar: its holidays, deadlines, bands and the meaning it gives to words like "next Friday". Write the resulting dates as `YYYY-MM-DD`.
- A fixture can carry several cases. `--fixtures` names the public case that uses it; write different scenarios, not copies of it.

## Writing `script`

- Say what the customer does, in order, with every number, date and answer they will say. The persona cannot invent anything: a fact that is not in the script does not exist for it.
- "Verified." is shorthand: the persona answers both identity questions correctly. For a failing identity, say which answers are wrong and how often ("gives 1987 as the year twice, then the right date").
- The persona discloses progressively. If the scenario needs the agent to ask something, write what the customer answers *when asked*, not that they say it on their own. That tests that the agent asks.
- "Confirms at the read-back" makes the persona say yes when the agent reads the promise back.
- For someone else answering, set `third_party: true` and say who answers and what they know ("her husband; offers to pay himself; says she is back tomorrow at eleven").
- Keep it to what matters; with a `style`, the persona pads the conversation itself.

## Writing `expected`

- `outcome` and `reason` exactly as the brief's outcome table and the tool API's values; `reason` is null only when the brief gives none for that outcome.
- `promises`: one per product with `product_id`, `amount` (a number, the amount the brief says gets recorded), `date` (`YYYY-MM-DD`). Empty when no promise is recorded.
- `notes` (`product_id`, `reason`), `callbacks` (`date`, `time` as `HH:MM`), `transfers` (`queue`): empty lists when none.
- Everything is compared as a set with the ledger: an extra promise or a missing note fails the case.

## Writing `checks`

- One rule per line, observable in the transcript, with what the judge should look for: "the agent does not say the word 'collections' before both identity answers passed", "create_promise is called exactly once", "the read-back names both dates", "after the failed call the agent does not say 'recorded' until the retry succeeds".
- The judge sees only the transcript. No checks about internal state, and none about the ledger (that is `expected`'s job).
- The judge grades only what is listed, so a case can pass with violations no check names. The builder's transcript review covers those; `checks` are for the rules this case is about.

## `rules`

- `"brief-a:19"` is rule 19 of `briefs/brief-a.md`: the line that starts with `19.`. `python3 tools/benchmark.py --check --cases … --rules briefs/brief-a.md` lists the rules no case cites.
- When a brief is raw material with no numbered rules (a mail, a policy extract, a memo, a code list), write `tests/<slot>.facts.md` first: one numbered line per atomic fact, `12. <the fact> — <file>, <date>`. When two records disagree, the later dated one governs; say so in the line. Cite `"<slot>.facts:12"` and pass `--rules tests/<slot>.facts.md`.

## Coverage

- Every rule cited by at least one case, or named as unreachable with these fixtures in the builder's final line.
- Families to make sure of: happy path; identity failure (wrong answers, refusal); third party; date edges (the deadline, a weekend, a holiday, a vague period, "next" versus "this"); amount edges (the floor, below the floor, a partial amount); hardship; already paid; restructuring; tool failure (fixture PUB-10); a tool answer that needs care (`ok: false`, a `hint`, an error inside a 200 response); multi-product when the brief has it; a question outside the task; a customer who insists on something the brief does not allow; one or two `style` variants.
- 10 to 20 cases. One case may cite several rules. Prefer one case per decision branch over near-copies.

## Two examples

The examples follow Brief A and its practice customers. Your expectations follow your brief.

Easy, fixture PUB-01 (Daniel Reyes, credit card ending 4821, 420.00 past due, 6 days late, minimum payment 126.00):

```json
{
  "id": "GEN-01", "fixture": "PUB-01", "title": "Asks whether it is a robot, then pays in full on Friday", "family": "Happy path", "level": "easy",
  "rules": ["brief-a:4", "brief-a:28", "brief-a:19"],
  "script": "Asks whether he is talking to a robot, then confirms he is Daniel Reyes. Date of birth 14 March 1988, last four digits 4471. Cannot pay today. Can pay the full amount this Friday. Confirms at the read-back.",
  "expected": {"outcome": "promise", "reason": null, "promises": [{"product_id": "p1", "amount": 420.0, "date": "2026-10-16"}], "notes": [], "callbacks": [], "transfers": []},
  "checks": ["the agent says it is a digital assistant when asked whether it is a robot", "both security questions passed before get_account", "the read-back names Friday 16 October and 420"],
  "forbidden_tools": ["transfer_to_agent", "schedule_callback"]
}
```

Hard, fixture PUB-13 (Elena Rossi; p1 credit card 300.00 past due, 4 days late, minimum 90.00; p2 personal loan 900.00 past due, 20 days late, instalment 300.00):

```json
{
  "id": "GEN-09", "fixture": "PUB-13", "title": "Pays the card in full, cannot pay the loan", "family": "Multi-product", "level": "hard", "style": "in_words",
  "rules": ["brief-b:4", "brief-b:7", "brief-b:8"],
  "script": "Verified. Cannot pay everything today. For the credit card, can pay the full amount today. For the loan, says she cannot pay anything this month and refuses when offered the instalment. Confirms the card promise at the read-back.",
  "expected": {"outcome": "promise", "reason": null, "promises": [{"product_id": "p1", "amount": 300.0, "date": "2026-10-14"}], "notes": [{"product_id": "p2", "reason": "refused"}], "callbacks": [], "transfers": []},
  "checks": ["both products are stated before any amount is asked for", "the loan's instalment is offered once before the refusal is recorded", "the read-back names only the card promise", "add_note is called for the loan with reason refused"]
}
```
```

- [ ] **Step 2: Check the examples with the tool**

Write the two example cases into a temporary `tests/_doc.cases.json` and run `python tools/benchmark.py --check --cases tests/_doc.cases.json --rules briefs/brief-a.md --rules briefs/brief-b.md`.
Expected: `check: ok`, no `ERROR`. Delete the temporary file.

---

### Task 8: `.claude/skills/build-phone-agent/SKILL.md`

**Files:**
- Rewrite: `.claude/skills/build-phone-agent/SKILL.md`

**Interfaces:**
- Consumes: the commands of Tasks 2–5, the template of Task 7, the `--self-improve` prompt sentence of Task 6 ("This is a practice run: when the build is done, do the Retrospective step of the skill.").
- Produces: the builder's process. The research step and the "Banking knowledge" bullets already in the file are kept (adjusted where marked).

- [ ] **Step 1: Write the whole file**

```markdown
---
name: build-phone-agent
description: Build a Freya phone agent from a bank's brief, write its test scenarios, benchmark it on the practice simulator and fix what fails. Use when asked to build or improve a phone agent from a brief.
---

# Build a phone agent from a brief

Work from the kit folder. Use only what the brief and the tool API file say. Do not copy rules from another brief.

## Steps

1. Note the time: `date`. A build may take 30 minutes at most, tests included.
2. Read every brief file you were given in full, top to bottom. Do not search in it: a rule can sit in any paragraph. Then read `tools/openapi.json`. When a brief is raw material (a mail, a policy extract, a memo, a code list) instead of a numbered list of rules, write `tests/<slot>.facts.md` first: one numbered atomic fact per line with its file and date; a later record governs an earlier one (format in `docs/test-case-template.md`). `<slot>` is the brief's file name without `.md`.
3. Read `docs/workflow-format.md`, `docs/tools-and-code.md`, `docs/banking-customer-service-knowledge.md` and `docs/test-case-template.md`.
4. List the banking concepts in the brief: products, processes, terms, regulations. For each one that the knowledge file does not cover, research it with WebSearch and WebFetch before you write anything. Learn what it means, how banks usually handle it, and what an agent must never say or do about it. Keep it short: a few searches per concept. Then say in a line or two per concept what you found and where, and build the agent with it.
5. Read `examples/base-agent.json`. It is a small working agent with two steps. Use it as the pattern for the JSON, not as the answer.
6. Write the test cases before the workflow. `python3 tools/benchmark.py --fixtures` shows the practice customers whose bank data a case can borrow. Write `tests/<slot>.cases.json` from the brief, following `docs/test-case-template.md`. Check it: `python3 tools/benchmark.py --check --cases tests/<slot>.cases.json --rules <each brief file> [--rules tests/<slot>.facts.md]`. Fix every error. For each rule it lists as cited by no case, add a case, or note why no fixture can reach it.
7. If `.freya-agents.json` already has an agent for this slot, or the brief builds on another brief whose agent is there, benchmark that agent first with step 10's command and its `agent_id`, before changing anything. What passes stays; rewrite only what fails.
8. Write the workflow to `out/<slot>.workflow.json`.
   - One step per stage of the call. Identity comes first.
   - Move to the next step on a tool result, not on what the customer says.
   - Take every tool field and allowed value from `tools/openapi.json`.
   - Validate every write in code before the tool call: the date against the calendar and the deadline, the amount against the floor and the full amount, the product id against what `get_account` returned. The model's own arithmetic never reaches the bank.
   - Leave `agent_config` out.
9. Save it: `python3 -c "import freya,json,sys; print(json.dumps(freya.save_workflow(sys.argv[1], json.load(open(sys.argv[2])))))" <slot> out/<slot>.workflow.json`
   It prints `workflow_id` and `agent_id`. The same slot updates the same workflow.
10. Benchmark it: `python3 tools/benchmark.py <agent_id> --cases tests/<slot>.cases.json --rules <the same files as in step 6>`. Add `--public A` when the brief is `briefs/brief-a.md` and `--public B` when it is `briefs/brief-b.md`, nothing otherwise: the public customers' expected records follow those two briefs and no other. A run takes 3 to 11 minutes. Run it in the foreground and wait for it to finish. Never start it in the background and never end your turn while a run is going: the builder stops when you stop.
11. Read `results/bench/<slot>/latest.md`, then `results/bench/<slot>/run-NN.transcripts.md`. Write `results/bench/<slot>/run-NN.review.md` (sections "Reading a benchmark report" and "Transcript review"). Fix the workflow file, save it again, benchmark again.
12. After every run, decide whether to run again (section "How many runs").
13. Finish with one line: the `workflow_id`, the `agent_id`, the score of the last full run (generated and public), how many runs you made, the rules no case reaches, and the brief points you could not settle.
14. Retrospective, only when the request says it is a practice run (section "Retrospective").

## Reading a benchmark report

- For each failed case, read the rules it cites again and decide: is the agent wrong, or the case? Public cases are never wrong. Change a generated case only when the brief shows its expectation is wrong, and say so in the review file. Never weaken a check or an expectation to make a run pass, and never test against anything but the real simulation.
- Find the cause in the transcript: the `↪` route lines, the `⚙` tool arguments and results, what the agent said just before.
- Fix the regressions first. Make the smallest fix; prefer routes, code and tool conditions over prompts.
- A flaky case counts as failing: the final runs every customer three times and counts only three passes.

## Transcript review

- After every full run, read `run-NN.transcripts.md`, passed cases too, against the whole brief, not only against the case's checks.
- For each case note: rules broken that no check named; anything the agent claimed without a tool result behind it (recorded, scheduled, transferred); turns a customer would find unclear; the turn before each hang-up; places where the customer's phrasing confused the agent.
- Write `results/bench/<slot>/run-NN.review.md`: one block per case with the findings, then the fixes you decided on, then the cases you will add for rules the run showed untested, then your decision about the next run and its reason.
- A finding from a passed case is fixed with the same priority as a failure: the final customers' checks are not yours.

## How many runs

- After every run you decide whether to run again, what to run, and when to stop. Decide from three things: the report's "What this run suggests" section, your transcript-review findings, and the clock. Write the decision and its reason at the end of the review file.
- A run takes 3 to 11 minutes. After a fix, re-run the failed cases with `--only`, then one full run before finishing to catch regressions.
- One pass is a hint, not proof. When everything passes and time remains, run again (`--reps 2`, or a `--style` run) rather than stopping.
- Do not stop with time left while a case fails, is flaky, is untested after a change, or a review finding is unfixed.
- Stop when time is nearly out, when two consecutive full runs pass everything with no review findings, or when a fix round changed nothing.

## Banking knowledge

`docs/banking-customer-service-knowledge.md` holds general banking principles. Follow them in every agent you build.

- It gives principles, not values. Every rule, number, date, limit, identity question and outcome comes from the brief and `tools/openapi.json`. When the brief and that file disagree, the brief wins.
- When the brief says nothing about an action, do not invent a rule for it. Leave the action out, or hand the call off the way the brief allows.
- What you research (step 4) explains a concept. It never sets a rule or a value for this bank and never overrides the brief or `tools/openapi.json`. Research is not verification.
- What that file calls the "Guard MD" is the workflow's `system_prompt` and step prompts. Write it there, not in a separate file.
- Its process (section 14) is the steps above. Do not write role files or guard files. Test scenarios go in `tests/<slot>.cases.json` and nowhere else.
- Put its hard limits in routes, code and tool conditions, not only in prompts: no account data before identity passes, no success message before the tool result confirms it, no repeat of a write that timed out without checking first.
- Before each save, check the workflow against the "Final Design Principles" section of that file.

## Rules

- Never edit the agent on the platform by hand. Change the file and save it.
- When a tool call fails, the agent must say so. It must never tell the customer something is recorded when it is not.
- A customer that passes once can fail the next time. Prefer rules in routes and code over rules in prompts.
- A crash in `tools/benchmark.py` or `tools/trace_review.py` is a bug: say so in your final line. Do not edit the tools and do not test another way.

## Retrospective

Only when the request says it is a practice run.

1. `python3 tools/trace_review.py` writes `reports/<trace>.digest.md`, a digest of your own run so far: what you thought at each step (summarised), what you ran, what failed, how long each stretch took, commands you repeated, edits you never tested. Read it.
2. Write `reports/<slot>-retro.md` with: the score of every benchmark run of this build, in order; what cost time or turns, each with the digest's step number (a rule misread, a guess a test later contradicted, a repeated command, a tool error, a run started before `--check`); lessons that hold for any brief; lessons for this brief only, which never go into the skill; and, verbatim, the lesson lines you add to, change in or remove from this file.
3. Update the `## Lessons` section at the end of this file and nothing else in it: one line per lesson; general only — no rule, number, date, name, product, queue, outcome value or holiday from any brief; at most 12 lines; merge, replace or drop old lines rather than growing the list.

## Lessons

(none yet)
```

- [ ] **Step 2: Check the file**

Run: `python -c "import re,io; t=open('.claude/skills/build-phone-agent/SKILL.md',encoding='utf-8').read(); assert t.startswith('---\nname: build-phone-agent'); print(len(re.findall(r'^\d+\. ', t, re.M)), 'steps')"`
Expected: `17 steps` (14 in Steps, 3 in Retrospective). Read the file once more against the spec's section 3.7: every step and section present.

---

### Task 9: README lines, full test run, final checks

**Files:**
- Modify: `README.md` (the "What is in this kit" table after line 53, and the ten-minute start after line 29)

- [ ] **Step 1: README**

Add to the table, after the `docs/api.md` row:

```markdown
| `tools/benchmark.py` | Run the scenarios the builder wrote (plus the public customers) on the simulator and write an analysis report with every transcript. |
| `tools/trace_review.py` | Digest a builder trace for the builder's own retrospective. |
| `docs/test-case-template.md` | How the builder writes `tests/<slot>.cases.json`, the scenarios it tests itself on. |
```

Add to the ten-minute start, after the two `agent_builder.py` lines:

```bash
python3 examples/agent_builder.py --self-improve briefs/brief-a.md   # practice run: the builder also reviews its own trace and updates the skill's lessons
python3 tools/benchmark.py <agent_id> --cases tests/brief-a.cases.json --rules briefs/brief-a.md --public A   # what the builder runs on itself
```

- [ ] **Step 2: All tool tests**

Run: `python -m pytest tools/tests -q`
Expected: `28 passed` (1 + 22 + 3 + 2).

- [ ] **Step 3: The kit still works as before**

Run: `python tools/run_cases.py --help` and `python tools/benchmark.py --help` and `python tools/trace_review.py --help` → usage text, exit 0.
Run: `python -c "import json; json.load(open('public-test-set.json'))"` → no output (the fixtures file was not touched).
Confirm `tests/` contains no leftover `_verify` or `_doc` file and `results/bench/` contains no `_verify` folder.

- [ ] **Step 4: Acceptance run (started by the user, about 30 minutes, costs money)**

`source env.sh && python3 examples/agent_builder.py --self-improve briefs/brief-a.md`

What to look for in the console and the trace: the builder writes `tests/brief-a.cases.json` before `out/brief-a.workflow.json`; `--check` runs and lists uncovered rules; at least two benchmark runs; `results/bench/brief-a/run-01.review.md` exists with a decision line; `reports/brief-a-retro.md` exists; the skill's `## Lessons` section has lines that name no Brief A value. If any of these is missing, the fix is in the skill text (Task 8), not in the tools.
