import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(tol=0.0, random_state=None, iterated_power='auto', svd_solver='auto', copy=True, n_components=2, whiten=False, n_oversamples=10, power_iteration_normalizer='auto')
