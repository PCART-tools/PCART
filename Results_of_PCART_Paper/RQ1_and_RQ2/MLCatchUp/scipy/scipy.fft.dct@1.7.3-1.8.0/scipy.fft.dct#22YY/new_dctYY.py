from scipy import fft
import numpy as np
x = np.array([1, 2, 3, 4, 5])
result = fft.dct(x, 2, 5, (- 1), 'ortho', overwrite_x=False, orthogonalize=None)
