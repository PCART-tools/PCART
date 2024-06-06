from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(random_state=None, bootstrap_features=False, warm_start=False, max_samples=1.0, bootstrap=True, oob_score=False, n_jobs=None, max_features=1.0, estimator=None)
