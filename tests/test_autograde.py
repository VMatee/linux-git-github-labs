import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "teacher_tools"))
from autograde import TASKS, _check, grade, validate_owner
from collect_results import latest_run, safe_login


def test_public_worksheet_fixture_passes_all_tasks():
    root = Path(__file__).resolve().parent / "fixtures" / "example-repo"
    report = grade(root, "example-student")
    assert report["status"] == "graded"
    assert report["submitted_weeks"] == 6
    assert report["points_earned"] == 30
    assert report["points_possible_for_submitted"] == 30


def test_empty_fork_is_detected(tmp_path: Path):
    report = grade(tmp_path, "student-xyz")
    assert report["status"] == "no_submissions"
    assert report["points_earned"] == 0


def test_incomplete_correctness_is_reported(tmp_path: Path):
    path = tmp_path / "submissions" / "learner" / "week01" / "answers.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps({"commands": {"print_path": "pwd"}}))
    report = grade(tmp_path, "learner")
    assert report["status"] == "needs_correction"
    assert report["points_earned"] == 1
    assert report["weeks"]["week01"]["checks"]["make_file"] is False


def test_shell_commands_accept_reasonable_flags():
    assert _check("week01", "list_hidden", "ls -lha")
    assert _check("week03", "make_executable", "chmod +x script.sh")
    assert _check("week06", "clone_repo", "git clone https://github.com/VMatee/sample.git")
    assert not _check("week06", "clone_repo", "git clone")
    assert not _check("week01", "list_hidden", "ls")


def test_username_validation_and_latest_run():
    assert validate_owner("example-student") == "example-student"
    assert not safe_login("../../secret")
    data = {"workflow_runs": [{"created_at":"2026-01-01", "id":1}, {"created_at":"2026-01-03", "id":2}]}
    assert latest_run(data)["id"] == 2
    assert latest_run({"workflow_runs": []}) is None
    assert len(TASKS) == 6
