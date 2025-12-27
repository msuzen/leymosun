import numpy as np
from itertools import cycle
from leymosun.stats import pdf, bootstrap_observed_matrix_ci


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


def empirical_spectral_density(
    ensemble_sample: list,
    mmes_order: int = -1,
    locations: np.array = np.arange(-2.05, 2.1, 0.05),
    scale: str = "no",
    epsilon: float = 1e-9,
):
    """Compute Empirical SD: Eigenvalues, densities and location of all matrices

    Args:
        ensemble_sample: List of matrices, representative of a matrix ensemble.
        mmes_order: If the ensemble is from mixed, put the max order used.
                     Defaults to -1, not mixed order. When in use, this will
                     pad the eigenvalues.
                     MMES algorithm is based on Mixed Matrix Ensemble Sampling (MMES)
                     Suzen 2021 https://hal.science/hal-03464130
        locations: Eigenvalue locations that we compute the density.
                   defaults np.arange(-2.05, 2.1, 0.05). Note that
                   these are the bin centres.
        scale: Scale resulting eigenvalues,
               * Defaults to "no" : No scaling
               * 'wigner': Scales with sqrt(N/2), assume a square matrix
                 ensemble, not a mixed ensemble.
        epsilon: Imaginary numbers epsilon, below considered zero.

    Returns:
        The value of eigenvalues (2D), densities (2D), eigenvalue locations.

    """
    eigenvalues = []
    densities = []
    for matrix_member in ensemble_sample:
        _eigens_member = np.linalg.eigvals(matrix_member)
        if mmes_order > 0:
            _eigens_member = np.array(apply_pbc(list(_eigens_member), mmes_order))
        if is_imaginary_zero(_eigens_member, epsilon=epsilon):
            _eigens_member = np.real(_eigens_member)
        else:
            raise ValueError("Non-zero imaginary in the eigenvalues.")
        if scale == "wigner":
            N = _eigens_member.shape[0]
            _eigens_member = _eigens_member / np.sqrt(N / 2.0)
        eigenvalues.append(_eigens_member)
        _empirical_density, _locations = pdf(_eigens_member, locations)
        densities.append(_empirical_density)
    return np.array(eigenvalues), np.array(densities), _locations


def eigenvalue_on_polynomial(eigen: float, coefficients: np.array):
    """Compute transformed eigenvalue on a polynomial

    Polynomial of degree n-1 with coefficients c defined as
    c[0] e^n-1 + c[1] r^n-2 + ... + c[n]

    Args:
        eigen: Single eigen valur
        coefficients: polynomial coefficient

    Returns:
        Transformed eigenvalur

    """
    degree = len(coefficients) - 1
    new_eigen = 0
    for i in range(degree + 1):
        current_degree = degree - i
        new_eigen = new_eigen + coefficients[i] * (eigen**current_degree)
    return new_eigen


def unfold_spectra(eigenvalues: np.array, iqr: bool = True, deg_max: int = 32):
    """Unfold given spectra and compute nearest neigbour spacing

    Using polynomial fits, with optimal degree finding that
    makes mean spacing 1.0, the closest. Then transform
    them to new values.

    We remove outliers as suggested in the literature.

    - O. Bohigas, in Random matrices and chaotic dynamics
    (LesHouches Session LII, North-Holland, 1989).
    - On the spectral unfolding of chaotic and mixed systems,
    Abuelenin, Physica A, 492, 564-570 (2018)

    Args:
        eigenvalues: Spectra
        iqr: Only consider within inter quantile range, defaults to True.

    Returns:
        Tuple of 3:
        Transformed eigenvalues (unfolded spectra).
        nearest neigbour spacings of unfolded spectra and the degree
        of the optimal polynomial

    """
    if iqr:
        q25 = np.quantile(eigenvalues, 0.25)
        q75 = np.quantile(eigenvalues, 0.75)
        eigenvalues = eigenvalues[np.where(eigenvalues >= q25)[0]]
        eigenvalues = eigenvalues[np.where(eigenvalues <= q75)[0]]
    eigenvalues_sorted = np.sort(eigenvalues)
    x = eigenvalues_sorted
    N = len(eigenvalues_sorted)
    y = np.arange(N)
    degrees = np.arange(1, deg_max)
    fluctuation_levels = []
    for deg in degrees:
        coefficients = np.polyfit(x, y, deg=deg)
        x_new = [eigenvalue_on_polynomial(x, coefficients) for x in eigenvalues_sorted]
        fluctuation_levels.append(np.mean(np.diff(x_new)))
    degree_ix = np.argmin(np.abs(np.array(fluctuation_levels) - 1.0))
    deg_opt = degrees[degree_ix]
    coefficients = np.polyfit(x, y, deg=deg_opt)
    unfolded_eigenvalues = np.array(
        [eigenvalue_on_polynomial(x, coefficients) for x in eigenvalues_sorted]
    )
    unfolded_eigen = np.sort(unfolded_eigenvalues)
    return unfolded_eigen, np.diff(unfolded_eigen), deg_opt


def nnsd(
    eigenvalues: np.array,
    locations: np.array = np.arange(0.0, 5.0, 0.1),
    unfold: bool = True,
):
    """Compute Nearest-Neigbour Spacing Densities (NNSD) given eigenvalues with
       polynomial unfolding.

    Args:
        eigenvalues: 2D, eigenvalues over repeaded samples.
        locations: Centers to compute PDF of NNSD, defaults to [0, 5] with 0.1 spacing.
        unfold: whether to unfold, defaults to True.

    Returns:
        Tuple of three: NNSDs 2D and location bins

    """
    nnsd_densities = []
    for eigenvalue in eigenvalues:
        if unfold:
            _, eigenvalue, _ = unfold_spectra(eigenvalue, deg_max=30, iqr=True)
        else:
            eigenvalue = np.diff(eigenvalue)
        density, _locations = pdf(eigenvalue, locations=locations)
        nnsd_densities.append(density)
    return np.array(nnsd_densities), np.array(_locations)


def mean_adjacent_gap_ratio(eigenvalues):
    """Compute ratio of adjacent spacing gap ratio
       Due to Oganesyan-Huse Phys. Rev. B 75, 155111 (2007)

    Args:
        eigenvalues: 2D, eigenvalues over repeaded samples.
        locations: Centers to compute PDF of NNSD.

    Returns:
        Mean given ensemble of eigenvalues

    """
    adjacent_gap_ratios = []
    adjacent_gap_ratios_mean = []
    for eigens in eigenvalues:
        eigens_sorted = np.sort(eigens)
        spacings = np.diff(eigens_sorted)
        adjacent_gap_ratio = np.minimum(spacings[:-1], spacings[1:]) / (
            np.maximum(spacings[:-1], spacings[1:]) + 1e-9
        )
        adjacent_gap_ratios.append(adjacent_gap_ratio)
        adjacent_gap_ratios_mean.append(np.mean(adjacent_gap_ratio))
    bar_adjacent_gap_ratio = np.mean(adjacent_gap_ratios_mean)
    return bar_adjacent_gap_ratio, adjacent_gap_ratios
