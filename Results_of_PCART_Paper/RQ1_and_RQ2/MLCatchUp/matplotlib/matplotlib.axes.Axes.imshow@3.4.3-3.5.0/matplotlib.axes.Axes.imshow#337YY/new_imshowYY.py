import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, aspect='auto', norm=None, filternorm=True, filterrad=4.0, alpha=None, cmap='viridis', vmin=None, interpolation='nearest', interpolation_stage=None)
