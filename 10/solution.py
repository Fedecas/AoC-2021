
PAIRS = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

POINTS = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}


def incomplete_error_score(incomplete: list):
    completion_points = list(POINTS.keys())
    lines = []
    for i in incomplete:
        score = 0
        for c in reversed(i):
            score *= 5
            score += completion_points.index(c) + 1
        lines.append(score)

    middle = sorted(lines)[len(lines) // 2]
    print(f'middle incomplete score: {middle}')


def syntax_error_score(wrong: list):
    score = sum([POINTS[c] for c in wrong])
    print(f'total syntax error score: {score}')


def split_failed_chunks(chunks: list) -> tuple:
    wrong, incomplete = [], []
    for line in chunks:
        expected = []
        for c in line:
            if c in PAIRS.keys():
                expected.append(PAIRS[c])
            elif c == expected[-1]:
                expected.pop()
            else:
                wrong.append(c)
                expected.clear()
                break
        if len(expected) > 0:
            incomplete.append(expected)

    return wrong, incomplete


def get_input() -> list:
    return [line.strip() for line in open(0)]


def main():
    chunks = get_input()

    wrong, incomplete = split_failed_chunks(chunks)

    syntax_error_score(wrong)
    incomplete_error_score(incomplete)


if __name__ == '__main__':
    main()
