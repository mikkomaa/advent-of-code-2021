def count_depth_increases():
    """Print the number of times a depth measurement increases."""
    with open('../data/day01.txt') as f:
        depths = [int(line) for line in f]

    print(sum(depths[i] < depths[i + 1] for i in range(len(depths) - 1)))


if __name__ == '__main__':
    count_depth_increases()
