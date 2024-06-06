from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.datasets import load_boston
(X, y) = load_boston(return_X_y=True)
est = HistGradientBoostingRegressor('least_squares', max_bins=255, warm_start=False, scoring=None, validation_fraction=0.1, n_iter_no_change=10, tol=1e-07, learning_rate=0.1, max_iter=100, max_leaf_nodes=31, max_depth=None, min_samples_leaf=20, l2_regularization=0.0, verbose=0, random_state=None)
