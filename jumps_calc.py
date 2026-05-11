import numpy as np

low_high_start = [
    [46.72,106.2],
    [44.80,106.4],
    [44.40,106.4],
    [44.60,106.4],
    [44.40,106.4]]
low_high_end = [
    [353.3,10.08],
    [355.6,10.60],
    [349.2,10.60],
    [345.6,10.80],
    [346.0,10.80]]

high_low_start = [
    [248.0,18.50],
    [247.6,18.40],
    [247.6,18.30],
    [246.8,18.30],
    [246.0,18.40]]
high_low_end = [
    [29.50,87.60],
    [28.80,85.90],
    [28.90,86.10],
    [28.90,86.40],
    [29.10,86.80]]

res1 = [20*abs((low_high_end[i][0] - low_high_start[i][0]) / (low_high_end[i][1] - low_high_start[i][1])) for i in range(0, 5)] 
res2 = [20*abs((high_low_end[i][0] - high_low_start[i][0]) / (high_low_end[i][1] - high_low_start[i][1])) for i in range(0, 5)] 

res = np.concatenate([res1, res2])

print(res)
print('mean resistance = ', np.mean(res))
print('std = ', np.std(res))
print('ci95 = ', np.percentile(res, [2.5, 97.5]))


