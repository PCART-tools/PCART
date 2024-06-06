from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(X, False, ensure_2d=True, accept_large_sparse=True, ensure_min_samples=1, allow_nd=False, order=None, copy=False, force_all_finite=True, dtype='numeric', input_name='')
