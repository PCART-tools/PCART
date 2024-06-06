import numpy as np

def main():
    x = np.array([1.0, np.inf, 5.6, np.nan, -np.inf, 0])
    y = np.empty_like(x, dtype=bool)
    np.isneginf(x)
    print('Original array:', x)
    print('isneginf result:', y)
if __name__ == '__main__':
    main()
