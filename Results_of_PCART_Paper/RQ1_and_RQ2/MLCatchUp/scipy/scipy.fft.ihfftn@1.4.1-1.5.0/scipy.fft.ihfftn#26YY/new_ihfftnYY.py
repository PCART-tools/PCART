import numpy as np
from scipy.fft import ihfftn
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=float)
s = (2, 3, 2)
axes = (0, 1, 2)
norm = 'ortho'
overwrite_x = False
result = ihfftn(x, s=s, axes=axes, norm=norm, overwrite_x=overwrite_x, workers=None, plan=None)
