from scipy.fft import ifftn
import numpy as np
x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
s = None
axes = None
norm = None
overwrite_x = False
workers = None
result = ifftn(x, s, axes, plan=None)
result
