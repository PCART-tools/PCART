import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(solver='cd', beta_loss='frobenius', tol=0.0001, random_state=0, init='random', max_iter=200, alpha=0.0, regularization='both')
