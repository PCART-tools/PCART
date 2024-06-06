from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
(X, y) = make_regression(random_state=0)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=0)
reg = GradientBoostingRegressor(loss='ls', min_weight_fraction_leaf=0.0, subsample=1.0, min_samples_split=2, criterion='friedman_mse', n_estimators=100, learning_rate=0.1, min_samples_leaf=1)
