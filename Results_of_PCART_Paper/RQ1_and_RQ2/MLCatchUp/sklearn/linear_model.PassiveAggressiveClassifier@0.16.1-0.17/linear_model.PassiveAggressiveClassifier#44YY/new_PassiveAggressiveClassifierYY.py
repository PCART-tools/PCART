from sklearn.linear_model import PassiveAggressiveClassifier
clf = PassiveAggressiveClassifier(1.0, fit_intercept=True, n_iter=5, shuffle=True, verbose=0, loss='hinge', n_jobs=1, random_state=None, class_weight=None)
