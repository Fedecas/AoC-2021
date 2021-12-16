

def get_constant_cost(crab: int, pos: int) -> int:
    return abs(crab - pos)


def get_sum_cost(crab: int, pos: int) -> int:
    dist = abs(crab - pos)
    return dist * (dist + 1) // 2


def move_all(crabs: list, pos: int, f: str) -> int:
    res = []
    if f == 'constant':
        res = [get_constant_cost(c, pos) for c in crabs]
    else:
        res = [get_sum_cost(c, pos) for c in crabs]

    return sum(res)


def cheapest_position_to_move(crabs: list, f: str):
    costs = []
    for i in range(min(crabs), max(crabs) + 1):
        costs.append(move_all(crabs, i, f))

    least = min(costs)
    print(f'least fuel possible with {f}: {least} (at {costs.index(least)})')


def get_input() -> list:
    data, *_ = open(0)
    return [int(v) for v in data.strip().split(',')]


def main():
    crabs = get_input()

    cheapest_position_to_move(crabs, 'constant')
    cheapest_position_to_move(crabs, 'sum')


if __name__ == '__main__':
    main()
