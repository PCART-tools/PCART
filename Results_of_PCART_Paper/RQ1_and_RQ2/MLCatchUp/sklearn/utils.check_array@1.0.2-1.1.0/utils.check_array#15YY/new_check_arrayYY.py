from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(X, dtype='numeric', accept_large_sparse=True, copy=False, order=None, force_all_finite=True, input_name='')
