from sklearn.preprocessing import KBinsDiscretizer
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
est = KBinsDiscretizer(3, strategy='uniform', dtype=None, encode='ordinal', subsample='warn', random_state=None)
