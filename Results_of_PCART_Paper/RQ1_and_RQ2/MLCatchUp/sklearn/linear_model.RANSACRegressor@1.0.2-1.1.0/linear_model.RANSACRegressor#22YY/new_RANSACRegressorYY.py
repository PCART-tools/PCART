from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(stop_n_inliers=np.inf, loss='absolute_error', is_data_valid=None, stop_probability=0.99, max_skips=np.inf, residual_threshold=None, min_samples=None, stop_score=np.inf, is_model_valid=None, max_trials=100, random_state=None, estimator=None)
