import functools
import collections
import math


# We store every integer in a snailfish number as Regular.
Regular = collections.namedtuple('Regular', 'level, value')


def parse_string(string):
    """Parse a snailfish number. Return it as a list of Regulars."""
    number = []
    level = 0
    for c in string:
        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
        elif str.isdigit(c):
            number.append(Regular(level, int(c)))
    return number


def add(a, b):
    """Add numbers a and b. Return the reduced result."""
    number = a + b
    for i, regular in enumerate(number):
        number[i] = Regular(regular.level + 1, regular.value)
    return reduce(number)


def reduce(number):
    """Reduce number. Return the result."""
    while True:
        while is_explodable(number):
            number = explode(number)
        if not is_splittable(number):
            return number
        number = split(number)


def is_explodable(number):
    """Return True if number can be exploded, else False."""
    return any(regular.level == 5 for regular in number)


def explode(number):
    """Explode number once. Return the result."""
    for i, regular in enumerate(number):
        if regular.level == 5:
            if i > 0:
                level, value = number[i - 1]
                number[i - 1] = Regular(level, value + regular.value)
            if i < len(number) - 2:
                level, value = number[i + 2]
                number[i + 2] = Regular(level, value + number[i + 1].value)
            return number[:i] + [Regular(4, 0)] + number[i+2:]


def is_splittable(number):
    """Return True if number can be split, else False."""
    return any(regular.value > 9 for regular in number)


def split(number):
    """Split number once. Return the result."""
    for i, regular in enumerate(number):
        if regular.value > 9:
            left = math.floor(regular.value / 2)
            right = math.ceil(regular.value / 2)
            level = regular.level + 1
            pair = [Regular(level, left), Regular(level, right)]
            return number[:i] + pair + number[i+1:]


def magnitude(number):
    """Return the magnitude of number."""
    while len(number) > 1:
        for i in range(len(number) - 1):
            if number[i].level == number[i + 1].level:
                level = number[i].level - 1
                value = 3 * number[i].value + 2 * number[i + 1].value
                number = number[:i] + [Regular(level, value)] + number[i+2:]
                break
    return number[0].value


if __name__ == '__main__':
    with open('../data/day18.txt') as f:
        numbers = [parse_string(line.strip()) for line in f.readlines()]

    final_sum = functools.reduce(add, numbers)
    print(magnitude(final_sum))
