import matplotlib.pyplot as plt
import numpy as np
data = np.random.rand(10, 10)
im = plt.imshow(data, cmap='viridis')
cbar = plt.colorbar(im)
ticks = np.arange(0, 1.1, 0.2)
cbar.set_ticks(minor=False, ticks=ticks, labels=None, update_ticks=None)
