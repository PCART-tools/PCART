import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(extrapolation='constant', include_bias=True, knots='uniform', degree=3, n_knots=5, sparse_output=False)
