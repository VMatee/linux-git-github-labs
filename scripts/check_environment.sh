#!/usr/bin/env bash
# Run from inside Ubuntu (WSL2 or native Linux). Do not print credentials.
set -u
errors=0
if [[ "$(uname -s)" != "Linux" ]]; then
  echo "ERROR: Open an Ubuntu/Linux terminal, not PowerShell or Git Bash."
  exit 1
fi
if [[ -n "${WSL_DISTRO_NAME:-}" ]]; then
  echo "Linux environment: WSL Ubuntu (${WSL_DISTRO_NAME})"
else
  echo "Linux environment: native Linux (or compatible environment)"
fi
for tool in git python3 gh; do
  if command -v "$tool" >/dev/null 2>&1; then
    echo "OK: $tool installed"
  else
    echo "MISSING: $tool; follow docs/setup/README.md"
    errors=1
  fi
done
if command -v git >/dev/null 2>&1; then
  if [[ -z "$(git config --global user.name || true)" ]]; then
    echo "MISSING: Git user.name (see docs/setup/)"
    errors=1
  else
    echo "OK: Git author name configured"
  fi
  if [[ -z "$(git config --global user.email || true)" ]]; then
    echo "MISSING: Git user.email (see docs/setup/)"
    errors=1
  else
    echo "OK: Git author email configured (not displayed)"
  fi
fi
if command -v gh >/dev/null 2>&1; then
  if gh auth status --hostname github.com >/dev/null 2>&1; then
    echo "OK: GitHub CLI signed in"
  else
    echo "MISSING: GitHub CLI login. Run gh auth login and gh auth setup-git."
    errors=1
  fi
fi
case "$PWD" in
  /mnt/*) echo "TIP: Clone your Linux project into ~/projects (not /mnt/c/)." ;;
esac
if (( errors != 0 )); then
  echo "Setup incomplete. See docs/setup/troubleshooting.md"
  exit 1
fi
echo "READY: You can start the Linux, Git and GitHub lessons."
