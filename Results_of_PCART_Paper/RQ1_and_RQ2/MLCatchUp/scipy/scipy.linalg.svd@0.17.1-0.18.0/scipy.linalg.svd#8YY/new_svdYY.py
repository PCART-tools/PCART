from scipy.linalg import svd
a = [[1, 2], [3, 4], [5, 6]]
(u, s, vt) = svd(a, full_matrices=True, compute_uv=True, lapack_driver='gesdd')
