from leymosun.qcore import (
    prepare_entangled,
    fidelity_evolution_pure_ed,
    fidelity_evolution_pure_krylov,
    spread_complexity_evolution # type: ignore
)
from leymosun.rosenzweig import rp
from leymosun.krylov import lanczos, validate_lanczos, get_ritz_matrix
import numpy as np  # pyright: ignore[reportMissingImports]

def test_fidelity():
    N=5
    gg = 0.1
    psi0 = prepare_entangled(N)
    H = rp(2**N, gamma=gg)
    delta = 1e-3
    ndelta = 1000
    _, fidelity = fidelity_evolution_pure_ed(H, psi0, delta, ndelta)
    assert np.sum(fidelity) < 1000
    up_to_dim = 2**N # We cover full Hilbert, but usually Krylov basis can be found much faster. 
    a_n, b_n, K_s = lanczos(H, psi0, up_to_dim)
    _, fidelity = fidelity_evolution_pure_krylov(K_s, H, psi0, delta, ndelta)
    assert np.sum(fidelity) < 1000
    r_matrix = get_ritz_matrix(H, up_to_dim, K_s)
    assert validate_lanczos(H, r_matrix) 
    
def test_spread():
    N=4 
    gg = 1.7  
    psi0 = prepare_entangled(N)
    up_to_dim = 2**N # We cover full Hilbert, but usually Krylov basis can be found much faster. 
    delta = 1.0
    ndelta = 50
    H = rp(2**N, gamma=gg)
    _, _, K_s = lanczos(H, psi0, up_to_dim)
    _, kcs = spread_complexity_evolution(K_s, H, psi0, delta, ndelta)
    assert np.sum(kcs) < 1000