from sklearn.linear_model import PassiveAggressiveClassifier
clf = PassiveAggressiveClassifier(1.0, True, n_iter=5, shuffle=True, verbose=0, loss='hinge', n_jobs=1, max_iter=None, tol=None, average=False)
