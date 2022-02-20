import collections


def parse():
    """Parse input. Return the polymer template and the update rules."""
    with open('../data/day14.txt') as f:
        polymer = f.readline().strip()
        f.readline()
        rules = dict()
        for line in f.readlines():
            key, value = line.strip().split(' -> ')
            rules[key] = value
    return polymer, rules


def step(polymer):
    """Update polymer once. Return the result."""
    updated = ''
    for i in range(len(polymer) - 1):
        pair = polymer[i: i + 2]
        if pair in rules:
            updated += pair[0] + rules[pair]
        else:
            updated += pair[0]
    return updated + polymer[-1]


if __name__ == '__main__':
    polymer, rules = parse()
    for _ in range(10):
        polymer = step(polymer)
    counts = collections.Counter(polymer).values()
    print(max(counts) - min(counts))
