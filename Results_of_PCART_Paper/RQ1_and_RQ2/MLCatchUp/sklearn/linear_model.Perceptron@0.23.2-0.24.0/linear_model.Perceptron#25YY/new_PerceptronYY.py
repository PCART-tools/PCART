from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(penalty=None, fit_intercept=True, verbose=0, shuffle=True, n_jobs=None, eta0=1.0, random_state=0, tol=0.001, alpha=0.0001, max_iter=1000, l1_ratio=0.15)
