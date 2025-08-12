from greeter import greet
from math_core import do_math
import time



def main():
    t0 = time.perf_counter()
    do_math(end=50_000_000)
    tt = time.perf_counter() - t0
    print(f'Finished in {tt:.5f} seconds')


if __name__ == '__main__':
    main()
