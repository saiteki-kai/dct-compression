import numpy as np

def dct2(A):
    N = A.shape[0]
    C_temp = np.zeros((N,N))
    out = np.zeros(A.shape)

    C_temp[0, :] = 1 * np.sqrt(1/N)
    for k in range(1, N):
        for j in range(N):
            C_temp[k, j] = np.cos(np.pi * k * (2*j+1) / (2 * N )) * np.sqrt(2 / N)

    out = np.dot(C_temp , A)
    return out

def dct2n(A):
    N, M = A.shape
    C_temp1 = np.zeros((N,N))
    C_temp2 = np.zeros((M,M))
    out = np.zeros(A.shape)

    C_temp1[0, :] = 1 * np.sqrt(1/N)
    for k in range(1, N):
        for j in range(N):
            C_temp1[k, j] = np.cos(np.pi * k * (2*j+1) / (2 * N )) * np.sqrt(2 / N)

    C_temp2[0, :] = 1 * np.sqrt(1/M)
    for q in range(1, M):
        for i in range(M):
            C_temp2[q, i] = np.cos(np.pi * q * (2*i+1) / (2 * M )) * np.sqrt(2 / M)

    out = np.dot(C_temp1 , A)
    out = np.dot(out, C_temp2)
    return out
