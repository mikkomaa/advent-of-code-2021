import math


def product_of_basins():
    """Return the product of the sizes of the three largest basins."""
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

    def basin_size(x, y):
        """Return the basin size of the low point (x, y)."""
        if (x, y) in visited or heightmap(x, y) == 9:
            return 0
        visited.add((x, y))
        value = heightmap(x, y)
        size = 1
        if x > 0 and value <= heightmap(x - 1, y):  # left
            size += basin_size(x - 1, y)
        if x < max_x and value <= heightmap(x + 1, y):  # right
            size += basin_size(x + 1, y)
        if y > 0 and value <= heightmap(x, y - 1):  # up
            size += basin_size(x, y - 1)
        if y < max_y and value <= heightmap(x, y + 1):  # down
            size += basin_size(x, y + 1)
        return size

    visited = set()
    basin_sizes = []
    lowpoints = ((x, y)
                 for x in range(max_x + 1)
                 for y in range(max_y + 1)
                 if is_lowpoint(x, y))

    for x, y in lowpoints:
        basin_sizes.append(basin_size(x, y))
    basin_sizes.sort(reverse=True)
    return math.prod(basin_sizes[:3])


if __name__ == '__main__':
    with open('../data/day09.txt') as f:
        values = [list(map(int, line.strip())) for line in f.readlines()]
    print(product_of_basins())
