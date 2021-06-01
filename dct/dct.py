import numpy as np

###################################################
# output: compute C matrix of the dct2
# params: N integer > 0
###################################################
def compute_cmatrix(N):
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
    if A.ndim == 2 and A.shape[0] != 1 and A.shape[1] != 1:
        raise Exception("Matrix non monodimensional!")
    A = A.squeeze()
    N = A.shape[0]
    return compute_cmatrix(N).dot(A)

###################################################
# output: compute dct 2D of the matrix A
# params: A matrix NxN
###################################################
def dct2(A):
    N, M = A.shape
    if N == 1 or M == 1:
        raise Exception("A is {}x{} but must be a NxN matrix with N > 1".format(N, M))
    if N != M:
        raise Exception("A is {}x{} but must be a NxN with same number of rows and columns!".format(N, M))

    C = compute_cmatrix(N)
    return C.dot(A).dot(C.T)
