import numpy as np
from itertools import cycle


def apply_pbc(lst: list, upper_bound: int):
    """Apply periodic boundaries to a list, cyclic to upper_bound.

    Given list repead the list up to a upper bound.
    This corresponds to a Periodic
    Boundary Condition (PBC), turn list ot cyclic up to an upper_bound,
    that has to be greater than the list.

    Args:
        lst: list of numbers, but would work for any.
        upper_bound: lenght of the new list, that original
        list will be applied PBC

    Returns:
        Boolean, if all are real.

    """
    pool = cycle(lst)
    c = 1
    lst_period = []
    for item in pool:
        c = c + 1
        lst_period.append(item)
        if c > upper_bound:
            break
    return lst_period


def is_imaginary_zero(ee: np.array, epsilon: float = 1e-9):
    """Check if all eigenvalues are real

    Args:
        ee: vector of eigenvalues

    Returns:
        Boolean, if all are real.

    """
    ee_img = np.imag(ee)
    return all([imag < epsilon for imag in ee_img])


def get_density(values: np.array, locations: np.array) -> tuple[np.array, np.array]:
    """Compute density given values and equidistant locations of bin centres.

     Args:
        values: set of values that density should be computed.
        locations: locations where density is defined, these are bin centres.

    Returns:
        density, location arrays as tuples.

    """
    delta = np.diff(locations[:2])
    _locations_edges = locations -  delta/ 2.0
    _locations_edges = np.concat([_locations_edges,_locations_edges[-1]+delta/2.0])
    density, _location_edges = np.histogram(values, bins=_locations_edges, density=True)
    locations = _location_edges[:-1]+delta/2.0
    return density, locations


def empirical_spectral_density(
    ensemble_sample: list,
    mixed_order: int = -1,
    locations: np.array = np.arange(-2.0, 2.1, 0.1),
    scale: str = "no",
    epsilon: float = 1e-9,
):
    """Compute Empirical SD: All eigenvalues of a given sampled matrix ensemble and its density

    Args:
        ensemble_sample: List of matrices, representative of a matrix ensemble.
        mixed_order : If the ensemble is from mixed, put the max order used.
        Defaults to -1, not mixed order. When in use, this will pad the eigen values.
        locations: Eigenvalue locations that we compute the density, must be eqiudistant,
        defaults np.arange(-2.05, 2.15, 0.1). Note that these are the bin centres.
        scale: Scale resulting eigenvalues,
               * Defaults to "no" : No scaling
               * 'wigner': Scales with sqrt(N/2), assume a square matrix
                 ensemble, not a mixed ensemble.
        epsilon: Imaginary numbers epsilon, below considered zero.

    Returns:
        The value of eigenvalues 1D, density values, eigenvalue locations.

    """
    _eigens = np.empty(0)
    for matrix_member in ensemble_sample:
        _eigens_member = np.linalg.eigvals(matrix_member)
        if mixed_order > 0:
            _eigens_member = np.array(apply_pbc(list(_eigens_member), mixed_order))
        _eigens = np.append(_eigens, _eigens_member)
    if is_imaginary_zero(_eigens, epsilon=epsilon):
        _eigens = np.real(_eigens)
    else:
        raise ValueError("Non-zero imaginary in the eigenvalues.")
    if scale == "wigner":
        N = ensemble_sample[0].shape[0]
        _eigens = _eigens / np.sqrt(N / 2.0)
    _empirical_density, _locations = get_density(_eigens, locations)
    return _eigens, _empirical_density, _locations


def wigner(locations: np.array, domain_boundary=2.0):
    """Wigner semi-circle density

    Density is defined as
    \rho(\lambda) = \frac{2}{\pi \cdot R^{2}} \sqrt{R^{2}-\lambda^{2}}

    Args:
        locations: An eigenvalue locations.
        domain_boundary: Domain boundary, as a list, [-domain_boundary, domain_boundary]

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
