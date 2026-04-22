from leymosun.gram import gram_schmidt, normalize_v
import numpy as np # type: ignore


def lanczos(H, psi0, up_to_dim):
    """Find Krylov bases and Lanczos coefficients
    See 
    * Journal of Research of the National Bureau of Standards 
    Vol. 45, No. 4, October 1950
    C. Lanczos
    https://www.cs.umd.edu/~oleary/lanczos1950.pdf
    * Algorithm is summarized here 
      Camargo et. al. J. High Energ. Phys. 2024, 241 (2024).

    Args:
        H: Hamiltonian matrix, 2D real array
        psi0: Initial Krylov bases vector
        up_to_dim: Termination order, integer (usually lower than the full-size)
        epsilion: absolute tolerance.

    Return
        a_s, b_s, K_s: Lanczos coeffients a_s, b_s vector,
                       K_s is the list of vectors (Krylov Bases)

    """

    def compute_a(K, H):
        expa = np.matmul(K.T.conj(), np.matmul(H, K))
        return np.ndarray.flatten(expa)[0]

    def compute_A(H, an, Kn, bn, Kminus):
        I = np.diag(np.ones(H.shape[0]))
        return np.matmul(H - an * I, Kn) - bn * Kminus

    def get_coeff(A, H):
        b = np.linalg.norm(A)
        K = (1.0 /b) * A
        K = normalize_v(K)
        a = compute_a(K, H)
        return b, K, a

    #
    # Initialize:
    #
    # Order of computation is b, K and a, capital A is intermediate.
    # n=0,1 needs to be initialized so that Lanczos iteration can start.
    #
    b_s = []
    K_s = []
    a_s = []

    # n = 0
    b_s.append(np.float64(0.0))
    K_s.append(psi0)
    a_s.append(compute_a(K_s[0], H))

    # n = 1
    I = np.diag(np.ones(H.shape[0]))
    A = np.matmul(H - a_s[0] * I, K_s[0])
    b = np.linalg.norm(A)
    b_s.append(b)
    K = (1.0 / b) * A
    K_s.append(K)
    K_s = gram_schmidt(K_s)
    a = compute_a(K, H)
    a_s.append(a)
    

    # n > 1
    n = 2
    while n < up_to_dim:  # Check Ritz values tolerance or up_to_dim; which ever first!
        A = compute_A(H, a_s[n - 1], K_s[n - 1], b_s[n - 1], K_s[n - 2])
        b, K, a = get_coeff(A, H)
        b_s.append(b)
        K_s.append(K)
        K_s = gram_schmidt(K_s)
        a_s.append(a)
        n = n + 1
        
    

    return a_s, b_s, K_s


def get_ritz_matrix(H, up_to_dim, K_s):
    """Find Ritz Matrix

    Args:
        H: Hamiltonian matrix, 2D real array
        up_to_dim: Termination order, integer (usually lower than the full-size)
        K_s: Krylov bases vectors
        
    Return
        return Ritz matrix
        
    """
    r_matrix = np.zeros([up_to_dim, up_to_dim])
    for i in range(up_to_dim):
        for j in range(up_to_dim):
            a = np.matmul(K_s[i].T, np.matmul(H, K_s[j]))[0][0]
            r_matrix[i, j] = a
    return r_matrix


def validate_lanczos(H, r_matrix, epsilon=1e-11):
    """Validate Lanczos found Krylov bases.
       Would work for the test case of up_to_dim == full_dim.
       This checks eigenvalues found by Lanczos against 
       Exact Diagonalization.

    Args:
        H: Hamiltonian matrix, 2D real array
        r_matrix: ritz matrix
        epsilon: zero, absolute tolerance  
        
    Return
        return boolean for correctness, True, 
        means all green. 
        
    """
    # Ritz values: 
    eigenvals = np.linalg.eigvals(r_matrix)
    ritz = np.sort([np.real(e) for e in eigenvals])
    full_ed = np.sort(np.linalg.eigvals(H))
    return np.allclose(ritz, full_ed, atol=epsilon)
