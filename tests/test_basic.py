"""Basic tests for qfinlib package."""

import qfinlib


def test_package_import():
    """Test that the package can be imported."""
    assert qfinlib is not None


def test_version():
    """Test that version is defined."""
    assert hasattr(qfinlib, "__version__")
    assert qfinlib.__version__ is not None
    assert isinstance(qfinlib.__version__, str)
    assert len(qfinlib.__version__) > 0
