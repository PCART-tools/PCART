from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(None, stop_n_inliers=0, max_skips=0, stop_probability=0.99, max_trials=100, stop_score=0, is_model_valid=None, is_data_valid=None, residual_threshold=None, min_samples=None)
