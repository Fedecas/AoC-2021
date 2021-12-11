
from copy import deepcopy

MIN_X, MAX_X = 0, 0
MIN_Y, MAX_Y = 0, 0
MAX_ENERGY = 9


def first_time_all_flash(octopus_map: list):
    step = 1
    while True:
        if do_step(octopus_map) == MAX_X * MAX_Y:
            break
        step += 1

    print(f'first step which all octopuses flash: {step}')


def get_neighbours(y: int, x: int) -> list:
    yi = (-1, 0, 1) if MIN_Y < y < MAX_Y - 1 else (
        (-1, 0) if y > MIN_Y else
        (0, 1)
    )
    xi = (-1, 0, 1) if MIN_X < x < MAX_X - 1 else (
        (-1, 0) if x > MIN_X else
        (0, 1)
    )

    return [(y + i, x + j) for i in yi for j in xi if not i == j == 0]


def increase_energy(octopus_map: list,
                    i: int, j: int,
                    flash_this_step: list) -> int:
    if (i, j) not in flash_this_step:
        if octopus_map[i][j] < MAX_ENERGY:
            octopus_map[i][j] += 1
        else:
            flash_this_step.append((i, j))
            octopus_map[i][j] = 0
            for (y, x) in get_neighbours(i,  j):
                increase_energy(octopus_map, y, x, flash_this_step)


def do_step(octopus_map: list) -> list:
    flash_this_step = []
    for i in range(MAX_Y):
        for j in range(MAX_X):
            increase_energy(octopus_map, i, j, flash_this_step)
    return len(flash_this_step)


def total_flashes(octopus_map: list, steps: int):
    flashes = sum([do_step(octopus_map) for _ in range(steps)])
    print(f'total flashes after {steps} steps: {flashes}')


def get_input() -> list:
    return [[int(c) for c in line.strip()] for line in open(0)]


def main():
    octopus_map = get_input()
    copy_map = deepcopy(octopus_map)

    global MAX_Y, MAX_X
    MAX_Y, MAX_X = len(octopus_map), len(octopus_map[0])

    total_flashes(octopus_map, 100)
    first_time_all_flash(copy_map)


if __name__ == '__main__':
    main()
