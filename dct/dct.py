import numpy as np


def _compute_c_matrix(N):
    C = np.zeros((N, N))

    C[0, :] = np.sqrt(1.0 / N)
    for k in range(1, N):
        for j in range(N):
            C[k, j] = np.cos(np.pi * k * (2 * j + 1) / (2.0 * N)) * np.sqrt(2.0 / N)

    return C

def _dct(A):
    if A.ndim != 1:
        raise ValueError("matrix 'A' must be 1-dimensional")

    N = A.shape[0]
    return _compute_c_matrix(N).dot(A)

def _dct2(A):
    if A.ndim != 2:
        raise ValueError("matrix 'A' must be 2-dimensional")

    N, M = A.shape
    if N != M:
        raise ValueError(f"Matrix 'A' ({N}x{M}) must be squared")

    C = _compute_c_matrix(N)
    return C.dot(A).dot(C.T)


def dct(A):
    """
    params: A matrix Nx1
    output: compute dct 1D of the matrix A
    """
    N = A.shape[0]
    C = np.zeros(N, dtype=np.float64)

    for k in range(0, N):
        a_k = np.sqrt(1.0 / N) if k == 0 else np.sqrt(2.0 / N)

        sum = 0
        for j in range(N):
            sum = sum + A[j] * np.cos(k * np.pi * (2 * j + 1) / (2.0 * N))

        C[k] = a_k * sum
    return C

def dct2(A):
    """
    params: A matrix NxM
    output: compute dct 2D of the matrix A
    """
    N, M = A.shape
    C = np.zeros((N, M), dtype=np.float64)

    for i in range(N):
        C[i] = dct(A[i])

    for j in range(M):
        C[:, j] = dct(C[:, j])
    return C
