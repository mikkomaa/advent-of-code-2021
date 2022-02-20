from day15_1 import find_path


def extend(rows, times=5):
    """Extend rows. Return the result."""
    extended = rows
    length = len(rows)
    for row in extended:  # Lengthen rows.
        for i in range((times - 1) * length):
            row.append(row[i] % 9 + 1)
    for i in range((times - 1) * length):  # Add rows.
        extended.append([j % 9 + 1 for j in extended[i]])
    return extended


def parse_and_extend():
    """Parse input, and extend. Return the the risk levels and the goal."""
    with open('../data/day15.txt') as f:
        lines = [list(map(int, line.strip())) for line in f.readlines()]
    lines = extend(lines)
    goal = (len(lines[0]) - 1, len(lines) - 1)  # (x, y)
    risks = dict()
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            risks[(x, y)] = value
    return risks, goal


if __name__ == '__main__':
    risks, goal = parse_and_extend()
    print(find_path(risks, goal))
