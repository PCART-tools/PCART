from sklearn.utils import check_array
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
check_array(copy=False, array=X, dtype='numeric', ensure_min_samples=1, force_all_finite=True, allow_nd=False, order=None, ensure_2d=True, accept_large_sparse=True, input_name='')
