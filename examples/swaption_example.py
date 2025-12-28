"""Example pricing a vanilla swaption using constant market data."""

import os
import sys
from datetime import date, timedelta

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from qfinlib.instruments.rates.swap.irs import Swap
from qfinlib.instruments.rates.option.swaption import Swaption
from qfinlib.market.container import MarketContainer
from qfinlib.pricing.pricers.rates.swaption import SwaptionPricer


class FlatDiscountCurve:
    def __init__(self, rate: float):
        self.rate = rate

    def discount_factor(self, t: float) -> float:
        return pow((1 + self.rate), -t)


class FlatForwardCurve:
    def __init__(self, forward: float):
        self.forward = forward

    def forward_rate(self) -> float:
        return self.forward


class ConstantVolSurface:
    def __init__(self, vol: float):
        self.vol = vol

    def __call__(self, expiry: float, strike: float, forward: float) -> float:
        return self.vol


if __name__ == "__main__":
    market = MarketContainer(as_of=date(2024, 1, 1))
    market.add_curve("discount_curve", FlatDiscountCurve(rate=0.02))
    market.add_curve("libor3m", FlatForwardCurve(forward=0.025))
    market.add_surface("swaption_vol", ConstantVolSurface(vol=0.20))

    swap = Swap.from_generator(
        "vanilla",
        notional=1_000_000,
        currency="USD",
        fixed_rate=0.03,
        float_forward_curve="libor3m",
        payment_times_fixed=[1, 2, 3, 4, 5],
        payment_times_float=[1, 2, 3, 4, 5],
        pay_fixed=True,
        spread=0.0,
        day_count=1.0,
    )

    expiry_date = market.as_of + timedelta(days=365)
    swaption = Swaption(swap=swap, expiry=expiry_date, option_type="payer")

    pricer = SwaptionPricer()
    result = pricer.price(swaption, market)

    print("Swaption valuation result:")
    for k, v in result.items():
        print(f"  {k}: {v:.6f}")
