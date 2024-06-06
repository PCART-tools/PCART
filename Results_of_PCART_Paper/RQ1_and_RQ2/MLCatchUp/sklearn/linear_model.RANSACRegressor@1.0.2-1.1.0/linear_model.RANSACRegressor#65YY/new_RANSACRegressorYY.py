from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(max_skips=np.inf, min_samples=None, stop_score=np.inf, is_data_valid=None, max_trials=100, residual_threshold=None, loss='absolute_error', is_model_valid=None, base_estimator=None, stop_probability=0.99, stop_n_inliers=np.inf, estimator=None)
