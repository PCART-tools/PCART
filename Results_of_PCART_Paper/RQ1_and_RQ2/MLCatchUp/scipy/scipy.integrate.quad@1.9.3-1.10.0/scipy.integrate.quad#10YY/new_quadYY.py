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
(result, error) = quad(func, a, b, args, full_output, complex_func=False)
print('Result:', result)
print('Error:', error)
