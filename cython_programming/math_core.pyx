from libc.math cimport sqrt
import cython

def do_math(start: cython.int = 0, end: cython.int = 10):
    position: cython.int = start
    number: cython.int = 1000 * 1000
    with nogil:
        while position < end:
            position += 1
            sqrt((position - number) * (position - number))
