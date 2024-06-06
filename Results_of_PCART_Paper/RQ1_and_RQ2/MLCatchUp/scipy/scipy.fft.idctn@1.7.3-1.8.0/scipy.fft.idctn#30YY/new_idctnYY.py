from scipy.fft import idctn
import numpy as np
x = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
result = idctn(x, 2, None, None, None, overwrite_x=False, workers=None, orthogonalize=None)
