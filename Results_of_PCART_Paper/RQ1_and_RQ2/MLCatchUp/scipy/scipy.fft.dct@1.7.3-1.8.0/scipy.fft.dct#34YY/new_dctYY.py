from scipy import fft
import numpy as np
x = np.array([1, 2, 3, 4, 5])
result = fft.dct(x, type=2, n=5, axis=(- 1), norm='ortho', overwrite_x=False, workers=None, orthogonalize=None)
