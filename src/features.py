import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

# Load data

df = pd.read_pickle("src/data/interim/01_data_resampled.pkl")


# Plotting outliers
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (20, 5)
plt.rcParams["figure.dpi"] = 100

df["acc_x"]

df[["acc_x"]].boxplot()

plt.show()
