#  multiprocessing -- better for cpu bound tasks(heavy cpu usage)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
def main():
    a = Process(target=counter, args=(10000000,))
    a.start()

    a.join()

    print('finished in: ',time.perf_counter(), 'secs')

if __name__ == '__main__':
    main()
