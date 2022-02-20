def is_octopus(y, x):
    """Return True if point (x, y) is an octopus, else False."""
    return 0 <= x <= max_x and 0 <= y <= max_y


def get_neighbors(y, x):
    """Return the coordinates of adjacent octopuses of an octopus (x, y)."""
    points = ((y, x - 1), (y, x + 1),  # left and right
              (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),  # upper
              (y + 1, x - 1), (y + 1, x), (y + 1, x + 1))  # lower
    return [point for point in points if is_octopus(*point)]


def process(y, x):
    """Process (x, y). Return the number of subsequent flashes."""
    if levels[y][x] == 0 and (y, x) in processed:  # Flashed already.
        return 0
    processed.add((y, x))
    levels[y][x] += 1
    if levels[y][x] > 9:
        levels[y][x] = 0
        return 1 + sum(process(i, j) for i, j in get_neighbors(y, x))
    return 0


if __name__ == '__main__':
    with open('../data/day11.txt') as f:
        levels = [list(map(int, line.strip())) for line in f.readlines()]
    max_x = len(levels[0]) - 1
    max_y = len(levels) - 1

    flashes = 0
    for step in range(100):
        processed = set()
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                flashes += process(y, x)
    print(flashes)
