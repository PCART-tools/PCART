from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
(X, y) = make_regression(random_state=0)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=0)
reg = GradientBoostingRegressor(min_impurity_decrease=0.0, min_samples_leaf=1, max_depth=3, alpha=0.9, subsample=1.0, verbose=0, random_state=0, min_impurity_split=None, min_weight_fraction_leaf=0.0, learning_rate=0.1, validation_fraction=0.1, presort='deprecated', n_estimators=100, warm_start=False, max_leaf_nodes=None, loss='ls', max_features=None, criterion='friedman_mse', min_samples_split=2, init=None)
