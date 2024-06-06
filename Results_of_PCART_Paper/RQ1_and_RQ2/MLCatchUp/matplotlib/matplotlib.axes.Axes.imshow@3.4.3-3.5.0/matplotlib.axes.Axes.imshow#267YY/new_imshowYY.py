import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(filterrad=4.0, norm=None, aspect='auto', interpolation='nearest', X=X, alpha=None, cmap='viridis', filternorm=True, interpolation_stage=None)
