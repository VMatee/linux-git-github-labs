# Week 01 — Navigate Linux for the first time

**Same lesson on both OS paths:** Windows → **Ubuntu in [WSL2](../../docs/setup/windows-wsl2.md)**, Linux → **native [Ubuntu Terminal](../../docs/setup/ubuntu-linux.md)**. Every command below runs inside Ubuntu.

**Goal:** learn `pwd`, `ls`, `ls -la`, `mkdir`, `cd` and `touch` through real practice.

## 1. Open the correct terminal

On **Windows**, open the Ubuntu app from the Start menu; do not use CMD or PowerShell for these Linux commands. On **Ubuntu Linux**, press Ctrl + Alt + T. If you have not installed your environment, use the [setup page](../../docs/setup/README.md).

## 2. Make a safe practice folder

Copy the following in **Ubuntu**, one line at a time:

```bash
cd ~
mkdir -p ~/linux-labs/week01
cd ~/linux-labs/week01
pwd
```

The last command prints the path of the current directory, normally ending in `/linux-labs/week01`. This is separate from your GitHub course clone.

## 3. Try your first Linux commands

```bash
ls
mkdir -p workspace
ls -la
cd workspace
pwd
touch notes.txt
ls -la
cd ..
pwd
```

Run each line, observe the result, and explain it in your own words:

| Command | What it means | Look for |
| --- | --- | --- |
| `pwd` | Print current working directory | A path starting with `/home/` |
| `ls` | List files and folders | The `workspace` folder |
| `ls -la` | Show details and hidden entries | Extra columns, `.` and `..` |
| `mkdir -p workspace` | Create a folder if missing | A new `workspace` folder |
| `cd workspace` | Change directory | `pwd` ends in `/workspace` |
| `touch notes.txt` | Make an empty file | `notes.txt` appears in `ls -la` |
| `cd ..` | Go to the parent directory | A shorter path |

## 4. Try an independent challenge

Within your `~/linux-labs/week01` practice directory, create a folder named `examples`, enter it, create an empty file `hello.py`, and list its contents. Explain the difference between **relative paths** (like `examples`) and the **home directory path** (like `~/linux-labs`).

## 5. Submit the worksheet

Follow the [Student Guide — Steps 6–8](../../docs/STUDENT_GUIDE.md). Copy `templates/week01/answers.json` into `submissions/YOUR_USERNAME/week01/answers.json` **inside your own fork**, fill in all five command fields, commit, push, and check GitHub Actions. Do not post your work in the teacher's repository.

**Check your understanding:** You should be able to demonstrate the commands in Ubuntu, not just write answers in JSON. Need help? [Troubleshooting](../../docs/setup/troubleshooting.md).
