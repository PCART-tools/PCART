from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(max_skips=np.inf, residual_threshold=None, stop_score=np.inf, loss='absolute_error', stop_probability=0.99, max_trials=100, stop_n_inliers=np.inf, is_model_valid=None, random_state=None, is_data_valid=None, min_samples=None, base_estimator=None, estimator=None)
