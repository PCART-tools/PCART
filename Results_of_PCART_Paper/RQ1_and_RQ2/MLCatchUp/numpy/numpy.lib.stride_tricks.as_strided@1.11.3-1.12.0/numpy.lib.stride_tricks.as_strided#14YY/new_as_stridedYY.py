import numpy as np

def main():
    x = np.array([1, 2, 3, 4, 5, 6])
    shape = (4, 2)
    strides = (8, 4)
    view = np.lib.stride_tricks.as_strided(x=x, shape=shape, strides=strides, subok=True, writeable=True)
    print(view)
if __name__ == '__main__':
    main()
