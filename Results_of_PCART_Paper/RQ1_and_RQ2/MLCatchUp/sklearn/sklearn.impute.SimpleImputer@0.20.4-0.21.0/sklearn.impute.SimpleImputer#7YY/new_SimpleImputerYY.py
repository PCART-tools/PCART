import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan, 'mean', None, add_indicator=False)
