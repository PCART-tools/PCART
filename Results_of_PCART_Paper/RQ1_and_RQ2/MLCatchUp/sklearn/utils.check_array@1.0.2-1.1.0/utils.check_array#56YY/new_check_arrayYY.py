from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(X, False, dtype='numeric', accept_large_sparse=True, copy=False, ensure_2d=True, force_all_finite=True, order=None, input_name='')
