import time
from os import path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import fftpack
from dct.dct import dct2

sizes = np.concatenate(
    [
        np.arange(10, 50, 5),
        np.arange(50, 1001, 50),
        np.arange(1000, 2001, 250),
        np.array([5000, 10000]),
    ]
)

data = []
for n in sizes:
    A = np.random.rand(n, n)

    start1 = time.time()
    dct2(A)
    elapsed1 = time.time() - start1

    start2 = time.time()
    fftpack.dctn(A, type=2, norm="ortho")
    elapsed2 = time.time() - start2

    x = {
        "N": n,
        "N^2": n ** 2,
        "N^3": n ** 3,
        "handcrafted": elapsed1,
        "fftpack": elapsed2,
    }

    data.append(x)
    print(x)

# Save results

df = pd.DataFrame(data)
df = df.melt(["N"], ["handcrafted", "fftpack", "N^2", "N^3"])
df.to_csv(path.join("output", "results.csv"))

# Plot results

sns.set_style("darkgrid", {"legend.frameon": True})
plt.figure(figsize=(10, 6))

ax = sns.lineplot(x="N", y="value", data=df, hue="variable")
ax.set_ylabel("Time (s)")
ax.set_yscale("log")

legend = plt.legend(labels=["handcrafted", "fftpack", "N^2", "N^3"], loc="upper left")
frame = legend.get_frame()
frame.set_facecolor("w")

plt.tight_layout()
plt.savefig(path.join("output", "results.png"), format="png", dpi=300)
plt.show()
