import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv('~/exp1/PartLast/1m.csv', usecols=['CH1'])
    Y = [float(val) for val in df['CH1'].values[1:]]
    X = [5*i for i in range(0,len(Y))]
    plt.scatter(X,Y)
    #plt.xticks([], [])
    plt.yticks([], [])
    plt.show()


if __name__ == "__main__":
    main()
