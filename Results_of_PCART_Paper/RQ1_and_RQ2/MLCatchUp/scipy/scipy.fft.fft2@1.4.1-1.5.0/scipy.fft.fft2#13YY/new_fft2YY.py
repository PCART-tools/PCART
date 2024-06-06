import numpy as np
from scipy.fft import fft2
x = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
result = fft2(x, s=(3, 3), axes=(0, 1), norm='ortho', plan=None)
