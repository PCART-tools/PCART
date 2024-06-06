import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(init='random', solver='cd', n_components=2, random_state=0, beta_loss='frobenius', max_iter=200, alpha=0.0, tol=0.0001, regularization='both')
