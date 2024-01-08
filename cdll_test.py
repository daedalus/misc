import ctypes

libc = ctypes.CDLL("libc.so.6")  # under Linux/Unix
t = libc.time(None)  # equivalent C code: t = time(NULL)
print(t)

m = libc.malloc(1024 * 1024 * 10)
print(m)
