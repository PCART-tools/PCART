from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(penalty=None, max_iter=1000, alpha=0.0001, fit_intercept=True, l1_ratio=0.15)
