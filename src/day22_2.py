import collections

from day22_1 import parse

Cuboid = collections.namedtuple('Cuboid',
                                'x_min x_max y_min y_max z_min z_max')


def get_overlap(c1, c2):
    """If cuboids c1 and c2 overlap, return overlapping cuboid, else None."""
    x_min = max(c1.x_min, c2.x_min)
    y_min = max(c1.y_min, c2.y_min)
    z_min = max(c1.z_min, c2.z_min)
    x_max = min(c1.x_max, c2.x_max)
    y_max = min(c1.y_max, c2.y_max)
    z_max = min(c1.z_max, c2.z_max)
    if x_min <= x_max and y_min <= y_max and z_min <= z_max:
        return Cuboid(x_min, x_max, y_min, y_max, z_min, z_max)


def split(c1, c2):
    """Split cuboid c1 into cuboids that do not overlap with slice c2."""
    cuboids = []
    if c1.z_min < c2.z_min:  # forward
        cuboids.append(Cuboid(c2.x_min, c2.x_max, c2.y_min,
                              c2.y_max, c1.z_min, c2.z_min - 1))
    if c2.z_max < c1.z_max:  # backward
        cuboids.append(Cuboid(c2.x_min, c2.x_max, c2.y_min,
                              c2.y_max, c2.z_max + 1, c1.z_max))
    if c2.x_max < c1.x_max:  # right
        cuboids.append(Cuboid(c2.x_max + 1, c1.x_max, c2.y_min,
                              c2.y_max, c1.z_min, c1.z_max))
    if c1.x_min < c2.x_min:  # left
        cuboids.append(Cuboid(c1.x_min, c2.x_min - 1, c2.y_min,
                              c2.y_max, c1.z_min, c1.z_max))
    if c2.y_max < c1.y_max:  # up
        cuboids.append(Cuboid(c1.x_min, c1.x_max, c2.y_max + 1,
                              c1.y_max, c1.z_min, c1.z_max))
    if c1.y_min < c2.y_min:  # down
        cuboids.append(Cuboid(c1.x_min, c1.x_max, c1.y_min,
                              c2.y_min - 1, c1.z_min, c1.z_max))
    return cuboids


def set_cuboid(cuboid, cuboids_on, on=True):
    """Turn cuboid on or off. Return an updated list of cuboids."""
    updated = []
    for cuboid_on in cuboids_on:
        overlap = get_overlap(cuboid, cuboid_on)
        if overlap:
            updated += split(cuboid_on, overlap)
        else:
            updated.append(cuboid_on)
    if on:
        updated.append(cuboid)
    return updated


def cuboid_volume(cuboid):
    """Return the volume of cuboid, i.e. the number of cuboids on."""
    return ((cuboid.x_max - cuboid.x_min + 1)
            * (cuboid.y_max - cuboid.y_min + 1)
            * (cuboid.z_max - cuboid.z_min + 1))


def reboot(steps):
    """Reboot the reactor. Return the number of cuboids on."""
    cuboids_on = []
    for step in steps:
        on, cuboid = step
        on = True if on == 'on' else False
        cuboids_on = set_cuboid(cuboid, cuboids_on, on)
    return sum(cuboid_volume(cuboid) for cuboid in cuboids_on)


if __name__ == '__main__':
    steps = parse('../data/day22.txt')
    print(reboot(steps))
