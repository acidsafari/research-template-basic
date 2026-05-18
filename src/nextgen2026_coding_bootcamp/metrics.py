"""Standardized metrics for research workflows."""

from __future__ import annotations
import numpy as np


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Return mean squared error."""
    y_true_array = np.asarray(y_true, dtype=float)
    y_pred_array = np.asarray(y_pred, dtype=float)
    if y_true_array.shape != y_pred_array.shape:
        raise ValueError("y_true and y_pred must have the same shape")
    return float(np.mean((y_true_array - y_pred_array) ** 2))


def coefficient_norm(coeffs: np.ndarray) -> float:
    """Return the L2 norm of fitted coefficients."""
    return float(np.linalg.norm(np.asarray(coeffs, dtype=float)))
