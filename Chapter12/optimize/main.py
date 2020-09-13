from time import time, sleep
from timeit import timeit, repeat
# main


def main():
    """
    # measure timing
    # example 1
    t1 = time()
    num = 5
    num *= 2
    print(time() - t1)

    # example 2
    t1 = time()
    sleep(1.0)
    print(time() - t1)

    # using timeit
    print(timeit('num = 5; num *= 2', number=1))
    print(repeat('num = 5; num *= 2', number=1, repeat=3))
    """

    # Algorithms and Data Structures
    # build a list in different ways
    def make_list_1():
        result = []
        for value in range(1000):
            result.append(value)
        return result

    def make_list_2():
        result = [value for value in range(1000)]
        return result

    print('make_list_1 takes', timeit(make_list_1, number=1000), 'seconds')
    print('make_list_2 takes', timeit(make_list_2, number=1000), 'seconds')


if __name__ == '__main__':
    main()
