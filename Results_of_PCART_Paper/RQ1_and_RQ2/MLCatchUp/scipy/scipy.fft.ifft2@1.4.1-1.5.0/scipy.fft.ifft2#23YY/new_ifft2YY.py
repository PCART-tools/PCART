from scipy.fft import ifft2
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=complex)
s = (3, 3)
axes = (0, 1)
norm = 'ortho'
overwrite_x = False
result = ifft2(x, s, axes, norm, overwrite_x=overwrite_x, workers=None, plan=None)
