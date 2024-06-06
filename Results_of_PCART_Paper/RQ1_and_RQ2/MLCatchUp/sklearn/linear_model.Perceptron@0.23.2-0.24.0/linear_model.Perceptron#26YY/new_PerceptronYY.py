from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
(X, y) = load_digits(return_X_y=True)
clf = Perceptron(n_jobs=None, tol=0.001, max_iter=1000, penalty=None, alpha=0.0001, random_state=0, verbose=0, eta0=1.0, shuffle=True, fit_intercept=True, early_stopping=False, l1_ratio=0.15)
