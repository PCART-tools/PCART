from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(gamma=None, n_components=2, random_state=None, affinity='nearest_neighbors', eigen_tol='auto')
