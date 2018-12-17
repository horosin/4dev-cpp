import numpy as np
import random
import timeit
import math
import pandas as pd
from matplotlib import pyplot as plt

from program import standard_deviation
# import python_example as std


if __name__ == '__main__':

    lens = range(10, 300, 10)
    py_time = []
    np_time = []
    c_time = []

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        numpy_rands = np.array(rands)
        py_time = np.append(py_time, timeit.timeit(lambda: standard_deviation(rands), number=10000))
        np_time = np.append(np_time, timeit.timeit(lambda: np.std(numpy_rands), number=10000))
        # c_time = np.append(c_time, timeit.timeit(lambda: std.stdev(rands), number=10000))

    # data = np.array([np.transpose(py_time), np.transpose(np_time), np.transpose(c_time)])
    data = np.array([np.transpose(py_time), np.transpose(np_time)])


    df = pd.DataFrame(data.transpose(), index=lens, columns=['Python', 'Numpy'])
    # df = pd.DataFrame(data.transpose(), index=lens, columns=['Python', 'Numpy', 'C++'])


    df.plot()
    plt.legend(loc='best')
    plt.ylabel('Time (Seconds)')
    plt.xlabel('Number of Elements')
    plt.title('10k Runs of Standard Deviation')
    plt.show()
