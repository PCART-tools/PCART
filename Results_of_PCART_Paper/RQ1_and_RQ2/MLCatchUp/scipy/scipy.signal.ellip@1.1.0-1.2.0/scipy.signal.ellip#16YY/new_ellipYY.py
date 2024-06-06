import scipy.signal
(N, rp, rs, Wn) = (4, 1.0, 10.0, 0.2)
btype = 'low'
analog = False
output = 'ba'
(b, a) = scipy.signal.ellip(N, rp, rs=rs, Wn=Wn, btype=btype, analog=analog, fs=None)
