from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(verbose=0, alpha=0.0001, max_iter=1000, penalty=None, fit_intercept=True, tol=0.001, shuffle=True, l1_ratio=0.15)
