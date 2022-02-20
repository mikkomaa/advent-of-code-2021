import collections


def parse():
    """Parse input. Return the polymer template, its pairs, and the rules."""
    with open('../data/day14.txt') as f:
        polymer = f.readline().strip()
        pairs = collections.defaultdict(int)
        for i in range(len(polymer) - 1):
            pairs[polymer[i:i+2]] += 1

        f.readline()
        rules = dict()
        for line in f.readlines():
            key, value = line.strip().split(' -> ')
            rules[key] = value
    return polymer, pairs, rules


def step(pairs):
    """Simulate the pair insertion. Return the updated counts of pairs."""
    updated = collections.defaultdict(int)
    for pair in pairs:
        if pair in rules:
            updated[pair[0] + rules[pair]] += pairs[pair]
            updated[rules[pair] + pair[1]] += pairs[pair]
        else:
            updated[pair] = pairs[pair]
    return updated


def count_elements(pairs, polymer):
    """Return the list of the counts of the elements in polymer."""
    counts = collections.defaultdict(int)
    for pair in pairs:
        counts[pair[0]] += pairs[pair]
        counts[pair[1]] += pairs[pair]
    counts[polymer[0]] += 1   # Every element in polymer is counted twice
    counts[polymer[-1]] += 1  # except the first and the last.
    return [count // 2 for count in counts.values()]


if __name__ == '__main__':
    polymer, pairs, rules = parse()
    for _ in range(40):
        pairs = step(pairs)
    counts = count_elements(pairs, polymer)
    print(max(counts) - min(counts))
