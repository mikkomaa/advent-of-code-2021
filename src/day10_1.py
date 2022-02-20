closings = {'(': ')',
            '[': ']',
            '{': '}',
            '<': '>'}

points = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}


def process_line(line):
    """Return the syntax error points of line."""
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif c != closings[stack.pop()]:
            return points[c]
    return 0


if __name__ == '__main__':
    with open('../data/day10.txt') as f:
        lines = f.read().strip().split('\n')
    print(sum(process_line(line) for line in lines))
