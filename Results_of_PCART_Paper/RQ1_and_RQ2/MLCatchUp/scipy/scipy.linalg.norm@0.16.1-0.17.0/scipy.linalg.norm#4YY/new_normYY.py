from scipy import linalg
a = [[1, 2], [3, 4]]
result = linalg.norm(a, ord='fro', axis=None, keepdims=False)
