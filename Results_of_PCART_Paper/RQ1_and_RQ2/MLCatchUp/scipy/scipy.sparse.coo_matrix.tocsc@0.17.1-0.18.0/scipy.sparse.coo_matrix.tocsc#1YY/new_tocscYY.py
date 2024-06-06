from scipy.sparse import coo_matrix
data = [1, 2, 3]
row_indices = [0, 1, 2]
col_indices = [2, 0, 1]
coo = coo_matrix((data, (row_indices, col_indices)))
csc = coo.tocsc(copy=False)
