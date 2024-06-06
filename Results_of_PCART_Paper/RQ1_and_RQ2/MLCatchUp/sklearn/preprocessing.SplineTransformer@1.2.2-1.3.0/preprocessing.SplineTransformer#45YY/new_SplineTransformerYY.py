import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(degree=3, order='C', n_knots=5, sparse_output=False)
