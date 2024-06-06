import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, aspect='auto', filternorm=True, cmap='viridis', norm=None, interpolation_stage=None)
