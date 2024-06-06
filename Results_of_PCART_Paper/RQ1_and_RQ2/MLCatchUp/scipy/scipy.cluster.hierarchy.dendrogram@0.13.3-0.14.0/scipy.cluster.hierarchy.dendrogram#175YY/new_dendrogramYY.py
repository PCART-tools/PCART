import scipy.cluster.hierarchy as sch
import numpy as np
import matplotlib
matplotlib.use('Agg')
Z = np.array([[1, 2, 0.1, 2], [3, 4, 0.2, 3], [0, 5, 0.3, 5], [6, 7, 0.4, 7]])
sch.dendrogram(Z, 30, None, None, True, 'top', None, False, False, True, False, False, None, None, leaf_rotation=None, leaf_label_func=None, no_leaves=False, show_contracted=False, ax=None)
