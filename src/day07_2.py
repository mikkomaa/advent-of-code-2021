import itertools


def solve_position(positions):
    """Return the least amount of fuel possible."""
    previous_fuel = float('inf')
    # Check target positions until the lowest fuel consumption is found.
    for target in itertools.count():
        fuel = 0
        for p in positions:
            dist = abs(target - p)
            fuel += dist * (dist + 1) // 2
        if fuel > previous_fuel:
            return previous_fuel
        previous_fuel = fuel


if __name__ == '__main__':
    with open('../data/day07.txt') as f:
        positions = [int(n) for n in f.read().split(',')]
    print(solve_position(positions))
