from scipy import fft
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
        lista_dct2.append(fft.dctn(x, norm="ortho"))

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
        lista_idct2.append(fft.idctn(x, norm="ortho"))

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
    return out
