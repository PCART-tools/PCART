import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(cmap='viridis', X=X, filternorm=True, norm=None, filterrad=4.0, interpolation_stage=None)
