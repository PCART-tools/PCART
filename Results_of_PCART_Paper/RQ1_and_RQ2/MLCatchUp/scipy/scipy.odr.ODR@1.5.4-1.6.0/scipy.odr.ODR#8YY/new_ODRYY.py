from scipy.odr import ODR, Data, Model
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 3.9, 6.2, 8.1, 9.8])
data = Data(x, y)

def my_linear_model(B, x):
    return B[0] * x
linear_model = Model(my_linear_model)
beta0 = [1.0]
ifixb = [1]
ifixx = None
job = 10
iprint = 0
errfile = None
rptfile = None
ndigit = 2
taufac = 1.0
sstol = 1e-06
partol = 1e-06
maxit = 500
stpb = [0.0]
stpd = [0.0]
sclb = [0.0]
scld = [1.0]
work = None
iwork = None
odr = ODR(data, model=linear_model, beta0=beta0, delta0=None, overwrite=False)
output = odr.run()
beta = output.beta
delta = output.delta
print('Fitted parameters (beta):', beta)
