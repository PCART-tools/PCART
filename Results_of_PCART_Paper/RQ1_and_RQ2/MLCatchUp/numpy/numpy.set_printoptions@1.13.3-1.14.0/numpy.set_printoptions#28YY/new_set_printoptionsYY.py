import numpy as np

def main():
    np.set_printoptions(precision=4, threshold=5, edgeitems=3, linewidth=75, suppress=True, nanstr='NaN', sign=None, floatmode=None)
    arr = np.array([0.123456789, 1.23456789, 12.3456789, np.nan, np.inf, -np.inf])
    print('Array:')
    print(arr)
if __name__ == '__main__':
    main()
