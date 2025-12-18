# Setting Up Git Pre-commit Hooks

This guide explains how to set up automatic pre-commit checks to avoid CI failures.

## Option 1: Manual Scripts (Recommended for Windows)

### Windows (.bat file)

Before committing, run:
```cmd
pre-commit.bat
```

If all checks pass, proceed with your commit:
```cmd
git add .
git commit -m "Your commit message"
```

### Unix/Mac/Linux (.sh file)

Before committing, run:
```bash
./pre-commit.sh
```

If all checks pass, proceed with your commit:
```bash
git add .
git commit -m "Your commit message"
```

## Option 2: Automatic Git Hooks (Unix/Mac/Linux)

To automatically run checks before every commit:

1. **Install the git hook**:
   ```bash
   # Copy the pre-commit hook to .git/hooks/
   cp .githooks/pre-commit .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

2. **Or use the setup script**:
   ```bash
   # Make the setup script executable
   chmod +x setup-git-hooks.sh
   ./setup-git-hooks.sh
   ```

Now, every time you run `git commit`, the pre-commit checks will run automatically.

### To skip the hook (not recommended):

```bash
git commit --no-verify
```

## What the Pre-commit Scripts Do

1. **Format code** with `black` (auto-fixes formatting)
2. **Check code style** with `flake8` (warnings only, non-blocking)
3. **Check types** with `mypy` (warnings only, non-blocking)
4. **Run tests** with `pytest` (must pass)

## Troubleshooting

### "Poetry is not installed"
Install Poetry: https://python-poetry.org/docs/#installation

### "Tests are failing"
Fix the failing tests before committing. The script will exit with an error code.

### "Black found formatting issues"
The script automatically fixes formatting. Just run it again or commit the formatted files.

### "I want to skip the hook"
Use `git commit --no-verify`, but be aware that CI will likely fail.

## Integration with IDEs

### VS Code

Add to `.vscode/tasks.json`:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Pre-commit Check",
            "type": "shell",
            "command": "${workspaceFolder}/pre-commit.sh",
            "windows": {
                "command": "${workspaceFolder}/pre-commit.bat"
            },
            "problemMatcher": []
        }
    ]
}
```

### PyCharm

1. Go to **File** → **Settings** → **Tools** → **External Tools**
2. Click **+** to add a new tool
3. Configure:
   - **Name**: Pre-commit Check
   - **Program**: `pre-commit.bat` (Windows) or `pre-commit.sh` (Unix)
   - **Working directory**: `$ProjectFileDir$`

