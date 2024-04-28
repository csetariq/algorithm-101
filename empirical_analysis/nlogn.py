import random
import time


def pow(x, y):
    if y == 0:
        return 1

    half = pow(x, y // 2)

    if y % 2 == 0:
        return half * half
    else:
        return half * half * x


def solve(n, x):
    a = [x for x in range(1, n + 2)]
    random.shuffle(a)

    r = 0
    for i in range(n + 1):
        r += a[i] * pow(x, i)

    return r


if __name__ == '__main__':
    # for n in range(10):
    for n in range(10000, 100001, 10000):
        start = time.process_time()
        r = solve(n, 2)
        end = time.process_time()
        print(f'n={n}\tr={r}\ttime={end - start}')
        # print(f'n={n}\ttime={end - start}')
