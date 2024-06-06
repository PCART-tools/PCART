import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filterrad=4.0, resample=None, filternorm=True, cmap='viridis', interpolation_stage=None)
