import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston

boston = load_boston()
x = boston.data
y = boston.target
columns = boston.feature_names

df = pd.DataFrame(x, columns=columns)
df["price"] = y
corr = df.corr()

target = corr.sort_values(by="price", ascending=False)
print(target.head())
