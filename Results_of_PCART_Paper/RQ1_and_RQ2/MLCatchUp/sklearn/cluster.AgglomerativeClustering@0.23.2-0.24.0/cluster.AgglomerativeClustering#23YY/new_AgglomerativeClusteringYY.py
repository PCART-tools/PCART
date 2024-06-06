from sklearn.cluster import AgglomerativeClustering
import numpy as np
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
clustering = AgglomerativeClustering(2, affinity='euclidean', memory=None, linkage='ward', compute_full_tree='auto', connectivity=None).fit(X, compute_distances=False)
