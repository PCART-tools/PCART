import scipy.signal
result = scipy.signal.correlate(in1=[1, 2, 3, 4, 5], in2=[0.1, 0.2, 0.3], method='auto')
