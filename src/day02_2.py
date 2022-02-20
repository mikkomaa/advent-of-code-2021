def pilot():
    """Print the product of the final horizontal position and final depth."""
    with open('../data/day02.txt') as f:
        lines = f.readlines()

    aim, depth, horizontal = 0, 0, 0
    for line in lines:
        command, value = line.split()
        value = int(value)

        if command == 'up':
            aim -= value
        elif command == 'down':
            aim += value
        else:  # forward
            horizontal += value
            depth += aim * value

    print(horizontal * depth)


if __name__ == '__main__':
    pilot()
