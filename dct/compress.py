from scipy import fftpack
import numpy as np


def compress_image(image, F, d):
    # blocchettizzazione immagine
    lista_blocchi = []
    n_blocchi_a = (image.shape[0]) // F
    n_blocchi_l = (image.shape[1]) // F
    for x in range(n_blocchi_a):
        for y in range(n_blocchi_l):
            lista_blocchi.append(image[x * F : ((x + 1) * F), y * F : ((y + 1) * F)])

    # applico la dct2 ai blocchi
    lista_dct2 = []
    for x in lista_blocchi:
        lista_dct2.append(fftpack.dctn(x, norm="ortho"))

    # eliminazione frequenze
    for x in lista_dct2:
        if d <= F:
            x[d:F, :] = 0
            x[:, d:F] = 0
            for k in range(d):
                for l in range(d - k, d):
                    x[k, l] = 0
        else:
            for k in range(F):
                for l in range(F - k - 1, F):
                    x[k, l] = 0

    # applico la IDCT2 ai blocchi modificati
    lista_idct2 = []
    for x in lista_dct2:
        lista_idct2.append(fftpack.idctn(x, norm="ortho"))

    # arrotondamento valori
    lista_round = []
    for x in lista_idct2:
        x = x.clip(0, 255)
        lista_round.append(x.round())

    # ricomposizione matrice immagine
    mat_ricostruzione = []
    for y in range(n_blocchi_a):
        mat_ricostruzione.append(np.concatenate((lista_round[y * n_blocchi_l : (y + 1) * n_blocchi_l]), axis=1))

    out = np.concatenate((mat_ricostruzione), axis=0)

    #cofronto con nuova immagine
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.subplot(1, 2, 2)
    plt.imshow(mat_ricostruzione, cmap='gray', vmin=0, vmax=255)
    plt.show()

    # N, M = img.shape

    # n_blocks = N // F
    # m_blocks = M // F

    # out = np.zeros((n_blocks * F, m_blocks * F), dtype=np.uint8)

    # for i in range(n_blocks):
    #     for j in range(m_blocks):
    #         f = img[i * F : i * F + F, j * F : j * F + F]
    #         c = dctn(f, norm="ortho")

    #         for k in range(F):
    #             for l in range(F):
    #                 if k + l >= d:
    #                     c[k, l] = 0

    #         ff = idctn(c, norm="ortho")
    #         ff = ff.round().clip(0, 255)

    #         out[i * F : i * F + F, j * F : j * F + F] = ff

    return out
