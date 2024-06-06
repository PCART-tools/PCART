import numpy as np
from scipy.linalg import solve_continuous_are
a = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
q = np.array([[7, 8], [8, 10]])
r = np.array([[11]])
solution = solve_continuous_are(a, b, q=q, r=r, e=None, s=None, balanced=True)
