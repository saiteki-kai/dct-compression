import time

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import fftpack
from dct.dct import dct2n

N = [10,50,100,500,1000,5000,10000]
data = []
for n in N:
    A = np.random.rand(n,n)

    start1 = time.time()
    out = dct2n(A)
    end1 = time.time()
    elapsed1 = end1 - start1

    start2 = time.time()
    out2 = fftpack.dctn(A, type=2, norm='ortho')
    end2 = time.time()
    elapsed2 = end2 - start2

    x = {"N": n, "N^2": n**2, "N^3": n**3, "dct2n_time": elapsed1, "fftpack.dctn_time": elapsed2}
    data.append(x)
    print(x)

df = pd.DataFrame(data)
df = df.melt(["N"], ["dct2n_time", "fftpack.dctn_time"])
df.to_csv('./python_results.csv')

sns.set_style("darkgrid")
grid = sns.lineplot(x="N", y="value", data=df, hue="variable")
grid.set(yscale="log")
plt.savefig("plt.svg")
plt.show()