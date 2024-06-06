import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X=X, norm=None, filterrad=4.0, interpolation='nearest', aspect='auto', cmap='viridis', interpolation_stage=None)
