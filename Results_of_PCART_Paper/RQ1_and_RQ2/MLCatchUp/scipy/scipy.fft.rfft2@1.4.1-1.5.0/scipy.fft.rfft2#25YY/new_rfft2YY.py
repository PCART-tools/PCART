import numpy as np
from scipy.fft import rfft2
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
result = rfft2(x, (4, 4), axes=(0, 1), norm='ortho', overwrite_x=False, workers=None, plan=None)
