import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(whiten=False, n_components=2, iterated_power='auto', svd_solver='auto', copy=True, tol=0.0, n_oversamples=10, power_iteration_normalizer='auto')
