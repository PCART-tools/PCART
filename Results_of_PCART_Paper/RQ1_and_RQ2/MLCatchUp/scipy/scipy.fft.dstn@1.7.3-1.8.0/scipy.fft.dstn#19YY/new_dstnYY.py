import numpy as np
from scipy.fft import dstn
x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=float)
result = dstn(x, type=2, s=(2, 2), axes=(0, 1), norm='ortho', orthogonalize=None)
