from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(random_state=0, fit_intercept=True, validation_fraction=0.1, verbose=0, eta0=1.0, tol=0.001, alpha=0.0001, early_stopping=False, max_iter=1000, penalty=None, shuffle=True, n_jobs=None, l1_ratio=0.15)
