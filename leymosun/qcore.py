import numpy as np # type: ignore
from numpy.linalg import eig # type: ignore

"""Basic Kets

ket0 : |0>
ket1 : |1>
one  : 1 in an array, for tensor product 
       1 to return the same.
"""
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])
one = np.array([1])


def prepare_entangled(M):
    """
    Prepare maximally entangled state


     Args:
        M: Number of qubits to consider

    Return
        return maximally entangled vector, column.


    """
    m0 = np.kron(ket0, one)
    m1 = np.kron(ket1, one)
    for _ in range(M - 1):
        m0 = np.kron(m0, ket0)
        m1 = np.kron(m1, ket1)
    return (1.0 / np.sqrt(2)) * (m0 + m1)

def fidelity_pure(psit, psi0):
    """Compute overlap fidelity for pure states

    Args:
        psit (state ket): State to compute fidelity.
        psi0 (state ket): Initial state. 

    Returns:
        fidelity value, float

    """
    overlap = np.vdot(psit, psi0)
    return float(np.abs(overlap) ** 2)

def fidelity_evolution_pure_ed(H, psi0, delta, ndelta):
    """Compute state fidelity unitary evolution in full Hilbert space
       Pure states.

    Args:
        H (2D numpy array): Hamiltonian, can be complex.
        psi0 (1D numpy array): Initial Ket-state
        delta (float): time increment
        ndelta (int): maximum time, in counts of deltat

    Returns:
        times, fidelity: Tuple of 1D arrays
    """
    lambdas, U = eig(H)
    tcurrent = 0.0
    psit = psi0
    fidelities = []
    times = []

    while tcurrent < delta * ndelta:
        times.append(tcurrent)
        fid = fidelity_pure(psi0, psit)
        fidelities.append(fid)
        phases = np.exp(-1j * lambdas * tcurrent)
        evolution_op = (U @ np.diag(phases)) @ U.conj().T
        psit = evolution_op @ psi0
        tcurrent += delta

    return times, fidelities

def fidelity_evolution_pure_krylov(K_s, H, psi0, delta, ndelta):
    """Compute state fidelity unitary evolution in Krylov basis
       Pure states.

    Args:
        K_s (list of Krylov vector): Krylov bases
        H (2D numpy array): Hamiltonian, can be complex (this is the full).
        psi0 (1D numpy array): Initial Ket-state
        delta (float): time increment
        ndelta (int): maximum time, in counts of deltat

    Returns:
        times, fidelities: Tuple of 1D arrays
    """
    V_basis = np.column_stack(K_s)
    H_proj = V_basis.conj().T @ H @ V_basis
    psi0_proj = V_basis.conj().T @ psi0

    lambdas, U = eig(H_proj)
    tcurrent = 0.0
    psit = psi0_proj.copy()
    fidelities = []
    times = []

    while tcurrent < delta * ndelta:
        times.append(tcurrent)
        fid = fidelity_pure(psi0_proj, psit)
        fidelities.append(fid)
        phases = np.exp(-1j * lambdas * tcurrent)
        evolution_op = (U @ np.diag(phases)) @ U.conj().T
        psit = evolution_op @ psi0_proj
        tcurrent += delta

    return times, fidelities

def spread_complexity(V_basis, psit):
    """Spread Complexity (KC) at a given state, scaled with basis size.
    See: Parker et al. Phys. Rev. X 9, 041017 (2019)

    Args:
        V_basis (basis matrix): Krylov basis matrix
        psit (1D column vector): projected state in the Krylov bases

    Returns:
        float number, Krylov Complexity.
    """
    size_basis = V_basis.shape[1]
    c_t = 0.0
    for n in range(size_basis):
        c_t = c_t + n*np.abs(np.vdot(V_basis[:,n], psit))**2
    return c_t/size_basis


def spread_complexity_evolution(K_s, H, psi0, delta, ndelta):
    """Compute krylov complexity unitary evolution in Krylov basis

    Args: 
        K_s (list of Krylov vector): Krylov bases
        H (2D numpy array): Hamiltonian, can be complex (this is the full).
        psi0 (1D numpy array): Initial Ket-state
        delta (float): time increment
        ndelta (int): maximum time, in counts of deltat

    Returns:
        times, kcomplexity: Tuple of 1D arrays
    """
    V_basis = np.column_stack(K_s)
    H_proj = V_basis.conj().T @ H @ V_basis
    psi0_proj = V_basis.conj().T @ psi0

    lambdas, U = eig(H_proj)
    tcurrent = 0.0
    psit = psi0.copy()
    kcomplexity = []
    times = []

    while tcurrent < delta * ndelta:
        times.append(tcurrent)
        kc = spread_complexity(V_basis, psit)
        kcomplexity.append(kc)
        phases = np.exp(-1j * lambdas * tcurrent)
        evolution_op = (U @ np.diag(phases)) @ U.conj().T
        psit_proj = evolution_op @ psi0_proj
        psit = V_basis @ psit_proj
        tcurrent += delta

    return times, kcomplexity
