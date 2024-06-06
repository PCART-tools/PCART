import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(2, l1_ratio=0.0, alpha=0.0, init='random', verbose=0, tol=0.0001, solver='cd', shuffle=False, max_iter=200, random_state=0, beta_loss='frobenius', regularization='both')
