from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(tol=0.001, shuffle=True, alpha=0.0001, fit_intercept=True, max_iter=1000, penalty=None, l1_ratio=0.15)
