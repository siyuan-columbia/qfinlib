"""Example showing bond valuation metrics."""

import os
import sys
from datetime import date

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from qfinlib.instruments.bond.bond import Bond
from qfinlib.market.container import MarketContainer
from qfinlib.pricing.engine import PricingEngine


if __name__ == "__main__":
    bond = Bond(
        face_value=100.0,
        currency_code="USD",
        coupon_rate=0.045,
        coupon_frequency=2,
        trade_date=date(2024, 1, 2),
        issue_date=date(2023, 1, 2),
        maturity_date=date(2030, 1, 2),
        quote_convention="price",
    )

    market = MarketContainer(as_of=date(2024, 1, 2))
    # Provide a flat yield for discounting and optional repo/roll inputs
    market.data.update({
        "yield": 0.04,
        "GCRepoCarry_bps_TN_3M_TN_2W_1M_2M_3M_6M_12M": 0.1,
        "CMTRollReturn_bps_1W_2W_1M_2M_3M_6M_12M": -0.2,
    })

    engine = PricingEngine(market)
    metrics = engine.price(bond)

    print("Bond valuation metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
