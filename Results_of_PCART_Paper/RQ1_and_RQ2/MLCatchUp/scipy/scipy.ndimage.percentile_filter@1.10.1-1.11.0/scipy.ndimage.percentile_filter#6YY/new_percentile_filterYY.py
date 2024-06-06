from scipy.ndimage import percentile_filter
import numpy as np
input = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
percentile = 50
size = (3, 3)
footprint = None
output = None
mode = 'reflect'
cval = 0.0
origin = 0
result = percentile_filter(input, percentile, size, footprint=footprint, axes=None)
