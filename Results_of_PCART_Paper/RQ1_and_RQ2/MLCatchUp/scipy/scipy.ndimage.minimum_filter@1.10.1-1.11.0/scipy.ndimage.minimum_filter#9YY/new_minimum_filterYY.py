import numpy as np
from scipy.ndimage import minimum_filter
input_array = np.array([[4, 2, 7], [1, 5, 8], [6, 3, 9]])
output_array = minimum_filter(input_array, (2, 2), None, output=None, axes=None)
