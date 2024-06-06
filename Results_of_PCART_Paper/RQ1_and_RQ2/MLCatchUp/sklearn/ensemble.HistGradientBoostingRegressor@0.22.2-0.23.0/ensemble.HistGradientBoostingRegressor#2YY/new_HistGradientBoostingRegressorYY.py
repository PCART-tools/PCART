from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.datasets import load_boston
(X, y) = load_boston(return_X_y=True)
est = HistGradientBoostingRegressor('least_squares', verbose=0, random_state=None)
