import numpy as np
from leymosun.random import get_rng
from numpy.random import PCG64, BitGenerator


def goe(matrix_order: int, scale: float = 1.0, loc: float= 0.0, bitget: BitGenerator = PCG64, seed_bits: int = 64) -> np.array:
    """Sample a square matrix from Gaussian Orthogonal Ensemble (GOE)
    
     Wigner, E. P. (1955). "Characteristic Vectors of Bordered Matrices with 
     Infinite Dimensions," 
     Annals of Mathematics*, 62(3), 548–564.

    Args:
        matrix_order: Order of the square matrix
        scale: Sigma of the Gaussian, defaults to 1.0
        loc: Location of the Gaussian, defaults to 0.0
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        np.array: square numpy array
    """
    rng = get_rng(bitgen=bitget, seed_bits=seed_bits)
    A = rng.normal(size=(matrix_order, matrix_order), scale=scale, loc=loc)
    return 0.50 * (A + A.transpose())


def wigner(locations: np.array, domain_boundary=2.0):
    """Wigner semi-circle density for GOE

    Density is defined as
    \rho(\lambda) = \frac{2}{\pi \cdot \sigma^{2}} \sqrt{\sigma^{2}-\lambda^{2}}

    Args:
        locations: An eigenvalue locations.
        domain_boundary: Domain boundary value (sigma for GOE), [-2sigma, 2sigma]

    Returns:
        The density at the locations, list.

    """
    domain_boundary_sqr = domain_boundary**2
    return [
        2.0
        * np.sqrt(np.abs(domain_boundary_sqr - x**2))
        / (domain_boundary_sqr * np.pi)
        for x in locations
    ]


def wigner_spacing(s:float):
    """ Nearest Neigbour Spacing Distribution
    
    Wigner, E. P. (1957). "Statistical Theory of Spectra: Fluctuations" 
    Annals of Mathematics*, 65(2), 203–216.
    
    P(s) = \frac{\pi}{2} \cdot s \exp(-\frac{\pi}{4} \cdot s^{2})
    s > 0
    
    Args:
        s: Spacing value

    Returns:
        float, analytic value
    """
    return 0.5*np.pi*s*np.exp(-0.25*np.pi*s*s)
