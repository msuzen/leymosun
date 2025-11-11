import numpy as np
from leymosun.random import get_rng
from numpy.random import PCG64, BitGenerator


def goe(matrix_order: int, scale: float = 1.0, bitget: BitGenerator = PCG64, seed_bits: int = 64) -> np.array:
    """Sample a square matrix from Gaussian Orthogonal Ensemble (GOE)

    Args:
        matrix_order: Order of the square matrix

    Returns:
        np.array: square numpy array
    """
    rng = get_rng(bitgen=bitget, seed_bits=seed_bits)
    A = rng.normal(size=(matrix_order, matrix_order), scale=scale)
    return 0.50 * (A + A.transpose())
