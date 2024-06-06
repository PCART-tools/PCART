from sklearn import linear_model
clf = linear_model.ElasticNet(1.0, 0.5, True, False, 'auto', 1000, True, tol=0.0001, random_state=None, selection='cyclic')
