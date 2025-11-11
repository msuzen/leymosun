from numpy.random import PCG64, RandomState, BitGenerator
import secrets
import numpy as np


def he_random_integer(bits: int = 64):
    """Generate high-entropy random integer given bits

    Generate a random integer given bits, that is suitable
    for random seeding in simulations.

    Args:
        bits: Number of bits to use, defaults to 64

    Returns:
        Random integer in given bits.

    """
    return secrets.randbits(bits)


def get_rng(bitgen: BitGenerator = PCG64, seed_bits: int = 64):
    """Get new RNG state

    Generate a new RNG state with a 'random' seed
    from the pool

    Args:
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        NumPy random state

    """
    return RandomState(bitgen(seed=he_random_integer(bits=seed_bits)))


def binomial(n: int, p: float, bitgen: BitGenerator = PCG64, seed_bits: int = 64):
    """Get a binomial random number with strong randomness

     Args:
        n: Number of trials, or max integer n, defining [1,n].
        p: probability of success, or probability of selecting the integer between [1,n]
        seed_bits: Number of bits to use to generate seed.
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        integer value

    """
    rng = get_rng(bitgen=bitgen, seed_bits=seed_bits)
    return rng.binomial(n, p)


def randint(
    low: int,
    high: int,
    size: int,
    dtype: np.dtype,
    bitgen: BitGenerator = PCG64,
    seed_bits: int = 64,
):
    rng = get_rng(bitgen=bitgen, seed_bits=seed_bits)
    return rng.randint(low, high, size, dtype)
