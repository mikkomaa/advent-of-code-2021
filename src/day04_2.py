from day04_1 import is_bingo, score

DRAWN = 0  # To mark already drawn numbers on boards.


def solve_final_score():
    """Print the final score of the last winning board."""
    with open('../data/day04.txt') as f:
        numbers = f.readline().strip().split(',')
        boards = f.read().split()

    boards_in_play = set(range(len(boards) // 25))

    for number in numbers:
        for i, item in enumerate(boards):
            if item == number:
                boards[i] = DRAWN
                if is_bingo(boards, i):
                    boards_in_play.discard(i // 25)
                    if not boards_in_play:
                        print(score(boards, item, i))
                        return


if __name__ == '__main__':
    solve_final_score()
