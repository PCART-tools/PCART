import numpy as np
from scipy.fft import fftn
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = (3, 3)
axes = (0, 1)
norm = 'ortho'
result = fftn(x=x, s=s, plan=None)
