from sklearn.datasets import make_blobs
(X, y) = make_blobs(10, 2, cluster_std=1.0, center_box=((- 10.0), 10.0), shuffle=True, random_state=0, centers=3, return_centers=False)
