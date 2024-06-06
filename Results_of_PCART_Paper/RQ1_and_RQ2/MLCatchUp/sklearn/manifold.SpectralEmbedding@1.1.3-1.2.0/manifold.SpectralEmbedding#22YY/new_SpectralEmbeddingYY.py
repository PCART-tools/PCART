from sklearn.datasets import load_digits
from sklearn.manifold import SpectralEmbedding
(X, _) = load_digits(return_X_y=True)
X.shape
embedding = SpectralEmbedding(2, eigen_solver=None, affinity='nearest_neighbors', gamma=None, random_state=None, eigen_tol='auto')
