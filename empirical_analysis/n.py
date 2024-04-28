import random
import time


def resolve(a, n, x, i):
    if i > n:
        return 0
    return x * (a[i] + resolve(a, n, x, i + 1))


def solve(n, x):
    a = [x for x in range(1, n + 2)]
    random.shuffle(a)

    r = 0
    for i in range(n, 0, -1):
        r = (r + a[i]) * x

    return r + a[0]


if __name__ == '__main__':
    # for n in range(10):
    for n in range(10000, 100001, 10000):
        start = time.process_time()
        r = solve(n, 2)
        end = time.process_time()
        # print(f'n={n}\tr={r}\ttime={end - start}')
        print(f'n={n}\ttime={end - start}')
