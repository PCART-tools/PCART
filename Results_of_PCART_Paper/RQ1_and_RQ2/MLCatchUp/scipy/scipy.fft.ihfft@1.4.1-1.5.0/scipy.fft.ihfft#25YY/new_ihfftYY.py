import numpy as np
from scipy.fft import ihfft
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
n = 5
axis = -1
norm = 'ortho'
overwrite_x = False
workers = 1
result = ihfft(x, n, axis=axis, norm=norm, overwrite_x=overwrite_x, workers=workers, plan=None)
