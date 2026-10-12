# Linux, Git & GitHub Labs

[![Learning checks](https://github.com/VMatee/linux-git-github-labs/actions/workflows/autograde.yml/badge.svg)](https://github.com/VMatee/linux-git-github-labs/actions/workflows/autograde.yml)

**From your first Linux command to your first collaborative pull request.**

A hands-on, beginner-friendly engineering course taught through short explanations, practical terminal exercises, and real GitHub workflows. You only need basic programming experience (Python, C, or C++); no prior Linux or Git experience is assumed.

**15 sessions · Linux command line · Git · GitHub · collaboration · portfolio**

## Start learning

1. [Read the student setup guide](docs/STUDENT_GUIDE.md).
2. [Explore the 15-session learning roadmap](COURSE_PLAN.md).
3. Open [Week 01: Linux navigation](weeks/week01/README.md) and follow the exercises.
4. Work in a **disposable practice directory** and keep your work in your own GitHub fork.
5. Use [GitHub Actions](https://github.com/VMatee/linux-git-github-labs/actions) to check the early command worksheets.

> **Windows users:** Linux commands are intended for an actual Linux shell such as Ubuntu, WSL, or a lab Linux computer. PowerShell/CMD syntax is not always equivalent.

## Learning roadmap

| Stage | Sessions | You'll learn |
| --- | --- | --- |
| Terminal essentials | 01–03 | Directories, files, pipes, permissions, processes |
| Version control | 04–06 | Commits, branches, merges, remotes |
| Collaboration | 07–09 | Forks, pull requests, code review, conflicts |
| Engineering workflow | 10–12 | GitHub Actions, team branches, integration |
| Professional portfolio | 13–15 | Documentation, a working project, demo |

[Browse all weekly lessons →](weeks/)

## Your first GitHub contribution

```bash
git clone https://github.com/YOUR_USERNAME/linux-git-github-labs.git
cd linux-git-github-labs
git switch -c lab/week01
mkdir -p submissions/YOUR_USERNAME/week01
cp templates/week01/answers.json submissions/YOUR_USERNAME/week01/answers.json
```

Replace `YOUR_USERNAME` with your GitHub username, then edit the copied worksheet and follow the [student guide](docs/STUDENT_GUIDE.md) to commit and push. Fork this repository on GitHub **before** cloning your copy.

## What you'll create

- Terminal practice you can explain and repeat.
- A readable commit history and meaningful feature branches.
- Pull requests with a clear description and review discussion.
- A small program with automated checks.
- A portfolio-ready GitHub project with a useful README.

## Getting help

Read the relevant [weekly lesson](weeks/) first. If a command fails, capture the command, its exact error message, and what you expected it to do. Discuss it in your class channel. Please do not open public issues containing class-specific information or personal records.

**Safety:** never commit passwords, API tokens, private emails, student IDs, grades, or confidential course files. Run destructive commands only in temporary practice directories.

## Community & license

Useful open-source contributions are welcome—see [CONTRIBUTING.md](CONTRIBUTING.md). Following, starring, and forking are different GitHub features; stars and follower counts are **optional** and not part of coursework.

Code is MIT licensed; original lesson text is licensed under [CC BY 4.0](CONTENT_LICENSE.md).

Maintained by [VMatee](https://github.com/VMatee).
