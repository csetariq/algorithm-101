import time


def sort(a):
    compare = 0
    swap = 0
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            compare += 1
            if a[j] > a[j + 1]:
                swap += 1
                a[j], a[j + 1] = a[j + 1], a[j]

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
