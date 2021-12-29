
LPX = '#'
DPX = '.'
PADDING = '.'
ALGO = ''


def get_adjacents(img: list[str],
                  row: int, col: int,
                  width: int, height: int) -> str:
    return ''.join([img[row + a][col + b]
                    if 0 <= (row + a) < height and 0 <= (col + b) < width
                    else PADDING
                    for a in (-1, 0, 1) for b in (-1, 0, 1)])


def pixels_to_bin(text: str) -> int:
    number = text.replace(DPX, '0').replace(LPX, '1')
    return int(number, 2)


def apply_algorithm(img: list[str]) -> list[str]:
    global PADDING
    height = len(img) + 2
    width = len(img[0]) + 2

    # expand
    img = [PADDING + p + PADDING for p in img]
    img.insert(0, PADDING * width)
    img.append(PADDING * width)

    # iterate
    new = []
    for i, row in enumerate(img):
        line = ''
        for j, _ in enumerate(row):
            adjacents = get_adjacents(img, i, j, width, height)
            number = pixels_to_bin(adjacents)
            line += ALGO[number]
        new.append(line)

    # update padding
    PADDING = ALGO[pixels_to_bin(PADDING * 9)]
    return new


def enhance_image(img: list[str], iters: int):
    actual_img = img
    for _ in range(iters):
        actual_img = apply_algorithm(actual_img)
    count = sum([s.count(LPX) for s in actual_img])
    print(f'light pixels after {iters} iterations: {count}')


def get_input() -> tuple[str, list[str]]:
    first, _, *other = open(0).read().splitlines()
    return first, other


def main():
    global ALGO
    ALGO, img = get_input()

    enhance_image(img, 2)
    enhance_image(img, 50)


if __name__ == '__main__':
    main()
