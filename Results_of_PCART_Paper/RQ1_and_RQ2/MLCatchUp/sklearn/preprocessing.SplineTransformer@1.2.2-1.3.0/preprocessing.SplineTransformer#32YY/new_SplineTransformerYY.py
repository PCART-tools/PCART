import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(5, 3, knots='uniform', include_bias=True, order='C', extrapolation='constant', sparse_output=False)
