import scipy
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=complex)
result = scipy.fft.hfft2(x, (3, 3), (0, 1), norm='ortho', plan=None)
print(result)
