"""Core model-fitting logic for research workflows."""

from __future__ import annotations
import numpy as np


def fit_linear_mle(x_matrix: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Standard least-squares fit."""
    coeffs, *_ = np.linalg.lstsq(x_matrix, y, rcond=None)
    return coeffs


def fit_ridge_map(
    x_matrix: np.ndarray,
    y: np.ndarray,
    lambda_reg: float = 0.0,
    penalize_bias: bool = False,
) -> np.ndarray:
    """Closed-form ridge regression/MAP estimate."""
    if lambda_reg < 0.0:
        raise ValueError("lambda_reg must be >= 0")

    n_features = x_matrix.shape[1]
    gram = x_matrix.T @ x_matrix
    rhs = x_matrix.T @ y
    penalty = np.eye(n_features)
    if not penalize_bias:
        penalty[0, 0] = 0.0

    regularized = gram + lambda_reg * penalty
    try:
        return np.linalg.solve(regularized, rhs)
    except np.linalg.LinAlgError:
        return np.linalg.lstsq(x_matrix, y, rcond=None)[0]
