from src.day23_1 import *


def test_23_1():
    least_energy = main('./tests/test_day23.txt')
    assert least_energy == 12521
