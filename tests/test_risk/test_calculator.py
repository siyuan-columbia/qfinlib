"""Unit tests for RiskCalculator."""

from datetime import date

from qfinlib.instruments.base import Instrument
from qfinlib.market.container import MarketContainer
from qfinlib.portfolio.portfolio import Portfolio
from qfinlib.risk.calculator import RiskCalculator


class DummyInstrument(Instrument):
    """Minimal instrument implementation for risk tests."""

    def __init__(self, notional_value: float = 0.0, currency_code: str = "USD"):
        super().__init__(trade_date=date(2024, 1, 1))
        self._notional_value = notional_value
        self._currency_code = currency_code

    def notional(self) -> float:
        return self._notional_value

    def currency(self) -> str:
        return self._currency_code


def test_risk_calculator_defaults_return_zero_like_values():
    calculator = RiskCalculator(MarketContainer())
    instrument = DummyInstrument(100_000, "GBP")

    assert calculator.pv(instrument) == 0.0
    assert calculator.dv01(instrument) == 0.0


def test_scenario_and_portfolio_risk_return_dicts():
    calculator = RiskCalculator(MarketContainer(as_of=date(2024, 6, 30)))
    instrument = DummyInstrument(50_000)
    portfolio = Portfolio(name="RiskTest")

    portfolio.add_position(instrument, quantity=1.5)

    scenario_result = calculator.scenario_analysis(instrument, shifts=[-10, 0, 10])
    portfolio_result = calculator.portfolio_risk(portfolio)

    assert isinstance(scenario_result, dict)
    assert isinstance(portfolio_result, dict)
    assert "RiskTest" in repr(portfolio)
