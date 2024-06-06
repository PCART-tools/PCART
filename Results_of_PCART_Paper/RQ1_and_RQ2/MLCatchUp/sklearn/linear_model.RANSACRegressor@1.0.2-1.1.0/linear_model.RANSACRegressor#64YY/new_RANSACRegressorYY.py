from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(max_skips=np.inf, residual_threshold=None, max_trials=100, base_estimator=None, min_samples=None, is_data_valid=None, is_model_valid=None, stop_probability=0.99, stop_score=np.inf, stop_n_inliers=np.inf, estimator=None)
