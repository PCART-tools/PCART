import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(filterrad=4.0, aspect='auto', norm=None, cmap='viridis', X=X, interpolation_stage=None)
