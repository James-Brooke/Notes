import ctypes
import pathlib 

if __name__ == '__main__':
    libname = pathlib.Path().absolute() / "hello_world.exe"
    c_lib = ctypes.CDLL(libname)

    c_lib.main()