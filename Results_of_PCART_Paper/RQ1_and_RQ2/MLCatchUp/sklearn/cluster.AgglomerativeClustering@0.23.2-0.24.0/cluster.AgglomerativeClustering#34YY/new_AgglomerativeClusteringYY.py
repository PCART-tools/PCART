from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
clustering = AgglomerativeClustering(n_clusters=2, connectivity=None, memory=None, compute_full_tree='auto', affinity='euclidean').fit(X, compute_distances=False)
