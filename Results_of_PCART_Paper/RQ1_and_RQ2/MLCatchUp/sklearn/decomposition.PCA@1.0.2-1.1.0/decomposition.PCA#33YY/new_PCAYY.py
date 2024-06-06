import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2, whiten=False, svd_solver='auto', copy=True, n_oversamples=10, power_iteration_normalizer='auto')
