import numpy as np


def trace_vent(vent_map: np.array,
               x1: int, y1: int,
               x2: int, y2: int,
               sign_x: int, sign_y: int):

    if sign_x == 0:
        diff = abs(y1 - y2)
    else:
        diff = abs(x1 - x2)

    for i in range(diff + 1):
        vent_map[x1 + (i * sign_x), y1 + (i * sign_y)] += 1


def overlaps_limited(coords: list, vent_map: np.array):
    for [(x1, y1), (x2, y2)] in coords:
        sign_x, sign_y = np.sign(x2 - x1), np.sign(y2 - y1)

        if sign_x == 0 or sign_y == 0:
            trace_vent(vent_map, x1, y1, x2, y2, sign_x, sign_y)

    overlaps = vent_map[vent_map >= 2]
    print(f'number of overlaps (horizontal + vertical): {len(overlaps)}')


def overlaps_total(coords: list, vent_map: np.array):
    for [(x1, y1), (x2, y2)] in coords:
        sign_x, sign_y = np.sign(x2 - x1), np.sign(y2 - y1)

        if sign_x != 0 and sign_y != 0:
            trace_vent(vent_map, x1, y1, x2, y2, sign_x, sign_y)

    overlaps = vent_map[vent_map >= 2]
    print(f'number of overlaps (total): {len(overlaps)}')


def get_input() -> list:
    coords = []
    with open(0) as file:
        for line in file:
            values = line.strip().split(' -> ')
            start = tuple(map(int, values[0].split(',')))
            end = tuple(map(int, values[1].split(',')))
            coords.append([start, end])
    return coords


def main():
    coords = get_input()

    vent_map = np.zeros((1000, 1000))
    overlaps_limited(coords, vent_map)
    overlaps_total(coords, vent_map)


if __name__ == '__main__':
    main()
