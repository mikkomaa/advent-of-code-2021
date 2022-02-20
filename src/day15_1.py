import queue


def parse():
    """Parse input. Return the risk levels of points and the goal point."""
    with open('../data/day15.txt') as f:
        lines = f.readlines()
    goal = (len(lines[0].strip()) - 1, len(lines) - 1)  # (x, y)
    risks = dict()
    for y, line in enumerate(lines):
        for x, value in enumerate(line.strip()):
            risks[(x, y)] = int(value)
    return risks, goal


def get_neigbors(x, y, risks):
    """Return the adjacent points of (x, y)."""
    points = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
    return [(i, j) for (i, j) in points if (i, j) in risks]


def find_path(risks, goal):
    """Find a path with Dijkstra's algorithm. Return the lowest total risk."""
    path_costs = queue.PriorityQueue()
    path_costs.put((0, (0, 0)))
    visited = set()

    while True:
        cost, node = path_costs.get()
        if node == goal:
            return cost
        if node not in visited:
            del risks[node]
            visited.add(node)
            neighbors = get_neigbors(*node, risks)
            for neighbor in neighbors:
                new_cost = cost + risks[neighbor]
                path_costs.put((new_cost, neighbor))


if __name__ == '__main__':
    risks, goal = parse()
    print(find_path(risks, goal))
