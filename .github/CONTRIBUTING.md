# Contributing to qfinlib

Thank you for your interest in contributing to qfinlib!

## Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/your-username/qfinlib.git
   cd qfinlib
   ```

2. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   export PATH="$HOME/.local/bin:$PATH"
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

## Development Workflow

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**

3. **Run pre-commit checks** (IMPORTANT - prevents CI failures):
   ```bash
   # Windows
   pre-commit.bat
   
   # Unix/Mac/Linux
   ./pre-commit.sh
   ```
   
   This will:
   - Auto-format code with black
   - Check code style with flake8
   - Check types with mypy
   - Run tests

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```
   
   **Note**: If you set up git hooks (see `SETUP_GIT_HOOKS.md`), checks run automatically.

4. **Push and create a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- **Formatting**: We use `black` with line length 100
- **Linting**: We use `flake8`
- **Type checking**: We use `mypy`

**Easiest way**: Run the pre-commit script before committing:
```bash
# Windows
pre-commit.bat

# Unix/Mac/Linux
./pre-commit.sh
```

Or manually:
```bash
poetry run black .
poetry run flake8 qfinlib tests
poetry run mypy qfinlib
poetry run pytest
```

## Testing

- Write tests for new features
- Ensure all tests pass: `poetry run pytest`
- Aim for good test coverage

## Pull Request Process

1. Update documentation if needed
2. Ensure CI passes (tests, linting, type checking)
3. Request review from maintainers
4. Once approved and merged, the package will be automatically published to PyPI

## Version Bumping

Version is managed in `pyproject.toml`. When merging to main:
- The CI will automatically publish the package
- Make sure to update the version if it's a new release

## Questions?

Open an issue or contact the maintainers.

