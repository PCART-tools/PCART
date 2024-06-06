import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(max_iter=200, verbose=0, init='random', l1_ratio=0.0, tol=0.0001, random_state=0, solver='cd', shuffle=False, beta_loss='frobenius', alpha=0.0, regularization='both')
