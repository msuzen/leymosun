from leymosun.random import he_random_integer, get_rng, binomial, normal, choice
from numpy.random import RandomState, BitGenerator, PCG64
import numpy as np


def test_random_integer():
    seed_int = he_random_integer(bits=64)
    assert seed_int.bit_length() < 65
    seed_int = he_random_integer(bits=32)
    assert seed_int.bit_length() < 33


def test_get_rng():
    rng = get_rng(bitgen=PCG64, seed_bits=42)
    assert isinstance(rng, RandomState)


def test_binomial():
    n = 1000
    p = 0.7
    values = np.array([binomial(n, p) for _ in range(1000)])
    assert np.mean(values) < 1.1 * n * p


def test_normal():
    n = 1000
    mu = 3.0
    sigma = 1.0
    values = normal(loc=mu, scale=sigma, size=n)
    assert np.mean(values) < 3.1


def test_choice():
    size = 5
    ndraws = 10
    replace = True
    values = choice(size, ndraws, replace)
    assert np.all([(x in [0, 1, 2, 3, 4, 5]) for x in values])
