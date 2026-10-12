# Teacher operations — 2 sections, 140–180 students

GitHub Classroom was retired on 2026-08-28. This workflow requires only GitHub
forks, GitHub Actions and the official GitHub CLI on the teacher computer.

## Before first class

- Publish the public source repo under VMatee.
- Run `python -m pytest -q` and inspect `.github/workflows/autograde.yml`.
- Prepare a private roster CSV **outside** any Git repository, using only
  `section,github_username,repository` columns. Keep the official student ID
  mapping separately in university-approved storage.
- Verify a fresh public fork can enable Actions and publish a report artifact.

## Each teaching week

- Announce the `weeks/weekNN/README.md` exercises.
- Have students commit to their own forks. Ask students to supply the fork URL
  through a private university form at the start of term.
- Have the class verify that GitHub Actions ran on their fork.
- After the deadline, collect feedback from the teacher's computer:

  ```bash
  gh auth login
  python teacher_tools/collect_results.py \
    --roster /secure-location/course-roster.csv \
    --output /secure-location/report-2026-week01.csv
  ```

  `gh` must be installed and authenticated on the teacher computer; do NOT
  place tokens in files or classroom repos. The collector downloads only
  published grading reports; it never executes student code.

- Review failed, missing and suspicious submissions first. Spot-check command
  history and quiz students on what they actually did.
- Maintain manual grades in official university storage. CI is only one piece.

## Section separation

The local roster labels each GitHub account `sec1` or `sec2`. The script preserves
this label in the CSV output, allowing filtered review in Excel or Sheets.
**Do not upload the resulting CSV to a public GitHub repository.**

## Important operational caveats

- Public forks may be renamed, private, deleted, or have Actions disabled.
- GitHub API rate limits can apply across 180 accounts.
- Reports are visible to anyone with access to public Actions artifacts.
  Do not include students' real names, student IDs, or official grades.
- The default visible checker grades six simple command worksheets, NOT
  independent programming, team contribution, or academic integrity.
- The workflow is intentionally read-only, with no privileged triggers,
  repository secrets, or writes back into a student's branch.
