import numpy as np
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = np.linalg.matrix_rank(M=M, tol=None, hermitian=False)
print(result)
