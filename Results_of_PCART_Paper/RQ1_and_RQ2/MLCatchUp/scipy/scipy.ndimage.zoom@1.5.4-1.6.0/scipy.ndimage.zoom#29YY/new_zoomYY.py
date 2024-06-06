import numpy as np
from scipy.ndimage import zoom
input_data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
zoomed_data = zoom(input_data, (2, 2, 1), None, 1, mode='reflect', cval=0.0, prefilter=False, grid_mode=False)
