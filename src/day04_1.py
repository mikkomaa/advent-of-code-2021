DRAWN = 0  # To mark already drawn numbers on boards.


def is_bingo(boards, index):
    """Return True, if the entire row or column containing index is marked."""
    row = index - index % 5
    col = index - index % 25 + index % 5
    return (all(boards[i] == DRAWN for i in range(row, row + 5)) or
            all(boards[j] == DRAWN for j in range(col, col + 25, 5)))


def score(boards, number, index):
    """Return the final score of the board that contains index."""
    first = index - index % 25
    return int(number) * sum(int(boards[i]) for i in range(first, first + 25))


def solve_final_score():
    """Print the final score of the first winning board."""
    with open('../data/day04.txt') as f:
        numbers = f.readline().strip().split(',')
        boards = f.read().split()

    for number in numbers:
        for i, item in enumerate(boards):
            if item == number:
                boards[i] = DRAWN
                if is_bingo(boards, i):
                    print(score(boards, item, i))
                    return


if __name__ == '__main__':
    solve_final_score()
