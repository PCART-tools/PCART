import numpy as np
from scipy import ndimage
input_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = 2
size = (3, 3)
output_array = ndimage.rank_filter(input_array, rank=rank, size=size, footprint=None, output=None, axes=None)
print(output_array)
