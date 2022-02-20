def solve_power_consumption():
    """Print the power consumption."""
    with open('../data/day03.txt') as f:
        lines = [line.strip() for line in f]

    ones = [sum(bit == '1' for bit in column) for column in zip(*lines)]
    gamma = ''.join('1' if n > len(lines) / 2 else '0' for n in ones)
    epsilon = ''.join('1' if char == '0' else '0' for char in gamma)
    print(int(gamma, 2) * int(epsilon, 2))


if __name__ == '__main__':
    solve_power_consumption()
