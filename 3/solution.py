

def power_consumption(diagnostic: list):
    i = 0
    gamma = ''
    diag_len = len(diagnostic[0]) - 1
    while i < diag_len:
        count = {'0': 0, '1': 0}
        for d in diagnostic:
            count[d[i]] += 1

        if count['0'] > count['1']:
            gamma += '0'
        else:
            gamma += '1'
        i += 1

    gamma_dec = int(gamma, 2)
    epsilon_dec = (2**diag_len - 1) - gamma_dec
    epsilon = bin(epsilon_dec)[2:]

    print(f'gamma rate: {gamma} ({gamma_dec})')
    print(f'epsilon rate: {epsilon} ({epsilon_dec})')
    print(f'power consumption rate: {gamma_dec * epsilon_dec}')


def life_support(diagnostic: list):
    # oxygen
    i = 0
    keep = diagnostic
    number_len = len(diagnostic[0]) - 1
    while i < number_len:
        count = {'0': [], '1': []}
        for number in keep:
            count[number[i]].append(number)

        if len(count['0']) > len(count['1']):
            keep = count['0']
        else:
            keep = count['1']

        if len(keep) == 1:
            break
        i += 1

    oxygen = keep[0].strip()
    oxygen_dec = int(oxygen, 2)

    # CO2
    i = 0
    keep = diagnostic
    while i < number_len:
        count = {'0': [], '1': []}
        for number in keep:
            count[number[i]].append(number)

        if len(count['0']) <= len(count['1']):
            keep = count['0']
        else:
            keep = count['1']

        if len(keep) == 1:
            break
        i += 1

    co2 = keep[0].strip()
    co2_dec = int(co2, 2)

    print(f'oxygen generator rating: {oxygen} ({oxygen_dec})')
    print(f'CO2 scrubber rating: {co2} ({co2_dec})')
    print(f'life support rating: {oxygen_dec * co2_dec}')


def get_input() -> list:
    *data, = open(0)
    return data


def main():
    diagnostic = get_input()

    power_consumption(diagnostic)
    life_support(diagnostic)


if __name__ == '__main__':
    main()
