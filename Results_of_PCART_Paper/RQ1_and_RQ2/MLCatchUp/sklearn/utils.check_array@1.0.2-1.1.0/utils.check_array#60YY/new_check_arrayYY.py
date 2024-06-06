from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(X, False, allow_nd=False, ensure_min_features=1, ensure_min_samples=1, force_all_finite=True, order=None, ensure_2d=True, estimator=None, dtype='numeric', accept_large_sparse=True, copy=False, input_name='')
