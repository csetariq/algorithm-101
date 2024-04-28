import random
import time


def solve(n, x):
    a = [x for x in range(1, n + 2)]
    random.shuffle(a)
    # print(a)

    r = 0
    for i in range(n + 1):
        r_x = 1
        for j in range(i):
            r_x = r_x * x
        r += a[i] * r_x

    return r


if __name__ == '__main__':
    for n in range(10000, 100001, 10000):
        start = time.process_time()
        r = solve(n, 2)
        end = time.process_time()
        # print(f'n={n}\tr={r}\ttime={end - start}')
        print(f'n={n}\ttime={end - start}')
