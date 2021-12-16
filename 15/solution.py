
from queue import PriorityQueue

RISK_MAP = []
RISK_DEFAULT_VALUE = float('inf')
MIN_X, MAX_X, MAP_MAX_X = 0, 0, 0
MIN_Y, MAX_Y, MAP_MAX_Y = 0, 0, 0
MAX_RISK = 9


def get_neighbours(pos: tuple[int, int]) -> list[tuple[int, int]]:
    y, x = pos
    return [(y + i, x + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if MIN_Y <= y + i < MAP_MAX_Y and MIN_X <= x + j < MAP_MAX_X]


def get_risk(pos: tuple[int, int]) -> int:
    y, x = pos
    block_y, block_x = y // MAX_Y, x // MAX_X
    rel_y, rel_x = y % MAX_Y, x % MAX_X
    risk = RISK_MAP[rel_y][rel_x] + block_y + block_x
    return risk - (MAX_RISK * ((risk - 1) // MAX_RISK))


def lowest_risk(start: tuple[int, int], end: tuple[int, int]) -> int:
    remaining = PriorityQueue()
    visited = set()
    risk_values = {start: 0}
    remaining.put((0, start))

    while not remaining.empty():
        _, current_vertex = remaining.get()
        visited.add(current_vertex)

        for n in get_neighbours(current_vertex):
            if n not in visited:
                risk = get_risk(n)
                old = risk_values.get(n, RISK_DEFAULT_VALUE)
                new = risk_values[current_vertex] + risk
                if new < old:
                    risk_values[n] = new
                    remaining.put((new, n))
    return risk_values[end]


def find_lowest_risk(blocks_y: int, blocks_x: int):
    global MAP_MAX_Y, MAP_MAX_X
    MAP_MAX_Y, MAP_MAX_X = MAX_Y * blocks_y, MAX_X * blocks_x

    start, end = (MIN_Y, MIN_X), (MAP_MAX_Y - 1, MAP_MAX_X - 1)
    print(f'lowest risk from {start} to {end}: {lowest_risk(start, end)}')


def get_input() -> list:
    return [[int(c) for c in ln] for ln in open(0).read().splitlines()]


def main():
    global RISK_MAP, MAX_X, MAX_Y
    RISK_MAP = get_input()
    MAX_Y, MAX_X = len(RISK_MAP), len(RISK_MAP[0])

    find_lowest_risk(1, 1)
    find_lowest_risk(5, 5)


if __name__ == '__main__':
    main()
