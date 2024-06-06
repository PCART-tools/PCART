import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(random_state=None, n_components=2, early_exaggeration=12.0, perplexity=30.0, method='barnes_hut', min_grad_norm=1e-07, angle=0.5, n_iter_without_progress=300, metric='euclidean', n_iter=1000, learning_rate=200.0, verbose=0, init='random').fit_transform(X, square_distances='legacy')
