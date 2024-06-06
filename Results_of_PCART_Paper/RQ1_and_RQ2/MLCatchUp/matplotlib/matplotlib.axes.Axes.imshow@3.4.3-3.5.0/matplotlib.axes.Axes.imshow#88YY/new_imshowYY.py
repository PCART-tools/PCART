import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(filternorm=True, cmap='viridis', filterrad=4.0, norm=None, X=X, resample=None, interpolation_stage=None)
