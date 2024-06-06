from sklearn import linear_model
reg = linear_model.LassoLars(1.0, precompute='auto', max_iter=500, eps=2.220446049250313e-16, copy_X=True, fit_path=True, positive=False, fit_intercept=True, verbose=False, normalize=True, jitter=None, random_state=None)
