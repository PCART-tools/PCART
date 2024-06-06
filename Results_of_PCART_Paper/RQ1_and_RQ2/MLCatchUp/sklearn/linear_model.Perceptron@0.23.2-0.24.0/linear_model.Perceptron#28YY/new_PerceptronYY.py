from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(verbose=0, n_jobs=None, eta0=1.0, random_state=0, shuffle=True, n_iter_no_change=5, tol=0.001, max_iter=1000, alpha=0.0001, early_stopping=False, penalty=None, fit_intercept=True, validation_fraction=0.1, l1_ratio=0.15)
