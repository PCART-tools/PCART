from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(eigen_solver=None, affinity='nearest_neighbors', gamma=None, n_jobs=None, random_state=None, n_neighbors=None, eigen_tol='auto')
