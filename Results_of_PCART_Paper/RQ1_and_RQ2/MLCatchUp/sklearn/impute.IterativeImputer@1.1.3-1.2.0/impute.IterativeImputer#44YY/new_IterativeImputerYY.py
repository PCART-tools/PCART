import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, max_iter=10, n_nearest_features=None, sample_posterior=False, missing_values=0, tol=0.001, keep_empty_features=False)
