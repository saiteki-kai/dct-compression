import numpy as np


###################################################
# output: compute C matrix of the dct2
# params: N integer > 0
###################################################
def _compute_c_matrix(N):
    C = np.zeros((N, N))

    C[0, :] = np.sqrt(1.0 / N)
    for k in range(1, N):
        for j in range(N):
            C[k, j] = np.cos(np.pi * k * (2 * j + 1) / (2.0 * N)) * np.sqrt(2.0 / N)

    return C


###################################################
# output: compute dct 1D of the matrix A
# params: A matrix Nx1 or 1xN
###################################################
def dct(A):
    if A.ndim != 1:
        raise ValueError("matrix 'A' must be 1-dimensional")

    N = A.shape[0]
    return _compute_c_matrix(N).dot(A)


###################################################
# output: compute dct 2D of the matrix A
# params: A matrix NxN
###################################################
def dct2(A):
    if A.ndim != 2:
        raise ValueError("matrix 'A' must be 2-dimensional")

    N, M = A.shape
    if N != M:
        raise ValueError(f"Matrix 'A' ({N}x{M}) must be squared")

    C = _compute_c_matrix(N)
    return C.dot(A).dot(C.T)
