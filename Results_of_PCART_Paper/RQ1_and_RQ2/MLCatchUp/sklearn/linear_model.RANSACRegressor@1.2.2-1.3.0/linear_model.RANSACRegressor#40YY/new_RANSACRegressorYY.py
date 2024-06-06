from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(None, is_model_valid=None, residual_threshold=None, is_data_valid=None, min_samples=None)
