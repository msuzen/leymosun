from collections import namedtuple
import dill

Params = namedtuple("Params", ["degree_of_mixtures", "mixed_order", "ensemble_size"])

""" 

Params: Simulation parameters in a namedtuple with the members.

degree_of_mixtures: List of degree of mixtures to compute.  
mixed_order: (Reference) matrix order.  
ensemble_size: The number of matrices to consider.  
 
"""

MixedEnsemble = namedtuple(
    "MixedEnsemble",
    [
        "uuid",
        "degree_of_mixture",
        "matrix_order",
        "ensemble_size",
        "eigenvalues",
        "spectra_values",
        "spectra_locations",
    ],
)

""" 

MixedEnsemble: Mixed ensemble storage for spectral distributions

uuid: unique uuid4. 
degree_of_mixture: Mixture strength.  
matrix_order: Order of the (reference) matrix.  
ensemble_size: Number of matrices to consider.  
eigenvalues: All eigenvalues vector in the ensemble.  
spectra_values: ESD, Empirical Spectral Density if eigenvalues.  
spectra_locations: ESD locations, eigenvalues, bin centers in histogram parlance.  
 
"""

MixedEnsembleSet = namedtuple(
    "MixedEnsembleSet", ["degree_of_mixtures", "mixed_ensembles"]
)

""" 

MixedEnsembleSet: Mixed ensemble sets.

degree_of_mixtures: List/array of mixture strenghts.  
mixed_ensembles: List/array of MixedEnsemble stroges, corresponding mixture strengths.  

"""

SpectralDataStorage = namedtuple("SpectralDataStorage", ["sim_params", "mixed_ensemble_set"])

""" 

SpectralDataStorage: Mixed ensemble datastorage full.  

sim_params: Sim Params. 
mixed_ensemble_set: Set of mixed ensembles.  

"""

def write_storage(storage: SpectralDataStorage, filename: str):
    """Write SpectralDataStorage object to a file.
    
    Args:
        storage: SpectralDataStorage object
        filename: Filename to store, using .dill extension is recommended. 

    Returns:
        None
    
    """
    return dill.dump(storage, open(filename, "wb"))


def read_storage(filename: str) -> SpectralDataStorage:
    """Write SpectralDataStorage object to a file.
    
    Args:
        filename: Filename to read from, using .dill extension is recommended. 

    Returns:
        SpectralDataStorage object
    
    """
    return dill.load(open(filename, "rb"))
