import numpy as np
data = np.loadtxt('/home/zhang/Packages/data.txt', float, '#', skiprows=2, max_rows=100, ndmin=2, unpack=True, converters=None, encoding='utf-8', usecols=(0, 1), delimiter=',', like=None, quotechar=None)
