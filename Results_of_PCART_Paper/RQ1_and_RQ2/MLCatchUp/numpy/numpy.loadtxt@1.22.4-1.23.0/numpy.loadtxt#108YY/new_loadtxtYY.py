import numpy as np
data = np.loadtxt('/home/zhang/Packages/data.txt', float, delimiter=',', ndmin=2, skiprows=2, unpack=True, usecols=(0, 1), converters=None, like=None, comments='#', encoding='utf-8', quotechar=None)
