from sklearn import linear_model
reg = linear_model.Lars(normalize=True, precompute='auto', fit_intercept=True, verbose=False, jitter=None, random_state=None)
