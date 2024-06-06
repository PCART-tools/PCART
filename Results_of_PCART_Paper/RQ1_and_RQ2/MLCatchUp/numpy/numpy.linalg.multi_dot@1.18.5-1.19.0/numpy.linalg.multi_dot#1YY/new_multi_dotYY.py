import numpy as np
A = np.random.rand(3, 4)
B = np.random.rand(4, 5)
C = np.random.rand(5, 6)
result = np.linalg.multi_dot([A, B, C], out=None)
