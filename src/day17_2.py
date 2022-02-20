import itertools
import re


def count_hits():
    """Return the number of distinct initial velocity values."""
    hits = 0
    x_speeds = range(1, x_max + 1)
    y_speeds = range(y_min, -y_min)

    for x_speed, y_speed in itertools.product(x_speeds, y_speeds):
        x_pos = y_pos = 0
        while x_pos <= x_max and y_pos >= y_min:
            if x_pos >= x_min and y_pos <= y_max:
                hits += 1
                break
            x_pos += x_speed
            y_pos += y_speed
            if x_speed > 0:
                x_speed -= 1
            y_speed -= 1
    return hits


if __name__ == '__main__':
    with open('../data/day17.txt') as f:
        line = f.readline()
    x_min, x_max, y_min, y_max = map(int, re.findall(r'-?\d+', line))
    print(count_hits())
