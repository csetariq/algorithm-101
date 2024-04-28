import time


compares = swaps = 0


def partition(a, l, h):
    global compares
    global swaps

    p = a[h]

    i = l - 1

    for j in range(l, h):
        compares += 1
        if a[j] <= p:
            swaps += 1
            i += 1
            a[i], a[j] = a[j], a[i]

    swaps += 1
    a[i + 1], a[h] = a[h], a[i + 1]

    return i + 1


def quick_sort(a, l, h):
    if l < h:
        pi = partition(a, l, h)

        quick_sort(a, l, pi - 1)
        quick_sort(a, pi + 1, h)


def sort(a):
    quick_sort(a, 0, len(a) - 1)


if __name__ == '__main__':
    # l = [x for x in range(1000000)]
    l = [x for x in range(1000, -1, -1)]

    # print('shuffling')
    # random.shuffle(l)

    print('calling sort')
    start = time.process_time()
    sort(l)
    end = time.process_time()

    print(f'min\t\t\t{l[0]}')
    print(f'max\t\t\t{l[-1]}')
    print(f'compares\t{compares}')
    print(f'swaps\t\t{swaps}')
    print(f'cpu time\t{end - start}')
