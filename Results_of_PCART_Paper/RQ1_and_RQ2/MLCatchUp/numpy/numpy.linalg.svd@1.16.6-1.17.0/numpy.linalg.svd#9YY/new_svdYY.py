import numpy as np
a = np.array([[1, 2], [3, 4], [5, 6]])
(u, s, vt) = np.linalg.svd(a=a, full_matrices=True, compute_uv=True, hermitian=False)
