from scipy.integrate import quad

def func(x):
    return x ** 2
a = 0
b = 1
args = ()
full_output = 0
epsabs = 1.49e-08
epsrel = 1.49e-08
limit = 50
points = None
weight = None
wvar = None
wopts = None
maxp1 = 50
limlst = 50
(result, error) = quad(func, a, b=b, args=args, full_output=full_output, epsabs=epsabs, epsrel=epsrel, limit=limit, points=points, weight=weight, wvar=wvar, wopts=wopts, maxp1=maxp1, complex_func=False)
print('Result:', result)
print('Error:', error)
