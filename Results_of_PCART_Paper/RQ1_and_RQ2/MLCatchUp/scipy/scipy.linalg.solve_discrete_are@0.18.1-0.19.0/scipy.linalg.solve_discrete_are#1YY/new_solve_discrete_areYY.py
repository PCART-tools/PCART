import numpy as np
from scipy.linalg import solve_discrete_are
a = np.array([[1.1, 0.5], [0.2, 1.1]])
b = np.array([[1.0], [0.0]])
q = np.array([[1.0, 0.0], [0.0, 1.0]])
r = np.array([[1.0]])
solution = solve_discrete_are(a, b, q, r, e=None, s=None, balanced=True)
