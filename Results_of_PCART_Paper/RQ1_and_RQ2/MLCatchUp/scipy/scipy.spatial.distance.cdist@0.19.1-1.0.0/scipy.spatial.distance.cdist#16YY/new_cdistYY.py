import numpy as np
from scipy.spatial.distance import cdist
XA = np.array([[1, 2, 3], [4, 5, 6]])
XB = np.array([[7, 8, 9], [10, 11, 12]])
distances = cdist(XA,  XB, metric='euclidean', p=2, V=None)
