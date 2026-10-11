import dataclasses, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "builder"))
import build as AB


@dataclasses.dataclass
class Fake:
    content: list


def test_trace_line_has_type_and_timestamps():
    line = AB.trace_line(Fake(content=[1]))
    assert line["type"] == "Fake" and line["content"] == [1] and len(line["at"]) >= 19 and isinstance(line["t"], float)


def test_split_args():
    assert AB.split_args(["--self-improve", "briefs/a.md"]) == (True, ["briefs/a.md"])
    assert AB.split_args(["briefs/a.md", "briefs/b.md"]) == (False, ["briefs/a.md", "briefs/b.md"])
    argv = ["case-folder", "--mock-url", "https://m.workers.dev/", "--self-improve"]
    assert AB.split_args(argv) == (True, ["case-folder"]) and AB.mock_url(argv) == "https://m.workers.dev"
    assert AB.mock_url(["briefs/a.md"]) is None and AB.mock_url(["x", "--mock-url"]) is None
    argv = ["cases/bank-folder/", "https://m.workers.dev"]                       # the final's run command: folder, then mock
    assert AB.split_args(argv) == (False, ["cases/bank-folder/"]) and AB.mock_url(argv) == "https://m.workers.dev"


def test_outside_dirs_adds_only_folders_outside_the_kit(tmp_path):
    case = tmp_path / "bank-folder"; case.mkdir()
    assert AB.outside_dirs([str(case), str(AB.KIT / "briefs" / "brief-a.md")]) == [str(case.resolve())]
    assert AB.outside_dirs([str(case / "BRIEF.md")]) == [str(case.resolve())]
