import numpy as np
from scipy.fft import idct
x = np.array([1.0, 2.0, 3.0, 4.0])
result = idct(x, 2, n=None, axis=(- 1), norm=None, overwrite_x=False, orthogonalize=None)
result
