import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(filternorm=True, cmap='viridis', X=X, norm=None, aspect='auto', interpolation_stage=None)
