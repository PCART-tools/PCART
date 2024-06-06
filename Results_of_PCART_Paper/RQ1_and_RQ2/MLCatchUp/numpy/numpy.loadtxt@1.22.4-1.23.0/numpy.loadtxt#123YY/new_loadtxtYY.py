import numpy as np
data = np.loadtxt('/home/zhang/Packages/data.txt', float, '#', ',', None, 2, usecols=(0, 1), unpack=True, ndmin=2, encoding='utf-8', max_rows=100, quotechar=None)
