from day06_1 import parse, count_fish


if __name__ == '__main__':
    fish = parse('../data/day06.txt')
    print(count_fish(256, fish))
