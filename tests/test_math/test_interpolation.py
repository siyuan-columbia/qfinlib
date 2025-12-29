"""Unit tests for interpolation utilities."""

from __future__ import annotations

import math

from qfinlib.math.interpolation.log_linear import LogLinearInterpolator


def test_log_linear_interpolator_matches_exponential_scaling():
    x = [0.0, 1.0]
    y = [1.0, math.exp(-0.05)]

    interp = LogLinearInterpolator()
    result = interp(x, y, 0.5)

    expected = math.exp(-0.05 * 0.5)
    assert math.isclose(result, expected, rel_tol=1e-12)
