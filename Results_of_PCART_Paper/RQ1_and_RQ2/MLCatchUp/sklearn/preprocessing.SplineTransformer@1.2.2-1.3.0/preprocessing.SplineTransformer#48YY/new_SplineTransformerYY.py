import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(n_knots=5, knots='uniform', include_bias=True, order='C', extrapolation='constant', degree=3, sparse_output=False)
