from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
(X, y) = make_regression(random_state=0)
(X_train, X_test, y_train, y_test) = train_test_split(X, y, random_state=0)
reg = GradientBoostingRegressor(init=None, min_impurity_decrease=0.0, verbose=0, warm_start=False, learning_rate=0.1, criterion='friedman_mse', min_samples_split=2, n_iter_no_change=None, max_features=None, alpha=0.9, random_state=0, presort='deprecated', max_depth=3, max_leaf_nodes=None, min_weight_fraction_leaf=0.0, loss='ls', n_estimators=100, min_samples_leaf=1, validation_fraction=0.1, min_impurity_split=None, subsample=1.0)
