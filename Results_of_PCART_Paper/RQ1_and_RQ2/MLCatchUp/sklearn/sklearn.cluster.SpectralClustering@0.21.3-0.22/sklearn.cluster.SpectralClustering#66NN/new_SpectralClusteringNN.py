from sklearn.cluster import SpectralClustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralClustering(5, None, None, 10, 1.0, 'rbf', 10, 0.0, 'kmeans', 3, 1).fit(X, n_components=None)
