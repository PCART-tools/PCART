import pandas as pd
import numpy as np
data = {'A': np.random.rand(5), 'B': np.random.rand(5), 'C': np.random.rand(5)}
df = pd.DataFrame(data)

def custom_gradient(val):
    if val < 0.4:
        return 'background-color: red'
    elif val < 0.7:
        return 'background-color: yellow'
    else:
        return 'background-color: green'
styled_df = df.style.background_gradient('PuBu',  0, high=0, axis=0, subset=None)
