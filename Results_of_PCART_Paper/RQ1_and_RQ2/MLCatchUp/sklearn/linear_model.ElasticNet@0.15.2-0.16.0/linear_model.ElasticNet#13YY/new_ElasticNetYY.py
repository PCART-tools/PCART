from sklearn import linear_model
clf = linear_model.ElasticNet(1.0, 0.5, fit_intercept=True, normalize=False, random_state=None, selection='cyclic')
