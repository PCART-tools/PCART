import numpy as np
x = 12345.6789
result = np.format_float_scientific(x, 2, True, 'k', False, pad_left=5, min_digits=None)
