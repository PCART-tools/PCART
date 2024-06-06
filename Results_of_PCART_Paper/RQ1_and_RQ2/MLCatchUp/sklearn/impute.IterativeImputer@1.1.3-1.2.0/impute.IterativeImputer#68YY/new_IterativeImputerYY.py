import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
imp_mean = IterativeImputer(missing_values=0, max_iter=10, sample_posterior=False, estimator=None, keep_empty_features=False)
