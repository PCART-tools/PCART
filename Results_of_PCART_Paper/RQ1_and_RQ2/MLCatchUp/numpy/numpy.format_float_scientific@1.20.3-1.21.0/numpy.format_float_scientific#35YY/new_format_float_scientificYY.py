import numpy as np
x = 12345.6789
result = np.format_float_scientific(x=x, precision=2, unique=True, trim='k', sign=False, pad_left=5, exp_digits=3, min_digits=None)
