import numpy as np
from scipy.ndimage import spline_filter1d
input = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
order = 3
axis = -1
output = np.float64
result = spline_filter1d(input, order, axis, mode='mirror')
