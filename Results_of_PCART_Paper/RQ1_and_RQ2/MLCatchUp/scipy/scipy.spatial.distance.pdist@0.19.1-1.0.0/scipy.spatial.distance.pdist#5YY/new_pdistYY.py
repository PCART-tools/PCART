from scipy.spatial.distance import pdist
X = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
result = pdist(X=X, metric='euclidean')
