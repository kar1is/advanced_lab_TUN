import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

skip = 1

df = pd.read_csv(
    '../new_data/fun_gen.csv',
)

df2 = pd.read_csv(
    '../new_data/fun_gen_CH2.csv',
)

fig, ax = plt.subplots(2, constrained_layout=True)

Y1 = np.array([float(val) for val in df['CH1'].values[1::5]])
Y2 = np.array([float(val) for val in df2['CH2'].values[1::5]])
time_spacing = float(df['Increment'].values[0])
X = [time_spacing * i * 1e3 for i in range(0, len(Y1))]

ax[0].scatter(X, Y1, c='k')
ax[1].scatter(X, Y2, c='k')
ax[0].text(
    1.02, 0.5, 'Input',
    transform=ax[0].transAxes,
    va='center',
    ha='left'
)
ax[1].text(
    1.02, 0.5, 'Output',
    transform=ax[1].transAxes,
    va='center',
    ha='left'
)
fig.supxlabel('Time, ms')
fig.supylabel('Signal voltage, V')
plt.savefig('signal.png', format='png', dpi=200)
plt.show()
