from sklearn import linear_model
clf = linear_model.ElasticNet(1.0, 0.5, True, False, 'auto', max_iter=1000, copy_X=True, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')
