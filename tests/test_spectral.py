from leymosun.spectral import (
    apply_pbc,
    is_imaginary_zero,
    get_density,
    empirical_spectral_density,
)
from leymosun.random import get_rng
from leymosun.matrix import ensemble, mixed_ensemble
from leymosun.gaussian import goe
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


def test_get_density():
    rng = get_rng()
    values = rng.normal(0, 1.0, 1000)
    locations = np.arange(-5.0, 5.1, 0.1)
    density, locations = get_density(values, locations)
    mean_index = np.argmax(density)
    assert locations[mean_index] > -1.0
    assert locations[mean_index] < 1.0


def test_empirical_spectral_density_goe():
    matrices = ensemble(matrix_order=100, ensemble_size=40, sampler=goe)
    _, density, locations = empirical_spectral_density(matrices, scale="wigner")
    mean_inx = np.argmax(density)
    mean = locations[mean_inx]
    assert np.abs(mean) < 0.5


def test_empirical_spectral_density_mixed_goe():
    matrices = mixed_ensemble(
        matrix_order=100, ensemble_size=30, degree_of_mixture=0.8, sampler=goe
    )
    _, density, locations = empirical_spectral_density(matrices, scale="wigner")
    mode_inx = np.argmax(density)
    mode = locations[mode_inx]
    assert np.abs(mode) < 1.8
