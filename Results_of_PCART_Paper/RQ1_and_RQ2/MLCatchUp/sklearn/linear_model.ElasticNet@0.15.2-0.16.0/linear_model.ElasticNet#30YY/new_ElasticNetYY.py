from sklearn import linear_model
clf = linear_model.ElasticNet(1.0, 0.5, True, False, 'auto', 1000, copy_X=True, random_state=None, selection='cyclic')
