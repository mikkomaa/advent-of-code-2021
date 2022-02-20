if __name__ == '__main__':
    with open('../data/day08.txt') as f:
        entries = [line.strip().split(' | ')[1] for line in f.readlines()]

    count = 0
    for entry in entries:
        count += len([digit for digit in entry.split()
                      if len(digit) in {2, 3, 4, 7}])
    print(count)
