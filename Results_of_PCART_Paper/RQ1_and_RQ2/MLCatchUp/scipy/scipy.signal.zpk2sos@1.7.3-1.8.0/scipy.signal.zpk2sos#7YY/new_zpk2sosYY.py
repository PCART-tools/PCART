from scipy.signal import zpk2sos
z = [1, 2, 3]
p = [0, -1, -2]
k = 2
pairing = 'nearest'
sos_matrix = zpk2sos(z, p, k=k, pairing=pairing, analog=False)
