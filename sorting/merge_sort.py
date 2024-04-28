import random
import time


compares = swaps = 0


def merge(left, right):
    merged = []
    i = j = 0

    global compares
    global swaps

    while i < len(left) and j < len(right):
        compares += 1
        swaps += 1
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        swaps += 1
        merged.append(left[i])
        i += 1

    while j < len(right):
        swaps += 1
        merged.append(right[j])
        j += 1

    return merged


def sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left = sort(a[:mid])
    right = sort(a[mid:])

    return merge(left, right)


if __name__ == '__main__':
    l = [x for x in range(1000000)]
    # l = [x for x in range(999999, -1, -1)]

    print('shuffling')
    random.shuffle(l)

    print('calling sort')
    start = time.process_time()
    s = sort(l)
    end = time.process_time()

    print(f'min\t\t\t{s[0]}')
    print(f'max\t\t\t{s[-1]}')
    print(f'compares\t{compares}')
    print(f'swaps\t\t{swaps}')
    print(f'cpu time\t{end - start}')
