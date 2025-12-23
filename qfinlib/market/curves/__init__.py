"""Curve module."""

# Create placeholder classes if they don't exist yet
from abc import ABC


class Curve(ABC):
    """Base curve class."""

    pass


class DiscountCurve(Curve):
    """Discount curve."""

    pass


class ForwardCurve(Curve):
    """Forward curve."""

    pass


class ZeroCurve(Curve):
    """Zero curve."""

    pass


class SpreadCurve(Curve):
    """Spread curve."""

    pass


__all__ = [
    "Curve",
    "DiscountCurve",
    "ForwardCurve",
    "ZeroCurve",
    "SpreadCurve",
]
