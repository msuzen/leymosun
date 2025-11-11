from leymosun.gaussian import goe
from leymosun.matrix import offdiagonal
import numpy as np


def test_goe_shape():
    A = goe(1000)
    assert A.shape[0] == 1000


def test_goe_mean():
    epsilon_mean = 0.1
    A = goe(1000)
    A_diag = np.diag(A)
    A_odiag = offdiagonal(A)
    assert np.abs(np.mean(A_odiag)) < epsilon_mean
    assert np.abs(np.mean(A_diag)) < epsilon_mean


def test_goe_variance():
    epsilon_variance = 0.2
    A = goe(1000)
    A_diag = np.diag(A)
    A_odiag = offdiagonal(A)
    assert np.abs(np.var(A_odiag) - 0.5) < epsilon_variance
    assert np.abs(np.var(A_diag) - 1.0) < epsilon_variance
    
def test_goe_variance_scale():
    epsilon_variance = 0.5
    A = goe(1000, scale=2.0)
    A_diag = np.diag(A)
    A_odiag = offdiagonal(A)
    assert np.abs(np.var(A_odiag) - 2.0) < epsilon_variance
    assert np.abs(np.var(A_diag) - 4.0) < epsilon_variance
