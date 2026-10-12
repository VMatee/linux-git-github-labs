# Student guide — Install, fork, clone, and submit

This course supports **Windows 10/11 (Ubuntu in WSL2)** and **Ubuntu Linux (native)**. You only need basic Python/C/C++ programming knowledge; you do not need prior Linux or Git experience.

## Step 1 — Prepare your computer (choose ONE guide)

| You use | What to follow |
| --- | --- |
| **Windows 10/11** | [Install WSL2 + Ubuntu step by step](setup/windows-wsl2.md) |
| **Ubuntu Linux** | [Set up Git, Python and GitHub CLI](setup/ubuntu-linux.md) |

From here onward, **all terminal commands are in the Ubuntu Bash terminal on both computer types**. On Windows, do not paste these commands into PowerShell/CMD. [Confused about terminals?](setup/README.md)

## Step 2 — Verify your tools and sign in (Ubuntu)

Run the following in your Ubuntu terminal:

```bash
git --version
python3 --version
gh --version
git config --global user.name
git config --global user.email
gh auth status
```

If Git name or email is blank, set it to your own name and GitHub-verified email (or GitHub noreply email):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-verified-email@example.com"
```

If `gh auth status` shows that you are not logged into GitHub in Ubuntu, run:

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
```

Complete the sign-in in your web browser, using the one-time code if provided. Do not add passwords or tokens to your project.

## Step 3 — Fork the course on GitHub

1. Sign in at [github.com](https://github.com).
2. Open [VMatee/linux-git-github-labs](https://github.com/VMatee/linux-git-github-labs).
3. Click **Fork** → select **your own GitHub account** → **Create fork**.
4. Check that the repository at the top of the page is `YOUR_USERNAME/linux-git-github-labs`.

Your fork is your personal learning workspace, not the teacher's repository.

## Step 4 — Clone YOUR fork (Ubuntu)

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/YOUR_USERNAME/linux-git-github-labs.git
cd linux-git-github-labs
git remote -v
```

**Replace `YOUR_USERNAME` everywhere** with your real GitHub username. The `origin` URL must point to your GitHub account. For Windows/WSL2, use `~/projects` in the **Linux filesystem**, not `/mnt/c/Users/...`.

Run the readiness check:

```bash
bash scripts/check_environment.sh
```

If anything is missing, use [setup troubleshooting](setup/troubleshooting.md).

## Step 5 — Practice Week 01 in a safe location

Read [Week 01: Your first Linux terminal](../weeks/week01/README.md). Practice file commands in a temporary directory outside this course repository. Understand each step before completing the worksheet.

## Step 6 — Make the first homework branch

Return to your own cloned fork and create a branch:

```bash
cd ~/projects/linux-git-github-labs
git switch -c lab/week01
mkdir -p submissions/YOUR_USERNAME/week01
cp templates/week01/answers.json submissions/YOUR_USERNAME/week01/answers.json
nano submissions/YOUR_USERNAME/week01/answers.json
```

Fill in the requested **command strings** inside the JSON file. Keep quotes and commas valid. In the Nano editor, save with **Ctrl + O**, Enter, and exit with **Ctrl + X**.

## Step 7 — Commit and push to YOUR fork

```bash
git status
git add submissions/YOUR_USERNAME/week01/answers.json
git commit -m "lab01: Linux navigation practice"
git push -u origin lab/week01
```

On GitHub, inspect your feature branch. Optionally open a pull request into `main` of **your own fork** (make sure the **base repository** is your account, not VMatee); review and merge it. Pushing your branch also triggers a learning check.

## Step 8 — Review your GitHub Actions feedback

1. Open **your fork → Actions** in the browser.
2. If asked, **enable workflows** on your fork.
3. Open the most recent **Autograde** run for your branch or `main`.
4. Check whether it succeeded. If not, expand the failed step, read the message, fix your file, commit and push again.

The automated check provides feedback on Weeks 01–06 worksheets; you must still be able to demonstrate the actual commands. For other weeks, follow the assigned project instructions.

## Step 9 — Submit your repository link safely

Share your GitHub username and **fork URL** through the private channel provided by your lecturer. Never upload student IDs, grade records, private emails, passwords, access tokens, or confidential files to public GitHub.

## Next

Follow the [15-session roadmap](../COURSE_PLAN.md) and build a portfolio-quality Python or C/C++ project with a useful README, tests, commits, branches, and pull requests.

**Useful projects matter more than stars and follower counts.**
