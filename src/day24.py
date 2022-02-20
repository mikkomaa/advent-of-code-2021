instructions = dict(inp=lambda a, b: b,
                    add=lambda a, b: a + b,
                    mul=lambda a, b: a * b,
                    div=lambda a, b: a // b,
                    mod=lambda a, b: a % b,
                    eql=lambda a, b: 1 if a == b else 0)


def run_command(c, variables):
    """Run command c (a list of three strings)."""
    name = c[0]
    param1 = variables[c[1]]
    param2 = variables[c[2]] if c[2] in variables else int(c[2])
    result = instructions[name](param1, param2)
    variables[c[1]] = result


def process_model_number(commands, model_number):
    """Return True if model_number (string) is accepted, else False."""
    variables = dict(w=0, x=0, y=0, z=0)
    number = list(reversed(model_number))
    for c in commands:
        if len(c) == 2:  # inp instruction
            c = c + [number.pop()]
        run_command(c, variables)
    return variables['z'] == 0


if __name__ == '__main__':
    with open('../data/day24.txt') as f:
        commands = [line.strip().split() for line in f.readlines()]

    # See file day24reversed.md for the explanation of the model numbers.
    print(process_model_number(commands, '89959794919939'))  # biggest
    print(process_model_number(commands, '17115131916112'))  # smallest
