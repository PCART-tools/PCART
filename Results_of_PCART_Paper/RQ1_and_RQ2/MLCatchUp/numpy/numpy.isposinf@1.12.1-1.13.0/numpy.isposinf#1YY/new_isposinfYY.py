import numpy as np

def main():
    x = np.array([1.0, np.inf, 5.6, np.nan, -np.inf, 0])
    y = np.empty_like(x, dtype=bool)
    np.isposinf(x)
    print('Original array:', x)
    print('isposinf result:', y)
if __name__ == '__main__':
    main()
