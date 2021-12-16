

def check_row(row: list) -> bool:
    return all(map(lambda n: n == '', row))


def check_column(board: list, column: int) -> bool:
    return all(map(lambda n: n[column] == '', board))


def check_bingo(board: list, row: list, column: int) -> bool:
    return any([check_row(row), check_column(board, column)])


def compute_score(board: list, last_number: str) -> int:
    score = 0
    for row in board:
        score += sum(map(int, filter(lambda n: n != '', row)))
    return score * int(last_number)


def mark(board: list, row_len: int, n: str) -> bool:
    for row in board:
        for i in range(row_len):
            if n == row[i]:
                row[i] = ''
                if check_bingo(board, row, i):
                    return True
    return False


def find_target_score(numbers: list, boards: list, target: int):
    boards_len = len(boards)
    row_len = len(boards[0])
    winners = []
    for n in numbers:
        for i in range(boards_len):
            win = mark(boards[i], row_len, n)
            if win and i not in winners:
                winners.append(i)
                if len(winners) == target:
                    score = compute_score(boards[i], n)
                    print(f'{target}º winner score: {score}')
                    return


def first_winner_score(numbers: list, boards: list):
    find_target_score(numbers, boards, 1)


def last_winner_score(numbers: list, boards: list):
    find_target_score(numbers, boards, len(boards))


def get_input() -> tuple[str, list[str]]:
    numbers = []
    boards = []
    with open(0) as file:
        numbers = file.readline().strip().split(',')

        for line in file:
            if line == '\n':
                boards.append([])
            else:
                boards[-1].append(line.strip().split())
    return numbers, boards


def main():
    numbers, boards = get_input()

    first_winner_score(numbers, boards)
    last_winner_score(numbers, boards)


if __name__ == '__main__':
    main()
