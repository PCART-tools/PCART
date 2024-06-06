import scipy.linalg
a = [[4, 7, 1], [3, 4, 7], [2, 0, 7]]
(lu, piv, q) = scipy.linalg.lu(a, permute_l=False, overwrite_a=False, check_finite=True, p_indices=False)
