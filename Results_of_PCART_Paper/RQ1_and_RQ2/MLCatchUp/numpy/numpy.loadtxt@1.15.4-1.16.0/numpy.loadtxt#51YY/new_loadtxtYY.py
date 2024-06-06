import numpy as np
data = np.loadtxt('/home/zhang/Packages/data.txt', float, '#', ',', None, skiprows=1, usecols=(0, 2), unpack=True, ndmin=1, encoding='utf-8', max_rows=None)
