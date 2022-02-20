import itertools


class Image:
    def __init__(self, pixels, fill_pixel):
        self.pixels = pixels  # a list of rows (strings)
        self.fill_pixel = fill_pixel  # the other pixels than self.pixels
        self.x_max = len(pixels[0]) - 1
        self.y_max = len(pixels) - 1

    def get_pixel(self, x, y):
        """Return the pixel at (x, y)."""
        if 0 <= x <= self.x_max and 0 <= y <= self.y_max:
            return self.pixels[y][x]
        return self.fill_pixel

    def get_decimal(self, x, y):
        """Return the decimal value of the pixel at (x, y)."""
        binary = ''
        for b, a in itertools.product((y - 1, y, y + 1), (x - 1, x, x + 1)):
            binary += '0' if self.get_pixel(a, b) == '.' else '1'
        return int(binary, 2)

    def lit_pixels(self):
        """Return the number of lit pixels in the image."""
        if self.fill_pixel == '#':
            return float('Infinity')
        return sum(row.count('#') for row in self.pixels)


def parse_input():
    """Parse input. Return the enhancement algorithm and the image."""
    with open('../data/day20.txt') as f:
        algorithm = f.readline().strip()
        f.readline()
        pixels = [line.strip() for line in f.readlines()]
    return algorithm, Image(pixels, '.')


def enhance(image, algorithm):
    """Enhance image using algorithm. Return the enhanced image."""
    pixels = []
    for y in range(-1, image.y_max + 2):
        row = ''
        for x in range(-1, image.x_max + 2):
            row += algorithm[image.get_decimal(x, y)]
        pixels.append(row)
    fill_pixel = algorithm[image.get_decimal(-2, -2)]
    return Image(pixels, fill_pixel)


if __name__ == '__main__':
    algorithm, image = parse_input()
    for _ in range(2):
        image = enhance(image, algorithm)
    print(image.lit_pixels())
