import numpy as np
result = np.argmin(np.array([[4, 2, 7], [1, 9, 3]]), axis=1, out=np.empty(2, dtype=int))
