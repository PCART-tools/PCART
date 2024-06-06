from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA, TruncatedSVD
union = FeatureUnion([('pca', PCA(n_components=1)), ('svd', TruncatedSVD(n_components=2))], None, transformer_weights=None, verbose=False)
