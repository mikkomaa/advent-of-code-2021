import collections


def update(score_1, space_1, score_2, space_2, steps, turn):
    """Return new score and space after steps taken."""

    def update_space(space, steps):
        updated = space + steps
        return updated - 10 if updated > 10 else updated

    if turn == 1:
        new_space = update_space(space_1, steps)
        return score_1 + new_space, new_space, score_2, space_2
    else:  # turn == 2
        new_space = update_space(space_2, steps)
        return score_1, space_1, score_2 + new_space, new_space


def roll_thrice(universes, turn, wins):
    """Roll the die thrice. Update wins. Return new universes."""
    # outcomes of 3 die rolls (steps forward, amount of outcomes)
    outcomes = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))
    new_universes = collections.defaultdict(int)
    for key, value in universes.items():
        for steps, amount in outcomes:
            score_1, space_1, score_2, space_2 = update(*key, steps, turn)
            times = value * amount
            if score_1 > 20 or score_2 > 20:
                wins[turn] += times
            else:
                new_universes[(score_1, space_1, score_2, space_2)] += times
    return new_universes


def play():
    """Play a game. Return the winner's number of wins."""
    turn = 1  # player 1 or player 2
    wins = [0] * 3  # We use wins[1] and wins[2].
    # (player 1 score, player 1 space, player 2 score, player 2 space)
    universes = {(0, 7, 0, 3): 1}

    while universes:
        universes = roll_thrice(universes, turn, wins)
        turn = 1 if turn == 2 else 2
    return max(wins)


if __name__ == '__main__':
    print(play())
