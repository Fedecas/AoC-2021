
VERSION_LEN = 3
TYPE_LEN = 3
HEADER_LEN = VERSION_LEN + TYPE_LEN
LITERAL_GROUP_LEN = 5
SUBS_BY_LENGHT_LEN = 15
SUBS_BY_NUMBER_LEN = 11

TYPES = ['+', '*', 'min', 'max', 'LITERAL', '>', '<', '==']
LENGTH_TYPES = ['BY_LENGTH', 'BY_NUMBER']


def bin_to_dec(n: str) -> int:
    return int(n, 2)


def do_calc(type_id: str, elems: list) -> int:
    if type_id in ['min', 'max']:
        calc = f'{type_id}({elems})'
    else:
        calc = type_id.join(map(str, elems))
    return int(eval(calc))


def get_literal(number: str):
    i, result, next_group = 1, '', HEADER_LEN
    while i != 0:
        i = int(number[next_group])
        result += number[next_group + 1:next_group + LITERAL_GROUP_LEN]
        next_group += LITERAL_GROUP_LEN
    return next_group, bin_to_dec(result)


def get_subs_by_length(number: str) -> tuple[int, int, list[int]]:
    start, versions, packs = (HEADER_LEN + SUBS_BY_LENGHT_LEN + 1), 0, []
    lenght = bin_to_dec(number[HEADER_LEN + 1:start])
    while lenght > 0:
        sub_lenght, sub_version, sub_result = parse(number[start:])
        start += sub_lenght
        lenght -= sub_lenght
        versions += sub_version
        packs.append(sub_result)
    return start, versions, packs


def get_subs_by_number(number: str) -> tuple[int, int, list[int]]:
    start, versions, packs = (HEADER_LEN + SUBS_BY_NUMBER_LEN + 1), 0, []
    subs = bin_to_dec(number[HEADER_LEN + 1:start])
    for _ in range(subs):
        sub_lenght, sub_version, sub_result = parse(number[start:])
        start += sub_lenght
        versions += sub_version
        packs.append(sub_result)
    return start, versions, packs


def parse(number: str) -> tuple[int, int, int]:
    length, result = 0, 0
    version_id = bin_to_dec(number[:VERSION_LEN])
    type_id = bin_to_dec(number[VERSION_LEN:HEADER_LEN])

    if TYPES[type_id] == 'LITERAL':
        length, result = get_literal(number)
    else:
        lenght_type_id = bin_to_dec(number[HEADER_LEN])
        if LENGTH_TYPES[lenght_type_id] == 'BY_LENGTH':
            length, versions, subs = get_subs_by_length(number)
        else:
            length, versions, subs = get_subs_by_number(number)
        version_id += versions
        result = do_calc(TYPES[type_id], subs)
    return length, version_id, result


def get_input() -> str:
    data = open(0).read().strip()
    res = bin(int(data, 16))[2:]
    diff = len(data) * 4 - len(res)
    return '0' * diff + res


def main():
    number = get_input()

    length, versions, result = parse(number)
    print(f'number length: {length}')
    print(f'all packets versions: {versions}')
    print(f'expression result: {result}')


if __name__ == '__main__':
    main()
