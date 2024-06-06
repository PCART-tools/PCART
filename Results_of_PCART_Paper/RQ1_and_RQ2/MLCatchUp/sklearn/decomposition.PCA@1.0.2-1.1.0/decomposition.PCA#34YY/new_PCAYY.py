import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(copy=True, n_components=2, svd_solver='auto', whiten=False, tol=0.0, n_oversamples=10, power_iteration_normalizer='auto')
