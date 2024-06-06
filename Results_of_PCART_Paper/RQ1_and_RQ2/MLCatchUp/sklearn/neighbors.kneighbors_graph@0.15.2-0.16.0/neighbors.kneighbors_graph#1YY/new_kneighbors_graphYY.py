from sklearn.neighbors import kneighbors_graph
X = [[0], [3], [1]]
A = kneighbors_graph(X, 2, metric='minkowski', p=2, metric_params=None, include_self=None)
