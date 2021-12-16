

simple_digits_length = {2: 1,
                        3: 7,
                        4: 4,
                        7: 8}


def normalize(pattern: str) -> set:
    return set(sorted(pattern))


def decimal_output(digits: list, value: list) -> int:
    out = ''
    for v in value:
        v = normalize(v)
        out += str(digits.index(v))
    return int(out)


def decode(pattern: list) -> list:
    digits = [set() for _ in range(10)]
    possible_2_3_5 = []
    possible_0_6_9 = []

    # first filter (simple/complex)
    for p in pattern:
        p = normalize(p)
        size = len(p)
        if size in simple_digits_length.keys():
            digits[simple_digits_length[size]] = p
        elif size == 5:
            possible_2_3_5.append(p)
        else:
            possible_0_6_9.append(p)

    # find digit 3
    for n in possible_2_3_5:
        if digits[1].issubset(n):
            digits[3] = n

    # find digits 0, 6 and 9
    for n in possible_0_6_9:
        i = 0
        if not digits[1].issubset(n):
            i = 6
        elif digits[3].issubset(n):
            i = 9
        digits[i] = n

    # find digit 5 and finally digit 2
    for e in digits[1]:
        possible_5 = digits[9] - set(e)
        if possible_5 in possible_2_3_5:
            digits[5] = possible_5

            possible_2_3_5.remove(digits[3])
            possible_2_3_5.remove(digits[5])
            digits[2] = possible_2_3_5[0]

    return digits


def sum_values(patterns: list, values: list):
    count = 0
    displays = len(patterns)
    for i in range(displays):
        digits = decode(patterns[i])
        count += decimal_output(digits, values[i])
    print(f'total sum of output values: {count}')


def count_simple_digits(values: list):
    count = 0
    for display in values:
        for digit in display:
            if len(digit) in simple_digits_length.keys():
                count += 1
    print(f'numbers 1, 4, 7 or 8 appear {count} times in the values')


def get_input() -> list:
    patterns, values = [], []
    with open(0) as file:
        for line in file:
            data = line.strip().split(' | ')
            patterns.append(data[0].split())
            values.append(data[1].split())
    return patterns, values


def main():
    patterns, values = get_input()

    count_simple_digits(values)
    sum_values(patterns, values)


if __name__ == '__main__':
    main()
