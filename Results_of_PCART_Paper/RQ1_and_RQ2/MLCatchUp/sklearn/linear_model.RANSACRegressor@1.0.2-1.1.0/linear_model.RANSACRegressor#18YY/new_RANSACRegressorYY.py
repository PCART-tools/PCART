from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(is_data_valid=None, max_skips=np.inf, is_model_valid=None, max_trials=100, min_samples=None, residual_threshold=None, stop_n_inliers=np.inf, estimator=None)
