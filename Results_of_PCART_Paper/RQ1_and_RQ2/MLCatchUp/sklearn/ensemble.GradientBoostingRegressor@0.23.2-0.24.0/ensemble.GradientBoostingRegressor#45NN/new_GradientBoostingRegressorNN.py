from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
(X, y) = make_regression(random_state=0)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=0)
reg = GradientBoostingRegressor(min_impurity_decrease=0.0, min_weight_fraction_leaf=0.0, random_state=0, min_samples_split=2, max_features=None, n_iter_no_change=None, tol=0.0001, presort='deprecated', loss='ls', max_leaf_nodes=None, alpha=0.9, subsample=1.0, verbose=0, init=None, min_samples_leaf=1, min_impurity_split=None, criterion='friedman_mse', max_depth=3, learning_rate=0.1, validation_fraction=0.1, warm_start=False, n_estimators=100)
