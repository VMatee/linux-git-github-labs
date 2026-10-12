# Grading policy and trust boundaries

Six worksheets (`week01`–`week06`) can each earn **five practice points**.
These points help students understand their Git and shell vocabulary and help
lecturers identify missing work. The rest of the course requires manual
review and project demonstrations.

The public tests and answers are not secret. Therefore a passing CI check is
**not** evidence of independent work, execution of shell commands, or genuine
collaboration. Treat them as formative feedback, and use random live checks.

The autograder scans only files under
`submissions/<github-username>/weekNN/answers.json`.
The GitHub workflow automatically chooses the fork owner from the GitHub event,
then checks only that owner's folder; it does not publish enrollment information.

### Security

- Do not use `pull_request_target` to execute unknown student code.
- Do not add secrets or credentials to student forks.
- Do not execute uploaded shell scripts in the teacher's grading aggregator.
- The teacher aggregator invokes only `gh api` and `gh run download`, parses
  JSON reports, and writes a private local CSV.
- Mark every final project and demonstration using a rubric and human review.
