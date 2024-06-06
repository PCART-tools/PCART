import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(init='warn', method='barnes_hut', n_iter=1000, early_exaggeration=12.0, n_jobs=None, min_grad_norm=1e-07, learning_rate='warn', verbose=0, perplexity=30.0, n_iter_without_progress=300, random_state=None, metric='euclidean', angle=0.5).fit_transform(X, metric_params=None)
