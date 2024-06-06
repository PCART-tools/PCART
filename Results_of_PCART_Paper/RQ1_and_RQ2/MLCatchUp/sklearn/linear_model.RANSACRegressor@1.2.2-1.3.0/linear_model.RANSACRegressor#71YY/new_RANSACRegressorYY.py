from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(random_state=None, loss='absolute_error', min_samples=None, stop_n_inliers=0, max_skips=0, residual_threshold=None, max_trials=100, stop_probability=0.99, is_model_valid=None, is_data_valid=None, stop_score=0, estimator=None)
