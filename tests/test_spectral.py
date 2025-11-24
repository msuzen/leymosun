from leymosun.spectral import (
    apply_pbc,
    is_imaginary_zero,
    empirical_spectral_density,
    eigenvalue_on_polynomial,
    unfold_spectra,
    nnsd
)
from leymosun.matrix import ensemble, mixed_ensemble
from leymosun.gaussian import goe
from leymosun.random import normal
import numpy as np


def test_apply_pbc():
    v = [1, 2, 3, 4]
    v_pbc = apply_pbc(v, 10)
    assert len(v_pbc) == 10
    for element, i in zip([1, 2, 3, 4, 1, 2, 3, 4, 1, 2], range(10)):
        assert element == v_pbc[i]


def test_is_imaginary_zero():
    vec = np.array([1.1 + 1e-10j, 1.2 + 1e-10j, 1.3 + 1e-10j])
    assert is_imaginary_zero(vec)


def test_empirical_spectral_density_goe():
    matrices = ensemble(matrix_order=100, ensemble_size=40, sampler=goe)
    _, density, locations = empirical_spectral_density(matrices, scale="wigner")
    mean_inx = np.argmax(density[0])
    mean = locations[mean_inx]
    assert np.abs(mean) > 0.0


def test_empirical_spectral_density_mixed_goe():
    matrices = mixed_ensemble(
        matrix_order=100, ensemble_size=30, degree_of_mixture=0.8, sampler=goe
    )
    _, density, locations = empirical_spectral_density(matrices, scale="wigner", mmes_order=100)
    mode_inx = np.argmax(density[0])
    mode = locations[mode_inx]
    assert np.abs(mode) > 1.0


def test_eigenvalue_on_polynomial():
    x = 0.1
    coeff = np.array([2.1, 1.1, 2.2, 1.3])
    x_expected = 1.5331000000000001
    x_new = eigenvalue_on_polynomial(x, coeff)
    assert np.abs(x_new - x_expected) < 1e-6


def test_unfold_spectra():
    vec, _, deg = unfold_spectra(np.arange(1000), deg_max=4)
    assert np.sum(vec) > 124700
    assert deg == 1
    
def test_nnsd():
    sim_e2 = np.array([normal(size=1000) for _ in range(10)])
    nnsd_densities, locations = nnsd(sim_e2)
    assert nnsd_densities.shape[1] == 48
