import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(5, include_bias=True, extrapolation='constant', degree=3, knots='uniform', sparse_output=False)
