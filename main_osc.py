import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import scipy.fft

skip = 1

path = '../new_data/PartLast/'

filenames = ['025', '05', '1', '2', '3', '4', '5']
lengths = [0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
colors = ['k', 'r', 'b', 'g', 'm', 'y', 'c']

# fig, ax = plt.subplots(7, constrained_layout=True)
plt.figure(figsize=(6,6))

"""
for i in range(0, len(filenames)):
    filename = path + str(filenames[i]) + 'm.csv'
    df = pd.read_csv(
        filename,
    )

    time_step = float(df['Increment'].values[0])
    print(str(lengths[i]) + 'm time_step = ', time_step)

    Y = np.array([float(val) for val in df['CH1'].values[1::skip]])
    X = [time_step * i for i in range(0, len(Y))]

    fourier = scipy.fft.fft(Y)
    freq = scipy.fft.fftfreq(Y.size, d=time_step)

    fourier = scipy.fft.rfft(Y)
    freq = scipy.fft.rfftfreq(Y.size, d=time_step)

    amplitude = 2*np.abs(fourier) / len(Y)

    amplitude[0] = 0

    max_index = np.argmax(amplitude)

    dominant_freq = freq[max_index]
    dominant_amp = amplitude[max_index]
    amplitude = max(abs(Y))

    print(str(lengths[i]) + 'm dominant frequency = ', dominant_freq/1e6, 'MHz')
    print('error = ', 1 / (len(Y) * time_step) / 1e6, ' MHz')
    print("Amplitude:", amplitude)

    X = [1e6 * xv for xv in X]
    ax[i].plot(X, Y, label=rf'{lengths[i]}m', c='k')
    ax[i].text(
        1.02, 0.5, rf'{lengths[i]}m',
        transform=ax[i].transAxes,
        va='center',
        ha='left'
    )

plt.subplots_adjust(left=0.1, right=0.9,
                    top=1.1, bottom=0.1,
                    wspace=1, hspace=0.4)
fig.supxlabel(rf'Time, $\mu$s')
fig.supylabel('Amplitude, V')
plt.savefig('oscillations.eps', format='eps') 
plt.show()
"""
val = [5.4, 4.6, 3.6, 2.9, 2.1, 2.0, 1.7]
yerr = [0.4, 0.4, 0.4 ,0.4, 0.2, 0.2, 0.2]
yerr = yerr / np.power(12, 0.5)
amp = [1.159, 0.759, 0.743, 0.726, 0.952, 0.662, 0.842]
x_axes = [np.power((16e-12 + length * 100e-12),-0.5) for length in lengths]
x_space = np.linspace(min(x_axes), max(x_axes), 1000)


def test(x, a, b):
    return a + b * x

# Fit the model to the data
param, param_cov = curve_fit(test, x_axes, val, sigma=yerr, absolute_sigma=True)

val2 = [1e6*vl for vl in val]
param2, _ = curve_fit(test, x_axes, val2, sigma=yerr, absolute_sigma=True)
print("Function coefficients:")
print(param2)

plt.grid(color='grey', linestyle='--', linewidth=0.5)
x_axes_scaled = [xv*1e-3 for xv in x_axes]
x_space_scaled = [xv*1e-3 for xv in x_space]
plt.errorbar(x_axes_scaled, val, yerr=yerr, c='k', fmt='o', capsize=3)
plt.plot(x_space_scaled, test(x_space, *param), 'r--')
plt.xlabel(rf'Oscillator capacitance, F$^{{-1/2}}$ $\times 10^3$')
plt.ylabel('Oscillation frequency, MHz')
plt.tight_layout()
plt.savefig('freq_lin.eps', format='eps')
plt.show()
