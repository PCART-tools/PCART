from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(affinity='nearest_neighbors', gamma=None, n_components=2, eigen_tol='auto')
