# CI/CD Setup Guide

This repository uses GitHub Actions for continuous integration and deployment.

## Workflows

### 1. CI Workflow (`.github/workflows/ci.yml`)

**Triggers:**
- On pull requests to `main`
- On pushes to `main`

**What it does:**
- Runs tests on Python 3.9, 3.10, 3.11, and 3.12
- Runs linting (black, flake8)
- Runs type checking (mypy)
- Runs test suite with coverage
- **Automatically publishes to PyPI** when code is merged to `main`

### 2. TestPyPI Workflow (`.github/workflows/testpypi.yml`)

**Triggers:**
- Manual workflow dispatch (Actions tab → "Publish to TestPyPI")

**What it does:**
- Builds the package
- Publishes to TestPyPI for testing before production release

## Required GitHub Secrets

To enable automatic publishing, you need to set up the following secrets in your GitHub repository:

### Setting up Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**

### Required Secrets

#### `PYPI_API_TOKEN` (Required for automatic publishing)

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token
   - **Token name**: `github-actions-qfinlib` (or any descriptive name)
   - **Scope**: 
     - For first publish: "Entire account"
     - For subsequent publishes: "Project: qfinlib" (if you want project-specific)
3. Copy the token (you'll only see it once!)
4. In GitHub: Create secret named `PYPI_API_TOKEN` with the token value

#### `TESTPYPI_API_TOKEN` (Optional, for TestPyPI workflow)

1. Go to https://test.pypi.org/manage/account/token/
2. Create a new API token
3. Copy the token
4. In GitHub: Create secret named `TESTPYPI_API_TOKEN` with the token value

## How It Works

### Automatic Publishing Flow

1. **Developer creates a PR** → CI runs tests
2. **PR is reviewed and approved**
3. **PR is merged to `main`** → CI runs again
4. **If tests pass** → Package is automatically built and published to PyPI
5. **Package is available** on PyPI within minutes

### Manual TestPyPI Publishing

1. Go to **Actions** tab in GitHub
2. Select **"Publish to TestPyPI"** workflow
3. Click **"Run workflow"**
4. Optionally specify a version number
5. Click **"Run workflow"** button

## Version Management

- Version is managed in `pyproject.toml` and `qfinlib/__init__.py`
- **Important**: PyPI doesn't allow re-uploading the same version
- Before merging to main, ensure the version is incremented if it's a new release

To update version:
```bash
poetry version patch  # 0.1.0 → 0.1.1
poetry version minor  # 0.1.0 → 0.2.0
poetry version major  # 0.1.0 → 1.0.0
```

Then update `qfinlib/__init__.py`:
```python
__version__ = "0.1.1"  # Match the version in pyproject.toml
```

## Troubleshooting

### "PYPI_API_TOKEN secret not set"

- The workflow will still build the package but won't publish
- Check that you've added the secret in GitHub Settings
- Verify the secret name is exactly `PYPI_API_TOKEN`

### "Version already exists on PyPI"

- You can't re-upload the same version
- Increment the version in `pyproject.toml` and `qfinlib/__init__.py`
- Commit and push the version change

### "Package name already exists"

- The package name "qfinlib" might be taken
- Check availability at: https://pypi.org/project/qfinlib/
- If taken, you'll need to choose a different name and update `pyproject.toml`

### CI Fails on Tests

- Fix the failing tests before merging
- All tests must pass for the package to be published

## Security Notes

- **Never commit API tokens** to the repository
- Secrets are encrypted and only accessible to GitHub Actions
- Use project-specific tokens when possible (after first publish)
- Rotate tokens periodically for security

## Testing the CI Locally

You can test the build process locally:

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run linters
poetry run black --check .
poetry run flake8 qfinlib tests
poetry run mypy qfinlib

# Build package
poetry build
```

