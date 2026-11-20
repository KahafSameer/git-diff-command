# git diff Practice: CLI To-Do App

A repo used to practice `git diff`. Its content is a small **Python command-line to-do app** in `python_mini_project/`.

## The app (`python_mini_project/main.py`)

- Add, list and remove tasks (by ID), and mark them completed
- Tasks are saved to `tasks.json`
- Standard library only (`json`, `os`)

```bash
git clone https://github.com/KahafSameer/git-diff-command.git
cd git-diff-command/python_mini_project
python main.py
```

More details are in [python_mini_project/README.md](python_mini_project/README.md).

## git diff cheatsheet

```bash
git diff                 # unstaged changes
git diff --staged        # staged changes
git diff HEAD~1 HEAD     # last commit
git diff main..feature   # between branches
```
