from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(eigen_solver=None, gamma=None, affinity='nearest_neighbors', n_components=2, random_state=None, eigen_tol='auto')
