from sklearn import linear_model
clf = linear_model.ElasticNet(1.0, 0.5, True, False, 'auto', max_iter=1000, random_state=None, selection='cyclic')
