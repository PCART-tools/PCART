from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(n_components=2, n_neighbors=None, gamma=None, eigen_solver=None, n_jobs=None, random_state=None, affinity='nearest_neighbors', eigen_tol='auto')
