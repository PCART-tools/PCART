import numpy as np
from scipy.ndimage import zoom
input_data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
zoomed_data = zoom(input_data, (2, 2, 1), output=None, order=1, grid_mode=False)
