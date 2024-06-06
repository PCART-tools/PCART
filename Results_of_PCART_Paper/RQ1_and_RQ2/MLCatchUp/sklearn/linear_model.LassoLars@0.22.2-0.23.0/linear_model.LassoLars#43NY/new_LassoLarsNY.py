from sklearn import linear_model
reg = linear_model.LassoLars(1.0, verbose=False, normalize=True, precompute='auto', max_iter=500, eps=2.220446049250313e-16, copy_X=True, fit_intercept=True, jitter=None, random_state=None)
