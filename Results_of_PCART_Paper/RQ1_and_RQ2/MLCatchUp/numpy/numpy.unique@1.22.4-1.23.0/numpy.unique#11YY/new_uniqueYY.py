import numpy as np
ar = np.array([1, 2, 2, 3, 3, 3])
(unique_values, unique_indices, unique_inverse, unique_counts) = np.unique(ar=ar, return_index=True, return_inverse=True, return_counts=True, axis=None, equal_nan=True)
(unique_values, unique_indices, unique_inverse, unique_counts)
