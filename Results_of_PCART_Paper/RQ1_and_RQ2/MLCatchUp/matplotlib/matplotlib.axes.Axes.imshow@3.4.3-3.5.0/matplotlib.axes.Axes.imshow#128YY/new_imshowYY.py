import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, filternorm=True, aspect='auto', cmap='viridis', filterrad=4.0, norm=None, resample=None, interpolation_stage=None)
