from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(2, affinity='nearest_neighbors', eigen_solver=None, random_state=None, n_neighbors=None, gamma=None, eigen_tol='auto')
