from sklearn import linear_model
clf = linear_model.Lasso(1.0, True, False, precompute='auto', copy_X=True, max_iter=1000, random_state=None, selection='cyclic')
