import collections


def make_map(connections):
    """Return the map of caves based on connections."""
    neighbors = collections.defaultdict(list)
    for start, end in connections:
        neighbors[start].append(end)
        neighbors[end].append(start)
    return neighbors


def find_paths(path):
    """Return the number of paths from start to end."""
    cave = path[-1]
    if cave == 'end':
        return 1

    paths = 0
    for neighbor in neighbors[cave]:
        if neighbor.isupper() or neighbor not in path:
            paths += find_paths(path + [neighbor])
    return paths


if __name__ == '__main__':
    with open('../data/day12.txt') as f:
        connections = [line.strip().split('-') for line in f.readlines()]
    neighbors = make_map(connections)
    print(find_paths(['start']))
