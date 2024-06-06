import numpy as np
from sklearn import datasets, cluster
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
agglo = cluster.FeatureAgglomeration(2, 'euclidean', None, None, compute_full_tree='auto', linkage='ward', pooling_func=np.mean, distance_threshold=None)
