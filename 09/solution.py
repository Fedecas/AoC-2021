
HEIGHT_MAP = []
MIN_X, MAX_X = 0, 0
MIN_Y, MAX_Y = 0, 0
MAX_HEIGHT = 9


def grow_basin_from(y: int, x: int, basin: list) -> list:
    for (i, j) in get_neighbours(y, x):
        height = HEIGHT_MAP[i][j]
        if height < MAX_HEIGHT and (i, j) not in basin:
            basin += [(i, j)]
            grow_basin_from(i, j, basin)
    return basin


def largest_basins(low_points: list):
    sizes = []
    for (y, x) in low_points:
        basin = grow_basin_from(y, x, [(y, x)])
        sizes.append(len(basin))

    sizes = sorted(sizes)[-3:]
    res = sizes[0] * sizes[1] * sizes[2]
    print(f'sizes of the three largest basins multiplied: {res}')


def risk_level(low_points: list):
    risk = sum([(HEIGHT_MAP[y][x] + 1) for (y, x) in low_points])
    print(f'sum of the risk levels: {risk}')


def get_neighbours(y: int, x: int) -> list:
    res = []
    if y > MIN_X:
        res.append((y - 1, x))
    if y < MAX_Y - 1:
        res.append((y + 1, x))

    if x > MIN_X:
        res.append((y, x - 1))
    if x < MAX_X - 1:
        res.append((y, x + 1))

    return res


def is_lowest(y: int, x: int) -> bool:
    neighbours = [
        HEIGHT_MAP[i][j]
        for (i, j) in get_neighbours(y, x)
    ]
    return HEIGHT_MAP[y][x] < min(neighbours)


def get_low_points() -> list:
    points = []
    for i in range(MAX_Y):
        for j in range(MAX_X):
            if is_lowest(i, j):
                points.append((i, j))
    return points


def get_input():
    data = []
    with open(0) as file:
        for line in file:
            data.append([int(c) for c in line.strip()])
    return data


def main():
    global HEIGHT_MAP, MAX_Y, MAX_X
    HEIGHT_MAP = get_input()
    MAX_Y, MAX_X = len(HEIGHT_MAP), len(HEIGHT_MAP[0])

    low_points = get_low_points()

    risk_level(low_points)
    largest_basins(low_points)


if __name__ == '__main__':
    main()
