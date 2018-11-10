import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
n = 4

def FitnessFunction(chromosome):
    # Frequency Matrix to find congestion
    frequency = [0]*(n*n)
    for l in chromosome:
        for x in l:
            frequency[x-1] += 1
    return frequency


def visualize(frequency):
    df = pd.DataFrame()
    y = []
    x = []
    for i in range(1, n+1):
        for j in range(n):
            y.append(i)
    for i in range(n):
        for j in range(1, n+1):
            x.append(j)
    df["Index"] = list(range(1, n*n+1))
    df["Data"] = frequency
    df["Y"] = y
    df["X"] = x
    # print(df)

    data = np.asarray(df['Data']).reshape(n, n)
    index = np.asarray(df['Index']).reshape(n, n)
    # print(data)
    # print(index)

    result = df.pivot(index="Y", columns="X", values="Data")
    label = (np.asarray(["{0} \n".format(ind, dat) for ind, dat in zip(index.flatten(), data.flatten())])).reshape(n, n)

    fig, ax = plt.subplots(figsize=(12, 7))
    title = "Congestion Visualization"
    plt.title(title, fontsize=18)
    ttl = ax.title
    ttl.set_position([0.5, 1.05])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis("off")

    sns.heatmap(result, annot=label,vmin=0,vmax=n, fmt="",cmap="RdBu_r", linewidths=0.30, ax=ax)
    plt.show()
