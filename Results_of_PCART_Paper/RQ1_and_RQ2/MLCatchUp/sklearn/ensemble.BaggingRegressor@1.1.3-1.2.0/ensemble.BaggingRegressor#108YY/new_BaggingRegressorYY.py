from sklearn.svm import SVR
from sklearn.ensemble import BaggingRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=100, n_features=4, n_informative=2, n_targets=1, random_state=0, shuffle=False)
regr = BaggingRegressor(random_state=None, oob_score=False, bootstrap=True, max_samples=1.0, n_jobs=None, verbose=0, n_estimators=10, max_features=1.0, base_estimator=SVR(), bootstrap_features=False, warm_start=False, estimator=None)
