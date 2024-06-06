import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(n_components=2, max_iter=200, tol=0.0001, init='random', solver='cd', beta_loss='frobenius', regularization='both')
