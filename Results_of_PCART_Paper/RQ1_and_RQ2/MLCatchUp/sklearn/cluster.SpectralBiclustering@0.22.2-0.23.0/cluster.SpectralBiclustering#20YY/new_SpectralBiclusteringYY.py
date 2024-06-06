from sklearn.cluster import SpectralBiclustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralBiclustering(n_clusters=2, method='bistochastic', n_components=6, n_best=3, svd_method='randomized').fit(X)
