import numpy as np
from scipy import signal
data = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
result = signal.detrend(data, axis=0, type='linear', bp=1, overwrite_data=False)
print(result)
