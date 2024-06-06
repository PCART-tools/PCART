from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(random_state=None, max_samples=1.0, verbose=0, bootstrap_features=False, bootstrap=True, warm_start=False, max_features=1.0, oob_score=False, n_jobs=None, base_estimator=SVR(), estimator=None)
