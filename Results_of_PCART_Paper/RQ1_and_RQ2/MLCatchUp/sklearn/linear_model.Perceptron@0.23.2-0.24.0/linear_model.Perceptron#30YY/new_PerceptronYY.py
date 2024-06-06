from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(tol=0.001, warm_start=False, shuffle=True, n_iter_no_change=5, random_state=0, alpha=0.0001, eta0=1.0, class_weight=None, n_jobs=None, penalty=None, verbose=0, validation_fraction=0.1, max_iter=1000, fit_intercept=True, early_stopping=False, l1_ratio=0.15)
