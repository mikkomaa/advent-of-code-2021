def parse():
    """Parse the input. Return a set of dots and a list of folds."""
    dots, folds = set(), list()
    with open('../data/day13.txt') as f:
        for line in f.readlines():
            if line[0].isdigit():
                x, y = line.split(',')
                dots.add((int(x), int(y)))
            elif line[0] == 'f':
                coord, val = line.lstrip('fold ang').split('=')
                folds.append((coord, int(val)))
    return dots, folds


def fold(dots, axis, line):
    """Return the dots folded along line, given axis x or y."""
    if axis == 'x':
        return {(line - abs(line - x), y) for (x, y) in dots}
    else:
        return {(x, line - abs(line - y)) for (x, y) in dots}


if __name__ == '__main__':
    dots, folds = parse()
    print(len(fold(dots, *folds[0])))
