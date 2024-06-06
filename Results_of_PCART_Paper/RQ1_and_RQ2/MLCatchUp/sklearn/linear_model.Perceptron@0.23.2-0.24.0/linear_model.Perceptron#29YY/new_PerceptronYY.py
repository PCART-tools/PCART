from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(shuffle=True, early_stopping=False, n_jobs=None, verbose=0, random_state=0, n_iter_no_change=5, eta0=1.0, class_weight=None, alpha=0.0001, max_iter=1000, fit_intercept=True, validation_fraction=0.1, tol=0.001, penalty=None, l1_ratio=0.15)
