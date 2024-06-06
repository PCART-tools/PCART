from scipy.sparse import coo_matrix
rows = [0, 1, 2, 3]
cols = [1, 2, 3, 4]
data = [10, 20, 30, 40]
coo = coo_matrix((data, (rows, cols)), shape=(4, 5))
dok = coo.todok(copy=False)
print(dok)
