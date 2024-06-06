import numpy as np
import scipy.sparse as sp
from scipy.sparse import linalg
A = sp.csc_matrix(np.array([[2.0, 0.0], [1.0, 3.0]]))
b = np.array([1.0, 2.0])
x = linalg.spsolve_triangular(A=A, b=b, lower=True, overwrite_A=False, unit_diagonal=False)
