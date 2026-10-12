# Student setup — Choose your operating system

All course exercises use an **Ubuntu Linux terminal**. If you have Windows, run Ubuntu via **WSL2**; if you already have Ubuntu Linux, use its native terminal.

| My computer | Installation guide | Where I run the class commands |
| --- | --- | --- |
| Windows 10 or 11 | [Install WSL2 and Ubuntu, step by step](windows-wsl2.md) | **Ubuntu app / WSL2 terminal** (not PowerShell or CMD) |
| Ubuntu Linux | [Set up Ubuntu, step by step](ubuntu-linux.md) | **Ubuntu Terminal** |

## Readiness checklist

- [ ] I can open an Ubuntu terminal.
- [ ] If I use Windows, `wsl --list --verbose` shows my Ubuntu distro running **WSL version 2**.
- [ ] Inside Ubuntu, `git --version`, `python3 --version`, and `gh --version` work.
- [ ] I configured Git name/email inside Ubuntu and can run `gh auth status`.
- [ ] My course project lives inside `~/projects/` (on WSL2: **not** `/mnt/c/Users/...`).
- [ ] After cloning my fork, `bash scripts/check_environment.sh` reports ready.

Then follow the [Student guide](../STUDENT_GUIDE.md) and [Week 01](../../weeks/week01/README.md).
Have a problem? See [troubleshooting](troubleshooting.md).

## Know which terminal you are using

| Windows PowerShell | Ubuntu Bash |
| --- | --- |
| Example prompt: `PS C:\Users\Student>` | Example prompt: `student@pc:~$` |
| For installing and checking WSL | For `sudo`, `pwd`, `ls`, `git`, all exercises |
