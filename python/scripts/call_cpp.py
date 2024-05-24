from ctypes import cdll, c_float, POINTER

lib = cdll.LoadLibrary('../Cpp/build/libUtilities.so')

data = (c_float * 5)(1.0, 2.0, 3.0, 4.0, 5.0)

lib.processSignal(data)

