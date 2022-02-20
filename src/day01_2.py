def count_depth_increases():
    """Print the number of depth measurement increases in sliding window."""
    with open('../data/day01.txt') as f:
        depths = [int(line) for line in f]

    # It suffices to compare the first and the last value in a sliding window.
    print(sum(depths[i] < depths[i + 3] for i in range(len(depths) - 3)))


if __name__ == '__main__':
    count_depth_increases()
