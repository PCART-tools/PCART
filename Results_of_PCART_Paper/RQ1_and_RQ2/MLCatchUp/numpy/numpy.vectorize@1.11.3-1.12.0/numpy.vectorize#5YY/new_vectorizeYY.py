import numpy as np

def my_function(x):
    return x ** 2

def main():
    vectorized_func = np.vectorize(pyfunc=my_function, otypes='', signature=None)
    input_array = np.array([1, 2, 3, 4, 5])
    result = vectorized_func(input_array, signature=None)
    print(result)
if __name__ == '__main__':
    main()
