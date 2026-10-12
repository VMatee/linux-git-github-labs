# Linux, Git & GitHub Labs — Engineering Version Control

[![Autograde](https://github.com/VMatee/linux-git-github-labs/actions/workflows/autograde.yml/badge.svg)](https://github.com/VMatee/linux-git-github-labs/actions/workflows/autograde.yml)

An open introductory course for programmers who already know some Python,
C/C++, but are new to Linux command-line work and team Git workflows.
Designed for **13–15 class meetings**, two sections, and approximately
**140–180 students**. No GitHub Classroom dependency.

> **Audience:** Engineering students; no prior Linux or Git experience required.
> **Public repo safety:** Never commit student IDs, grades, attendance,
> private emails, passwords, service tokens or confidential coursework.

## Outcomes

1. Navigate Linux files, processes, permissions, streams and SSH safely.
2. Use Git local history, branching, remotes, merges and recovery techniques.
3. Collaborate with GitHub Issues, Forks, Pull Requests and code review.
4. Understand continuous integration with GitHub Actions.
5. Present a clear personal GitHub profile and a maintainable project.

## Start here

- [Course roadmap](COURSE_PLAN.md) — all 15 meetings and corresponding practice.
- [Student guide](docs/STUDENT_GUIDE.md) — fork, clone, submit and get feedback.
- [Teacher guide](docs/TEACHER_GUIDE.md) — two sections and local CSV collector.
- [Grading policy](docs/GRADING.md) — what can and cannot be automated.
- [Weekly labs](weeks) — instructions for weeks 01–15.
- [Submission templates](templates) — JSON command worksheets for weeks 01–06.

## Demo for auto-checking (no network)

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
python scripts/autograde.py --repository-owner example-student --root tests/fixtures/example-repo
```

Students edit their own forks, not this instructor repository. GitHub Actions
runs the checker on `push` and `workflow_dispatch` (students must enable Actions
in newly forked repositories). Score artifacts are for **formative checks**:
automatic answers alone are never sufficient evidence of practical command
execution or project contribution.

## Grading architecture

```text
teacher repo (curriculum + public checker)
                 |
        GitHub Fork per student
                 |
          commits / branches
                 |
        GitHub Actions on fork
                 |
           grading-report
                 |
  teacher-only local roster + collector
                 |
         private CSV per section
```

Grades and real student identities remain local to the instructor. The collector
is not a learning management system and does not replace faculty assessment.

## Open-source participation

Forking, starring, watching and contributing are introduced as different GitHub
activities. **Stars and forks are never required for course credit**, and the
teacher never accepts artificial metrics as a substitute for meaningful work.

## License

MIT for code, lesson material licensed CC BY 4.0 unless otherwise stated in a file.
