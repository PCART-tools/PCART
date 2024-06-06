import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, tol=0.001, sample_posterior=False, max_iter=10, n_nearest_features=None, initial_strategy='mean', missing_values=0, keep_empty_features=False)
