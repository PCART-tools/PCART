from sklearn.preprocessing import OrdinalEncoder
import numpy as np
enc = OrdinalEncoder(categories='auto', handle_unknown='error', unknown_value=None)
