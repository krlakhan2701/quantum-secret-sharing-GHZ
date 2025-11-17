"""
Temporary placeholder for estimate_qber so the notebooks can run.
Replace this with the real implementation when available.
"""

from typing import Union

def estimate_qber(trials: int = 1000, eavesdrop: bool = False) -> float:
    """
    Placeholder QBER estimator.
    - trials: number of Monte-Carlo trials (ignored)
    - eavesdrop: if True returns a larger QBER (simulating Eve)
    Returns a float between 0 and 1.
    """
    # deterministic placeholder values:
    return 0.15 if eavesdrop else 0.02

__all__ = ["estimate_qber"]
