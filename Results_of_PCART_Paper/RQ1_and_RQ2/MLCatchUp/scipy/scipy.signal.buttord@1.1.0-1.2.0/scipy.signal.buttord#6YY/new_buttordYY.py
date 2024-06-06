from scipy.signal import buttord
wp = 0.4
ws = 0.5
gpass = 2.0
gstop = 30.0
(N, Wn) = buttord(wp, ws, gpass, gstop, False, fs=None)
