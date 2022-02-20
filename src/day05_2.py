import itertools
import math
import re


def add_vents(x1, y1, x2, y2, vents):
    """Set point(s) (x, y) False, if it is met the first time, else True."""
    if x1 == x2:
        sign = int(math.copysign(1, y2 - y1))
        for x, y in zip(itertools.repeat(x1), range(y1, y2 + sign, sign)):
            vents[x, y] = True if (x, y) in vents else False
    elif y1 == y2:
        sign = int(math.copysign(1, x2 - x1))
        for x, y in zip(range(x1, x2 + sign, sign), itertools.repeat(y1)):
            vents[x, y] = True if (x, y) in vents else False
    else:
        sign_x = int(math.copysign(1, x2 - x1))
        sign_y = int(math.copysign(1, y2 - y1))
        for x, y in zip(range(x1, x2 + sign_x, sign_x),
                        range(y1, y2 + sign_y, sign_y)):
            vents[x, y] = True if (x, y) in vents else False


def solve_overlap():
    """Print the number of points where at least two lines overlap."""
    with open('../data/day05.txt') as f:
        segments = []
        for line in f:
            segments.append([int(c) for c in re.findall(r'[0-9]+', line)])

    vents = dict()
    for segment in segments:
        add_vents(*segment, vents)
    print(sum(vents.values()))


if __name__ == '__main__':
    solve_overlap()
