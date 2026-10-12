"""Safe, static JSON worksheet checks for student forks. No code execution.

Six five-point practice worksheets are checked. This is formative grading only.
"""
import argparse
import json
import re
import shlex
import sys
from pathlib import Path


TASKS = {
    "week01": {
        "print_path": ("pwd",),
        "list_hidden": ("ls", "a"),
        "create_dir": ("mkdir", "workspace"),
        "change_dir": ("cd", "workspace"),
        "make_file": ("touch", "notes.txt"),
    },
    "week02": {
        "read_file": ("cat", "notes.txt"),
        "copy_file": ("cp", "notes.txt", "backup.txt"),
        "move_file": ("mv", "backup.txt", "archive.txt"),
        "remove_file": ("rm", "archive.txt"),
        "search_text": ("grep", "error", "app.log"),
    },
    "week03": {
        "make_executable": ("chmod", "script.sh"),
        "list_processes": ("ps",),
        "sort_lines": ("sort", "names.txt"),
        "redirect_output": ("echo", ">", "hello.txt"),
        "pipe_filter": ("cat", "|", "grep"),
    },
    "week04": {
        "init_repo": ("git", "init"),
        "stage_file": ("git", "add", "main.py"),
        "commit_change": ("git", "commit", "-m"),
        "check_status": ("git", "status"),
        "show_history": ("git", "log"),
    },
    "week05": {
        "new_branch": ("git", "switch", "-c", "feature"),
        "list_branches": ("git", "branch"),
        "merge_branch": ("git", "merge", "feature"),
        "show_diff": ("git", "diff"),
        "switch_main": ("git", "switch", "main"),
    },
    "week06": {
        "add_remote": ("git", "remote", "add", "origin"),
        "fetch_remote": ("git", "fetch", "origin"),
        "push_branch": ("git", "push", "origin"),
        "pull_remote": ("git", "pull", "origin", "main"),
        "clone_repo": ("git", "clone"),
    },
}


def _tokens(value: object) -> list[str]:
    if not isinstance(value, str) or len(value) > 600:
        return []
    try:
        return shlex.split(value, posix=True)
    except ValueError:
        return []


def _check(week: str, task: str, value: object) -> bool:
    tokens = _tokens(value)
    if not tokens:
        return False
    wanted = TASKS[week][task]
    if week == "week01" and task == "list_hidden":
        return tokens[0] == "ls" and any(t.startswith("-") and "a" in t for t in tokens[1:])
    if week == "week03" and task == "make_executable":
        return tokens[0] == "chmod" and "script.sh" in tokens and ("+x" in tokens or "755" in tokens)
    # Check valid command prefix, required operands in order, allowing optional flags.
    if tokens[0] != wanted[0]:
        return False
    remaining = tokens[1:]
    for token in wanted[1:]:
        try:
            index = remaining.index(token)
        except ValueError:
            return False
        remaining = remaining[index + 1:]
    # Avoid accepting a prefix such as `git clone` without specifying any repository.
    if week == "week06" and task == "clone_repo":
        return len(tokens) >= 3
    if week == "week06" and task == "add_remote":
        return len(tokens) >= 5
    if week == "week04" and task == "commit_change":
        return len(tokens) >= 4
    return True


def check_week(week: str, payload: object) -> dict:
    """Return per-command feedback, five maximum points per worksheet."""
    if not isinstance(payload, dict) or not isinstance(payload.get("commands"), dict):
        commands = {}
    else:
        commands = payload["commands"]
    checks = {name: _check(week, name, commands.get(name)) for name in TASKS[week]}
    return {"score": sum(checks.values()), "max_score": len(checks), "checks": checks}


def validate_owner(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", value):
        raise ValueError("Invalid GitHub username")
    return value


def grade(root: Path, owner: str) -> dict:
    owner = validate_owner(owner)
    base = root / "submissions" / owner
    status = "reference_repository" if owner.lower() == "vmatee" and not base.exists() else "graded"
    submitted, rows, earned, possible = 0, {}, 0, 0
    for week in TASKS:
        path = base / week / "answers.json"
        if not path.is_file():
            rows[week] = {"status": "not_submitted", "score": 0, "max_score": 5}
            continue
        submitted += 1
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError):
            document = None
        outcome = check_week(week, document)
        rows[week] = {"status": "checked", **outcome}
        earned += outcome["score"]
        possible += outcome["max_score"]
    if submitted == 0 and status != "reference_repository":
        status = "no_submissions"
    elif submitted > 0 and earned < possible:
        status = "needs_correction"
    return {
        "github_username": owner, "status": status,
        "submitted_weeks": submitted, "points_earned": earned,
        "points_possible_for_submitted": possible, "points_possible_all": 30,
        "weeks": rows,
        "warning": "Practice checks only; not official course grades or evidence of command execution.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Assess visible JSON command worksheets without executing student code")
    parser.add_argument("--repository-owner", required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = grade(args.root, args.repository_owner)
    body = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(body + "\n", encoding="utf-8")
    print(body)
    if report["status"] in ("no_submissions", "needs_correction"):
        sys.exit(1)


if __name__ == "__main__":
    main()
