import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(missing_values=0, sample_posterior=False, initial_strategy='mean', estimator=None, max_iter=10, n_nearest_features=None, tol=0.001, fill_value=None)
