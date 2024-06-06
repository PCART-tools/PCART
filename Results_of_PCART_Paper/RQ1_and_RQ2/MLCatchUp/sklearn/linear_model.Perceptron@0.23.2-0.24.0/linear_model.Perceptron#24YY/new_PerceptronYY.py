from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(penalty=None, verbose=0, shuffle=True, eta0=1.0, max_iter=1000, tol=0.001, alpha=0.0001, n_jobs=None, fit_intercept=True, l1_ratio=0.15)
