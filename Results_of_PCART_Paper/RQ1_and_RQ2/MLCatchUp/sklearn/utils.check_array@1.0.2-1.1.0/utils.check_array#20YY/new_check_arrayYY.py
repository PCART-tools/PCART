from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(X, force_all_finite=True, ensure_min_features=1, copy=False, allow_nd=False, ensure_min_samples=1, dtype='numeric', accept_large_sparse=True, estimator=None, ensure_2d=True, order=None, input_name='')
