import plotly.figure_factory as ff
import numpy as np
(x, y) = np.meshgrid(np.arange(-2, 2, 0.2), np.arange(-2, 2, 0.25))
u = np.cos(x) * y
v = np.sin(x) * y
fig = ff.create_quiver(x=x, y=y, u=u, v=v, scale=0.1, arrow_scale=0.3, angle=0.3490658503988659, scaleratio=None)
