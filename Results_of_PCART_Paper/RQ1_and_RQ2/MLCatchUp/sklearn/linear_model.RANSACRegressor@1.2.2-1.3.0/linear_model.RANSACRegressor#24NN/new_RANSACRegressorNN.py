from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(stop_n_inliers=0, random_state=None, min_samples=None, base_estimator='deprecated', max_skips=0, stop_score=0, is_data_valid=None, is_model_valid=None, max_trials=100, residual_threshold=None, stop_probability=0.99, loss='absolute_error')
