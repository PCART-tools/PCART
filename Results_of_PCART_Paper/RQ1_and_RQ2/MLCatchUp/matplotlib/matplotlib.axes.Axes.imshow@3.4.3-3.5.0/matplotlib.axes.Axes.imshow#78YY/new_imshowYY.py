import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filternorm=True, resample=None, norm=None, filterrad=4.0, cmap='viridis', interpolation_stage=None)
