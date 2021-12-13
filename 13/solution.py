
BLANK_CHAR = '.'
DOT_CHAR = '#'


def dump(paper: set[tuple[int, int]]):
    width = max(paper, key=lambda x: x[0])[0] + 1
    height = max(paper, key=lambda x: x[1])[1] + 1
    text = [[BLANK_CHAR for _ in range(width)] for _ in range(height)]
    for (x, y) in paper:
        text[y][x] = DOT_CHAR
    print('\n'.join([''.join(line) for line in text]))


def get_coord_after_fold(x: int, y: int,
                         fold: tuple[str, int]) -> tuple[int, int]:
    axis, n = fold
    if axis == 'x' and x > n:
        x = 2 * n - x
    elif axis == 'y' and y > n:
        y = 2 * n - y

    return x, y


def dump_activation_code(dots: list[tuple[int, int]],
                         folds: list[tuple[str, int]]):
    paper = set(dots)
    for f in folds:
        paper = {get_coord_after_fold(x, y, f) for (x, y) in paper}
    dump(paper)


def dots_after_first_fold(dots: list[tuple[int, int]],
                          folds: list[tuple[str, int]]):
    first_fold = folds[0]
    paper = {get_coord_after_fold(x, y, first_fold) for (x, y) in dots}
    print(f'dots after first fold: {len(paper)}')


def get_input() -> tuple[list[tuple[int, int]], list[tuple[str, int]]]:
    data = [], []
    i = 0
    for line in open(0):
        line = line.strip()
        if line != '':
            if i == 0:
                x, y = line.split(',')
                item = (int(x), int(y))
            else:
                axis, pos = line.split('=')
                item = (axis[-1], int(pos))
            data[i].append(item)
        else:
            i += 1
    return data


def main():
    dots, folds = get_input()

    dots_after_first_fold(dots, folds)
    dump_activation_code(dots, folds)


if __name__ == '__main__':
    main()
