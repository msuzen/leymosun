import numpy as np # pyright: ignore[reportMissingImports]
from leymosun.gram import gram_schmidt, is_all_normal, is_all_orthogonal
from leymosun.rosenzweig import rp, diagonal_normal

def test_gram_schmidt():
    A = diagonal_normal(100) # This is an orthogonal matrix
    Q = gram_schmidt(A)
    assert is_all_normal(Q)
    assert is_all_orthogonal(Q)
    assert not is_all_normal(A)
    assert is_all_orthogonal(A)
