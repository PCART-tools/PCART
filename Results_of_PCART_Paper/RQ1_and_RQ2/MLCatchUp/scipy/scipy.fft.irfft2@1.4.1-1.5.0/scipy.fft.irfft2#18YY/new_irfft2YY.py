import numpy as np
from scipy.fft import irfft2
x = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
s = (4, 4)
axes = (0, 1)
norm = 'ortho'
overwrite_x = False
workers = 1
result = irfft2(x, s, axes=axes, norm=norm, overwrite_x=overwrite_x, plan=None)
print(result)
