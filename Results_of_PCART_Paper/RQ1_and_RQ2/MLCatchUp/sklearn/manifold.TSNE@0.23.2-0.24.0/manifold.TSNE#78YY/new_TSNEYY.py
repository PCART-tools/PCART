import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(min_grad_norm=1e-07, angle=0.5, early_exaggeration=12.0, n_iter_without_progress=300, verbose=0, n_jobs=None, init='random', n_iter=1000, perplexity=30.0, metric='euclidean', n_components=2, method='barnes_hut', random_state=None, learning_rate=200.0).fit_transform(X, square_distances='legacy')
