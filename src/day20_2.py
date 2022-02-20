from day20_1 import parse_input, enhance


if __name__ == '__main__':
    algorithm, image = parse_input()
    for _ in range(50):
        image = enhance(image, algorithm)
    print(image.lit_pixels())
