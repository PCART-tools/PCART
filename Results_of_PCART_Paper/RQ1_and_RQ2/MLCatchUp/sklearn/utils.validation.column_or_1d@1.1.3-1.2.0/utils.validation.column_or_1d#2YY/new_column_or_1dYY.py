from sklearn.utils.validation import column_or_1d
import numpy as np
y = np.array([1, 2, 3, 4, 5, 6])
column_or_1d(y, warn=False, dtype=None)
