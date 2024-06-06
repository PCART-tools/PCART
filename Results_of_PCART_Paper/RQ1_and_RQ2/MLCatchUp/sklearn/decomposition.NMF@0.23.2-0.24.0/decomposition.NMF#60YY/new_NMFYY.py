import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(tol=0.0001, random_state=0, max_iter=200, init='random', solver='cd', verbose=0, l1_ratio=0.0, shuffle=False, beta_loss='frobenius', n_components=2, alpha=0.0, regularization='both')
