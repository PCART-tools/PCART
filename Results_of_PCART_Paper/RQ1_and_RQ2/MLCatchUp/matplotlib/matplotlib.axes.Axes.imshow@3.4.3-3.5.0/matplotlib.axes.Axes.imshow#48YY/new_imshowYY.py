import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(filternorm=True, X=X, cmap='viridis', filterrad=4.0, resample=None, interpolation_stage=None)
