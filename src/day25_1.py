def move(cucumbers):
    """Move cucumbers one step. Return True if at least one cucumber moved."""
    moved = False
    # Move east.
    for row in cucumbers:
        first, last = row[0], row[-1]
        i = 0
        while i < len(row) - 1:
            if row[i] == '>' and row[i+1] == '.':
                row[i], row[i+1] = '.', '>'
                i += 1
                moved = True
            i += 1
        if first == '.' and last == '>':
            row[0], row[-1] = '>', '.'
            moved = True

    # Move south.
    for col in range(len(cucumbers[0])):
        first, last = cucumbers[0][col], cucumbers[-1][col]
        row = 0
        while row < len(cucumbers) - 1:
            if cucumbers[row][col] == 'v' and cucumbers[row+1][col] == '.':
                cucumbers[row][col], cucumbers[row + 1][col] = '.', 'v'
                row += 1
                moved = True
            row += 1
        if first == '.' and last == 'v':
            cucumbers[0][col], cucumbers[-1][col] = 'v', '.'
            moved = True
    return moved


if __name__ == '__main__':
    with open('../data/day25.txt') as f:
        cucumbers = [list(line.strip()) for line in f.readlines()]
    steps = 1
    while move(cucumbers):
        steps += 1
    print(steps)
