import random
import time


def minmax_sort(input_list):
    input_list.sort()
    return input_list[0], input_list[-1]


def minmax(input_list):
    local_min = int(2 ** 63) - 1
    local_max = -int(2 ** 63)

    for i in input_list:
        if i > local_max:
            local_max = i
        if i < local_min:
            local_min = i

    return local_min, local_max


if __name__ == '__main__':
    for i in range(1000000, 10000001, 1000000):
        test_list = [x for x in range(i - 1, -1, -1)]
        random.shuffle(test_list)

        start = time.process_time()
        result_minmax = minmax(test_list)
        time_minmax = time.process_time() - start

        start = time.process_time()
        result_minmax_sort = minmax_sort(test_list)
        time_minmax_sort = time.process_time() - start

        print(
            f'size={i}\tmatch={result_minmax_sort == result_minmax}\tminmax={time_minmax}\tminmax_sort={time_minmax_sort}')
