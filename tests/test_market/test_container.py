"""Unit tests for MarketContainer."""

from datetime import date

from qfinlib.market.container import MarketContainer


def test_add_and_get_curve():
    container = MarketContainer(as_of=date(2024, 1, 2))
    container.add_curve("discount", {"1Y": 0.02})

    assert container.get_curve("discount") == {"1Y": 0.02}
    assert container.get_curve("missing") is None


def test_add_and_get_surface_and_repr():
    container = MarketContainer()
    container.add_surface("vol", [[0.2, 0.25]])

    representation = repr(container)

    assert container.get_surface("vol") == [[0.2, 0.25]]
    assert "MarketContainer" in representation
    assert "0 curves" in representation
    assert "1 surfaces" in representation
