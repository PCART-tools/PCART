import numpy as np
from scipy.fft import idct
x = np.array([1.0, 2.0, 3.0, 4.0])
result = idct(x=x, type=2, n=None, axis=(- 1), orthogonalize=None)
result
