import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(init='random', verbose=0, solver='cd', l1_ratio=0.0, random_state=0, beta_loss='frobenius', n_components=2, alpha=0.0, tol=0.0001, max_iter=200, regularization='both')
