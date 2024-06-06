import numpy as np
data = np.loadtxt('/home/zhang/Packages/data.txt', float, '#', ',', None, encoding='utf-8', usecols=(0, 1), skiprows=2, unpack=True, ndmin=2, like=None, quotechar=None)
