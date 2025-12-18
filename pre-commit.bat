@echo off
REM Pre-commit script to run linters and tests
REM Run this before committing to avoid CI failures

echo ========================================
echo Running pre-commit checks...
echo ========================================

REM Check if Poetry is available
where poetry >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Poetry is not installed or not in PATH
    echo Please install Poetry: https://python-poetry.org/docs/#installation
    exit /b 1
)

REM Format code with black
echo.
echo [1/4] Formatting code with black...
poetry run black .
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Black formatting failed
    exit /b 1
)
echo OK: Code formatted successfully

REM Check linting with flake8
echo.
echo [2/4] Checking code style with flake8...
poetry run flake8 qfinlib tests
if %ERRORLEVEL% NEQ 0 (
    echo WARNING: Flake8 found issues (non-blocking)
)

REM Check types with mypy
echo.
echo [3/4] Checking types with mypy...
poetry run mypy qfinlib
if %ERRORLEVEL% NEQ 0 (
    echo WARNING: Mypy found issues (non-blocking)
)

REM Run tests
echo.
echo [4/4] Running tests...
poetry run pytest
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Tests failed
    exit /b 1
)
echo OK: All tests passed

echo.
echo ========================================
echo All pre-commit checks passed!
echo ========================================
exit /b 0

