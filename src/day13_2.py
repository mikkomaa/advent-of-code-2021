import matplotlib.pyplot as plt

from day13_1 import parse, fold


def plot(dots):
    """Plot the result to read the code."""
    plt.scatter(*list(zip(*dots)))
    plt.axis('equal')
    plt.gca().invert_yaxis()
    plt.show()


if __name__ == '__main__':
    dots, folds = parse()
    for f in folds:
        dots = fold(dots, *f)
    plot(dots)
