from plotly.tools import FigureFactory as FF
import numpy as np
data1 = np.random.randn(200) - 2
data2 = np.random.randn(200)
data3 = np.random.randn(200) + 2
data4 = np.random.randn(200) + 4
hist_data = [data1, data2, data3, data4]
group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']
fig = FF.create_distplot(hist_data,  group_labels,  1.0,  'kde',  [],  [], show_hist=True, show_curve=True, show_rug=True)
