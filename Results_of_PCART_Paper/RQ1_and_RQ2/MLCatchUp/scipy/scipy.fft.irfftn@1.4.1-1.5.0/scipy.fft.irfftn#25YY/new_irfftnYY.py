import numpy as np
from scipy.fft import irfftn
x = np.random.random((4, 4, 4, 2))
s = (8, 8, 8)
axes = (0, 1, 2)
norm = 'ortho'
overwrite_x = False
workers = 1
result = irfftn(x, s, axes=axes, norm=norm, overwrite_x=overwrite_x, workers=workers, plan=None)
