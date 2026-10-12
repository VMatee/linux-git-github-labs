# Student guide: make a first fork and submit homework

Your instructor will provide the official course repository URL.

1. Create a GitHub account (use a professional nickname, not a student ID).
2. Click **Fork** on the official course repo to create your own public fork.
3. In the fork, go to **Actions** and enable workflows when GitHub asks.
4. On your computer, run:

   ```bash
   git clone https://github.com/YOUR_USERNAME/linux-git-github-labs.git
   cd linux-git-github-labs
   git switch -c lab/week01
   mkdir -p submissions/YOUR_USERNAME/week01
   cp templates/week01/answers.json submissions/YOUR_USERNAME/week01/answers.json
   ```

5. Fill out the answers using a text editor and save them as valid JSON.
6. Commit and push:

   ```bash
   git add submissions/YOUR_USERNAME/week01/answers.json
   git commit -m "lab01: practice basic Linux commands"
   git push -u origin lab/week01
   ```

7. Inspect **Actions → Autograde** in your own fork. Review the results and
   download its `grading-report` artifact if you want to see your own feedback.
8. For subsequent weeks, follow your lecturer's instructions about branches.
   Keep the existing submissions; do not overwrite a previous week's work.

**What to submit to the lecturer:** your GitHub username and public fork URL
through the private course registration channel, not through GitHub Issues.
The instructor will use the private roster for aggregation.

## Important

- Auto-grader checks visible answers; it does not prove you ran a command.
- Never put tokens, private class files, access keys, student IDs or grades
  into your public repository.
- Do not copy answers or fake commits. Be ready to explain commands in class.
- Stars, followers and fork counts are not graded.
- After this course, keep your repository clean and build your own portfolio.
