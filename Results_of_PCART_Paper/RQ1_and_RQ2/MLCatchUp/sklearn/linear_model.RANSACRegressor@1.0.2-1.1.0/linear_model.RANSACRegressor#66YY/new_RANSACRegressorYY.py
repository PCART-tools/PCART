from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(stop_score=np.inf, loss='absolute_error', stop_n_inliers=np.inf, min_samples=None, random_state=None, is_model_valid=None, max_trials=100, is_data_valid=None, stop_probability=0.99, max_skips=np.inf, base_estimator=None, residual_threshold=None, estimator=None)
