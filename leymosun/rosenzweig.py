from leymosun.random import normal
from leymosun.gaussian import goe
import numpy as np

def diagonal_normal(N:int):
    """
    
    Create square matrix NxN with diagonal normal 

    Args:
        N (int): Matrix order

    Returns:
        np.array: A matrix
    """
    H0 = np.zeros([N,N])
    # H0_diag_indices = np.diag_indices(H0)
    diagonal_vector = normal(size=N)
    diag_i, diag_j = np.diag_indices(N)
    H0[diag_i, diag_j] = diagonal_vector
    return H0

def rp(N:int, gamma:float):
    """
    
    Sample a matrix from RP ensemble
    
    Rosenzweig Porter Ensemble
    
    See M Pino et al 2019 J. Phys. A: Math. Theor. 52 475101
    
    $H_{rp} = H_{0} + N^{-\gamma/2.0} H_{goe}$
    $H_{0} \in \mathbb{R}^{N \times N}$ 
    $diag(H_{0}) \in \mathcal{N}(0,1.0)$
    Wigner-Dyson (Ergodic-Chaotic): $1.0 \gt \gamma \ge 0.0$. 
    Wigner-Dyson-short (Fractal): $2.0 \gt \gamma \gt 1.0$. 
    Poisson (Localized-Regular): $7.0 \gt \gamma \ge 2.0$. 

    Args:
        N (int): Matrix order 
        gamma (float): disorder parameter 

    Returns:
        np.array: Matrix sampled from RP ensemble 
    """
    Hgoe = goe(N)
    H0 = diagonal_normal(N)
    localization_coeff = 1.0/np.sqrt(N**gamma)
    return H0+localization_coeff*Hgoe
