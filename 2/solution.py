

def move(commands: list):
    x, y = 0, 0

    for c in commands:
        if c[0] == 'forward':
            x += c[1]
        elif c[0] == 'down':
            y += c[1]
        else:
            y -= c[1]

    print(f'final position: {x}, final depth: {y}')
    print(f'final multiply: {x * y}')


def move_with_aim(commands: list):
    x, y, aim = 0, 0, 0

    for c in commands:
        if c[0] == 'forward':
            x += c[1]
            y += (c[1] * aim)
        elif c[0] == 'down':
            aim += c[1]
        else:
            aim -= c[1]

    print(f'final position (with aim): {x}, final depth (with aim): {y}')
    print(f'final multiply (with aim): {x * y}')


def get_input() -> list:
    res = []
    with open(0) as file:
        for line in file:
            command, units = line.split(' ')
            res.append((command, int(units)))
    return res


def main():
    commands = get_input()

    move(commands)
    move_with_aim(commands)


if __name__ == '__main__':
    main()
