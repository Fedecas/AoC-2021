
spots = [80, 256]


def glow(fishes: list):
    incoming = fishes[0]
    for i in range(8):
        fishes[i] = fishes[i + 1]
    fishes[6] += incoming
    fishes[8] = incoming


def spawn(fishes: list):
    for i in range(1, max(spots) + 1):
        glow(fishes)
        if i in spots:
            print(f'After {i} days: {sum(fishes)}')


def get_input() -> list:
    data, *_ = open(0)
    return list(map(int, data.strip().split(',')))


def main():
    fishes = [0] * 9
    for i in get_input():
        fishes[i] += 1

    spawn(fishes)


if __name__ == '__main__':
    main()
