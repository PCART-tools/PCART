from sklearn import linear_model
reg = linear_model.Lars(n_nonzero_coefs=500, eps=2.220446049250313e-16, copy_X=True, fit_path=True, fit_intercept=True, verbose=False, normalize=True, precompute='auto', jitter=None, random_state=None)
