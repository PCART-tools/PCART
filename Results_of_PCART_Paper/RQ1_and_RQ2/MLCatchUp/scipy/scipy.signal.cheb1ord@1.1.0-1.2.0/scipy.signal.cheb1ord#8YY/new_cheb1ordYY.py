import scipy.signal
wp = 0.2
ws = 0.3
gpass = 1
gstop = 40
cheb1ord_result = scipy.signal.cheb1ord(wp, ws, gpass, gstop=gstop, analog=False, fs=None)
