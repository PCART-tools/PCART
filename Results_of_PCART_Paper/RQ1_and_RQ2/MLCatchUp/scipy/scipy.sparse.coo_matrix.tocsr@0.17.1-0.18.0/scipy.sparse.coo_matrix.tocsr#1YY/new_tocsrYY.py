from scipy.sparse import coo_matrix
data = [1, 2, 3, 4]
row = [0, 1, 2, 3]
col = [0, 1, 2, 3]
coo_matrix_obj = coo_matrix((data, (row, col)))
csr_matrix_obj = coo_matrix_obj.tocsr(copy=False)
