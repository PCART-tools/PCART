import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(max_iter=10, tol=0.001, initial_strategy='mean', n_nearest_features=None, sample_posterior=False, missing_values=0, fill_value=None)
