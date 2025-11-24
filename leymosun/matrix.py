import numpy as np
from typing import Callable
from leymosun.random import binomial


def ensemble(
    matrix_order: int, ensemble_size: int, sampler: Callable[[int], np.array]
) -> list:
    """Generate a representative matrix ensemble given sampler function

    Args:
        matrix_order: A square matrix size, order.
        ensemble_size: The number of matrices to generate.
        sampler: A function that samples the matrix ensemble.

    Returns:
        Sampled representative matrix ensemble, 1D list.
    """
    return [sampler(matrix_order) for _ in range(ensemble_size)]


def mixed_ensemble(
    matrix_order: int,
    ensemble_size: int,
    degree_of_mixture: float,
    sampler: Callable[[int], np.array],
) -> list:
    """Generate a representative mixed matrix ensemble given sampler function.
       Implements Mixed Matrix Ensemble Sampling (MMES) algorithm [suzen21]
       Suzen 2021 https://hal.science/hal-03464130

    Args:
        matrix_order: A square matrix size, order.
        ensemble_size: The number of matrices to generate.
        degree_of_mixture: This sets the mixture level [0,1],
        closer to 1.0 ensemble is closer to
        sampler: A function that samples the matrix ensemble.

    Returns:
        Sampled representative mixed matrix ensemble, 1D list.
    """
    mixed_sample = []
    for _ in range(ensemble_size):
        mixed_order = binomial(n=matrix_order, p=degree_of_mixture)
        mixed_sample.append(sampler(mixed_order))
    return mixed_sample


def offdiagonal(A: np.array) -> np.array:
    """Extract offdiagonal elements from a square matrix into a vector

    Args:
        A: A square matrix

    Returns:
        np.array: 1D array.
    """
    matrix_order = A.shape[0]
    tril_ix = np.tril_indices(matrix_order, k=-1)
    triu_ix = np.triu_indices(matrix_order, k=1)
    od = A[tril_ix].flatten()
    return np.hstack([od, A[triu_ix].flatten()]).flatten()
