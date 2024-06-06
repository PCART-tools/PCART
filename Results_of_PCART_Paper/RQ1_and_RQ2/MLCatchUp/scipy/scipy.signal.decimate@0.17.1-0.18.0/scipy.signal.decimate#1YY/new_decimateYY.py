import numpy as np
from scipy.signal import decimate
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
result = decimate(x, 2, zero_phase=None)
