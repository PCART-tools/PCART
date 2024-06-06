from scipy.sparse import coo_matrix
coo = coo_matrix(([1, 2, 3, 4], ([0, 1, 2, 3], [1, 2, 0, 3])), shape=(4, 4))
bsr = coo.tobsr(copy=False)
