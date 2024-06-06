from sympy.stats import Normal, sample
from sympy import Symbol
mu = Symbol('mu')
sigma = Symbol('sigma')
X = Normal('X', mu, sigma)
sample(expr=X.subs({mu: 0, sigma: 1}), seed=None)
