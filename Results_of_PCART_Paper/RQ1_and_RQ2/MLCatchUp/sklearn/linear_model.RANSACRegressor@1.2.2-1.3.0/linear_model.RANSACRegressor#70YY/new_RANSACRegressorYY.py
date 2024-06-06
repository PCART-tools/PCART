from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(is_model_valid=None, max_trials=100, loss='absolute_error', stop_score=0, estimator=None, residual_threshold=None, is_data_valid=None, stop_probability=0.99, stop_n_inliers=0, min_samples=None, max_skips=0)
