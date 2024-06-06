import matplotlib.pyplot as plt
import matplotlib.collections as mcoll
collection = mcoll.PolyCollection([[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]], edgecolors='k')
transOffset = plt.matplotlib.transforms.Affine2D().scale(2.0)
collection.set_offset_transform(transOffset + plt.gca().transData)
plt.gca().add_collection(collection)
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.gca().set_aspect('equal')
