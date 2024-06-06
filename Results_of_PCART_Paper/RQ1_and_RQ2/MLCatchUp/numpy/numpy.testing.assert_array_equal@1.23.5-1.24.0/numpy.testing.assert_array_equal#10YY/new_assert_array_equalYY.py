import numpy as np
from numpy.testing import assert_array_equal
x = np.array([1, 2, 3])
y = np.array([1, 2, 3])
assert_array_equal(x, y, err_msg='', verbose=True, strict=False)
