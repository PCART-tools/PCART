from sklearn.cluster import SpectralBiclustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralBiclustering(2, mini_batch=False, init='k-means++', n_init=10, n_jobs=None, method='bistochastic', n_components=6, n_best=3, svd_method='randomized', n_svd_vecs=None).fit(X)
