from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(bootstrap=True, n_jobs=None, max_samples=1.0, warm_start=False, random_state=None, bootstrap_features=False, verbose=0, oob_score=False, max_features=1.0, estimator=None)
