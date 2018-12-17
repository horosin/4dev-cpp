import random
import math


def mean(lst):
    """Compute mean of given iterable"""
    return sum(lst) / len(lst)


def standard_deviation(lst):
    """Compute standard deviation of given iterable"""
    m = mean(lst)
    variance = sum([(value - m) ** 2 for value in lst])
    return math.sqrt(variance / len(lst))


def main():
    """Compute standard deviation for the whole dataset"""

    lens = range(10, 10000, 10)

    for l in lens:
        rands = [random.random() for _ in range(0, l)]
        standard_deviation(rands)


if __name__ == '__main__':

    main()
