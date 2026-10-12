"""Aggregate formative public-fork GitHub Actions reports into LOCAL private CSV.

Requires GitHub CLI authenticated in a teacher workstation. Never executes student code.
"""
import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import tempfile


def safe_login(value: str) -> bool:
    import re
    return bool(re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?", value))


def latest_run(payload: dict) -> dict | None:
    runs = payload.get("workflow_runs", [])
    if not isinstance(runs, list) or not runs:
        return None
    return max(runs, key=lambda run: run.get("created_at", ""))


def gh(*args: str, timeout: int = 75) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=timeout, check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip()[:250] or "GitHub CLI command failed")
    return result.stdout


def collect_one(row: dict, include_details: bool = True) -> dict:
    login = row["github_username"].strip()
    repo = (row.get("repository") or "linux-git-github-labs").strip()
    output = {
        "section": row["section"].strip(), "github_username": login,
        "repository": repo, "workflow_state": "unknown",
        "points_earned": "", "points_available": "", "submitted_weeks": "",
        "workflow_url": "", "note": "",
    }
    if not safe_login(login) or not safe_login(repo):
        output["note"] = "Invalid GitHub login or repository"
        return output
    full_name = f"{login}/{repo}"
    try:
        payload = json.loads(gh("api", f"repos/{full_name}/actions/workflows/autograde.yml/runs?per_page=10"))
        run = latest_run(payload)
        if not run:
            output["workflow_state"] = "no_run"
            return output
        output["workflow_state"] = run.get("conclusion") or run.get("status") or "unknown"
        output["workflow_url"] = run.get("html_url", "")
        if not include_details or output["workflow_state"] in ("queued", "in_progress"):
            return output
        with tempfile.TemporaryDirectory(prefix="vmatee-grade-") as tmp:
            gh("run", "download", str(run["id"]), "-R", full_name, "-n", "grading-report", "-D", tmp)
            report_file = Path(tmp) / "summary.json"
            if not report_file.is_file():
                output["note"] = "No summary.json artifact"
                return output
            report = json.loads(report_file.read_text(encoding="utf-8"))
            if report.get("github_username", "").lower() != login.lower():
                raise ValueError("Report username does not match roster")
            output["points_earned"] = report.get("points_earned", "")
            output["points_available"] = report.get("points_possible_for_submitted", "")
            output["submitted_weeks"] = report.get("submitted_weeks", "")
            output["note"] = report.get("status", "")
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.TimeoutExpired) as error:
        output["note"] = str(error)[:250]
    return output


def main():
    parser = argparse.ArgumentParser(description="Download student fork Actions reports into a LOCAL private section CSV")
    parser.add_argument("--roster", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--skip-details", action="store_true", help="Only collect latest workflow CI status")
    args = parser.parse_args()
    if not 1 <= args.workers <= 8:
        parser.error("--workers must be between 1 and 8")
    if args.output.resolve().is_relative_to(Path(__file__).resolve().parents[1]):
        parser.error("Output must be outside this public Git repository")
    if args.roster.resolve().is_relative_to(Path(__file__).resolve().parents[1]):
        parser.error("Roster must be stored outside this public Git repository")
    with args.roster.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.DictReader(stream))
    if not rows or not {"section", "github_username"}.issubset(rows[0]):
        parser.error("Roster must include section,github_username columns")
    gh("auth", "status")
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(collect_one, row, not args.skip_details) for row in rows]
        results = [job.result() for job in as_completed(futures)]
    results.sort(key=lambda row: (row["section"], row["github_username"].lower()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    print(f"Wrote {len(results)} section-labeled status rows to {args.output}")
    print("Store this file privately. CI practice points are not official final grades.")


if __name__ == "__main__":
    main()
