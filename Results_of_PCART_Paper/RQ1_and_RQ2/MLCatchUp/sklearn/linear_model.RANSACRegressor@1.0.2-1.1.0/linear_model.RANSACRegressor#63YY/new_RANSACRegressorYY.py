from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
import numpy as np
(X, y) = make_regression(n_samples=200, n_features=2, noise=4.0, random_state=0)
reg = RANSACRegressor(max_skips=np.inf, is_model_valid=None, residual_threshold=None, stop_n_inliers=np.inf, max_trials=100, stop_score=np.inf, base_estimator=None, is_data_valid=None, min_samples=None, estimator=None)
