from scipy.linalg import svd
a = [[1, 2], [3, 4], [5, 6]]
(u, s, vt) = svd(a, True, compute_uv=True, overwrite_a=False, lapack_driver='gesdd')
