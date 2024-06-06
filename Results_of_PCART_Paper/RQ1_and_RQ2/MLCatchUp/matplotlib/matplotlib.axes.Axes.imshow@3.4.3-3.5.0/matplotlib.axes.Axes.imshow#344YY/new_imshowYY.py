import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(cmap='viridis', X=X, interpolation='nearest', aspect='auto', vmin=None, resample=None, norm=None, alpha=None, interpolation_stage=None)
