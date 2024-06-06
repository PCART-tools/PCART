from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(10, max_features=1.0, warm_start=False, bootstrap_features=False, max_samples=1.0, n_jobs=None, bootstrap=True, oob_score=False, base_estimator=SVR(), estimator=None)
