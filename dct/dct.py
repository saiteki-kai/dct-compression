import numpy as np


def dct2(A, n_dim=True):
    N, M = A.shape
    if N != M:
        raise Exception("A must be a NxN with same number of rows and columns!")

    C = np.zeros((N, N))

    C[0, :] = np.sqrt(1 / N)
    for k in range(1, N):
        for j in range(N):
            C[k, j] = np.cos(np.pi * k * (2 * j - 1) / (2 * N)) * np.sqrt(2 / N)

    if n_dim:
        return C.dot(A).dot(C.T)
    return C.dot(A)


def _dct2(A):
    N, M = A.shape
    C_temp1 = np.zeros((N, N))
    C_temp2 = np.zeros((M, M))
    out = np.zeros(A.shape)

    C_temp1[0, :] = 1 * np.sqrt(1 / N)
    for k in range(1, N):
        for i in range(N):
            C_temp1[k, i] = np.cos(np.pi * k * (2 * i + 1) / (2 * N)) * np.sqrt(2 / N)

    C_temp2[0, :] = 1 * np.sqrt(1 / M)
    for q in range(1, M):
        for j in range(M):
            C_temp2[q, j] = np.cos(np.pi * q * (2 * j + 1) / (2 * M)) * np.sqrt(2 / M)

    out = np.dot(C_temp1, A)
    out = np.dot(out, C_temp2)
    return out
