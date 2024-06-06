import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(verbose='deprecated', copy=True, add_indicator=False, fill_value=None, missing_values=np.nan, strategy='mean', keep_empty_features=False)
