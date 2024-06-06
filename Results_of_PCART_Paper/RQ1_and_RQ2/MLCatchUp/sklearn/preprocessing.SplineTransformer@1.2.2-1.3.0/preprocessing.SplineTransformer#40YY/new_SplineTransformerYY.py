import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(5, degree=3, order='C', include_bias=True, knots='uniform', extrapolation='constant', sparse_output=False)
