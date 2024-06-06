from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(fit_intercept=True, eta0=1.0, penalty=None, max_iter=1000, tol=0.001, shuffle=True, verbose=0, alpha=0.0001, l1_ratio=0.15)
