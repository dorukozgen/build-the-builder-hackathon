"""A small agentic builder: Claude reads the brief, writes the phone agent, tests it and fixes it.

    pip install claude-agent-sdk
    python3 examples/agent_builder.py briefs/brief-a.md
    python3 examples/agent_builder.py --self-improve briefs/brief-a.md   # practice run: the builder also reviews its own trace and updates the skill's lessons

It runs Claude through the Claude Agent SDK with one skill, `.claude/skills/build-phone-agent`.
The skill is the builder's knowledge. Improve the skill and you improve every agent it builds.
Needs FREYA_API_KEY and FREYA_BANK_TEAM_KEY (see env.example) and a Claude login or ANTHROPIC_API_KEY.
Every message of the run is written to traces/<start time>.jsonl. That file is the trace you submit.

The console shows every message in full: Claude's text and thinking, each tool call and each tool result.
BUILDER_LOG_MAX=<n> cuts each printed message to n characters. When nothing new arrives for 30 seconds,
a "still working" line shows that the run is alive (Claude may be writing a long file or waiting for a test).
"""
import asyncio, dataclasses, json, os, pathlib, sys, time

from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, ResultMessage, TextBlock, ThinkingBlock, ToolResultBlock, ToolUseBlock, UserMessage, query

KIT = pathlib.Path(__file__).resolve().parent.parent
LOG_MAX = int(os.environ.get("BUILDER_LOG_MAX", "0"))      # 0: print every message in full
HEARTBEAT_S = 30
CLOCK = {"start": time.time(), "last": time.time()}
if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(errors="replace")   # a character the console cannot show must not stop the run


def mmss(seconds):
    return f"{int(seconds // 60)}m{int(seconds % 60):02d}s"


def say(text, indent="", touch=True):
    """Print with a time stamp. Continuation lines are indented under the first one."""
    text = str(text)
    if LOG_MAX and len(text) > LOG_MAX:
        text = text[:LOG_MAX] + f" ... [{len(text) - LOG_MAX} more characters]"
    first, *rest = text.splitlines() or [""]
    print(f"[{time.strftime('%H:%M:%S')}] {indent}{first}", flush=True)
    for line in rest:
        print(" " * 11 + indent + line, flush=True)
    if touch:
        CLOCK["last"] = time.time()


def tool_input(value):
    """A tool call's arguments, one per line. Multi-line strings (commands, file contents) are printed as they are."""
    if not isinstance(value, dict):
        return str(value)
    lines = []
    for k, v in value.items():
        v = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
        lines.append(f"{k}:\n{v}" if "\n" in v else f"{k}: {v}")
    return "\n".join(lines)


def result_text(content):
    """A tool result's content, which is either a string or a list of content blocks."""
    if isinstance(content, list):
        return "\n".join(c.get("text", "[" + str(c.get("type")) + "]") if isinstance(c, dict) else str(c) for c in content)
    return "" if content is None else str(content)


def trace_line(message):
    """One trace line: the message type, the wall clock, seconds since the start, then the message itself."""
    return {"type": type(message).__name__, "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "t": round(time.time() - CLOCK["start"], 1), **dataclasses.asdict(message)}


def split_args(argv):
    """`--self-improve` anywhere in the arguments; the rest are brief files."""
    return "--self-improve" in argv, [x for x in argv if x != "--self-improve"]


async def heartbeat():
    while True:
        await asyncio.sleep(HEARTBEAT_S)
        quiet = time.time() - CLOCK["last"]
        if quiet >= HEARTBEAT_S:
            say(f"... still working: {mmss(quiet)} since the last message, {mmss(time.time() - CLOCK['start'])} in total", touch=False)


async def main(briefs, self_improve=False):
    trace = KIT / "traces" / (time.strftime("%Y%m%d-%H%M%S") + ".jsonl")
    trace.parent.mkdir(exist_ok=True)
    options = ClaudeAgentOptions(
        cwd=KIT,
        model=os.environ.get("BUILDER_MODEL", "claude-opus-5-5"),
        skills=["build-phone-agent"],          # the skill in .claude/skills
        setting_sources=["project"],           # only this folder's settings, not your own
        allowed_tools=["Read", "Write", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch"],   # web: research concepts the knowledge file lacks
        permission_mode="dontAsk",             # anything not listed above is refused
        thinking={"type": "adaptive", "display": "summarized"},   # the trace keeps a summary of each thinking step for the retrospective
        max_turns=300,                         # scenarios, several benchmark runs and the retrospective need the room
        # A test run takes up to 11 minutes. Let a command run that long, and keep it in the foreground:
        # the builder stops when Claude ends its turn, so a test left in the background is never read.
        env={"BASH_DEFAULT_TIMEOUT_MS": "900000", "BASH_MAX_TIMEOUT_MS": "1200000", "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS": "1"},
    )
    prompt = "Use the build-phone-agent skill to build a phone agent for: " + " ".join(briefs)
    if self_improve: prompt += ". This is a practice run: when the build is done, do the Retrospective step of the skill."
    beat = asyncio.create_task(heartbeat())
    try:
        with trace.open("w") as out:
            out.write(json.dumps({"start": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "briefs": briefs, "model": options.model, "self_improve": self_improve}) + "\n")
            say(f"builder started, model {options.model}, trace {trace}")
            async for message in query(prompt=prompt, options=options):
                out.write(json.dumps(trace_line(message), default=str) + "\n")
                out.flush()
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            say(block.text)
                        elif isinstance(block, ThinkingBlock) and block.thinking.strip():
                            say("(thinking) " + block.thinking.strip())
                        elif isinstance(block, ToolUseBlock):
                            say(f"[{block.name}] " + tool_input(block.input), "  ")
                elif isinstance(message, UserMessage) and isinstance(message.content, list):
                    for block in message.content:
                        if isinstance(block, ToolResultBlock):
                            say(("[result, error] " if block.is_error else "[result] ") + result_text(block.content), "    ")
                elif isinstance(message, ResultMessage):
                    say(f"done: {message.num_turns} turns, {message.duration_ms / 1000:.0f} s, ${message.total_cost_usd or 0:.2f}. Trace: {trace}")
    finally:
        beat.cancel()


if __name__ == "__main__":
    self_improve, briefs = split_args(sys.argv[1:])
    if not briefs:
        sys.exit(__doc__)
    asyncio.run(main(briefs, self_improve))
