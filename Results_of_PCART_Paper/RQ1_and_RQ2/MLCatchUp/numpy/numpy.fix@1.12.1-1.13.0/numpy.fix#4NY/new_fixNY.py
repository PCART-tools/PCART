import numpy as np

def main():
    x = np.array([-3.7, -2.3, 1.5, 3.9, 0])
    y = np.empty_like(x)
    np.fix(x, out=y)
    print('Original array:', x)
    print('Fixed array:', y)
if __name__ == '__main__':
    main()
