class Die:
    def __init__(self):
        self.value = 1
        self.rolls = 0

    def roll(self):
        """Roll die once. Return the result."""
        value = self.value
        self.value %= 100
        self.value += 1
        self.rolls += 1
        return value


class Player:
    def __init__(self, space):
        self.space = space
        self.score = 0

    def update(self, steps):
        """Update player's position and score after steps taken."""
        self.space = (self.space + steps) % 10
        if self.space == 0:
            self.space = 10
        self.score += self.space


def play():
    """Play a game. Return the result."""
    die = Die()
    player_1 = Player(7)
    player_2 = Player(3)

    while True:
        player_1.update(die.roll() + die.roll() + die.roll())
        if player_1.score >= 1000:
            return player_2.score * die.rolls
        player_2.update(die.roll() + die.roll() + die.roll())
        if player_2.score >= 1000:
            return player_1.score * die.rolls


if __name__ == '__main__':
    print(play())
