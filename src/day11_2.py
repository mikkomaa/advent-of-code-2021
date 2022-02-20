import itertools


def get_neighbors(y, x):
    """Return the coordinates of adjacent octopuses of an octopus (x, y)."""
    points = ((y, x - 1), (y, x + 1),  # left and right
              (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),  # upper
              (y + 1, x - 1), (y + 1, x), (y + 1, x + 1))  # lower
    return [point for point in points if point in octopuses]


def process(y, x):
    """Process (x, y) and the subsequent flashes."""
    if levels[y][x] == 0 and (y, x) in processed:  # Flashed already.
        return
    processed.add((y, x))
    levels[y][x] += 1
    if levels[y][x] > 9:
        levels[y][x] = 0
        [process(i, j) for i, j in get_neighbors(y, x)]


if __name__ == '__main__':
    with open('../data/day11.txt') as f:
        levels = [list(map(int, line.strip())) for line in f.readlines()]
    octopuses = set((y, x)
                    for y in range(len(levels))
                    for x in range(len(levels[0])))

    for step in itertools.count(1):
        processed = set()
        [process(y, x) for (y, x) in octopuses]
        if all(levels[y][x] == 0 for (y, x) in octopuses):
            print(step)
            break
