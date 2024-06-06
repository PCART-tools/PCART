import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(tol=0.0, svd_solver='auto', whiten=False, copy=True, random_state=None, iterated_power='auto', n_oversamples=10, power_iteration_normalizer='auto')
