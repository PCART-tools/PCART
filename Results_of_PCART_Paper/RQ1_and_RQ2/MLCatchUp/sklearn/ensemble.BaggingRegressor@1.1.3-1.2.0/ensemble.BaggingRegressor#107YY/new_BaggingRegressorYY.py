from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(max_features=1.0, random_state=None, warm_start=False, oob_score=False, bootstrap_features=False, n_jobs=None, bootstrap=True, base_estimator=SVR(), n_estimators=10, max_samples=1.0, estimator=None)
