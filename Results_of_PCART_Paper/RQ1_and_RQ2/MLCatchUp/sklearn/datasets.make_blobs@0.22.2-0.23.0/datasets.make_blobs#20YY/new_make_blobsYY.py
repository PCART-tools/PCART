from sklearn.datasets import make_blobs
(X, y) = make_blobs(10, n_features=2, centers=3, cluster_std=1.0, center_box=((- 10.0), 10.0), return_centers=False)
