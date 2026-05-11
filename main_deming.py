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

XX = np.array([float(val) for val in df['CH1'].values[1::skip]])
YY = np.array([(-1.0)*float(val)/20.0 for val in df2['CH2'].values[1::skip]])

# sort and select the data where negative slope is
data = np.array(sorted(zip(XX, YY)))
data2 = data[(data[:,0] > 0.490)]
data = data[(data[:,0] > 0.11) & (data[:,0] < 0.15)]


# find the grid spacing
dx, dy = 1, 1
for i in range(0,len(data[:,0])-1):
    if abs(data[i,0]-data[i+1,0]) != 0.0:
        dx = min(dx, abs(data[i,0]-data[i+1,0]))
    if abs(data[i,1]-data[i+1,1]) != 0.0:
        dy = min(dy, abs(data[i,1]-data[i+1,1]))

# -----------------------
# Deming regression
# -----------------------

def deming_regression(x, y, lam=1.0):

    cov_mtx = np.cov(x, y, ddof=1)
    Sxx = cov_mtx[0,0]
    Syy = cov_mtx[1,1]
    Sxy = cov_mtx[0,1]

    # Deming slope (closed form)
    numerator = Syy - lam * Sxx + np.sqrt((Syy - lam * Sxx)**2 + 4 * lam * Sxy**2)
    denominator = 2 * Sxy

    slope = numerator / denominator

    return 1/slope


def deming_bootstrap(x, y, dx, dy, n=50):
    lam = (dy**2) / (dx**2)

    slopes = []

    for _ in range(n):
        x_pert = x + np.random.uniform(-dx/2, dx/2, size=len(x))
        y_pert = y + np.random.uniform(-dy/2, dy/2, size=len(y))

        slope = deming_regression(x_pert, y_pert, lam)
        slopes.append(slope)

    slopes = np.array(slopes)

    return np.mean(slopes), np.median(slopes), np.std(slopes), np.percentile(slopes, [2.5, 97.5])
# -----------------------
# Usage
# -----------------------

lam = (dy**2) / (dx**2)

slope = deming_regression(data[:,0], data[:,1], lam=lam)
slope2 = deming_regression(data2[:,0], data2[:,1], lam=lam)

print("slope:", slope)
print("slope2:", slope2)

mean, median, std, ci95 = deming_bootstrap(data[:,0], data[:,1], dx, dy)
print('mean = ', mean)
print('median = ', median)
print('std = ', std)
print('ci95 = ', ci95)
mean, median, std, ci95 = deming_bootstrap(data2[:,0], data2[:,1], dx, dy)
print('mean2 = ', mean)
print('median2 = ', median)
print('std2 = ', std)
print('ci95_2 = ', ci95)

plt.figure(figsize=(6,6))

x_mean = np.mean(data[:,0])
x2_mean = np.mean(data2[:,0])
y_mean = np.mean(data[:,1])
y2_mean = np.mean(data2[:,1])
t = np.linspace(data[0,0], 1.05*data[-1,0], 3) - x_mean
t2 = np.linspace(data2[0,0], 1.045*data2[-1,0], 3) - x2_mean
line = [1e3*(y_mean + tv * (1/slope)) for tv in t]
line2 = [1e3*(y2_mean + tv * (1/slope2)) for tv in t2]
print(slope2*(0.0061 - y2_mean) + x2_mean)
# line2 = [1e3*(y_mean + tv * (1/(-24.9))) for tv in t]
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.scatter(1e3*XX[::10], 1e3*YY[::10], c='k', s=6, rasterized=True)
plt.plot(1e3*(x_mean + t), line, c='r')
plt.plot(1e3*(x2_mean + t2), line2, c='b')
# plt.plot(1e3*data[:,0], line2, c='b')
plt.xlabel('Voltage across the diode, mV')
plt.ylabel('Current through the diode, mA')
plt.tight_layout()
plt.savefig('neg_diff_r.eps', format='eps')
plt.show()
