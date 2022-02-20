def solve_oxygen_or_co2_rating(lines, rating):
    """Return the oxygen generator rating or the CO2 scrubber rating."""
    index = 0
    while len(lines) > 1:
        ones = sum(line[index] == '1' for line in lines)
        if (ones >= len(lines) / 2 and rating == 'oxygen' or
                ones < len(lines) / 2 and rating != 'oxygen'):
            filter = '1'
        else:
            filter = '0'
        lines = [line for line in lines if line[index] == filter]
        index += 1
    return lines[0]


def solve_life_support_rating():
    """Print the life support rating."""
    with open('../data/day03.txt') as f:
        lines = [line.strip() for line in f]

    oxygen = solve_oxygen_or_co2_rating(lines, 'oxygen')
    co2 = solve_oxygen_or_co2_rating(lines, 'co2')
    print(int(oxygen, 2) * int(co2, 2))


if __name__ == '__main__':
    solve_life_support_rating()
