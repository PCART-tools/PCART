import numpy as np
from scipy.fft import rfftn
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
s = (2, 2, 3)
axes = (0, 1, 2)
norm = 'ortho'
overwrite_x = False
workers = 1
result = rfftn(x, s, axes, norm, overwrite_x=overwrite_x, plan=None)
