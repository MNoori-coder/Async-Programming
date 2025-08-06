import time
import threading


# def main():
#     t1 = threading.Thread(target=greeter, args=('Mohammad',), daemon=True)
#     t2 = threading.Thread(target=greeter, args=('Ali', 5), daemon=True)

#     t1.start()
#     t2.start()

#     print('Another job to do...')

#     t1.join()
#     t2.join()

#     print('Task done!')

def main():
    threads = [
        threading.Thread(target=greeter, args=('Mohammad',), daemon=True),
        threading.Thread(target=greeter, args=('Mobina', 5), daemon=True),
        threading.Thread(target=greeter, args=('Ali', 7), daemon=True)
    ]

    [t.start() for t in threads]

    print('Another job to do...')
    [t.join() for t in threads]
    print('Task done!')

def greeter(name: str, count: int = 10):
    for i in range(count):
        print(f'{i + 1} - Hello {name}')
        time.sleep(1)

if __name__ == '__main__':
    main()