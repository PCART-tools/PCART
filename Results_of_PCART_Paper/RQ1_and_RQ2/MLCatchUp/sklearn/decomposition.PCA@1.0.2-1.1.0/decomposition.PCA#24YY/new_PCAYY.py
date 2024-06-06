import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(2, random_state=None, tol=0.0, copy=True, svd_solver='auto', iterated_power='auto', whiten=False, n_oversamples=10, power_iteration_normalizer='auto')
