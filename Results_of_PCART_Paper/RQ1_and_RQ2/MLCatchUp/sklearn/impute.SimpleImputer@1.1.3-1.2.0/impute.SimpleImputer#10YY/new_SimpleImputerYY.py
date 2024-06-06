import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(fill_value=None, verbose='deprecated', missing_values=np.nan, strategy='mean', keep_empty_features=False)
