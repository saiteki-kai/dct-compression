import time
from os import path
import numpy as np
import pandas as pd

from scipy import fftpack
import os
import cv2 as cv
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

#richiesta parametri e controlli
F=""
d=""

print("Buongiorno")

#finestra filedialog 
filename = askopenfilename()

while F.isnumeric()!=True:
    F = input('Inserisci intero "F": ')
    if F.isnumeric()!=True:
        print("errore, valore inserito non valido")
F=int(F)

while d.isnumeric()!=True:
    d = input('Inserisci intero "d": ')
    if d.isnumeric()!=True:
        print("errore, valore inserito non valido")
    else:
        if int(d)<0 or int(d)>2*F-2:
            print('errore, valore inserito non conforme al parametro "F"')
            d=""
d=int(d)

# lettura immagine
image= cv.imread(os.path.join(filename),0)

#blocchettizzazione immagine
lista_blocchi=[]
n_blocchi_a=(image.shape[0])//F
n_blocchi_l=(image.shape[1])//F
for x in range(n_blocchi_a):
    for y in range(n_blocchi_l):
        lista_blocchi.append(image[x*F:((x+1)*F),y*F:((y+1)*F)])

#applico la dct2 ai blocchi   
lista_dct2=[]
for x in lista_blocchi:
    lista_dct2.append(fftpack.dctn(x, norm="ortho"))

#eliminazione frequenze
for x in lista_dct2:
    for k in range(x.shape[0]):
        for l in range(x.shape[1]):
            if k+l>=d:
                x[k,l]=0

#applico la IDCT2 ai blocchi modificati
lista_idct2=[]
for x in lista_dct2:
    lista_idct2.append(fftpack.idctn(x, norm="ortho"))

#arrotondamento valori
lista_round=[]
for x in lista_idct2:
    x = x.clip(0, 255)
    lista_round.append(x.round())
    
#ricomposizione matrice immagine
mat_ricostruzione=[]
for y in range(n_blocchi_a):
    ricostruzione_righe=lista_round[y*n_blocchi_l]
    for x in range(1,n_blocchi_l):
        ricostruzione_righe=np.concatenate((ricostruzione_righe, lista_round[x+y*n_blocchi_l]),axis=1)
    mat_ricostruzione.append(ricostruzione_righe)
    
mat_ricostruzione=np.concatenate((mat_ricostruzione),axis=0)

#cofronto con nuova immagine
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.subplot(1, 2, 2)
plt.imshow(mat_ricostruzione, cmap='gray', vmin=0, vmax=255)
plt.show()