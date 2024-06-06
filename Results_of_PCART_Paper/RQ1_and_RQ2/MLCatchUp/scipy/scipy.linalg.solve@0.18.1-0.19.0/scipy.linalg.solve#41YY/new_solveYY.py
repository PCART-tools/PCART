import scipy.linalg
a = [[3, 2, 0], [1, -1, 0], [0, 5, 1]]
b = [2, 4, -1]
x = scipy.linalg.solve(a, b=b, sym_pos=False, lower=False, overwrite_a=False, overwrite_b=False, debug=False, check_finite=True, assume_a='gen', transposed=False)
