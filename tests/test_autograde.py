import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from autograde import TASKS, _check, grade, validate_owner


def test_worksheet_commands_are_checked(tmp_path: Path):
    directory = tmp_path / "submissions" / "example-student" / "week01"
    directory.mkdir(parents=True)
    directory.joinpath("answers.json").write_text(
        json.dumps({"commands": {
            "print_path": "pwd",
            "list_hidden": "ls -la",
            "create_dir": "mkdir workspace",
            "change_dir": "cd workspace",
            "make_file": "touch notes.txt",
        }}), encoding="utf-8"
    )
    report = grade(tmp_path, "example-student")
    assert report["status"] == "graded"
    assert report["submitted_weeks"] == 1
    assert report["points_earned"] == 5


def test_empty_fork_is_detected(tmp_path: Path):
    report = grade(tmp_path, "student-xyz")
    assert report["status"] == "no_submissions"
    assert report["points_earned"] == 0


def test_incomplete_worksheet_is_reported(tmp_path: Path):
    path = tmp_path / "submissions" / "learner" / "week01" / "answers.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"commands": {"print_path": "pwd"}}), encoding="utf-8")
    report = grade(tmp_path, "learner")
    assert report["status"] == "needs_correction"
    assert report["points_earned"] == 1
    assert report["weeks"]["week01"]["checks"]["make_file"] is False


def test_command_variants():
    assert _check("week01", "list_hidden", "ls -lha")
    assert _check("week03", "make_executable", "chmod +x script.sh")
    assert _check("week06", "clone_repo", "git clone https://github.com/VMatee/sample.git")
    assert not _check("week06", "clone_repo", "git clone")
    assert not _check("week01", "list_hidden", "ls")


def test_username_validation():
    assert validate_owner("example-student") == "example-student"
    try:
        validate_owner("../../secret")
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid path-like usernames must be rejected")
    assert len(TASKS) == 6
