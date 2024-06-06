import numpy as np

def main():
    x = 3.5
    xp = [3, 4, 5]
    fp = [1, 2, 3]
    left = 0
    right = 4
    result = np.interp(x, xp, fp, period=None)
    print(result)
if __name__ == '__main__':
    main()
