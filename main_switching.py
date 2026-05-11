import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

skip = 1

df = pd.read_csv(
    '../new_data/fun_gen.csv',
)

df2 = pd.read_csv(
    '../new_data/NewFle.csv',
)

Y1 = np.array([float(val) for val in df['CH1'].values[1::skip]])
Y2 = np.array([float(val) for val in df2['CH2'].values[1::skip]])
time_spacing = float(df['Increment'].values[0])
X = [time_spacing * i for i in range(0, len(Y1))]
data = np.array(sorted(zip(X, Y1)))
unique_data = np.unique(data, axis=0)
data = unique_data

plt.scatter(data[:,0], data[:,1])
plt.show()
