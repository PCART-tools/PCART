from scipy.linalg import svd
a = [[1, 2], [3, 4], [5, 6]]
(u, s, vt) = svd(a, True, True, False, True, lapack_driver='gesdd')
