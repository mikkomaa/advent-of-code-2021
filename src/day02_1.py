def pilot():
    """Print the product of the final horizontal position and final depth."""
    with open('../data/day02.txt') as f:
        lines = f.readlines()

    commands = {
        'forward': 0,
        'down': 0,
        'up': 0
    }

    for line in lines:
        command, value = line.split()
        commands[command] += int(value)

    print(commands['forward'] * (commands['down'] - commands['up']))


if __name__ == '__main__':
    pilot()
