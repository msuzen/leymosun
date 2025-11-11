from leymosun.matrix import ensemble, mixed_ensemble, offdiagonal
from leymosun.gaussian import goe
import numpy as np


def test_ensemble_size_goe():
    ensemble_size = 10
    matrix_order = 1000
    ensemble_sample = ensemble(matrix_order, ensemble_size, goe)
    assert len(ensemble_sample) == ensemble_size
    
def test_ensemble_orders_goe():
    ensemble_size = 10
    matrix_order = 1000
    ensemble_sample = ensemble(matrix_order, ensemble_size, goe)
    for matrix_sample in ensemble_sample:
        assert matrix_sample.shape[0] == matrix_order

def test_mixed_ensemble_size_goe():
    ensemble_size = 10
    matrix_order = 1000
    degree_of_mixture = 0.9
    ensemble_sample = mixed_ensemble(matrix_order, ensemble_size, degree_of_mixture, goe)
    assert len(ensemble_sample) == ensemble_size
    
def test_mixed_ensemble_orders_goe():
    ensemble_size = 10
    matrix_order = 1000
    degree_of_mixture = 0.9
    ensemble_sample = mixed_ensemble(matrix_order, ensemble_size, degree_of_mixture, goe)
    for matrix_sample in ensemble_sample:
        assert matrix_sample.shape[0] < matrix_order

def test_offdiagonal():
    A = np.array([[11,12,13],[21,22,23],[31,32,33]])
    A_od = offdiagonal(A)
    assert A_od.shape[0] == 6
    for off_element in [12,13,21,23,31,32]:
        assert off_element in A_od