import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(2, random_state=0, max_iter=200, solver='cd', tol=0.0001, init='random', alpha=0.0, l1_ratio=0.0, beta_loss='frobenius', regularization='both')
