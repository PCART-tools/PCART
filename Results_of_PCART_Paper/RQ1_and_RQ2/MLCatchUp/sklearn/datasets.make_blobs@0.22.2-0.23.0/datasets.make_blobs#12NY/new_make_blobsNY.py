from sklearn.datasets import make_blobs
(X, y) = make_blobs(10, 2, cluster_std=1.0, centers=3, return_centers=False)
