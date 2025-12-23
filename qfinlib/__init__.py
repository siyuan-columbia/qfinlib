"""qfinlib - A comprehensive quantitative finance library for hedge fund portfolio management."""

__version__ = "0.1.0"

# Core modules - import at package level
try:
    from qfinlib import core
    from qfinlib.core import date, math, utils
except ImportError:
    pass

# Market data
try:
    from qfinlib import market
    from qfinlib.market.container import MarketContainer
except ImportError:
    pass

# Calibration
try:
    from qfinlib import calibration
    from qfinlib.calibration.curve.builder import CurveBuilder
except ImportError:
    pass

# Instruments
try:
    from qfinlib import instruments
except ImportError:
    pass

# Pricing
try:
    from qfinlib import pricing
    from qfinlib.pricing.engine import PricingEngine
except ImportError:
    pass

# Risk
try:
    from qfinlib import risk
    from qfinlib.risk.calculator import RiskCalculator
except ImportError:
    pass

# Monitoring
try:
    from qfinlib import monitoring
    from qfinlib.monitoring.scanner import Scanner
except ImportError:
    pass

# Portfolio
try:
    from qfinlib import portfolio
    from qfinlib.portfolio.portfolio import Portfolio
    from qfinlib.portfolio.position import Position
except ImportError:
    pass

# Strategy
try:
    from qfinlib import strategy
    from qfinlib.strategy.generator import StrategyGenerator
except ImportError:
    pass

__all__ = [
    "__version__",
    # Core
    "core",
    "date",
    "math",
    "utils",
    # Market
    "market",
    "MarketContainer",
    # Calibration
    "calibration",
    "CurveBuilder",
    # Instruments
    "instruments",
    # Pricing
    "pricing",
    "PricingEngine",
    # Risk
    "risk",
    "RiskCalculator",
    # Monitoring
    "monitoring",
    "Scanner",
    # Portfolio
    "portfolio",
    "Portfolio",
    "Position",
    # Strategy
    "strategy",
    "StrategyGenerator",
]
