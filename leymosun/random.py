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
        integer value from binomial distribution

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
    """Uniform strong random integer on the given interval

     Args:
        low: Lower bound [low, high]
        high: Higher bound [low, high]
        size: Number of integers to generate
        dtype: Number of bits to use to generate seed.
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        integer value from binomial distribution

    """
    rng = get_rng(bitgen=bitgen, seed_bits=seed_bits)
    return rng.randint(low, high, size, dtype)


def random(size: int, bitgen: BitGenerator = PCG64, seed_bits: int = 64):
    """Uniform strong random float in the half open interval [0.1.0]

     Args:
        size: Number of floats to generate
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        np.array of float within the half open interval [0.1.0]

    """
    rng = get_rng(bitgen=bitgen, seed_bits=seed_bits)
    return rng.random(size)

def normal(loc:float=0.0, scale:float=1.0, size:int=None, bitgen: BitGenerator = PCG64, seed_bits: int = 64):
    """Generate Normal distribution numbers, or given Gaussian parameters

     Args:
        loc: mean parameter, defaults to 0.0 for normal.
        scale: sigma, standard deviation, defaults to 1.0 for normal.
        size: Number of floats to generate
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        np.array of float within the half open interval [0.1.0]

    """
    rng = get_rng(bitgen=bitgen, seed_bits=seed_bits)
    return rng.normal(loc=loc, scale=scale, size=size)

def choice(size:int, ndraws:int, replace:bool, bitgen: BitGenerator = PCG64, seed_bits: int = 64):
    """Draw integers from a sequence given size, with or without replacement.
       Zero being the first index.
    
     Args:
        size: upper size of the set.
        ndraws: Number of draws
        replace: With or without replacement
        bitgen: Bitgenerator, defaults PCG64
        seed_bits: Number of bits to use to generate seed.

    Returns:
        np.array of integers.

    """
    rng = get_rng(bitgen=bitgen, seed_bits=seed_bits)
    return rng.choice(a=size, size=ndraws, replace=replace)
