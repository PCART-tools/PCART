from sklearn.datasets import make_blobs
(X, y) = make_blobs(10, 2, shuffle=True, centers=3, cluster_std=1.0, center_box=((- 10.0), 10.0), return_centers=False)
