

PAIRS: dict[str, str] = {}


def count(counter: dict, e: str, n: int):
    if not counter.get(e):
        counter[e] = 0
    counter[e] += n


def grow(start: str, spots: list[int]):
    polymer = dict.fromkeys(PAIRS, 0)
    for i in range(len(start) - 1):
        polymer[start[i:i+2]] += 1

    counter = {}
    for i in set(start):
        count(counter, i, start.count(i))

    for step in range(1, max(spots) + 1):
        next_step = dict.fromkeys(PAIRS, 0)
        for e in polymer:
            n = polymer[e]
            if n > 0:
                new_e = PAIRS[e]
                next_step[e[0] + new_e] += n
                next_step[new_e + e[1]] += n

                count(counter, new_e, n)
        polymer = next_step

        if step in spots:
            values = counter.values()
            most_common, least_common = max(values), min(values)
            print(f'after {step} steps: {most_common - least_common}')


def get_input() -> tuple[str, dict[str, str]]:
    first, *data = open(0)
    pairs = {}
    for line in data:
        line = line.strip()
        if line != '':
            pair, elem = line.split(' -> ')
            pairs[pair] = elem
    return first.strip(), pairs


def main():
    global PAIRS
    template, PAIRS = get_input()

    spots = [10, 40]
    grow(template, spots)


if __name__ == '__main__':
    main()
