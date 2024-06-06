from sklearn import linear_model
reg = linear_model.Lars(verbose=False, normalize=True, precompute='auto', fit_intercept=True, jitter=None, random_state=None)
