import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(alpha=0.0, init='random', random_state=0, solver='cd', beta_loss='frobenius', tol=0.0001, max_iter=200, n_components=2, l1_ratio=0.0, regularization='both')
