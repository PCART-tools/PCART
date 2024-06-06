import numpy as np
from scipy.ndimage import gaussian_filter1d
input = np.array([1, 2, 3, 4, 5])
sigma = 1.5
axis = 0
order = 1
output = None
mode = 'constant'
cval = 0.0
truncate = 4.0
result = gaussian_filter1d(input, sigma, axis, order, output=output, mode=mode, cval=cval, truncate=truncate, radius=None)
