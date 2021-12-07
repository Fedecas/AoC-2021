

def get_input() -> list:
    *data, = open(0)
    return [int(n) for n in data]


def increases(depths: list, group_size: int):
    up = 0
    last = None
    group = []
    for d in depths:
        group.append(d)

        if len(group) == group_size:
            measure = sum(group)
            if last:
                if measure > last:
                    up += 1
            last = measure
            group.pop(0)

    print(f'number of increases by {group_size}: {up}')


def main():
    depths = get_input()

    increases(depths, 1)
    increases(depths, 3)


if __name__ == '__main__':
    main()
