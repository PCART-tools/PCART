import numpy as np
a = np.array([[True, False], [True, True]])
result = np.all(a, axis=0, out=None, keepdims=False)
