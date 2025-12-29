"""Unit tests for Portfolio and Position classes."""

from qfinlib.instruments.base import Instrument
from qfinlib.portfolio.portfolio import Portfolio


class DummyInstrument(Instrument):
    """Simple instrument used for testing."""

    def __init__(self, notional_value: float, currency_code: str = "USD"):
        super().__init__()
        self._notional_value = float(notional_value)
        self._currency_code = currency_code

    def notional(self) -> float:
        return self._notional_value

    def currency(self) -> str:
        return self._currency_code


def test_add_position_creates_positions():
    portfolio = Portfolio(name="Test")
    instrument = DummyInstrument(1_000_000, "EUR")

    portfolio.add_position(instrument, quantity=2, entry_price=101.5)

    positions = portfolio.get_positions()
    assert len(positions) == 1
    assert positions[0].instrument is instrument
    assert positions[0].quantity == 2
    assert positions[0].entry_price == 101.5
    assert repr(portfolio) == "Portfolio(Test, 1 positions)"


def test_portfolio_len_and_repr_updates_with_multiple_positions():
    portfolio = Portfolio()
    instruments = [DummyInstrument(10_000 * i) for i in range(1, 4)]

    for idx, instrument in enumerate(instruments, start=1):
        portfolio.add_position(instrument, quantity=idx)
        assert len(portfolio) == idx

    assert "3 positions" in repr(portfolio)
