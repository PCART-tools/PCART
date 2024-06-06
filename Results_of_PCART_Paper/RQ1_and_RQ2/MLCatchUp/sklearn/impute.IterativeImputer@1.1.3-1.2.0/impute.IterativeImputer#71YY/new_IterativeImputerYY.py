import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(tol=0.001, sample_posterior=False, max_iter=10, n_nearest_features=None, missing_values=0, estimator=None, initial_strategy='mean', keep_empty_features=False)
