import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, aspect='auto', cmap='viridis', norm=None, filternorm=True, alpha=None, interpolation='nearest', interpolation_stage=None)
