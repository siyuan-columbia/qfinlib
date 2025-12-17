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

2. **Make your changes** and ensure:
   - Code follows the project style (black, flake8)
   - Tests pass: `poetry run pytest`
   - Type checking passes: `poetry run mypy qfinlib`

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

4. **Push and create a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- **Formatting**: We use `black` with line length 100
- **Linting**: We use `flake8`
- **Type checking**: We use `mypy`

Run before committing:
```bash
poetry run black .
poetry run flake8 qfinlib tests
poetry run mypy qfinlib
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

