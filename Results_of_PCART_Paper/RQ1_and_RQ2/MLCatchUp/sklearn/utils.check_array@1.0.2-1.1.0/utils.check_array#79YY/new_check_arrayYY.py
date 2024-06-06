from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(X, ensure_min_features=1, accept_sparse=False, dtype='numeric', force_all_finite=True, accept_large_sparse=True, copy=False, ensure_2d=True, allow_nd=False, ensure_min_samples=1, order=None, input_name='')
