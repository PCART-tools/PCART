from sklearn.neighbors import radius_neighbors_graph
X = [[0], [3], [1]]
A = radius_neighbors_graph(X=X, radius=1.5, metric='minkowski', p=2, metric_params=None, include_self=None)
