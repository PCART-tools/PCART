import numpy as np
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(np.nan, strategy='mean', add_indicator=False)
