import numpy as np
from scipy.interpolate import interp1d
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 1.0, 4.0, 9.0, 16.0])
f = interp1d(x, y, 'linear', axis=(- 1), copy=True, bounds_error=True, assume_sorted=False)
