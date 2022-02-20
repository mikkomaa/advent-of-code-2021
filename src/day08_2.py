def decode(entries):
    """Decode output values. Return the sum of the output values."""
    sum_of_outputs = 0
    for entry in entries:
        numbers = 10 * ['']
        patterns = sorted(entry[0].split(), key=len)

        # Match the signal patterns with numbers 1, 4, 7, and 8.
        numbers[1], numbers[7], numbers[4], *patterns = patterns
        numbers[8] = patterns.pop()

        # Match the rest (0, 2, 3, 5, 6, and 9).
        for pattern in patterns:
            if len(pattern) == 5:
                if all(c in pattern for c in numbers[1]):
                    numbers[3] = pattern
                elif sum(c in numbers[4] for c in pattern) == 2:
                    numbers[2] = pattern
                else:
                    numbers[5] = pattern
            elif len(pattern) == 6:
                if all(c in pattern for c in numbers[4]):
                    numbers[9] = pattern
                elif all(c in pattern for c in numbers[1]):
                    numbers[0] = pattern
                else:
                    numbers[6] = pattern

        # Decode output values
        numbers = [sorted(number) for number in numbers]
        outputs = [sorted(output) for output in entry[1].split()]
        value = 0
        for output in outputs:
            for i, number in enumerate(numbers):
                if output == number:
                    value = 10 * value + i
                    break
        sum_of_outputs += value
    return sum_of_outputs


if __name__ == '__main__':
    with open('../data/day08.txt') as f:
        entries = [line.strip().split(' | ') for line in f.readlines()]
    print(decode(entries))
