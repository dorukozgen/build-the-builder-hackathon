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
