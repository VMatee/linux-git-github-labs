# Architecture and threat model

The source repository is the public course template. The only GitHub workflows
run in students' forks, based on push or manual dispatch. The published
`autograde.py` parses JSON worksheet data without importing or running student
scripts. Only standard-library code parses the worksheets.

The private instructor-only `collect_results.py` runs the official `gh` CLI to
read GitHub workflow reports and downloads JSON artifacts into temporary
folders. It does not run or source downloaded code. Incoming artifact JSON is
untrusted and must never be treated as official grades.

Never insert student names/IDs/tokens into a public fork. No GitHub API secrets
are supplied to Actions. If moving to private grading in the future, assess
untrusted-code execution and restrict cloud workflow permissions first.
