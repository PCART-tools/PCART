import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, aspect='auto', interpolation='nearest', filternorm=True, alpha=None, norm=None, filterrad=4.0, cmap='viridis', interpolation_stage=None)
