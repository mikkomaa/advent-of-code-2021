import itertools

from day18_1 import *


if __name__ == '__main__':
    with open('../data/day18.txt') as f:
        numbers = [parse_string(line.strip()) for line in f.readlines()]

    largest = 0
    for a, b in itertools.product(numbers, numbers):
        largest = max(largest, magnitude(add(a, b)))
    print(largest)
