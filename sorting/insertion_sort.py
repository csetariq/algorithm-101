import time
import random


def sort(a):
    compare = 0
    swap = 0
    for k in range(1, len(a)):
        c = a[k]
        j = k

        while True:
            compare += 1
            if j > 0 and a[j - 1] > c:
                a[j] = a[j - 1]
                j -= 1
                swap += 1
            else:
                break

        a[j] = c

    return compare, swap


if __name__ == '__main__':
    l = [x for x in range(10000)]
    # l = [x for x in range(9999, -1, -1)]

    # print('shuffling')
    # random.shuffle(l)

    print('calling sort')
    start = time.process_time()
    compares, swaps = sort(l)
    end = time.process_time()

    print(f'min\t\t\t{l[0]}')
    print(f'max\t\t\t{l[-1]}')
    print(f'compares\t{compares}')
    print(f'swaps\t\t{swaps}')
    print(f'cpu time\t{end - start}')
