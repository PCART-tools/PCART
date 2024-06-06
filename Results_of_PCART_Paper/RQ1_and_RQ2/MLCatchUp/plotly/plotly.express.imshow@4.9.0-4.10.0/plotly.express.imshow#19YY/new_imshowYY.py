import plotly.express as px
import numpy as np
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [255, 0, 0]]], dtype=np.uint8)
fig = px.imshow(img_rgb, zmin=None, zmax=None, origin=None, labels={}, contrast_rescaling=None, binary_string=None, binary_backend='auto', binary_compression_level=4, binary_format='png')
