import numpy as np
from scipy.fft import fft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x, None, axis=(- 1), plan=None)
