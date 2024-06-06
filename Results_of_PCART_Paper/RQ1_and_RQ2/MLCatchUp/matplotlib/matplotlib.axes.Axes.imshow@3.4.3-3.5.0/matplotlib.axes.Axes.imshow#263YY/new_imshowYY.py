import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(aspect='auto', X=X, interpolation='nearest', norm=None, filterrad=4.0, cmap='viridis', alpha=None, interpolation_stage=None)
