import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', filterrad=4.0, url=None, resample=None, filternorm=True, interpolation_stage=None)
