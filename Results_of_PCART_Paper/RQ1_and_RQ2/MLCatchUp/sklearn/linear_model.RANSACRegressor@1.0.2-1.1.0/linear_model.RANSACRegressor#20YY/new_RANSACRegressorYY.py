from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(is_data_valid=None, max_trials=100, stop_probability=0.99, is_model_valid=None, max_skips=np.inf, stop_n_inliers=np.inf, min_samples=None, stop_score=np.inf, residual_threshold=None, estimator=None)
