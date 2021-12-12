
CONNECTIONS = {}


def walk(cave: str, actual_path: list, repeated: bool):
    possible_paths = 0
    actual_path.append(cave)
    for c in CONNECTIONS[cave]:
        if c not in actual_path or c.isupper():
            if c == 'end':
                possible_paths += 1
            else:
                possible_paths += walk(c, actual_path.copy(), repeated)
        elif c != 'start' != 'end' and not repeated:
            possible_paths += walk(c, actual_path.copy(), True)
    return possible_paths


def all_paths_each_once():
    paths = walk('start', [], True)
    print(f'paths visiting small caves at most once: {paths}')


def all_paths_single_twice():
    paths = walk('start', [], False)
    print(f'paths repeating single small cave at most twice: {paths}')


def get_input() -> dict:
    data = {}
    for line in open(0):
        a, b = line.strip().split('-')
        if a not in data:
            data[a] = []
        if b not in data:
            data[b] = []

        data[a].append(b)
        data[b].append(a)
    return data


def main():
    global CONNECTIONS
    CONNECTIONS = get_input()

    all_paths_each_once()
    all_paths_single_twice()


if __name__ == '__main__':
    main()
