from sklearn import linear_model
reg = linear_model.Lars(verbose=False, normalize=True, precompute='auto', n_nonzero_coefs=500, eps=2.220446049250313e-16, copy_X=True, fit_path=True, fit_intercept=True, jitter=None, random_state=None)
