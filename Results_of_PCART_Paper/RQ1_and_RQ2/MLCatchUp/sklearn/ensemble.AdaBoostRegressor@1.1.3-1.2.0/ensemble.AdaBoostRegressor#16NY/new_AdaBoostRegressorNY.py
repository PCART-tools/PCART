from sklearn.ensemble import AdaBoostRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
regr = AdaBoostRegressor(loss='linear', n_estimators=50, random_state=0, learning_rate=1.0, base_estimator=None, estimator=None)
