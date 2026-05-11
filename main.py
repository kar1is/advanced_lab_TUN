import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

skip = 1
df = pd.read_csv('../new_data/CH1.csv', dtype={'CH1': float}, usecols=['CH1'], skiprows=[1])
df2 = pd.read_csv('../new_data/CH2.csv', dtype={'CH2': float}, usecols=['CH2'], skiprows=[1])
X = [1e3*float(val) for val in df['CH1'].values[1::skip]]
Y = [1e3*(-1.0)*float(val)/20 for val in df2['CH2'].values[1::skip]]

data = np.array(sorted(zip(X, Y)))
data = data[(data[:,0]>100)]
unique_data = np.unique(data, axis=0)
data = unique_data

max_val = min(row[1] for row in data)

# Get all rows with that value
rows = [row for row in data if row[1] == max_val]
print(rows)

"""
data = unique_data
dx, dy = 1, 1
for i in range(0,len(data[:,0])-1):
    if abs(data[i,0]-data[i+1,0]) != 0.0:
        dx = min(dx, abs(data[i,0]-data[i+1,0]))
    if abs(data[i,1]-data[i+1,1]) != 0.0:
        dy = min(dy, abs(data[i,1]-data[i+1,1]))
print(dx, dy)
"""
# data = data[(data[:,0]>0.09) & (data[:,0]<0.16)]

# plt.figure(figsize=(6,6))
# plt.scatter(X, Y, c='k', s=4)
# mean = np.array([0.13179537, 0.06960378/20]) 
# slp = np.array([-0.54176912, 0.84052734/20])
# xX = np.linspace(-0.08,0.08,2)
# line = np.array([1e3*mean + 1e3*xv * slp for xv in xX])
# print(slp[0]/slp[1])
# plt.plot(line[:,0],line[:,1], c='r')
# plt.xlabel('Voltage across the diode, mV')
# plt.ylabel('Current through the diode, mA')
# plt.savefig('neg_diff_r.eps', format='eps')
# plt.show()
