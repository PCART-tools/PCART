import plotly.figure_factory as ff
import numpy as np
from scipy.cluster.hierarchy import linkage
X = np.array([[1, 2], [3, 4], [1, 4], [4, 2]])

def custom_linkage(X):
    Z = linkage(X, 'single')
    return Z
fig = ff.create_dendrogram(X, orientation='bottom', labels=None, color_threshold=None)
