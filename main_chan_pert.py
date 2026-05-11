import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

skip = 1

df = pd.read_csv(
    '../new_data/CH1.csv',
    dtype={'CH1': float},
    usecols=['CH1'],
    skiprows=[1]
)

df2 = pd.read_csv(
    '../new_data/CH2.csv',
    dtype={'CH2': float},
    usecols=['CH2'],
    skiprows=[1]
)

X = np.array([float(val) for val in df['CH1'].values[1::skip]])
Y = np.array([(-1.0)*float(val)/20.0 for val in df2['CH2'].values[1::skip]])

data = np.array(sorted(zip(X, Y)))
data = data[(data[:,0] > 0.09) & (data[:,0] < 0.16)]

# find the spacing
dx, dy = 1, 1
for i in range(0,len(data[:,0])-1):
    if abs(data[i,0]-data[i+1,0]) != 0.0:
        dx = min(dx, abs(data[i,0]-data[i+1,0]))
    if abs(data[i,1]-data[i+1,1]) != 0.0:
        dy = min(dy, abs(data[i,1]-data[i+1,1]))

print('errors = ', dx, dy)

# original PCA fit

pca = PCA(n_components=2)
pca.fit(data)

vx, vy = pca.components_[0]
print(pca.components_[0], pca.components_[1])
print("explained variance ratio:", pca.explained_variance_ratio_)

slope = vx / vy

print('slope =', slope)
# angle
theta = np.arctan2(vx, vy)

# line for plotting
t = np.linspace(-0.05, 0.05, 100)
line = np.array([pca.mean_ + tv * pca.components_[0] for tv in t])


# Monte Carlo uncertainty
# add some noise corresponding to dx and dy to the original data

Nboot = 5000

dx = dx/100
dy = dy/100

slopes = np.empty(Nboot)
angles = np.empty(Nboot)

for i in range(Nboot):

    perturbed = np.empty_like(data)

    perturbed[:,0] = (
        data[:,0]
        + np.random.uniform(-dx/2, dx/2, len(data))
    )

    perturbed[:,1] = (
        data[:,1]
        + np.random.uniform(-dy/2, dy/2, len(data))
    )
    perturbed = perturbed[(perturbed[:,0] > 0.09) & (perturbed[:,0] < 0.16)]

    pca_boot = PCA(n_components=1)
    pca_boot.fit(perturbed)

    vx_b, vy_b = pca_boot.components_[0]

    slopes[i] = vx_b / vy_b
    angles[i] = np.arctan2(vx_b, vy_b)


# statistics
mean_slope = np.mean(slopes)
std_slope = np.std(slopes)

ci_low, ci_high = np.percentile(slopes, [2.5, 97.5])

theta_mean = np.mean(angles)
theta_std  = np.std(angles)

theta_low, theta_high = np.percentile(angles, [2.5, 97.5])
slope_low  = np.tan(theta_low)
slope_high = np.tan(theta_high)

print('mean = ', mean_slope)
print('std  = ', std_slope)
print('95% CI = ', ci_low, ci_high)
print('min slope = ', slope_low, ' max slope = ', slope_high) 
print('original angle = ', np.arctan2(vx, vy))
print('min angle = ', theta_low, ' max angle = ', theta_high)


# plot
plt.scatter(1e3*X, 1e3*Y)
plt.plot(1e3*line[:,0], 1e3*line[:,1])
plt.scatter(*pca.mean_*(1e3), color='red', s=100)
plt.yticks([], [])
plt.show()
