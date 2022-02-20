from day12_1 import make_map


def find_paths(path, twice):
    """Return the number of paths from start to end."""
    cave = path[-1]
    if cave == 'end':
        return 1

    paths = 0
    for neighbor in neighbors[cave]:
        if neighbor.isupper() or neighbor not in path:
            paths += find_paths(path + [neighbor], twice)
        elif not twice and neighbor != 'start':
            paths += find_paths(path + [neighbor], True)
    return paths


if __name__ == '__main__':
    with open('../data/day12.txt') as f:
        connections = [line.strip().split('-') for line in f.readlines()]
    neighbors = make_map(connections)
    print(find_paths(['start'], False))
