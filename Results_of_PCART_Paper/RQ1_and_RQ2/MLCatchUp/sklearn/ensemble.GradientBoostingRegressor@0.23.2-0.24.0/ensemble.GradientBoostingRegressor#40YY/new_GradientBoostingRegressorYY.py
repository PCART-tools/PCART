from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
(X, y) = make_regression(random_state=0)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=0)
reg = GradientBoostingRegressor(subsample=1.0, min_impurity_split=None, max_depth=3, alpha=0.9, verbose=0, criterion='friedman_mse', min_samples_split=2, loss='ls', max_features=None, random_state=0, max_leaf_nodes=None, min_samples_leaf=1, min_weight_fraction_leaf=0.0, n_estimators=100, init=None, min_impurity_decrease=0.0, learning_rate=0.1)
