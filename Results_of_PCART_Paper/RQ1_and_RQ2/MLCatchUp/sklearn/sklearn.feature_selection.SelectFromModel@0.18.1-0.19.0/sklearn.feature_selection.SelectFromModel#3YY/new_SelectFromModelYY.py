from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
X = [[0.87, -1.34, 0.31], [-2.79, -0.02, -0.85], [-1.34, -0.48, -2.55], [1.92, 1.48, 0.65]]
y = [0, 1, 0, 1]
selector = SelectFromModel(LogisticRegression(), None).fit(X, y, norm_order=1)
