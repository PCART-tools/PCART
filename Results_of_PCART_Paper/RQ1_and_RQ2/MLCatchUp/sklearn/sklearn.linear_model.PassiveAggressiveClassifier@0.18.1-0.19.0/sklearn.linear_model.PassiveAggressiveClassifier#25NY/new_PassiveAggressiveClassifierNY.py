from sklearn.linear_model import PassiveAggressiveClassifier
clf = PassiveAggressiveClassifier(1.0, True, 5, shuffle=True, verbose=0, loss='hinge', max_iter=None, tol=None, average=False)
