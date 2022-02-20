import collections
import re

Cuboid = collections.namedtuple('Cuboid',
                                'x_min x_max y_min y_max z_min z_max')


def parse(filename):
    """Return the input parsed as a list of (on/off, cuboid) tuples."""
    steps = []
    with open(filename) as f:
        for line in f.readlines():
            on, ints = line.strip().split()
            steps.append((on, Cuboid(*map(int, re.findall(r'-?\d+', ints)))))
    return steps


def reboot(steps):
    """Reboot the reactor. Return the number of cuboids on."""
    cuboids_on = set()
    for step in steps:
        on, cuboid = step
        if (cuboid.x_min < -50 or cuboid.y_min < -50 or
            cuboid.z_min < -50 or cuboid.x_max > 50 or
            cuboid.y_max > 50 or cuboid.z_max > 50):
            continue

        # Brute force is fast enough.
        cubes = set((x, y, z)
                    for x in range(cuboid.x_min, cuboid.x_max + 1)
                    for y in range(cuboid.y_min, cuboid.y_max + 1)
                    for z in range(cuboid.z_min, cuboid.z_max + 1))
        if on == 'on':
            cuboids_on |= cubes
        else:
            cuboids_on -= cubes
    return len(cuboids_on)


if __name__ == '__main__':
    steps = parse('../data/day22.txt')
    print(reboot(steps))
