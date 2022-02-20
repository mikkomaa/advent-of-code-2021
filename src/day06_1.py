def parse(filename):
    """Return the initial list of ages of lanternfish."""
    with open(filename) as f:
        ages = [int(n) for n in f.read().split(',')]
    fish = [0] * 9
    for age in ages:
        fish[age] += 1
    return fish


def count_fish(days, fish):
    """Return the number of fish after days, given the initial state fish."""
    for _ in range(days):
        newfish = fish[0]
        for i in range(1, len(fish)):
            fish[i - 1] = fish[i]
        fish[8] = newfish
        fish[6] += newfish
    return sum(fish)


if __name__ == '__main__':
    fish = parse('../data/day06.txt')
    print(count_fish(80, fish))
