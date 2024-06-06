from scipy.sparse import coo_matrix, lil_matrix
data = [1, 2, 3, 4]
row_indices = [0, 1, 2, 3]
col_indices = [0, 1, 2, 3]
coo = coo_matrix((data, (row_indices, col_indices)), shape=(4, 4))
lil = coo.tolil(copy=False)
