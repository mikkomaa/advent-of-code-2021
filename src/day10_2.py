closings = {'(': ')',
            '[': ']',
            '{': '}',
            '<': '>'}

points = {'(': 1,
          '[': 2,
          '{': 3,
          '<': 4}


def make_stack(line):
    """Return stack to score, or None if line is corrupted."""
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif c != closings[stack.pop()]:
            return None
    return stack


def score(stack):
    """Return the score of stack."""
    score = 0
    while stack:
        score = 5 * score + points[stack.pop()]
    return score


if __name__ == '__main__':
    with open('../data/day10.txt') as f:
        lines = f.read().strip().split('\n')

    stacks = [s for s in [make_stack(line) for line in lines] if s is not None]
    scores = sorted([score(stack) for stack in stacks])
    print(scores[len(scores) // 2])
