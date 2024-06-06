from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
(X, y) = make_regression(random_state=0)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=0)
reg = GradientBoostingRegressor(max_leaf_nodes=None, n_estimators=100, criterion='friedman_mse', tol=0.0001, min_samples_split=2, loss='ls', alpha=0.9, verbose=0, min_weight_fraction_leaf=0.0, ccp_alpha=0.0, max_features=None, max_depth=3, presort='deprecated', warm_start=False, n_iter_no_change=None, validation_fraction=0.1, min_impurity_split=None, min_impurity_decrease=0.0, random_state=0, init=None, subsample=1.0, learning_rate=0.1, min_samples_leaf=1)
