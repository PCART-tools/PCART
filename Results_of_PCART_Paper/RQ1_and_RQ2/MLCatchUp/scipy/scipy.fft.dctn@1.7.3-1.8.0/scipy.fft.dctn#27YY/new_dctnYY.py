import numpy as np
from scipy.fft import dctn
x = np.random.randn(4, 4, 4)
result = dctn(x=x, type=2, s=(3, 3, 3), axes=(0, 1, 2), norm='ortho', overwrite_x=False, orthogonalize=None)
