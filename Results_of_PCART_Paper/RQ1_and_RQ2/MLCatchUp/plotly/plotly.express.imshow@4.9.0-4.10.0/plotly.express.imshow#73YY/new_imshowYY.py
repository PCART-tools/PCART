import plotly.express as px
import numpy as np
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [255, 0, 0]]], dtype=np.uint8)
fig = px.imshow(img_rgb, None, None, None, labels={}, x=None, y=None, color_continuous_scale=None, color_continuous_midpoint=None, range_color=None, title=None, contrast_rescaling=None, binary_string=None, binary_backend='auto', binary_compression_level=4, binary_format='png')
