from sklearn.preprocessing import OrdinalEncoder
import numpy as np
enc = OrdinalEncoder(dtype=np.float, handle_unknown='error', unknown_value=None)
