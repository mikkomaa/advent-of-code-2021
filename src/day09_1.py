def sum_of_risk_levels():
    """Return the sum of the risk levels of all low points."""
    max_x = len(values[0]) - 1
    max_y = len(values) - 1

    def heightmap(x, y):
        """Return the height value in (xth column, yth row)."""
        return values[y][x]

    def is_lowpoint(x, y):
        """Return True if (x, y) is a lowpoint, else False."""
        value = heightmap(x, y)
        return all((x == 0 or value < heightmap(x - 1, y),  # left
                    x == max_x or value < heightmap(x + 1, y),  # right
                    y == 0 or value < heightmap(x, y - 1),  # up
                    y == max_y or value < heightmap(x, y + 1)))  # down

    return sum(heightmap(x, y) + 1
               for x in range(max_x + 1)
               for y in range(max_y + 1)
               if is_lowpoint(x, y))


if __name__ == '__main__':
    with open('../data/day09.txt') as f:
        values = [list(map(int, line.strip())) for line in f.readlines()]
    print(sum_of_risk_levels())
