import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('~/exp1/CH1_2.csv', usecols=['CH1'])
    df2 = pd.read_csv('~/exp1/CH2_2.csv', usecols=['CH2'])
    X = [float(val) for val in df['CH1'].values[1:]]
    Y = [(-1.0)*float(val) for val in df2['CH2'].values[1:]]
    plt.scatter(X,Y)
    plt.xticks([], [])
    plt.yticks([], [])
    plt.show()


if __name__ == "__main__":
    main()
