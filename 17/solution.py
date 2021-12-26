
def check_if_reach_target(x: int, y: int, rx: range, ry: range) -> bool:
    aux_x, aux_y = x, y
    fx, fy = 0, 0
    while fx <= max(rx) and fy >= min(ry):
        fx += aux_x
        fy += aux_y
        if fx in rx and fy in ry:
            break

        if aux_x > 0:
            aux_x -= 1
        aux_y -= 1
    return fx in rx and fy in ry


def find_all_initial_values(rx: range, ry: range):
    min_y, max_y = min(ry), abs(min(ry)) - 1
    min_x, max_x = 0, max(rx)
    reach_target = sum(check_if_reach_target(x, y, rx, ry)
                       for y in range(min_y, max_y + 1)
                       for x in range(min_x, max_x + 1))

    print(f'distinct initial valid velocities: {reach_target}')


def find_max_height(ry: range):
    max_y = abs(min(ry)) - 1
    value = max_y * ((max_y + 1) // 2)
    print(f'the highest y position is: {value}')


def get_input() -> list[int]:
    data = open(0).read().strip()
    limits = [a.split('=')[-1].split('..') for a in data.split(',')]
    return [int(r) for axis in limits for r in axis]


def main():
    rxa, rxb, rya, ryb = get_input()

    rx, ry = range(rxa, rxb + 1), range(rya, ryb + 1)

    find_max_height(ry)
    find_all_initial_values(rx, ry)


if __name__ == '__main__':
    main()
