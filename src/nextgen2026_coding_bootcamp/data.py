"""Data handling and reproducibility utilities."""

from __future__ import annotations
import numpy as np


def _to_rng(
    seed: int | None = None, rng: np.random.Generator | None = None
) -> np.random.Generator:
    """
    Standardize random number generator creation.
    If an existing RNG is provided, return it. Otherwise, create a new one from seed.
    """
    if rng is not None:
        return rng
    return np.random.default_rng(seed)
