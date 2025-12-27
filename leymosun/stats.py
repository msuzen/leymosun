import numpy as np
from leymosun.random import choice


def pdf(values: np.array, locations: np.array) -> tuple[np.array, np.array]:
    """Compute density given values and arbitrary monotonic locations of bin centres.

     Args:
        values: set of values that density should be computed.
        locations: locations where density is defined, these are bin centres!
                   numpy uses bin-edges, so we would lose 1st and last bin centers,

    Returns:
        density, location arrays as tuples.

    """
    delta = np.diff(locations)/2.0
    _locations_edges = locations[1:] - delta
    density, _location_edges = np.histogram(values, bins=_locations_edges, density=True)
    _locations = _location_edges + delta
    return density, _locations[:-1]


def bootstrap_observed_matrix_ci(
    observations: np.array,
    nboot: int = 1000,
    lower_quantile: float = 0.025,
    upper_quantile: float = 0.975,
):
    """Compute bootstrapped confidence intervals (CI) and the mean given experimental matrix

     Args:
        observations: Experimental matrix, row are different measurements, columns are different variates.
        nboot: Number of bootstraps to use, defaults to 1000
        lower_quantile: Lower bound for the confidence interval, defaults to 2.5%
        upper_quantile: Upper bound for the confidence interval, defaults to 97.5%

    Returns:
       Tuple of vectors, observed_mean, observed_upper, observed_lower

    """
    nrow = observations.shape[0]
    ncol = observations.shape[1]

    bootmatrix = []
    for _ in range(nboot):
        boot_indices = choice(nrow, nrow, replace=True)
        observations_boot = observations[boot_indices,]
        observed_means = np.mean(observations_boot, axis=0)
        bootmatrix.append(observed_means)
    bootmatrix = np.array(bootmatrix)

    observed_mean = np.mean(bootmatrix, axis=0)
    observed_upper = np.array(
        [np.quantile(bootmatrix[:, col], q=upper_quantile) for col in range(ncol)]
    )
    observed_lower = np.array(
        [np.quantile(bootmatrix[:, col], q=lower_quantile) for col in range(ncol)]
    )
    return observed_mean, observed_upper, observed_lower
