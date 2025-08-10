import datetime
import multiprocessing
import math


def do_math(start=0, num=10):
    print(f'start: {start} --------- num: {num}\n')
    position = start
    random_number = 1000 * 1000
    while position < num:
        position += 1
        math.sqrt((position - random_number) ** 2)


def main():
    t0 = datetime.datetime.now()
    
    processor_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool()
    for n in range(1, processor_count + 1):
        pool.apply_async(do_math, args=(50_000_000 * (n - 1) / processor_count, 50_000_000 * n / processor_count))

    pool.close()
    pool.join()
    
    dt = datetime.datetime.now() - t0
    print(f'Done in {dt.total_seconds()} seconds')


if __name__ == '__main__':
    main()