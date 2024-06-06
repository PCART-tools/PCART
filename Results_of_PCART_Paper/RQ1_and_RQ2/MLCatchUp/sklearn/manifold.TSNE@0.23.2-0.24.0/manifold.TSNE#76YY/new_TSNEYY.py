import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(random_state=None, n_iter=1000, min_grad_norm=1e-07, early_exaggeration=12.0, method='barnes_hut', init='random', metric='euclidean', n_components=2, verbose=0, perplexity=30.0, n_iter_without_progress=300, learning_rate=200.0).fit_transform(X, square_distances='legacy')
