import numpy as np
from scipy.ndimage import zoom
input_data = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
zoomed_data = zoom(input=input_data, zoom=(2, 2, 1), output=None, grid_mode=False)
