# Publishing qfinlib to PyPI

This guide explains how to publish the qfinlib package to PyPI.

## Prerequisites

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   export PATH="$HOME/.local/bin:$PATH"
   ```

2. **Create a PyPI account**:
   - Go to https://pypi.org/account/register/
   - Create an account if you don't have one

3. **Get a PyPI API token**:
   - Go to https://pypi.org/manage/account/token/
   - Create a new API token (scope: "Entire account" for first publish, or project-specific)
   - Copy the token (you'll only see it once!)

## Configuration

Configure Poetry with your PyPI API token:

```bash
poetry config pypi-token.pypi YOUR_API_TOKEN
```

Or for TestPyPI:
```bash
poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry config pypi-token.testpypi YOUR_TESTPYPI_TOKEN
```

## Publishing Steps

### Option 1: Using the publish script

```bash
# Make the script executable
chmod +x publish.sh

# Test on TestPyPI first (recommended)
./publish.sh --test

# Publish to PyPI
./publish.sh
```

### Option 2: Manual steps

1. **Build the package**:
   ```bash
   poetry build
   ```
   This creates distribution files in the `dist/` directory.

2. **Test on TestPyPI first** (recommended):
   ```bash
   poetry publish --repository testpypi
   ```
   
   Then test installation:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ qfinlib
   ```

3. **Publish to PyPI**:
   ```bash
   poetry publish
   ```

## Verifying the Publication

After publishing, verify the package is available:

```bash
pip install qfinlib
python -c "import qfinlib; print(qfinlib.__version__)"
```

## Updating the Package

To publish a new version:

1. Update the version in `pyproject.toml`:
   ```toml
   version = "0.1.1"  # or whatever new version
   ```

2. Also update `qfinlib/__init__.py`:
   ```python
   __version__ = "0.1.1"
   ```

3. Build and publish:
   ```bash
   poetry build
   poetry publish
   ```

## Important Notes

- **TestPyPI first**: Always test on TestPyPI before publishing to production PyPI
- **Version numbers**: PyPI doesn't allow re-uploading the same version. Increment the version for each release
- **Package name**: The name "qfinlib" must be available on PyPI. If it's taken, you'll need to choose a different name
- **Credentials**: Never commit your PyPI API tokens to version control

## Troubleshooting

### "Package name already exists"
- The package name "qfinlib" might be taken on PyPI
- You can check availability at: https://pypi.org/project/qfinlib/
- If taken, update the name in `pyproject.toml` and `setup.py`

### "Authentication failed"
- Verify your API token is correct
- Check token hasn't expired
- Ensure you're using the right token (TestPyPI vs PyPI)

### "Version already exists"
- You can't re-upload the same version
- Increment the version number in `pyproject.toml`

