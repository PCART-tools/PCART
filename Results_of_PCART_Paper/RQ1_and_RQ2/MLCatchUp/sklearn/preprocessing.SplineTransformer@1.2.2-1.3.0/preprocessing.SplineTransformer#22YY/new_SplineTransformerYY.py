import numpy as np
from sklearn.preprocessing import SplineTransformer
X = np.arange(6).reshape(6, 1)
spline = SplineTransformer(knots='uniform', n_knots=5, extrapolation='constant', sparse_output=False)
