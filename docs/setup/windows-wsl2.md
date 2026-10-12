# Windows 10/11 — Install Ubuntu with WSL2

**Goal:** Run real Ubuntu Linux commands on your Windows computer, without replacing Windows or dual-booting. All course Linux/Git commands will run **inside Ubuntu**, not Windows PowerShell.

> **Important:** Commands labeled *PowerShell* are typed in Windows; commands labeled *Ubuntu* are typed in the Ubuntu app. They are not interchangeable.

## Step 1 — Check your Windows version

1. Press **Windows + R**.
2. Type `winver` and press Enter.
3. Confirm **Windows 11** or **Windows 10 version 2004 (Build 19041) or newer**.
4. Confirm that you have an internet connection, free disk space, and Windows Administrator permission (or ask campus IT).
5. Save your work because installation may request a restart.

## Step 2 — Install WSL and Ubuntu (Windows PowerShell as Administrator)

1. Open the **Start** menu, type **PowerShell**.
2. Right-click it, choose **Run as administrator**, and accept the prompt.
3. Paste this command and press Enter:

```powershell
wsl --install -d Ubuntu
```

4. Wait for installation, then **restart Windows** if prompted.
5. If the installer says Ubuntu is already installed, do not reinstall or erase it. Continue to the version check.

## Step 3 — Create an Ubuntu user (Ubuntu terminal)

1. Open **Start → Ubuntu**. (Alternatively, from PowerShell enter `wsl -d Ubuntu`).
2. On first launch, wait for Linux setup and choose a **Linux username** (for example, `student`).
3. Create and confirm a **Linux password**. The screen shows no characters as you type—that is normal.
4. You should see a prompt similar to `student@computer:~$`. You are now **inside Ubuntu**.

## Step 4 — Confirm it is WSL2 (Windows PowerShell)

Open a Windows PowerShell window and run:

```powershell
wsl --update
wsl --list --verbose
```

Look for your Ubuntu distribution, with `VERSION` equal to **2**. The name might be `Ubuntu` or `Ubuntu-24.04`; the state may be Running or Stopped.
If VERSION is **1**, use your **exact distribution name** from the list:

```powershell
wsl --set-version Ubuntu 2
wsl --list --verbose
```

Never run `wsl --unregister` to troubleshoot; that command deletes the Linux distribution's data.

## Step 5 — Install Git, Python, and GitHub CLI (Ubuntu terminal)

Reopen **Ubuntu**, then copy these **Linux** commands:

```bash
cd ~
sudo apt update
sudo apt install -y git gh python3 python3-pip python3-venv
```

When `sudo` asks for a password, enter your **Ubuntu password** (characters stay invisible). Verify:

```bash
git --version
python3 --version
gh --version
```

If the `gh` package cannot be found, see [troubleshooting](troubleshooting.md#github-cli-gh-is-not-available).

## Step 6 — Connect your Git and GitHub account (Ubuntu terminal)

Replace the example name and email with your own. Use a GitHub-verified email or your GitHub noreply email.

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-verified-email@example.com"
gh auth login --hostname github.com --git-protocol https --web
```

Follow the terminal's browser/device-code sign-in flow. If Ubuntu cannot open a browser automatically, enter the shown URL and one-time code in your **Windows browser**. Then:

```bash
gh auth setup-git
gh auth status
git config --global user.name
git config --global user.email
```

**Windows Git settings and WSL Ubuntu Git settings are different.** Configure and authenticate Git **inside Ubuntu** even if Git already works in PowerShell. Never paste tokens into files.

## Step 7 — Create your Linux workspace (Ubuntu terminal)

```bash
cd ~
mkdir -p ~/projects
cd ~/projects
pwd
```

Expected path: something like `/home/student/projects`. Store Linux projects here, **not** under `/mnt/c/Users/...`, for better file permissions and performance.
To view the current Ubuntu folder in Windows File Explorer:

```bash
explorer.exe .
```

## Step 8 — Start the course

Follow the [Student guide](../STUDENT_GUIDE.md) to fork, clone, verify, and submit your first lab. All subsequent `bash` examples run in your **Ubuntu terminal**.

## Official references

- [Microsoft WSL install](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Microsoft WSL commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)
- [Microsoft filesystems guide](https://learn.microsoft.com/en-us/windows/wsl/filesystems)
- [GitHub CLI sign-in](https://cli.github.com/manual/gh_auth_login)
- [Course troubleshooting](troubleshooting.md)
