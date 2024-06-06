from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(None, stop_probability=0.99, max_trials=100, is_model_valid=None, loss='absolute_error', stop_score=0, residual_threshold=None, max_skips=0, min_samples=None, random_state=None, stop_n_inliers=0, is_data_valid=None, base_estimator='deprecated')
