import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(None, tol=0.001, max_iter=10, missing_values=0, initial_strategy='mean', n_nearest_features=None, sample_posterior=False, fill_value=None)
