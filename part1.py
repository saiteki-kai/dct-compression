#!env/bin/python3
from time import time
from os import path
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import fft

from dct.dct import dct2


sizes = np.concatenate([np.arange(8, 128, 8), np.array([160, 196, 228, 256, 512])])

data = []
for n in sizes:
    A = np.random.rand(n, n)

    start1 = time()
    dct2(A)
    elapsed1 = time() - start1

    start2 = time()
    fft.dctn(A, type=2, norm="ortho")
    elapsed2 = time() - start2

    x = {
        "N": n,
        "N^2*log(N)": n ** 2 * math.log(n),
        "N^3": n ** 3,
        "handcrafted": elapsed1,
        "scipy": elapsed2,
    }

    data.append(x)
    print(x)

# Save results

df = pd.DataFrame(data)
df = df.melt(["N"], ["handcrafted", "scipy", "N^2*log(N)", "N^3"])
df.to_csv(path.join("output", "part1", "results.csv"))

# Plot results

sns.set_style("darkgrid", {"legend.frameon": True})
plt.figure(figsize=(10, 6))

ax = sns.lineplot(x="N", y="value", data=df, hue="variable")
ax.set_ylabel("Time (s)")
ax.set_yscale("log")

legend = plt.legend(labels=["handcrafted", "scipy", "N^2*log(N)", "N^3"], loc="upper left")
frame = legend.get_frame()
frame.set_facecolor("w")

plt.tight_layout()
plt.savefig(path.join("output", "part1", "results.png"), format="png", dpi=300)
plt.show()
