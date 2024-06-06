import numpy as np
a = np.array([[10, 7, 4], [3, 2, 1]])
result = np.percentile(a, [25, 50, 75], None, None, False, interpolation='linear', keepdims=False, method='linear')
print(result)
