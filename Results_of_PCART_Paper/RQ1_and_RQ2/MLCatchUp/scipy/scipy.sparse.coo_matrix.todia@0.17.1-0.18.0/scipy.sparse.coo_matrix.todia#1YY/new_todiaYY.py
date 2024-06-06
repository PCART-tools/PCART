from scipy.sparse import coo_matrix
data = [1, 2, 3]
row = [0, 1, 2]
col = [0, 1, 2]
coo = coo_matrix((data, (row, col)), shape=(3, 3))
coo.todia(copy=False)
