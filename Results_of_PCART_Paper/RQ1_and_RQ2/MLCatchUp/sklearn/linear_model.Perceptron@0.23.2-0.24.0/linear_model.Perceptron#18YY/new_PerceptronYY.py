from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(fit_intercept=True, penalty=None, alpha=0.0001, l1_ratio=0.15)
