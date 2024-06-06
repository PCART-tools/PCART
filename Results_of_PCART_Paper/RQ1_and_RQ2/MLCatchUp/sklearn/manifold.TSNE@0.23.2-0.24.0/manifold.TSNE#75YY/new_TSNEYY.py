import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(verbose=0, min_grad_norm=1e-07, n_components=2, random_state=None, early_exaggeration=12.0, n_iter=1000, n_iter_without_progress=300, init='random', learning_rate=200.0, perplexity=30.0, metric='euclidean').fit_transform(X, square_distances='legacy')
