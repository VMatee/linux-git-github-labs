# Help — Common Windows/WSL2 and Ubuntu problems

**Always check the terminal first:** `wsl` runs in **Windows PowerShell**; `sudo`, `apt` and course Linux commands run in **Ubuntu**.

## Windows / WSL2 installation

### `wsl` is not recognized / installer fails

Check your Windows version using `winver`. Windows 10 version 2004 (Build 19041+) or Windows 11 is needed for this installation path. If WSL is installed but Ubuntu is missing, run in Administrator PowerShell:

```powershell
wsl --list --online
wsl --install -d Ubuntu
```

### Administrator access is required

Start PowerShell with **Run as administrator**. On school-managed computers, ask campus IT to install WSL. Do not bypass device restrictions.

### Download stays at 0%

Microsoft suggests this alternative in Administrator PowerShell:

```powershell
wsl --install --web-download -d Ubuntu
```

### Error `0x80370102` / Virtual Machine Platform

WSL2 needs supported hardware virtualization. Check **Task Manager → Performance → CPU → Virtualization**. If it says Disabled, ask your PC manufacturer or IT before modifying BIOS/UEFI. See [Microsoft troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting) for the required Windows components, then restart.

### WSL VERSION shows 1 instead of 2

Use the exact name from `wsl --list --verbose` in PowerShell; example:

```powershell
wsl --set-version Ubuntu 2
wsl --list --verbose
```

## Using the Ubuntu terminal

### `sudo` is not recognized

You probably typed a Linux command in Windows PowerShell. Open **Start → Ubuntu** and run the command there.

### Linux password is invisible

This is expected for Ubuntu's initial password setup and `sudo`. Carefully type the password and press Enter.

### GitHub CLI `gh` is not available

Inside Ubuntu try:

```bash
sudo apt update
sudo apt install -y gh
```

If it says 'Unable to locate package gh', follow the official [GitHub CLI Linux installation instructions](https://github.com/cli/cli/blob/trunk/docs/install_linux.md) for its signed package repository.

### Git asks 'Please tell me who you are'

Inside Ubuntu (not PowerShell) set:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your-verified-email@example.com"
```

### Git push asks for GitHub password / authentication fails

GitHub HTTPS Git pushes do not accept your account password. From Ubuntu:

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh auth status
```

Logging in with GitHub CLI on **Windows PowerShell** does not automatically authenticate Git inside **WSL Ubuntu**.

### `git push` reports repository not found or permission denied

Run `git remote -v` and verify that `origin` points to **your fork**, `https://github.com/YOUR_USERNAME/linux-git-github-labs.git`, not the teacher's repository. Check the account shown by `gh auth status`.

### Actions not running on a fork

Open **your fork → Actions**, enable workflows if prompted, then commit and push to your fork. Check the Actions run and the worksheet path: `submissions/YOUR_USERNAME/weekNN/answers.json`.

### WSL files appear under `/mnt/c/...`

Use `cd ~` and `mkdir -p ~/projects`; clone there. Access current Linux files in Windows Explorer using `explorer.exe .`.

## Ask for help safely

In the private class channel share: your OS, step number, attempted command, and exact error with any personal information, passwords, access tokens, and email addresses removed. **Do not use `wsl --unregister` to troubleshoot:** it erases your Linux distribution's files.

References: [Microsoft WSL installation](https://learn.microsoft.com/en-us/windows/wsl/install) · [Microsoft troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting) · [GitHub CLI](https://cli.github.com/manual/)
