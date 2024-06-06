from sklearn.cluster import SpectralBiclustering
import numpy as np
X = np.array([[1, 1], [2, 1], [1, 0], [4, 7], [3, 5], [3, 6]])
clustering = SpectralBiclustering(2, method='bistochastic').fit(X)
