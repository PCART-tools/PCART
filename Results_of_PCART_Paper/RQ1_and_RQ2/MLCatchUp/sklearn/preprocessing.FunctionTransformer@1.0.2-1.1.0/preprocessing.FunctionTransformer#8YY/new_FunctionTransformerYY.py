import numpy as np
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(accept_sparse=False, validate=False, check_inverse=True, feature_names_out=None)
