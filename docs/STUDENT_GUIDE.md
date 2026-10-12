# Student guide · Set up, practice, and submit

Welcome to Linux, Git & GitHub Labs! You do **not** need to know Git or Linux before starting.

## 1. Before your first lab

- Create a GitHub account with a username you are comfortable showing publicly.
- Install [Git](https://git-scm.com/downloads) and check: `git --version`.
- For Linux lessons, use an Ubuntu/Linux shell (a lab Linux computer or WSL on Windows).
- Configure your Git commit identity (you may use a verified GitHub noreply address):

```bash
git config --global user.name "Your Name"
git config --global user.email "your-verified-email@example.com"
```

Never put your GitHub password or access token into a repository.

## 2. Make your fork

Open [the course repository](https://github.com/VMatee/linux-git-github-labs) and click **Fork**. Select your own account, then clone **your fork**:

```bash
git clone https://github.com/YOUR_USERNAME/linux-git-github-labs.git
cd linux-git-github-labs
git remote -v
```

Replace `YOUR_USERNAME` everywhere with your GitHub username. Confirm that `origin` points to your account—not `VMatee`.

## 3. Complete your first worksheet

```bash
git switch -c lab/week01
mkdir -p submissions/YOUR_USERNAME/week01
cp templates/week01/answers.json submissions/YOUR_USERNAME/week01/answers.json
```

Open `submissions/YOUR_USERNAME/week01/answers.json` in an editor. Fill the **command strings** requested by [Week 01](../weeks/week01/README.md), using valid JSON syntax. Practice each command separately in a throwaway Linux working directory.

```bash
git status
git add submissions/YOUR_USERNAME/week01/answers.json
git commit -m "lab01: practice Linux navigation"
git push -u origin lab/week01
```

On GitHub, create a pull request **from `lab/week01` into `main` of your own fork** (not into the instructor's repository). Inspect the changes and merge it when ready.

## 4. Check your result

After merging, open **Actions** in your own fork. GitHub may ask you to enable workflows on a newly forked repository. The **Autograde** workflow runs on pushes to your fork; you can also run it via **Run workflow** on `main`.

If a check fails, read the logs, update your worksheet, commit, and push again. The checks provide feedback for Weeks 01–06. They do not replace the in-class practical work.

For later weeks, follow the linked weekly lessons and your lecturer's submission instructions.

## 5. Share your work safely

Submit your **GitHub username and fork URL** using the private classroom channel provided by your lecturer. Do not post real names with student IDs, class rosters, personal email addresses, credentials, or grade details in public GitHub Issues or files.

## 6. Build a lasting portfolio

Choose descriptive repository names, add installation/run instructions, write tests, and make small meaningful commits. Use GitHub Issues and pull requests to show how you collaborate. Stars and followers are optional—not proof of skill.

**Troubleshooting:** `git status` explains your local changes; `git remote -v` shows where you will push; the Actions tab contains workflow logs.
