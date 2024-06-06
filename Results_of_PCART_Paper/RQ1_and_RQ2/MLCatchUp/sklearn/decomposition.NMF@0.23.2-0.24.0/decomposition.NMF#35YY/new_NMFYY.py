import numpy as np
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]])
from sklearn.decomposition import NMF
model = NMF(2, beta_loss='frobenius', solver='cd', init='random', max_iter=200, tol=0.0001, regularization='both')
