import plotly.express as px
import numpy as np
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]], [[0, 255, 0], [0, 0, 255], [255, 0, 0]]], dtype=np.uint8)
fig = px.imshow(img_rgb, None, None, None, {}, None, None, None, None, None, None, None, None, None, None, None, template=None, width=None, height=None, aspect=None, contrast_rescaling=None, text_auto=False)
