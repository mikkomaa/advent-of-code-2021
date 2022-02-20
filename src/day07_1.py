if __name__ == '__main__':
    with open('../data/day07.txt') as f:
        positions = [int(n) for n in f.read().split(',')]

    # The best horizontal position is the median value.
    positions.sort()
    median = positions[len(positions) // 2]
    print(sum(abs(p - median) for p in positions))
