import numpy as np
from scipy.fft import idstn
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
result = idstn(x, 2, (2, 3), (0, 2), norm='ortho', overwrite_x=False, orthogonalize=None)
print(result)
