# Ubuntu Linux — Native installation guide

This page is for students who already use Ubuntu Linux directly. **You do not need WSL2.** WSL2 is for Windows PCs. Other Linux distributions can run the labs but may use different package installation commands.

## Step 1 — Open your terminal

On Ubuntu, press **Ctrl + Alt + T** or search for **Terminal** in Applications. Type:

```bash
cat /etc/os-release
uname -s
```

The second command should print `Linux`.

## Step 2 — Install the course tools

Run inside Ubuntu (enter your Ubuntu password when asked):

```bash
sudo apt update
sudo apt install -y git gh python3 python3-pip python3-venv
```

Check that the tools work:

```bash
git --version
python3 --version
gh --version
```

If `gh` is unavailable, see [troubleshooting](troubleshooting.md#github-cli-gh-is-not-available).

## Step 3 — Configure Git and log into GitHub

Use **your own name and GitHub-verified email** (or a GitHub noreply email):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-verified-email@example.com"
gh auth login --hostname github.com --git-protocol https --web
```

Approve the sign-in in your browser. If it does not open, use the device URL/code shown in the terminal. Then:

```bash
gh auth setup-git
gh auth status
```

Never commit your password, GitHub token, or private class information.

## Step 4 — Make a clean workspace

```bash
cd ~
mkdir -p ~/projects
cd ~/projects
pwd
```

Expected: `/home/YOUR_LINUX_USER/projects`.

## Step 5 — Begin

Go to the [Student guide](../STUDENT_GUIDE.md) to fork the course, clone your copy, and run setup checks. The [Week 01 lesson](../../weeks/week01/README.md) uses this same Ubuntu terminal.

References: [GitHub CLI](https://cli.github.com/manual/gh_auth_login) · [Course troubleshooting](troubleshooting.md)
