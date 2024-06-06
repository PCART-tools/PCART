import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(tol=0.001, sample_posterior=False, missing_values=0, max_iter=10, fill_value=None)
