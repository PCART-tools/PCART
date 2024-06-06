from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(is_model_valid=None, stop_probability=0.99, stop_score=0, max_trials=100, is_data_valid=None, loss='absolute_error', max_skips=0, stop_n_inliers=0, residual_threshold=None, base_estimator='deprecated', random_state=None, min_samples=None, estimator=None)
