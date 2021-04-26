import ctypes

if __name__ == '__main__':
    c_lib = ctypes.CDLL("./addition.so")

    result = c_lib.c_addition(ctypes.c_float(1.0), ctypes.c_float(2.0))
    print(f'1 + 2 = {result}')