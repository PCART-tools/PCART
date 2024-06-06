import numpy as np
data = np.loadtxt('/home/zhang/Packages/data.txt', float, '#', unpack=True, ndmin=2, usecols=(0, 1), skiprows=2, encoding='utf-8', delimiter=',', like=None, converters=None, quotechar=None)
