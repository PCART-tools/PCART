import numpy as np
from scipy.signal import resample
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
num = 7
t = None
axis = 0
window = None
result = resample(x, num=num, domain='time')
