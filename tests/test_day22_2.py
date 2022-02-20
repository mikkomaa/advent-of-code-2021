from src.day22_2 import *


def test_get_overlap_is_overlap():
    c1 = Cuboid(1, 5, 2, 5, 4, 10)
    c2 = Cuboid(3, 7, 1, 3, 2, 6)
    result = Cuboid(3, 5, 2, 3, 4, 6)
    assert get_overlap(c1, c2) == result


def test_get_overlap_is_overlap_2():
    c1 = Cuboid(10, 12, 10, 12, 10, 12)
    c2 = Cuboid(11, 13, 11, 13, 11, 13)
    result = Cuboid(11, 12, 11, 12, 11, 12)
    assert get_overlap(c1, c2) == result


def test_get_overlap_no_overlap():
    c1 = Cuboid(-1, 5, 2, 5, -4, 10)
    c2 = Cuboid(6, 7, 1, 3, 2, 6)
    assert get_overlap(c1, c2) is None


def test_split():
    c1 = Cuboid(10, 12, 10, 12, 10, 12)
    c2 = Cuboid(11, 12, 11, 12, 11, 12)
    cuboids = [Cuboid(11, 12, 11, 12, 10, 10), Cuboid(10, 10, 11, 12, 10, 12),
               Cuboid(10, 12, 10, 10, 10, 12)]
    assert split(c1, c2) == cuboids


def test_cuboid_volume():
    c = Cuboid(-10, -10, 10, 10, 10, 10)
    assert cuboid_volume(c) == 1


def test_reboot():
    steps = parse('./tests/test_day22.txt')
    assert reboot(steps[:20]) == 590784


def test_reboot_2():
    steps = parse('./tests/test_day22.txt')
    assert reboot(steps[20:24]) == 39


def test_reboot_3():
    steps = parse('./tests/test_day22.txt')
    assert reboot(steps[24:]) == 2758514936282235


def test_reboot_4():
    steps = parse('./data/day22.txt')
    assert reboot(steps[:20]) == 537042
