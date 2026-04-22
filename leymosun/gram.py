from itertools import combinations
import numpy as np # type: ignore


def norm_l2(v):
    """Compute L2 norm of a vector

    Args:
        v: 1D array, vector.

    Returns:
        L2 norm, value.

    """
    return np.sqrt(np.sum(np.abs(v) ** 2))


def normalize_v(v, epsilon=1e-11):
    """Normalize given vector

    Args:
        v: 1D array, vector.
        epsilon: value to check if it is already normalized,
                 defaults to 1e-11.

    Returns:
        L2 norm, value.

    """
    n = norm_l2(v)
    if n < epsilon:
        return v
    return v / n


def oproj(ort, v, epsilon=1e-11):
    """Vector Orthogonal projection: v over ort

    Args:
        ort: 1D array, vector that we are projecting on.
        v: 1D array, vector that is being projected.
        epsilon: value to check if it is already normalized,
                 defaults to 1e-11.

    Returns:
        projected vector, array.

    """
    orth = normalize_v(ort)
    return np.vdot(v, orth) * orth


def gram_schmidt(set_vectors):
    """Ortho-normalize given set of vectors (1D arrays)

    Args:
        set_vectors: list of 1D arrays, that we
        are orthonormalizing.

    Returns:
        orthonormalized set

    """
    ort_vectors = []
    ort_vectors.append(normalize_v(set_vectors[0]))
    for inx in np.arange(1, len(set_vectors)):
        v = set_vectors[inx]
        projections = 0.0
        for ort in ort_vectors:
            projections = projections + oproj(ort, v)
        ort_vectors.append(v - projections)
    return [normalize_v(v) for v in ort_vectors]


def is_orthogonal(a, b, epsilon=1e-11):
    """If two vectors are orthogonal

    Args:
        a: a vector, 1D array
        b: a vector, 1D array
        epsilon: absolute numerical tolerance for zero,
                defaults to 1e-11.

    Returns:
        boolean, whether two vectors are orthogonal

    """
    dd = np.vdot(a, b)
    dd_r = np.real(dd)
    dd_i = np.imag(dd)
    return bool(dd_r < epsilon and dd_i < epsilon)


def is_normal(v, epsilon=1e-11):
    """Check if given vector is normalized

    Args:
        v: 1D array, vector.
        epsilon: value to check if it is already normalized,
                 defaults to 1e-11.

    Returns:
        boolean, whether it is a normal vector.

    """
    dd = np.vdot(v, v)
    dd_r = np.real(dd)
    dd_i = np.imag(dd)
    return bool(np.abs(dd_r - 1.0) < epsilon and np.abs(dd_i) < epsilon)


def get_pairs(n):
    """Get pairs from 0 to n, combination
    assuming (i,j) = (j, i)

    Args:
        n: Upper bound number that, index, to be used.
    Returns:
        list of pairs, combination

    """
    return list(combinations(range(n), 2))


def is_all_orthogonal(set_vectors):
    """Given set of vectors check if they are pairwise orthogonal

    Args:
        set_vectors: Set of vectors
    Returns:
        Boolean whether all vectors pairwise orthogonal.

    """
    n = len(set_vectors)
    pairs_in = get_pairs(n)
    check_ort = []
    for pp in pairs_in:
        x = set_vectors[pp[0]]
        y = set_vectors[pp[1]]
        is_x_y_ort = is_orthogonal(x, y)
        check_ort.append(is_x_y_ort)
    return all(check_ort)


def is_all_normal(set_vectors):
    """Given set of vectors check if they are normal vectors

    Args:
        set_vectors: Set of vectors
    Returns:
        Boolean whether all vectors are normal.

    """
    check_n = []
    for v in set_vectors:
        check_n.append(np.abs(np.vdot(v, v)) - 1.0 < 1e-11)
    return all(check_n)
