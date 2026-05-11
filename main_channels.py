import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

skip = 1
scale = 2e-9
df = pd.read_csv('../new_data/CH1.csv', dtype={'CH1': float}, usecols=['CH1'], skiprows=[1])
df2 = pd.read_csv('../new_data/CH2.csv', dtype={'CH2': float}, usecols=['CH2'], skiprows=[1])

X = [float(val) for val in df['CH1'].values[1::skip]]
Y = [(-1.0)*float(val) for val in df2['CH2'].values[1::skip]]

data = np.array(sorted(zip(X, Y)))
data = data[(data[:,0]>0.09) & (data[:,0]<0.16)]

pca = PCA(n_components=1)
pca.fit(data)
t = np.linspace(-0.05,0.05,100)
line = [pca.mean_ + tv*pca.components_[0] for tv in t]
line = np.array(line)

plt.scatter(data[:,0],data[:,1])
plt.plot(line[:,0],line[:,1])
plt.scatter(*pca.mean_, color='red', s=100)
plt.yticks([], [])
print(pca.mean_, pca.components_[0])
plt.show()
