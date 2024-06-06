from plotly.figure_factory import create_violin
import numpy as np
from scipy import stats
data_list = np.random.randn(100)
fig = create_violin(data_list, data_header=None, group_header=None, colors='#604d9e', sort=False)
